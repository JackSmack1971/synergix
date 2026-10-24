#!/usr/bin/env python3
"""Offline, deterministic 36+ month token supply model (base units only)."""
import argparse
import csv
from decimal import Decimal, InvalidOperation, ROUND_DOWN, localcontext
import io
import json
from pathlib import Path
import re
import sys


class ModelError(ValueError):
    pass


ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")
SLUG = re.compile(r"^[a-z][a-z0-9-]{0,40}$")
INTEGER = re.compile(r"^(0|[1-9][0-9]*)$")


def units(v, label):
    if not isinstance(v, str) or not INTEGER.fullmatch(v):
        raise ModelError(f"{label}: expected nonnegative integer STRING in base units")
    if len(v) > 78:
        raise ModelError(f"{label}: exceeds 78-digit base-unit limit")
    return int(v)


def integer(v, label, lo, hi):
    if type(v) is not int or not lo <= v <= hi:
        raise ModelError(f"{label}: expected integer in [{lo},{hi}]")
    return v


def ident(v, label, pattern=ID):
    if not isinstance(v, str) or not pattern.fullmatch(v):
        raise ModelError(f"{label}: invalid identifier")
    return v


def factor(v, label):
    if not isinstance(v, str) or len(v) > 100:
        raise ModelError(f"{label}: expected decimal STRING (up to 100 characters)")
    try:
        d = Decimal(v)
    except InvalidOperation as exc:
        raise ModelError(f"{label}: invalid decimal") from exc
    if not d.is_finite() or not 0 <= d <= 1000000:
        raise ModelError(f"{label}: expected finite nonnegative number <= 1000000")
    return d


def scaled(n, d):
    # Decimal defaults to 28-digit precision, which silently destroys raw token
    # base units for 18-decimal ERC20 supplies. Keep every input digit exact.
    with localcontext() as ctx:
        ctx.prec = max(160, len(str(n)) + len(d.as_tuple().digits) + 10)
        return int((Decimal(n) * d).to_integral_value(rounding=ROUND_DOWN))


def pct(n, base):
    if base == 0:
        return None
    with localcontext() as ctx:
        ctx.prec = 160
        return (format(Decimal(n) * 100 / Decimal(base), ".8f").rstrip("0").rstrip(".")) or "0"


def checked_list(v, label):
    if not isinstance(v, list):
        raise ModelError(f"{label}: expected list")
    return v


