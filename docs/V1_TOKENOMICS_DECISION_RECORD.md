# SynergiX V1 Tokenomics Decision Record

**Record:** TDR-V1-001
**Version:** 0.2 (conditional architecture approval; owner review pending)
**Status:** PROPOSED / AWAITING OWNER APPROVAL — architecture only.
**Date:** 2026-10-24

This record documents the user's conditional approval of V1 architecture principles and the still-open tokenomics and authority decisions. The approval is **CONDITIONAL — Architecture only**; it does not approve final tokenomics, parameter selection, implementation that depends on open decisions, deployment, or production release. Non-economic preparation, including test planning and source-integrity work, may proceed independently. The current compile and test baseline is recorded in [`V1_BASELINE_VERIFICATION_2026-10-24.md`](V1_BASELINE_VERIFICATION_2026-10-24.md), and the full test plan is in [`V1_INVARIANT_TEST_MATRIX.md`](V1_INVARIANT_TEST_MATRIX.md); the hold point is in [`V1_REMEDIATION_PLAN.md`](V1_REMEDIATION_PLAN.md). [`audit/REPORT.md`](../audit/REPORT.md) remains incomplete. Do not infer deployed behavior or tokenholder commitments from this proposal.

## Approved design principles

These principles are approved as architectural direction only. They do not supply the numeric schedule, governance identities, or operational policies needed for implementation.

- **Principal:** escrow and return principal to the staker at maturity.
- **Rewards:** fund rewards separately and fully reserve commitments before creating them.
- **Supply:** prefer a fixed-supply model; exact cap remains open.
- **Staking contracts:** use immutable, versioned V1 contracts.
- **Solvency:** keep principal and reward liabilities covered at all times.
- **Administration:** no authority may withdraw committed user funds.
- **Legacy behavior:** retain legacy source behavior as historical observation, not approved V1 economics.

## Decision summary

| ID | Decision | Draft direction | State / required approval |
|---|---|---|---|
| TDR-01 | Supply and issuance | Fixed-supply model is preferred; exact cap and initial issuance remain undecided. | OPEN. Owner must approve total supply, allocations, release schedule, and post-genesis mint authority. |
| TDR-02 | Principal custody | Escrow principal and return it to the staker at maturity; do not mint principal as a substitute for repayment. | APPROVED DESIGN PRINCIPLE; detailed withdrawal behavior and implementation remain subject to the open policies below. |
| TDR-03 | Reward source | Fund rewards separately; fully reserve each commitment before creating it. | APPROVED DESIGN PRINCIPLE; funding source, reserve accounting, and exact handling of unavailable funds remain open. |
| TDR-04 | Reward schedule and liability | No rate, duration schedule, or maximum reward liability has been selected. | OPEN. Owner must approve reward formula/rates, permitted durations, compounding/time basis, rounding, and per-position/global liability caps. |
| TDR-05 | Referral rewards | Referral liabilities, if included, must follow the approved reserve-coverage principle. | OPEN under TDR-04. Define eligibility, depth, percentages or amounts, and whether referral rewards add to or partition base rewards. |
| TDR-06 | Stake bounds and exits | Minimum and maximum stake amounts, emergency controls, and withdrawal policies remain undecided. | OPEN. Maturity principal return is an approved principle; owner must define stake bounds, claim timing, any early exit, and pause/withdrawal behavior. |
| TDR-07 | Governance and administrative powers | Immutable, versioned V1 contracts; no authority may withdraw committed user funds. | OPEN. Owner must approve governance addresses, multisig threshold, timelock, mutable settings (if any), emergency-control authority/scope, and recovery procedure. |
| TDR-08 | Reward shortfall | Reward commitments must be fully reserved. | OPEN. Specify operational behavior when new commitments cannot be fully funded or a reserve discrepancy/loss occurs; no committed user funds may be withdrawn by an administrator. |
| TDR-09 | Referral / reward cap interactions | All reward liabilities, including any referral component, must fit within the approved funded commitment. | OPEN under TDR-04/TDR-05. Specify reservation timing and concurrent-position accounting in the approved schedule. |
| TDR-10 | Initial deployment network | No network selected. Network choice is deferred to deployment planning. | OPEN for Phase 4; not a tokenomics or Phase 1 approval prerequisite. |

