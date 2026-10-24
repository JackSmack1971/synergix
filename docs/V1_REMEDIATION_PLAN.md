# SynergiX V1 Remediation Plan

**Status:** Proposed sequence with a formal Phase 1 economics/authority hold point active. This plan does not claim that remediation is complete, that the current checkout is production-ready, or that a deployment exists.

## Baseline and constraints

Use the current checkout and [`audit/REPORT.md`](../audit/REPORT.md) as the initial evidence baseline. The report is historical, explicitly `STATUS: INCOMPLETE`, and records unknown payout intent, no supplied deployment address, and unresolved economics, operations, and compatibility questions. Its build/test results refer to an audit-session working tree. The original source baseline was `8de8af76e3e9b42abc92abe56e2756f7368f267d`; subsequent remediation source and tests were committed in `a9b63dc`, and the current checkout is `cce0031a2a22db9f7540be9966ce613e00f5c396`. `git diff --name-only a9b63dc..HEAD` contains no contract or test paths, so the current source tree matches the source/test snapshot covered by [`SECURITY_REMEDIATION_STATUS_2026-10-24.md`](SECURITY_REMEDIATION_STATUS_2026-10-24.md); the historical `npm run compile -- --force` result is not claimed as a fresh run at `cce0031`. `ISynergiXStaking.sol` contains only the interface. The full test inventory and V1 invariant gap analysis are in [`V1_BASELINE_VERIFICATION_2026-10-24.md`](V1_BASELINE_VERIFICATION_2026-10-24.md); the unit, integration, property-based, and adversarial test plan are in [`V1_INVARIANT_TEST_MATRIX.md`](V1_INVARIANT_TEST_MATRIX.md). This reconciles the stale duplicate-interface/build-defect warning in `AGENTS.md` for this checkout, but does not establish economic correctness or security approval. Preserve the historical audit unchanged.

The current continuation's exact `main` comparison, source changes, implementation regressions, and fresh build/test results are recorded separately in [`SECURITY_REMEDIATION_STATUS_2026-10-24.md`](SECURITY_REMEDIATION_STATUS_2026-10-24.md). Narrow source repairs have begun, but H-01 and the Phase 1 economics/authority hold remain open. Preserve the historical audit unchanged.

The proposed economic direction is in [`V1_ECONOMIC_SPEC.md`](V1_ECONOMIC_SPEC.md), with open decisions, sustainability sensitivities, and acceptance criteria in [`V1_TOKENOMICS_DECISION_RECORD.md`](V1_TOKENOMICS_DECISION_RECORD.md): escrow principal, separately funded rewards, solvency invariants, and an immutable non-upgradeable V1. Numeric parameters, supply policy, stake limits, and testnet are still undecided. Any discovered live deployment triggers a separate compatibility and migration assessment before choosing implementation or migration steps.

## Phases and exit gates

### Formal Phase 1 hold point — economics and authority

**HOLD:** Do not implement contract behavior that depends on unresolved economic parameters or administrative authority. The preferred candidate is scenario v0.4 / schedule v1.4 and remains unapproved. [`V1_ADMINISTRATIVE_AUTHORITY.md`](V1_ADMINISTRATIVE_AUTHORITY.md) is a proposed policy artifact, not an approved authority specification. [`V1_OWNER_DECISIONS.md`](V1_OWNER_DECISIONS.md) records TDR-01 through TDR-09 as lacking attributable decisions. Compatibility remains `COMPATIBILITY_UNDETERMINED` in [`V1_COMPATIBILITY_STATUS_2026-10-24.md`](V1_COMPATIBILITY_STATUS_2026-10-24.md). The unsigned [draft artifact manifest](V1_PHASE1_DRAFT_ARTIFACT_MANIFEST_2026-10-24.json) pins proposed file bytes but is not approval evidence. This hold point remains active until approval and all required review evidence are recorded.

The hold point does not block independent preparation. The following lanes may proceed without selecting tokenomics or deployment parameters:

- Source-integrity repairs based on defects reproduced in the current checkout, in their own scoped changes with build and security validation. The known duplicate interface/build-defect claims do not reproduce on the current checkout; forced compilation succeeds.
- Deployment-independent test planning. Map scenarios to the `ECON-*` criteria in the decision record, mark parameter-dependent oracles as pending, and do not hard-code placeholder economics as approved values.
- Security-control mapping. Map the conditional architecture direction and planned invariants to applicable control families while preserving the current audit statuses and the `STATUS: INCOMPLETE` conclusion.
- Documentation and baseline reconciliation that do not assert unapproved economics or deployment state.

**Release condition:** an accountable owner approves a versioned economic schedule covering supply/issuance, rewards and maximum liabilities, staking bounds and terms, funding shortfall behavior, and referral treatment, plus an administrative authority specification covering governance identities/custody, thresholds, timelocks, mutable controls, emergency actions, and withdrawal policy. Initial deployment network selection remains deferred to Phase 4.

### 1. Preserve and establish the baseline

Record the exact commit and working-tree state; inventory contracts, tests, deployment scripts, configuration, dependencies, and existing audit artifacts. Reproduce the claimed build and test outcomes in a controlled local setup and resolve the discrepancy with repository guidance about source defects. Preserve the historical audit unchanged.

**Exit gate:** a reviewed baseline record identifies the precise source revision, reproducible build/test status, known source defects, and whether any deployment or deployed bytecode has been discovered. If a deployment is found, stop V1 implementation planning until its compatibility and migration assessment is complete.

### 2. Implement the minimal V1 after hold-point release

Resolve and approve every open economic decision in the economic specification and [`V1_TOKENOMICS_DECISION_RECORD.md`](V1_TOKENOMICS_DECISION_RECORD.md), including reward parameters, supply policy, stake limits, referral rules, and administrative authority. Translate those decisions into explicit interfaces and contract behavior. Implement only the agreed V1 scope: escrowed principal, separately funded reward liabilities, minimal administration, and immutable non-upgradeable contracts. Add focused tests alongside behavior changes. Defer testnet selection to deployment planning in Phase 4.

**Exit gate:** approved, versioned economics exist; implementation matches them; source and configuration build reproducibly; reviewers can trace each privileged power and each economic parameter; no open decision has been silently assigned a value.

### 3. Validate economic and security invariants

Exercise principal deposits and withdrawals, reward funding and claims, reserve exhaustion, rounding and parameter boundaries, referral liabilities, pause behavior, and authorization. Test the solvency invariants in the economic specification across sequences of actions, not only isolated happy paths. Reconcile current audit findings and any newly found defects against the new design. Review the token and staking source together with deployment configuration.

**Exit gate:** required invariant and adversarial tests pass on the reviewed source revision; no unresolved critical or high-severity issue remains; any accepted residual risk has an owner and written rationale; an independent final security review is ready to begin. Passing tests alone is not security approval.

### 4. Deploy to the approved testnet

After selecting the testnet and completing prior gates, deploy the exact reviewed artifacts. Record chain ID, addresses, compiler and dependency versions, bytecode or build identifiers, deployer and role custody, initial reserve funding, and explorer verification. Exercise stake, maturity, withdrawal, reward claims, pause, and administrative operations using testnet transactions.

**Exit gate:** deployment artifacts and addresses are reproducible and verified; role custody and reserve balances match the approved configuration; end-to-end testnet evidence covers the intended lifecycle; no unexplained differences exist between reviewed and deployed bytecode.

### 5. Complete final security review and release decision

Review the frozen V1 source and testnet deployment against the approved economics, threat model, and all prior findings. Confirm there is no unassessed live-system compatibility issue, and document operational procedures for funding, monitoring, pausing, and incident response. This review must be independent of the implementation checks where practicable.

**Exit gate:** final review findings are resolved or explicitly accepted by accountable owners; economic and operational assumptions are documented; deployed bytecode is tied to reviewed source; release approval is recorded. Until this gate passes, the V1 is not approved for production release.

## Change control

Keep this work separately scoped from `audit/REPORT.md` and from generated/reference material. Update the economic specification when approved parameters change, with a version and decision record. Any change to deployed code or any discovered deployment follows its own compatibility, migration, and security review; this plan does not authorize an upgrade or migration.