def parse(doc):
    if not isinstance(doc, dict):
        raise ModelError("root: expected JSON object")
    symbol = ident(doc.get("token_symbol"), "token_symbol")
    decimals = integer(doc.get("token_decimals"), "token_decimals", 0, 30)
    horizon = integer(doc.get("horizon_months", 36), "horizon_months", 36, 600)
    genesis = units(doc.get("genesis_supply_units"), "genesis_supply_units")
    if genesis == 0:
        raise ModelError("genesis_supply_units: must be > 0")
    cap = None if doc.get("outstanding_cap_units") is None else units(doc["outstanding_cap_units"], "outstanding_cap_units")
    if cap is not None and cap < genesis:
        raise ModelError("outstanding cap is below genesis supply")
    allocs, names = [], set()
    for i, a in enumerate(checked_list(doc.get("allocations"), "allocations")):
        if not isinstance(a, dict):
            raise ModelError(f"allocations[{i}]: expected object")
        name = ident(a.get("id"), f"allocations[{i}].id")
        if name in names:
            raise ModelError(f"duplicate allocation id {name}")
        names.add(name)
        amount = units(a.get("amount_units"), f"{name}.amount_units")
        tge = units(a.get("tge_unlocked_units"), f"{name}.tge_unlocked_units")
        if tge > amount:
            raise ModelError(f"{name}: TGE released exceeds amount")
        allocs.append(dict(id=name, cohort=ident(a.get("cohort", "other"), f"{name}.cohort"),
                           amount=amount, tge=tge,
                           cliff=integer(a.get("cliff_months"), f"{name}.cliff_months", 0, 600),
                           duration=integer(a.get("linear_months"), f"{name}.linear_months", 0, 600)))
    if not allocs or sum(a["amount"] for a in allocs) != genesis:
        raise ModelError("allocation amounts must sum exactly to genesis supply")

    def streams(field):
        result, seen = [], set()
        for i, item in enumerate(checked_list(doc.get(field, []), field)):
            if not isinstance(item, dict):
                raise ModelError(f"{field}[{i}]: expected object")
            name = ident(item.get("id"), f"{field}[{i}].id")
            if name in seen:
                raise ModelError(f"duplicate {field} id {name}")
            seen.add(name)
            start = integer(item.get("from_month"), f"{name}.from_month", 1, horizon)
            end = integer(item.get("through_month"), f"{name}.through_month", start, horizon)
            result.append(dict(start=start, end=end, amount=units(item.get("monthly_units"), f"{name}.monthly_units")))
        return result

    emissions, burns = streams("emissions"), streams("burns")
    cases, seen = [], set()
    for i, x in enumerate(checked_list(doc.get("scenarios"), "scenarios")):
        if not isinstance(x, dict):
            raise ModelError(f"scenarios[{i}]: expected object")
        name = ident(x.get("name"), f"scenarios[{i}].name", SLUG)
        if name in seen:
            raise ModelError(f"duplicate scenario name {name}")
        seen.add(name)
        bypass = x.get("assume_cap_bypass", False)
        if type(bypass) is not bool:
            raise ModelError(f"{name}.assume_cap_bypass: expected boolean")
        extras = []
        for j, extra in enumerate(checked_list(x.get("extra_mints", []), f"{name}.extra_mints")):
            if not isinstance(extra, dict):
                raise ModelError(f"{name}.extra_mints[{j}]: expected object")
            extras.append(dict(month=integer(extra.get("month"), f"{name}.mint.month", 1, horizon),
                               amount=units(extra.get("amount_units"), f"{name}.mint.amount_units")))
        cases.append(dict(name=name, emission_factor=factor(x.get("emission_multiplier", "1"), f"{name}.emission_multiplier"),
                          burn_factor=factor(x.get("burn_multiplier", "1"), f"{name}.burn_multiplier"),
                          bypass=bypass, extras=extras))
    if not cases:
        raise ModelError("at least one scenario required")
    return dict(symbol=symbol, decimals=decimals, horizon=horizon, genesis=genesis,
                cap=cap, allocs=allocs, emissions=emissions, burns=burns, cases=cases)


def vested(a, month):
    amount = a["amount"] - a["tge"]
    n = max(0, month - a["cliff"])
    if a["duration"] == 0:
        return amount if n else 0
    return amount * min(n, a["duration"]) // a["duration"]