Approval must be recorded per row with approver identity/role, date, rationale, and a versioned parameter schedule. The approval recorded below covers architecture principles only. Code defaults, historical tests, and legacy deployment configuration do not count as approval of V1 economics. If an owner chooses a direction different from a principle above, update this record and the economic spec before implementation.

## Legacy source snapshot — not approved V1 economics

The following observations are from local `HEAD` `8de8af76e3e9b42abc92abe56e2756f7368f267d` on 2026-10-24. They describe current source only, not a deployment, and are recorded to prevent accidental reuse as approved parameters:

| Topic | Current source observation | V1 implication |
|---|---|---|
| Supply / minting | `SynergiXToken.mint` has no cap check and permits callers with `STAKING_ROLE` to mint. The token implementation is UUPS-upgradeable. | Conflicts with the proposed fixed-supply, no-post-genesis-mint, immutable V1 direction. Set initial supply and issuance policy explicitly; assess any live deployment separately. |
| Principal payout | `SynergiXStaking.stakeStart` escrows principal; `stakeEnd` mints `stakeValue + interest` rather than transferring escrowed principal back. | Conflicts with TDR-02's proposed escrow return. Payout intent is not established by these source semantics or tests. |
| Reward source | Stake payout and referral rewards are minted. Referral constants are 2% to referrer and 1% to referred staker. | These are not reserve-funded terms and are not approved V1 percentages. Do not carry them forward without an explicit decision and sustainability analysis. |
| Stake size | Staking contract requires at least 1,000,000 SNX; token wrapper caps at 1,000,000 SNX, so the exposed range is exactly that amount. | Legacy behavior is not a V1 recommendation; V1 minimum, maximum, and aggregate exposure remain open. |
| Duration | Token wrapper accepts 1–365 days; staking contract has `MAX_STAKE_DAYS = 5555` and owner-controlled `maxStakeDays`. | Conflicting bounds and mutable authority require a single approved V1 rule. |
| Interest schedule | Payout derives interest from indexed `dailyData`, stake shares, and cumulative interest; it does not define a fixed APR in the source. | The sensitivity rates above are scenario inputs only. The V1 formula, funding, accrual, and schedule lifecycle need explicit decisions. |
| Administrative powers | Staking owner can change maximum stake days, burn behavior/rate, launch-bonus settings, referral assignments, and append daily reward data; it can grant/revoke staking operators. Token admin can upgrade the token, grant/revoke admin roles, and manage trusted contracts. No public pause setter appears in these sources despite a private token pause flag. | Decide which settings are fixed at deployment, which are governance-controlled, and whether any emergency control exists. Specify who holds each role and what each control can affect. |

These observations do not establish the behavior of any deployed instance. Reconcile the source baseline and investigate deployments before migration or compatibility decisions, as required by the remediation plan.

### Repository authority check

A repository search on 2026-10-24 covered `README.md`, `docs/`, `contracts/`, `test/`, `scripts/`, and `audit/` (excluding dependencies, generated build output, and the bundled OWASP reference corpus). It found no separately approved tokenomics schedule, allocation decision, reward APR, treasury commitment, governance charter, or administrative custody record. Existing tests assert selected legacy behavior, including 1%/2% referral minting, but do not establish approval or intended V1 economics. The user's conditional direction now approves architecture principles only; the numerical schedule and administrative authority details remain unresolved under TDR-01 through TDR-09. TDR-10 is intentionally deferred to Phase 4.

## Quantitative sustainability sensitivities

These are arithmetic sensitivities, not forecasts, recommendations, promised returns, or approved V1 parameters. They intentionally use hypothetical inputs so reviewers can see how reserve longevity changes with active principal and rate. No market price, adoption, token demand, or fiat value is assumed. All amounts are SNX units; a real schedule must define integer precision, decimals, accrual granularity, rounding, and caps.

For simple, non-compounding rewards:

```text
annual_base_rewards = active_principal × annual_rate
annual_referral_rewards = annual_base_rewards × referral_add_on
annual_reward_outflow = annual_base_rewards + annual_referral_rewards
reserve_runway_years = reward_reserve ÷ annual_reward_outflow
```

