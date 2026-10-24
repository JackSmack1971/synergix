# SynergiX V1 Economic Specification

**Status:** Proposed economic scenario v0.4 — preferred candidate for accountable owner review; all values remain unapproved. This document does not approve final tokenomics, deployment, or production release, and it does not certify the current contracts. The complete candidate is in [`V1_APPROVED_PARAMETER_SCHEDULE.md`](V1_APPROVED_PARAMETER_SCHEDULE.md). Phase 1 remains on HOLD; see [`V1_OWNER_DECISIONS.md`](V1_OWNER_DECISIONS.md).

The decision register, illustrative sustainability sensitivities, and machine-testable economic acceptance criteria are in [`V1_TOKENOMICS_DECISION_RECORD.md`](V1_TOKENOMICS_DECISION_RECORD.md). The supporting candidate is scenario v0.4, schedule v1.4, and model v1.4-draft; all remain unapproved. `T0`, token symbol clearance, recipient/custody identities, and compatibility remain unresolved.

Candidate staking bounds, maturity/withdrawal behavior, shortfall response, and administrative custody/pause policy are evaluated in [`V1_ADMINISTRATIVE_AUTHORITY.md`](V1_ADMINISTRATIVE_AUTHORITY.md). All detailed rules remain open for owner approval.

## Purpose and baseline

This specification proposes the economic model for a first release. Its evidence baseline is the current repository checkout and [`audit/REPORT.md`](../audit/REPORT.md), which remains `STATUS: INCOMPLETE`. The report records a source-only review, no supplied deployment address, unknown payout intent, and unresolved economic and operational assumptions. The current remediation record separately reconciles the exact `main` and branch revisions, documents the present token-proxy/staking-constructor architecture, and records current build and test evidence. That reconciliation does not amend the historical report, supply the missing economics, establish deployment state, or establish production readiness.

The audit report is historical evidence and must not be rewritten to make this proposal appear validated. Any discovered live deployment requires a separate compatibility and migration assessment before changing contracts or token economics.

## Proposed economic model

### Principal

- A stake transfers the user's SNX principal into the staking contract as escrow.
- The principal remains segregated in accounting from reward funds and cannot be minted as a substitute for returning escrow.
- On an eligible withdrawal, the contract returns the recorded principal once and closes the position. A second withdrawal must fail.
- Preferred candidate: early exit returns principal only and forfeits the unpaid reward on that position. This is unapproved and requires explicit owner approval before implementation.

### Rewards

- Candidate reward is 3% simple, noncompounding, with 30/90/180 elapsed-day terms; paid referrals are zero. These values remain unapproved. Rewards are separate liabilities from principal and are paid only from an explicitly funded reserve.
- A stake or claim must not create an unfunded reward promise. At all times, the reward reserve must cover accrued and claimable rewards under the chosen accounting model.
- Reward funding and payout accounting must be observable on chain. If a reserve is depleted, the specification must define whether new stakes stop, claims queue, or another bounded behavior applies; principal withdrawals remain available.
- V1 must not rely on unrestricted minting to satisfy rewards. Any token mint authority and its limits are a separate supply-policy decision.

### Solvency invariants

The implementation and tests must establish, at minimum:

1. **Principal coverage:** escrowed principal held for users is at least the aggregate outstanding principal liability.
2. **No double withdrawal:** each position's principal can be returned no more than once.
3. **Reward coverage:** reserved reward assets cover aggregate accrued and claimable rewards, including referral rewards.
4. **No principal subsidy:** reward payouts cannot consume assets owed as principal.
5. **Bounded accounting:** accepted stake, duration, rate, and referral parameters cannot overflow calculations or create liabilities outside the funded reserve.
6. **Failure isolation:** reward-reserve exhaustion cannot prevent a valid principal withdrawal.

These are design requirements, not claims about the current contracts. Their exact accounting formulas depend on the decisions below.

## Proposed V1 contract and authority model

- V1 contracts should be immutable and non-upgradeable after deployment. Correctness changes require a new deployment and an explicitly reviewed migration path.
- Keep administrative powers minimal and visible. Proposed powers are limited to funding the reward reserve, pausing new stake creation in an emergency, and configuring only parameters that are explicitly approved as mutable.
- Administrative actions should emit events. Privileged roles should be assigned to documented custody, with multisig and timelock expectations decided before deployment.
- Administrators must not be able to withdraw user principal, rewrite existing positions, or change terms for already-open positions.
- Emergency pause behavior must preserve withdrawals of matured principal and claims that remain fully funded, unless a specific threat model justifies a narrower temporary restriction.

## Proposed exclusions from the first release

Unless product review explicitly adds and specifies them, V1 excludes proxy upgrades, arbitrary reward minting, price oracles, cross-chain functionality, compounding, transferable stake positions, discretionary changes to open-position terms, and unbounded referral traversal. Each exclusion reduces the initial state space; it does not establish that excluded behavior is unsafe in every design.

## Candidate definitions (all unapproved)

The candidate uses a 100M fixed supply and schedule in the parameter artifact. A 30-day epoch is exactly 30 elapsed 24-hour days, with epoch `k = [T0 + 30k days, T0 + 30(k+1) days)`. The exact `T0` remains unresolved and must be approved before genesis allocations or tokenholder terms are finalized. Reward per position is `floor(P_units * 300 * D / (10,000 * 365))`, independently floored in smallest units; `D` is exact elapsed 24-hour days. Monthly allocation releases use UTC calendar-month anniversaries from an illustrative date and are not epoch-based. Liability is the sum of unpaid individually floored rewards, bounded by both actual prefunded reserve and a candidate 500,000 SNX aggregate cap. Principal remains separately escrowed. See the schedule for allocation totals, release rules, limits, and custody recommendations.

## Open decisions (no values are approved)

| Decision | Must define before implementation |
|---|---|
| Reward parameters | Rate or schedule, time unit, compounding policy, rounding, maximum reward per position, and whether rates are fixed at entry or shared over time |
| Supply policy | Initial supply, any maximum supply, mint authority and limits, burn behavior, and how reward funding relates to circulating supply |
| Stake limits | Minimum and maximum principal, allowed durations, per-user or global caps, and behavior at each boundary |
| Referral policy | Eligibility, depth, percentages or fixed amounts, cycle handling, and reserve accounting for referral liabilities |
| Reward reserve | Accepted funding asset, required prefunding, accounting method, and behavior when funds are insufficient |
| Exit rules | Maturity definition, claim timing, early exit availability, and any disclosed penalties |
| Administration | Role holders, multisig threshold, timelock, mutable settings, pause authority, and recovery procedures |
| Supported testnet (deployment planning) | Deferred until Phase 4; then select and name the network, chain ID, RPC/deployment process, and explorer verification procedure. Do not infer it from legacy configuration. |

No economic rate, token cap, stake limit, or other unresolved tokenomics value in this document should be treated as settled. Product owners must approve these decisions in a versioned economic schedule before implementation acceptance. Testnet selection is deferred until deployment planning in Phase 4.

## Acceptance boundary

This proposal becomes an implementation specification only after the open decisions are approved and the current checkout's source/build baseline is reconciled. Security review, invariant tests, and deployment evidence remain separate gates; approval of this document alone does not establish that contracts are safe or deployed.
