#!/usr/bin/env python3
"""Reproducible hypothetical V1 SNX allocation and reward-solvency model.

Standard-library only. Outputs integer base-unit CSV/JSON; no chain data or
economic approval is implied. Run from repository root:
  python scripts/v1_economic_model.py --output-dir docs/generated/v1-economic-model-review-v1.4
"""
import argparse
import csv
import json
from datetime import date
from pathlib import Path

DECIMALS = 18
UNIT = 10 ** DECIMALS
GENESIS = date(2027, 4, 1)
SUPPLY = 100_000_000 * UNIT
MODEL_VERSION = "1.4-draft"
SCENARIO_VERSION = "0.4-draft"
PARAMETER_SCHEDULE_VERSION = "1.4-draft"

ALLOCATIONS = [
    ("staking_rewards", 20_000_000, 2_000_000, 0, 0, "treasury/reserve authority; reward beneficiaries"),
    ("ecosystem", 20_000_000, 0, 0, 48, "ecosystem recipients; recipient list and custody approver"),
    ("treasury", 20_000_000, 0, 0, 0, "treasury custody and spending signers"),
    ("team", 15_000_000, 0, 12, 36, "team members and vesting beneficiaries"),
    ("liquidity", 10_000_000, 2_000_000, 0, 24, "liquidity custodian/venues; release operator"),
    ("community", 10_000_000, 1_000_000, 0, 36, "community recipients and distribution operator"),
    ("partnerships", 5_000_000, 0, 6, 18, "partner identities and vesting beneficiaries"),
]

def month_date(month):
    year = GENESIS.year + (GENESIS.month - 1 + month) // 12
    mon = (GENESIS.month - 1 + month) % 12 + 1
    return date(year, mon, 1).isoformat()

def unlock(amount, tge, cliff, periods, month):
    locked = amount - tge
    if month == 0:
        return tge
    if periods == 0:
        return 0
    # First tranche occurs on the cliff anniversary (e.g. month 12), then
    # monthly; month zero is the separate TGE release.
    offset = 1 if cliff else 0
    elapsed = max(0, min(periods, month - cliff + offset))
    vested = locked * elapsed // periods
    prior = locked * max(0, min(periods, month - 1 - cliff + offset)) // periods
    return vested - prior

def rewards(principal_sn, days):
    return principal_sn * UNIT * 300 * days // (10_000 * 365)

def exact_snx(units):
    whole, fraction = divmod(units, UNIT)
    return f"{whole}.{fraction:018d}"