Assumptions for this table: reserve starts at **1,000,000 SNX**, remains fully available for rewards, active principal remains constant for a full year, all positions accrue for that year, referrals add **20% of base rewards**, and there are no new deposits, withdrawals, reserve top-ups, slashing, fees, or compounding. The 20% referral add-on is a sensitivity input only, not a proposed referral term.

| Active principal (SNX) | Annual base rate (sensitivity) | Base rewards / year (SNX) | Referral add-on (SNX) | Total outflow / year (SNX) | Runway for 1,000,000 SNX reserve |
|---:|---:|---:|---:|---:|---:|
| 1,000,000 | 5% | 50,000 | 10,000 | 60,000 | 16.67 years |
| 1,000,000 | 10% | 100,000 | 20,000 | 120,000 | 8.33 years |
| 1,000,000 | 20% | 200,000 | 40,000 | 240,000 | 4.17 years |
| 10,000,000 | 5% | 500,000 | 100,000 | 600,000 | 1.67 years |
| 10,000,000 | 10% | 1,000,000 | 200,000 | 1,200,000 | 0.83 years |
| 10,000,000 | 20% | 2,000,000 | 400,000 | 2,400,000 | 0.42 years |
| 50,000,000 | 5% | 2,500,000 | 500,000 | 3,000,000 | 0.33 years |
| 50,000,000 | 10% | 5,000,000 | 1,000,000 | 6,000,000 | 0.17 years |
| 50,000,000 | 20% | 10,000,000 | 2,000,000 | 12,000,000 | 0.08 years |

The table demonstrates sensitivity, not sustainability approval. Runway is not sufficient by itself: position durations and reward obligations can cluster, so a reserve can fail a claim before its average annual runway elapses. Before selecting terms, the economic owner must provide scenarios for at least low/base/high active principal, reward schedule, referral exposure, duration mix, withdrawal timing, reserve top-up cadence, and a zero-top-up stress case. Each scenario must report peak outstanding liabilities as well as annual outflow and runway.

### Required scenario model inputs

The approved schedule and scenario workbook or reproducible calculation must state:

- Genesis supply, initial allocations, release timing, maximum supply, and post-genesis issuance authority.
- Active principal assumptions by duration and time, including concentration and concurrent maximum exposure.
- Reward rates/formula, time basis, compounding, rounding direction, and per-position/global caps.
- Referral eligibility, maximum depth, aggregate referral cap, and whether rewards add to or partition base rewards.
- Starting reward reserve, reserve asset, top-up schedule, and zero-top-up stress case.
- Withdrawal and claim timing assumptions, including simultaneous claims at maturity.
- The exact rule used to decide whether a proposed stake is fully funded when accepted.

## Machine-testable economic acceptance criteria

These criteria specify behaviors for a future implementation; the current contracts have not been shown to satisfy them. The final test suite should encode each as stateful/property-based tests across action sequences, with bounded fuzz inputs derived from the approved parameter schedule. Use a test reference model for aggregate liabilities and balances; do not use test success as a substitute for independent security review.

| ID | Requirement and observable pass condition | Verification oracle / failure condition |
|---|---|---|
| ECON-01 | After every successful stake, contract-held principal is at least aggregate outstanding principal liability. | Stateful invariant over deposits, withdrawals, and multiple users; fail on any state where held principal is lower. |
| ECON-02 | Each position returns its principal at most once; a second withdrawal always reverts and changes no balances or liabilities. | Sequence test: mature, withdraw, repeat; compare snapshots and assert unchanged state on revert. |
| ECON-03 | At every transition, funded reward reserve after subtracting all reserved, accrued, and claimable base plus referral liabilities is nonnegative. | Stateful invariant and independent model; fail on accepted stake or payout that makes available reserve negative. |
| ECON-04 | Reward payouts reduce only reward-reserve assets; they never reduce principal coverage below outstanding principal liability. | Interleaved stake, fund, reward claim, and principal withdrawal sequences; assert both balances and liabilities after each action. |
| ECON-05 | A stake is rejected atomically if its maximum committed base and referral liabilities cannot be reserved under the approved schedule. | Boundary tests at exact available reserve and one smallest unit above it; rejected call must leave all state unchanged. |
| ECON-06 | Exhausting or disabling reward funding cannot block an otherwise valid matured principal withdrawal. | Set reward availability to zero, then withdraw matured positions; assert principal is returned and accounting closes. |
| ECON-07 | No user action or administrative action can increase total supply after genesis when TDR-01 is approved as fixed supply. | Assert total supply never increases across all callable paths and roles; attempt every mint-capable path as authorized and unauthorized actors. |
| ECON-08 | Rates, durations, stake bounds, referral parameters, and rounding cannot overflow, underflow, or produce a liability above its approved cap. | Fuzz exact boundaries and extreme values from the approved schedule; calls either produce reference-model-equal values or revert atomically. |
| ECON-09 | Existing positions retain their entry terms; administrative changes cannot alter their principal, rate, maturity, or referral entitlement. | Open position, change each approved mutable global setting, then compare stored/effective terms; fail on retroactive change. |
| ECON-10 | Emergency pause blocks only the operations explicitly listed in the approved pause policy and preserves matured principal withdrawal and fully funded claims. | Role and pause matrix over every public state-changing method; assert allowed actions remain available while paused. |
| ECON-11 | Referral graph traversal is bounded by the approved maximum depth, rejects cycles, and reserves aggregate referral liabilities within the same solvency invariant. | Fuzz referral chains including cycles, maximum depth, and maximum percentage; assert bounded work and model-equal liabilities. |
| ECON-12 | Every rejected economic operation is atomic: token balances, supply, positions, aggregate liabilities, reserve, and events reflect no partial action. | Snapshot all observable state before boundary and unauthorized failures; compare after revert. |

