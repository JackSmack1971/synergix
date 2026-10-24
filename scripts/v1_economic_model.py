#!/usr/bin/env python3
"""Reproducible hypothetical V1 SNX allocation and reward-solvency model.

Standard-library only. Outputs integer base-unit CSV/JSON; no chain data or
economic approval is implied. Run from repository root:
  python scripts/v1_economic_model.py --output-dir docs/generated/v1-economic-model
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
    return principal_sn * UNIT * 400 * days // (10_000 * 365)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="docs/generated/v1-economic-model")
    args = parser.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty output directory: {out}")
    rows = []
    cumulative = {a[0]: 0 for a in ALLOCATIONS}
    previous_float = 0
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
        row["projected_circulating_upper_bound_units"] = str(released - 2_000_000 * UNIT)
        row["unlock_pct_of_prior_float"] = "" if previous_float == 0 else f"{monthly_release * 100 / previous_float:.8f}"
        previous_float = released - 2_000_000 * UNIT
        rows.append(row)
    with (out / "allocation_monthly.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

    liability_rows = []
    for principal in (5_000_000, 10_000_000, 20_000_000):
        for days in (30, 90, 180):
            liability_rows.append({"principal_snx": principal, "duration_days": days,
                "base_reward_units": str(rewards(principal, days)),
                "base_reward_snx_exact_decimal": f"{rewards(principal, days)/UNIT:.18f}",
                "referral_zero_snx": "0",
                "optional_referral_5pct_units": str(rewards(principal, days) * 5 // 100),
                "optional_total_liability_units": str(rewards(principal, days) + rewards(principal, days) * 5 // 100)})
    with (out / "liability_scenarios.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(liability_rows[0]))
        writer.writeheader(); writer.writerows(liability_rows)
    data = {"status":"DRAFT / NOT APPROVED; hypothetical scenario only", "genesis_utc":"2027-04-01T00:00:00Z",
        "token_decimals":DECIMALS,"genesis_supply_units":str(SUPPLY),"horizon_months":48,
        "reward_formula":"floor(P_units * 400 * D / (10000 * 365))","reward_reserve_snx":2_000_000,
        "aggregate_outstanding_reward_cap_snx":500_000,"maximum_active_principal_snx":20_000_000,
        "continuous_max_principal_base_outflow_snx_per_year":800_000,
        "reserve_runway_years_at_continuous_max_principal":2.5,
        "reserve_to_global_cap_multiple":4,
        "global_cap_is_binding_at_given_max_principal":False,
        "referrals":"base case zero; optional alternative is single-level 5% of rounded base reward, within same 500,000 SNX cap",
        "limitations":["projected circulation assumes treasury 20m and reward reserve 2m remain segregated in custody; recipient wallet behavior not known", "calendar month schedule; not block-level", "no legacy deployment, wallet, beneficiary, or enforceable obligation verified", "runway assumes constant full exposure, all claims paid, no top-ups and no reserve diversion"]}
    (out / "summary.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    assert sum(a[1] for a in ALLOCATIONS) == 100_000_000
    assert sum(a[2] for a in ALLOCATIONS) == 5_000_000
    assert all(sum(int(r[a[0]+"_unlocked_this_month_units"]) for r in rows) == (a[2] if a[0] in ("staking_rewards", "treasury") else a[1])*UNIT for a in ALLOCATIONS)
    print(f"Wrote hypothetical model outputs to {out}")
    print("Allocation conservation: 100,000,000 / 100,000,000 SNX; all tranches reconcile.")
    print("Reward examples (SNX):")
    for principal in (5_000_000,10_000_000,20_000_000):
        vals = [rewards(principal,d)/UNIT for d in (30,90,180)]
        print(f"  {principal:,}: 30d={vals[0]:.6f}, 90d={vals[1]:.6f}, 180d={vals[2]:.6f}")

if __name__ == "__main__": main()