def simulate(model, case):
    allocs = model["allocs"]
    circ = sum(a["tge"] for a in allocs)
    outstanding = model["genesis"]
    cohort_release = {}
    for a in allocs:
        cohort_release[a["cohort"]] = cohort_release.get(a["cohort"], 0) + a["tge"]
    rows, breached, peak = [], [], None
    sum_emission = sum_burns = sum_extra = 0
    for m in range(model["horizon"] + 1):
        tranches = {a["id"]: (a["tge"] if m == 0 else vested(a, m) - vested(a, m - 1)) for a in allocs}
        unlock = sum(tranches.values()) if m else 0
        if m:
            for a in allocs:
                cohort_release[a["cohort"]] += tranches[a["id"]]
        new = sum(scaled(s["amount"], case["emission_factor"]) for s in model["emissions"] if s["start"] <= m <= s["end"])
        burn = sum(scaled(s["amount"], case["burn_factor"]) for s in model["burns"] if s["start"] <= m <= s["end"])
        extra = sum(x["amount"] for x in case["extras"] if x["month"] == m)
        prev_circ = circ
        if m:
            # Check pre-burn total; a later burn may not make an earlier mint legal.
            before_burn = outstanding + new + extra
            if model["cap"] is not None and before_burn > model["cap"]:
                if not case["bypass"]:
                    raise ModelError(f"{case['name']} month {m}: outstanding cap breached before burn; bypass must be explicitly counterfactual")
                breached.append(m)
            if burn > circ + unlock + new + extra:
                raise ModelError(f"{case['name']} month {m}: burns exceed circulating balance")
            outstanding = before_burn - burn
            circ += unlock + new + extra - burn
        else:
            new = burn = extra = 0
        locked = sum(a["amount"] - a["tge"] - vested(a, m) for a in allocs)
        if min(circ, outstanding, locked) < 0 or locked + circ != outstanding:
            raise ModelError(f"{case['name']} month {m}: supply conservation failed")
        shock = pct(unlock, prev_circ) if m else None
        row = dict(month=m, unlock_existing_units=unlock, new_emissions_units=new,
                   additional_mints_units=extra, burned_units=burn, circulating_units=circ,
                   genesis_locked_units=locked, outstanding_units=outstanding,
                   unlock_shock_pct=shock,
                   mint_shock_pct=pct(new + extra, prev_circ) if m else None,
                   circulating_delta_pct=pct(circ - prev_circ, prev_circ) if m else None)
        row.update({f"unlock_{a['id']}_units": tranches[a["id"]] for a in allocs})
        rows.append(row)
        if m > 0 and shock is not None and (peak is None or Decimal(shock) > Decimal(peak["shock_pct"])):
            peak = {"month": m, "released_units": str(unlock),
                    "prior_circulating_units": str(prev_circ), "shock_pct": shock}
        sum_emission += new
        sum_burns += burn
        sum_extra += extra
    summary = {
        "name": case["name"], "status": "modeled_from_inputs_not_verified_on_chain",
        "emission_multiplier": str(case["emission_factor"]),
        "burn_multiplier": str(case["burn_factor"]),
        "assume_cap_bypass": case["bypass"], "cap_breach_months": breached,
        "total_emissions_units": str(sum_emission), "additional_mints_units": str(sum_extra),
        "total_burns_units": str(sum_burns),
        "final_outstanding_units": str(outstanding), "final_circulating_units": str(circ),
        "final_genesis_locked_units": str(locked), "peak_unlock_shock": peak,
        "cumulative_releases_by_cohort_units": {k: str(v) for k, v in sorted(cohort_release.items())},
        "warning": "Cohort releases are not observed balances or governance votes. Hypothetical emissions, burns and admin mints require separate source validation."
    }
    return rows, summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as f:
            model = parse(json.load(f))
        contents, summaries = {}, []
        # Validate all scenarios before any output side effects.
        for case in model["cases"]:
            rows, report = simulate(model, case)
            filename = f"monthly_{case['name']}.csv"
            out = io.StringIO()
            writer = csv.DictWriter(out, fieldnames=rows[0].keys(), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
            contents[filename] = out.getvalue()
            report["csv_file"] = filename
            summaries.append(report)
        contents["summary.json"] = json.dumps({
            "symbol": model["symbol"], "token_decimals": model["decimals"],
            "horizon_months": model["horizon"], "genesis_supply_units": str(model["genesis"]),
            "outstanding_cap_units": None if model["cap"] is None else str(model["cap"]),
            "scope": "offline mathematical projection; does not verify chain, source data or realistic permissions",
            "scenarios": summaries,
        }, indent=2) + "\n"
        dest = args.output_dir
        if dest.exists() and not dest.is_dir():
            raise ModelError("output path is not a directory")
        if any((dest / name).exists() for name in contents):
            raise ModelError("refusing to overwrite existing output files")
        dest.mkdir(parents=True, exist_ok=True)
        for name, content in contents.items():
            with (dest / name).open("x", encoding="utf-8", newline="") as f:
                f.write(content)
        print(json.dumps({"files": sorted(contents), "output_dir": str(dest), "scenarios": len(summaries)}))
        return 0
    except (ModelError, OSError, json.JSONDecodeError) as exc:
        print(f"MODEL_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