def reserve_reuse_ledger(referral_bps, scenario):
    """Model repeated 180-day cohorts that respect the draft stake limits.

    Each cohort has 80 wallets, each with two 100K and one 50K SNX positions.
    This reaches 20M SNX while respecting per-position and wallet caps. All
    240 positions mature together; claims are serialized. This is a narrow
    hypothetical stress case, not an adoption forecast.
    """
    duration_days = 180
    reserve_balance = 2_000_000 * UNIT
    reward_cap = 500_000 * UNIT
    cohort_principals = [100_000, 100_000, 50_000] * 80
    base_per_position = [rewards(principal, duration_days) for principal in cohort_principals]
    referral_per_position = [reward * referral_bps // 10_000 for reward in base_per_position]
    commitment = sum(base_per_position) + sum(referral_per_position)
    position_count = len(cohort_principals)
    reserved = 0
    next_maturity = None
    accepted_cohorts = 0
    rows = []

    for elapsed_day in range(0, 1_440 + duration_days, duration_days):
        opening_balance = reserve_balance
        matured_payout = 0
        matured_positions = 0
        if next_maturity == elapsed_day:
            matured_payout = reserved
            matured_positions = position_count
            reserve_balance -= matured_payout
            reserved = 0
            next_maturity = None

        available_before = reserve_balance - reserved
        cap_headroom_before = reward_cap - reserved
        rejection_reason = ""
        accepted = 0
        if reserved != 0:
            rejection_reason = "prior cohort remains open"
        elif commitment > cap_headroom_before:
            rejection_reason = "aggregate liability cap"
        elif commitment > available_before:
            rejection_reason = "funded reserve"
        else:
            reserved = commitment
            next_maturity = elapsed_day + duration_days
            accepted = position_count
            accepted_cohorts += 1

        rows.append({
            "scenario": scenario,
            "elapsed_day": elapsed_day,
            "cohort_wallets": 80,
            "cohort_position_amounts_snx": "100000,100000,50000 per wallet",
            "cohort_position_count": position_count,
            "opening_reward_assets_units": str(opening_balance),
            "matured_positions": matured_positions,
            "matured_claims_paid_units": str(matured_payout),
            "new_positions_requested": position_count,
            "new_position_liability_units": str(commitment),
            "new_positions_accepted": accepted,
            "rejection_reason": rejection_reason,
            "closing_reward_assets_units": str(reserve_balance),
            "closing_reserved_liability_units": str(reserved),
            "closing_available_reserve_units": str(reserve_balance - reserved),
            "closing_cap_headroom_units": str(reward_cap - reserved),
            "accepted_cohort_count": accepted_cohorts,
        })
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="docs/generated/v1-economic-model-review-v1.4")
    args = parser.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty output directory: {out}")
    rows = []
    cumulative = {a[0]: 0 for a in ALLOCATIONS}
    previous_proxy = 0
    for m in range(49):
        row = {"month": m, "date_utc": month_date(m)}
        monthly_release = 0
        for key, total, tge, cliff, periods, _ in ALLOCATIONS:
            amount, immediate = total * UNIT, tge * UNIT
            rel = unlock(amount, immediate, cliff, periods, m)
            cumulative[key] += rel
            row[key + "_unlocked_this_month_units"] = str(rel)
            row[key + "_cumulative_unlocked_units"] = str(cumulative[key])
            monthly_release += rel
        released = sum(cumulative.values())
        row["genesis_minted_units"] = str(SUPPLY)
        row["allocation_unlock_units"] = str(monthly_release)
        row["cumulative_unlocked_units"] = str(released)
        row["locked_genesis_units"] = str(SUPPLY - released)
        row["custodied_units_assumed"] = str(22_000_000 * UNIT) # 20m treasury + 2m reward reserve
        proxy = released - 2_000_000 * UNIT
        row["released_less_assumed_reserve_proxy_units"] = str(proxy)
        row["unlock_pct_of_prior_proxy"] = "" if previous_proxy == 0 else f"{monthly_release * 100 / previous_proxy:.8f}"
        previous_proxy = proxy
        rows.append(row)
    with (out / "allocation_monthly.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

    liability_rows = []
    for principal in (5_000_000, 10_000_000, 20_000_000):
        for days in (30, 90, 180):
            liability_rows.append({"principal_snx": principal, "duration_days": days,
                "base_reward_units": str(rewards(principal, days)),
                "base_reward_snx_exact_decimal": exact_snx(rewards(principal, days)),
                "referral_zero_snx": "0",
                "paid_referral_units": "0",
                "total_liability_units": str(rewards(principal, days))})
    with (out / "liability_scenarios.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(liability_rows[0]))
        writer.writeheader(); writer.writerows(liability_rows)
    reserve_rows = reserve_reuse_ledger(0, "candidate; zero paid referrals")
    with (out / "reserve_cohort_ledger.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(reserve_rows[0]))
        writer.writeheader(); writer.writerows(reserve_rows)
    max_base_liability_bound = rewards(20_000_000, 180)
    max_referral_liability_bound = max_base_liability_bound
    liability_cap_units = 500_000 * UNIT
    data = {"status":"DRAFT / NOT APPROVED; hypothetical scenario only",
        "scenario_version":SCENARIO_VERSION,"parameter_schedule_version":PARAMETER_SCHEDULE_VERSION,
        "model_version":MODEL_VERSION,"model_source":"scripts/v1_economic_model.py",
        "canonical_output_directory":"docs/generated/v1-economic-model-review-v1.4",
        "genesis_utc":"2027-04-01T00:00:00Z (illustrative only; exact T0 unresolved)",
        "epoch_definition":"30 elapsed 24-hour days from approved T0; epoch k is [T0+30k days, T0+30(k+1) days); T0 must be owner-approved before terms are finalized",
        "release_timing":"allocation releases occur at UTC calendar-month boundaries relative to illustrative genesis; not epoch-based",
        "rounding":"floor each position reward in integer token base units; monthly vesting uses cumulative floor and final-tranche remainder",
        "token_decimals":DECIMALS,"genesis_supply_units":str(SUPPLY),"horizon_months":48,
        "reward_formula":"floor(P_units * 300 * D / (10000 * 365))","reward_rate":"3% simple, noncompounding; draft candidate",
        "reward_reserve_snx":2_000_000,
        "aggregate_outstanding_reward_cap_snx":500_000,"maximum_active_principal_snx":20_000_000,
        "maximum_liability_upper_bound_base_units":str(max_base_liability_bound),
        "maximum_liability_upper_bound_zero_referral_units":str(max_base_liability_bound),
        "liability_cap_headroom_upper_bound_zero_referral_units":str(liability_cap_units-max_base_liability_bound),
        "continuous_max_principal_base_outflow_snx_per_year":600_000,
        "reserve_runway_years_at_continuous_max_principal":3.3333333333,
        "reserve_to_global_cap_multiple":4,
        "global_cap_is_binding_at_given_max_principal":max_base_liability_bound >= liability_cap_units,
        "referrals":"zero paid referrals; no referral liability is generated",
        "reserve_cohort_ledger":"80 wallets each enter two 100K and one 50K SNX positions (240 positions, 20M principal total); all mature together at 180 days; claims are serialized before a same-size re-entry attempt; no top-ups; elapsed-day timeline.",
        "reserve_cohort_ledger_limitations":["one fixed cohort size and duration only", "claim transactions are modeled as serial transitions at the same maturity boundary", "no token loss, transfer failure, reserve diversion, or governance action is modeled", "re-entry failure is not a forecast of user behavior"],
        "release_proxy_definition":"cumulative unlocked allocations less an assumed 2M SNX ring-fenced reserve; not observed circulation, liquid float, holder distribution, or on-chain balances",
        "limitations":["released-token proxy assumes the 2M reward reserve remains segregated; recipient wallet behavior and actual custody are unknown", "allocation release dates use UTC calendar months; reward cohorts use exact elapsed days", "no legacy deployment, wallet, beneficiary, or enforceable obligation verified", "runway assumes constant full exposure, all claims paid, no top-ups and no reserve diversion"]}
    (out / "summary.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    assert sum(a[1] for a in ALLOCATIONS) == 100_000_000
    assert sum(a[2] for a in ALLOCATIONS) == 5_000_000
    assert all(sum(int(r[a[0]+"_unlocked_this_month_units"]) for r in rows) == (a[2] if a[0] in ("staking_rewards", "treasury") else a[1])*UNIT for a in ALLOCATIONS)
    print(f"Wrote hypothetical model outputs to {out}")
    print("Allocation conservation: 100,000,000 / 100,000,000 SNX; all tranches reconcile.")
    print("Reserve cohort ledger: 80 wallets / 240 positions / 20M principal; 180-day clustered maturity; zero paid referrals.")
    print("Reward examples (SNX):")
    for principal in (5_000_000,10_000_000,20_000_000):
        vals = [rewards(principal,d)/UNIT for d in (30,90,180)]
        print(f"  {principal:,}: 30d={vals[0]:.6f}, 90d={vals[1]:.6f}, 180d={vals[2]:.6f}")

if __name__ == "__main__": main()
