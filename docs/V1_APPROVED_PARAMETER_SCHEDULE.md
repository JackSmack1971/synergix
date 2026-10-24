# SynergiX V1 Candidate Parameter Schedule — DRAFT / NOT APPROVED

**Scenario:** proposed economic scenario v0.4. **Schedule:** v1.4. **Model:** v1.4-draft. This is the preferred candidate for accountable owner review only. No value, recipient, beneficiary, policy, identity, signature, implementation, deployment, or release authorization is approved or implied. TDR-01–09 remain open and the Phase 1 hold remains active.

The source model is [`../scripts/v1_economic_model.py`](../scripts/v1_economic_model.py); generated outputs are in [`generated/v1-economic-model-review-v1.4/`](generated/v1-economic-model-review-v1.4/). Prior v1.3 outputs are historical and superseded for this candidate.

## Candidate schedule

| Field | Preferred candidate for review | Approval state |
|---|---|---|
| Supply | 100,000,000 SNX fixed genesis supply; no post-genesis mint; 18 decimals | Proposed; TDR-01 open |
| Allocation | Rewards 20M (2M initially segregated, 18M restricted); ecosystem 20M; treasury 20M; team 15M; liquidity 10M; community 10M; partnerships 5M | Proposed; recipients, custody, and releases unapproved |
| Release | Ecosystem 48 monthly tranches; team 12-month cliff then 36 monthly; liquidity 2M at genesis then 24 monthly for 8M; community 1M at genesis then 36 monthly for 9M; partnerships 6-month cliff then 18 monthly; treasury genesis custody; restricted 18M reward remainder has no release assumed | Proposed; UTC calendar-month dates from illustrative 2027-04-01; T0 unresolved |
| Reward | 3% simple, noncompounding; `floor(P_units * 300 * D / (10,000 * 365))`; integer elapsed 24-hour days | Proposed; TDR-04 open |
| Epoch and T0 | 30 elapsed 24-hour days. Epoch k is `[T0 + 30k days, T0 + 30(k+1) days)`. `T0` is the exact approved genesis/epoch origin and remains unresolved. No epoch-based release occurs until T0 is approved. | Proposed definition; exact T0 open |
| Terms | 30, 90, or 180 elapsed days, fixed at entry; maturity is `entry_timestamp + duration_days * 86,400`; mature at `timestamp >= maturity` | Proposed; TDR-04/06 open |
| Reward rounding | Floor each position's reward independently in smallest token units; no carry between positions. Vesting uses cumulative floor and final-tranche remainder. | Proposed; TDR-04 open |
| Referral | Zero paid referrals; no referral liability path in this candidate | Proposed exclusion; TDR-05/09 open |
| Stake bounds | 100–100,000 SNX per position; 250,000 SNX wallet aggregate; 16 active positions per wallet; 20M SNX active principal protocol cap | Proposed; TDR-06 open |
| Exits | Early exit returns principal only and forfeits unpaid reward for that position; maturity returns principal and fully funded reward once. | Proposed; TDR-02/06 open |
| Reserve | 2M SNX initially segregated from preminted 20M reward allocation; reward commitments fully reserved before acceptance | Proposed; TDR-03/08 open |
| Liability bound | Outstanding reward liability capped at 500,000 SNX; per-stake acceptance requires both funded reserve headroom and cap headroom | Proposed; TDR-04/09 open |

## Liability and reserve definitions

Let `F` be actual funded reward-reserve assets, `L` the sum of maximum unpaid reward entitlements for accepted positions, and `C = 500,000 SNX`. Available reserve is `F - L`; cap headroom is `C - L`. Accept a position only if its maximum reward keeps both quantities nonnegative. With zero paid referrals, total reward liability is the sum of individually floored base rewards. Payout reduces reserve assets and the matching unpaid liability atomically. Principal escrow is accounted separately and must cover outstanding principal at all times. At maximum active principal (20M) and 180 days, the base liability ceiling by formula is 295,890.410958… SNX before per-position flooring; the 500K cap remains a separate hard limit.

At 20M continuously active principal, annualized simple rewards are 600,000 SNX. A 2M reserve therefore represents 3.333… years of gross throughput only under constant full exposure, all claims paid, no top-ups, no diversion, and no losses. It is not a solvency guarantee. Model cohort timing and caps are sensitivities, not adoption forecasts.

## Genesis allocations and release rules

All candidate totals sum to 100M SNX. Every beneficiary and custody identity remains unresolved. Vesting is integer base units with cumulative `floor(total_locked * elapsed_periods / periods)`; the final tranche receives the remainder. First monthly tranche occurs on the cliff anniversary, then monthly. Calendar release dates use UTC anniversaries from an illustrative genesis of 2027-04-01; exact `T0` requires owner approval. The model's released-minus-assumed-reserve value is only a proxy, never circulation or observed custody.

| Allocation | Total | At genesis | Candidate rule |
|---|---:|---:|---|
| Staking rewards | 20M | 2M segregated | 18M restricted; no release assumed |
| Ecosystem | 20M | 0 | 48 monthly tranches |
| Treasury | 20M | 0 | Genesis custody; spending candidate subject to timelock |
| Team | 15M | 0 | 12-month cliff, then 36 monthly tranches |
| Liquidity | 10M | 2M | Remaining 8M over 24 monthly tranches |
| Community | 10M | 1M | Remaining 9M over 36 monthly tranches |
| Partnerships | 5M | 0 | 6-month cliff, then 18 monthly tranches |

## Required gates

Explicit token-symbol clearance is required before genesis allocations or tokenholder terms are finalized. `T0`, beneficiary/recipient identities, custody identities, and the deployment/legacy-obligation inventory remain unresolved. Compatibility status is `COMPATIBILITY_UNDETERMINED`. This packet does not authorize implementation of economics-dependent behavior, migration, deployment, or release. H-01 disposition, independent security review, and separate deployment authorization remain required. Legal/commercialization review is outside this packet's selected gate scope and remains required before any token sale or promoted staking rewards.
