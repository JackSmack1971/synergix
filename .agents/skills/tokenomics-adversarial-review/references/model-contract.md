# Offline supply model: input and interpretation

Use `python scripts/supply_model.py --input <input.json> --output-dir <new-directory>` from the installed skill directory. The script uses Python standard library only; it performs **integer arithmetic in raw token base units** and writes monthly CSVs plus `summary.json`. This is a *scenario calculation*, not an on-chain data fetch or verification of source claims. Do not feed secret keys, nonpublic user data, or raw credentials.

## Required input

```json
{
  "token_symbol": "DEMO",
  "token_decimals": 0,
  "horizon_months": 48,
  "genesis_supply_units": "1000",
  "outstanding_cap_units": "1400",
  "allocations": [
    {"id": "team", "cohort": "team", "amount_units": "300", "tge_unlocked_units": "0", "cliff_months": 12, "linear_months": 36},
    {"id": "community", "cohort": "community", "amount_units": "700", "tge_unlocked_units": "200", "cliff_months": 0, "linear_months": 12}
  ],
  "emissions": [
    {"id": "rewards", "from_month": 1, "through_month": 24, "monthly_units": "5"}
  ],
  "burns": [
    {"id": "fees", "from_month": 1, "through_month": 24, "monthly_units": "1"}
  ],
  "scenarios": [
    {"name": "base", "emission_multiplier": "1", "burn_multiplier": "1", "extra_mints": []},
    {"name": "low-usage", "emission_multiplier": "1", "burn_multiplier": "0", "extra_mints": []},
    {"name": "admin-mint", "emission_multiplier": "1", "burn_multiplier": "1", "extra_mints": [{"month": 12, "amount_units": "100"}]}
  ]
}
```

The numbers above are *illustrative synthetic inputs*, **never token facts**. For a live model derive values from actual evidence, cite per field in the report, and record which scenario inputs are hypothetical. All names must be slugs (`[a-z][a-z0-9-]*` for scenario names); allocation IDs and stream IDs use alphanumeric, hyphen or underscore. Positive genesis and complete allocation coverage are required: `sum(amount_units) == genesis_supply_units`. `token_decimals` must match the actual on-chain asset or be declared an assumption. Numeric units are nonnegative integer **strings**; never input floating-point amounts. Unsafe path characters are rejected. A null outstanding cap means **not disclosed**, not proof that minting is uncapped. Monthly schedules approximate time-stamped on-chain vesting.

- `genesis_supply_units`: all tokens minted at time zero, including locked allocations.
- `tge_unlocked_units`: immediately circulating at month 0. The remainder stays locked.
- `cliff_months`: number of complete months with no release after month 0.
- `linear_months`: monthly release periods after the cliff. Zero releases as a lump at month `cliff_months+1`. Cumulative vested after cliff equals `floor(locked * elapsed / linear_months)` capped at the locked amount; final tranche receives dust.
- `emissions`: newly minted and immediately released tokens. Transfers from a pre-minted treasury belong in the allocation schedule, not emission.
- `burns`: circulating tokens destroyed after releases and mints in a month. Excess burns are rejected.
- `outstanding_cap_units`: optional cap on instantaneous outstanding total supply, tested before the modeled monthly burns. Lifetime issuance caps and separate mint budgets need independent checks.
- `extra_mints`: immediate circulating supply injections; treated as hypothetical until role/cap authority are proven.
- Multipliers: decimal **strings** >= 0; monthly issuance/burn is multiplied and rounded DOWN to base units. Cap-violating cases are rejected unless `assume_cap_bypass` is explicitly true; that labels a counterfactual, not proof of bypass.

## Outputs and limits

Each scenario produces `monthly_<scenario>.csv`, with months 0 through the horizon inclusive, allocation-specific unlocks, released genesis, new mints, burned units, circulating units, locked genesis, outstanding supply, and monthly shock percentages. A value of `25` in a `*_pct` field means 25 percent. The `summary.json` marks results as unverified projections, gives largest monthly unlock shocks, and lists scenario assumptions. Values are **raw base units**; divide by `10 ** token_decimals` for display.

`Outstanding[t] = Outstanding[t-1] + new_mints - burn`.

`Circulating[t] = Circulating[t-1] + releases + new_mints - burn`.

`Locked[t] = GenesisSupply - cumulative allocation releases`.

`Outstanding[t] = Circulating[t] + Locked[t]` is checked each month.

`UnlockShock[t] = releases_from_locked[t] / Circulating[t-1]` (undefined if prior circulation is zero); newly minted shock is separate.

This model does **not** determine prices, liquidity, wallet ownership, voting weight, staking restrictions, rebases, intra-month behavior, fee elasticity, bridges or whether arbitrary mints are permitted. Cite each factual input separately; do not label projected float as observed float. Event-driven or nonlinear tokenomics not representable by this schema need a different verified model.

## Failure

Invalid inputs, insufficient allocation reconciliation, cap breaches or burns exceeding circulating balance result in an error before writing any output. Existing files are never overwritten. Use a fresh output directory for new runs. A cap-bypass scenario is explicitly marked counterfactual.