Criteria that depend on an unresolved economic decision remain **blocked for implementation** until that decision is approved. In particular ECON-07 depends on TDR-01; ECON-05 and ECON-08 depend on approved rates, caps, rounding, and referral rules; ECON-09 and ECON-10 depend on the authority schedule and pause policy. The acceptance suite must preserve that traceability rather than hard-code draft values.

### Deployment-independent test plan

This section is the deployment-independent test plan. Since it was drafted, legacy characterization and narrow source-repair regressions have been implemented and run; their exact revision, commands, results, and limitations are recorded in [`SECURITY_REMEDIATION_STATUS_2026-10-24.md`](SECURITY_REMEDIATION_STATUS_2026-10-24.md). Those tests do not satisfy the V1 acceptance criteria below, which remain gated on owner decisions and a V1 implementation. Test scenarios may still be prepared now, but assertions that depend on unresolved parameters must remain parameterized and marked pending until the approved schedule exists.

| Plan ID | Planned scenario | Criteria | Can prepare before owner schedule? | Values/oracle still needed |
|---|---|---|---|---|
| PLAN-01 | Stake escrow, mature, return principal exactly once; interleave independent users and ensure reward reserve state cannot reduce principal coverage. | ECON-01, ECON-02, ECON-04, ECON-06 | Yes, as a scenario and state model around the approved escrow/maturity principles. | Final time semantics, claim interface, and executable implementation. |
| PLAN-02 | Fund reserve, accept reward commitments, claim, and reject a commitment that is not fully covered. | ECON-03, ECON-05, ECON-12 | Partly; define model variables and conservation assertions now. | Reward formula, reserve asset, rounding, commitment timing, maximum liability, and shortfall behavior. |
| PLAN-03 | Exercise post-genesis issuance paths and role bypass attempts. | ECON-07 | Partly; enumerate all mint paths and expected no-mint invariant. | Exact initial supply, allocation/mint-at-genesis path, and final authority model. |
| PLAN-04 | Fuzz stake amount/duration, rate arithmetic, rounding, and liability boundaries against an independent reference model. | ECON-08 | No executable boundary values yet; prepare the harness shape only. | Approved min/max stake, durations, formula, rates, rounding, and caps. |
| PLAN-05 | Verify open-position terms survive governance changes; exercise each authorized and unauthorized admin action. | ECON-09, ECON-10 | Partly; preserve the invariant that committed user funds cannot be withdrawn. | Role matrix, mutable settings, timelock, pause scope, emergency policy, and recovery actions. |
| PLAN-06 | Bound referral traversal, reject cycles, and account referral commitments within the reward reserve. | ECON-03, ECON-08, ECON-11 | Partly; scenario skeleton can be written without choosing percentages. | Whether referrals exist, eligibility, depth, percentages/amounts, and referral cap. |

### Security-control mapping for planned verification

