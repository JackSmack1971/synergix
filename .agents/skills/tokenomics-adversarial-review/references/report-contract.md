# Tokenomics review report contract

Report these six sections in the stated order. For narrow questions, make irrelevant cells "Not assessed (outside scope)" rather than implying an audit of everything. Cite source URL/block or exact file path and function/line where possible. Figures are **as of the stated block/time**, not automatically live.

## 1. Summary

2–4 sentences: reviewed scope, most serious substantiated issue, overall confidence (verified / partially verified / provisional / gap-only), and strongest blocker. No safe/unsafe certification.

## 2. Mechanics

Identify units and supply definitions first. Use an allocation table with: cohort; amount or %; amount at TGE; cliff and vesting semantics; authority; evidence/confidence. Use a monthly unlock table (month 0 through at least month 36) or link to a generated CSV plus representative checkpoints when a full table would crowd the report. Include earliest, largest and concentrated unlock windows, and any `UNRECONCILED` totals. Present equations with definitions:

- `R_i(t) = TGE_i + floor((A_i - TGE_i) * clamp(t - cliff_i, 0, duration_i) / duration_i)` for linear vesting with the first release at `cliff_i + 1`, and a cliff-only lump release if duration is zero. `R_i(0)=TGE_i`.
- `C(t) = sum_i R_i(t) + cumulative new freely circulating emissions + extra mints - cumulative burns`, **only if** all relevant circulating components are represented and burnable balance is available.
- `Outstanding(t) = GenesisMinted + cumulative new mints - cumulative burns`. A supply cap may apply to outstanding, lifetime minted, or both depending on actual code.
- `UnlockShock(t) = unlocked_from_existing_locked_allocations(t) / Circulating(t-1)` (undefined if prior circulating is zero); distinguish pure unlocks from new issuance.
- `YearGrossEmissionRate = gross minted during specified 12 months / explicitly named reference supply` (do not label an unlock rate as mint inflation).

For value capture, show who pays, asset paid, routing, recipient, token impact, discretion/bypass, and on-chain evidence. State whether the token is required or optional; staking locks are not burns and staking rewards are not automatically revenue.

## 3. Contract Alignment

Provide a crosswalk: documented promise | observed contract/transaction path | effective permissions/parameters | enforcement verdict | evidence. Examine actual proxy and role configuration, access grants and time-dependent settings. State if sources differ. Separate function presence from reachable effective authorization.

## 4. Risk Register

Use `Critical`, `High`, `Medium` (or `Not Assessed` for unsupported concerns). Columns: ID; severity; reachable mechanism; evidence or gap; adverse outcome/quantification; mitigation; test. `Critical`: evidenced active unrestricted issuance/transfer-control/governance bypass or similarly existential path with credible preconditions. `High`: bounded but material supply/privilege/concentration threat, or major unverified enforcement claim. `Medium`: material but less immediate weakness or missing disclosure. Severity must be justified; mark provisional if key deployment data unavailable. A discrepancy is not automatically an exploit.

## 5. Recommendations

Prioritize by control criticality, feasibility and reversibility. State exact suggested constraints, allowable min/max parameter changes, timelock/quorum or emission bounds, vesting schedule changes, and code + scenario tests that would show risk reduction. If design choices depend on product economics or governance preferences, offer conditional alternatives rather than force a universal standard. Never execute live changes.

## 6. Assumptions & Gaps

Separate: `not disclosed` (material absent from supplied documentation), `ambiguous` (multiple plausible meanings), `cannot verify from provided sources` (claimed but unproven), `not tested` (tool/call/check not performed), and `explicit hypothetical` (stress input). Include contract/chain/block identifiers, dated evidence, formula assumptions, unassessed cross-chain supply, and regulatory **risk flags only**. For jurisdiction-dependent risk, consult current primary regulators and refer legal determinations to counsel; do not assume an asset's classification from a single mechanism.

**Verification declaration:** Name the executed commands, actual results, scripts used, and whether a real deployed contract or only hypothetical implementation was checked. If no runtime or chain checks ran, say so.