This maps the planned principles and criteria to the control statuses already reported in [`audit/REPORT.md`](../audit/REPORT.md). The statuses below are reproduced from that report, not re-audited in this documentation pass. Do not interpret `FAIL` or `NOT TESTED` as cleared by this mapping.

| Principle / criteria | Relevant control IDs | Status in audit report | Planned evidence |
|---|---|---|---|
| Escrow, principal coverage, withdrawal | SCSVS-COMP-3; SCSVS-GOV-3 | NOT TESTED; FAIL (H-01) | Stateful balance/liability invariants; maturity, repeat withdrawal, reserve-exhaustion scenarios. |
| Fixed supply and reward economics | SCSVS-GOV-1/2; SCSVS-ORACLE-1/2; SCSTG-TEST-0015/0016 | NOT TESTED; SCSTG-TEST-0015 FAIL (H-01) | Total-supply invariant, independent reward model, boundary and full-reserve commitment tests after TDR approval. |
| Governance and least privilege | SCSVS-AUTH-1/2; SCSTG-TEST-0001/0003/0004 | NOT TESTED | Role/action matrix, unauthorized-call cases, custody evidence, and owner approval of governance specification. |
| Immutable versioned contracts | SCSVS-ARCH-2; SCSTG-TEST-0007 | NOT TESTED | Verify implementation has no upgrade path; if deployment history exists, separately assess compatibility and storage. |
| Bounded referral and gas behavior | SCSVS-BLOCK-2; SCSTG-TEST-0008/0014 | NOT TESTED | Maximum-depth/cycle scenarios, bounded traversal, and gas checks once referral scope is approved. |
| Test adequacy and review process | SCSVS-CODE-3 | NOT TESTED | Map each ECON criterion to a scenario/property test and independent security review on frozen reviewed source. |

The audit report remains `STATUS: INCOMPLETE`; this mapping is a preparation artifact and does not change that status.

## Decision owners and approval log

The repository does not identify accountable economic or governance approvers. Assign these roles before treating any row as approved:

| Approval area | Required accountable role | Evidence to record |
|---|---|---|
| Supply, allocations, issuance | Product/economic owner plus protocol governance authority | Approved supply schedule and issuance rationale |
| Rewards, referrals, reserve stress model | Product/economic owner plus treasury/reserve authority | Versioned formula/parameter schedule and reproducible scenario results |
| Stake terms and exits | Product/economic owner | User-facing terms and boundary behavior |
| Administrative powers and custody | Governance/security authority | Role matrix, custody identities, threshold/timelock decision, pause/recovery procedure |
| Acceptance criteria | Engineering owner and independent security reviewer | Tests mapped to ECON IDs and review record |

| Decision ID | Approver / role | Date | Rationale or linked evidence | Approved version |
|---|---|---|---|---|
| Architecture principles only | User (identity/owner authority not established in this record) | 2026-10-24 | Conditional approval stated in conversation; disposition: `CONDITIONAL — Architecture only` | V1 architecture direction |
| TDR-01, TDR-04 through TDR-09 | **Owner approval pending** | — | Open decisions listed above; next gate is an explicit owner-approved economic schedule and administrative authority specification | — |
| TDR-02 and TDR-03 | User-approved design principles only | 2026-10-24 | Escrowed principal returned at maturity; separate reward funding with fully reserved commitments. Detailed policies remain open. | V1 architecture direction |
| TDR-10 | Deferred to deployment planning | — | Select initial network during Phase 4; no deployment authorization is granted | — |

## Exit gate for Phase 1

Phase 1 economics are ready for implementation planning only when:

1. TDR-01 through TDR-09 each have an explicit approved outcome, or a documented exclusion with rationale.
2. The quantitative model includes low/base/high exposure and a zero-top-up stress case, reports peak liabilities and reserve runway, and is reproducible from recorded inputs.
3. Every parameter in the model maps to a named approved schedule field; no test or contract default silently fills an open decision.
4. Each applicable ECON criterion has a concrete test oracle tied to the approved model and schedule.
5. The source/build baseline and any deployment or compatibility question are reconciled under Phase 1 of the remediation plan.

Until the owner-approved schedule and administrative authority specification exist, this record remains **PROPOSED / AWAITING OWNER APPROVAL**. No implementation depending on unresolved economic parameters may begin. Testnet selection remains deferred to deployment planning, consistent with the remediation plan.
