# SynergiX V1 Remediation Plan

**Status:** Proposed sequence. This plan does not claim that remediation has started, that the current checkout is production-ready, or that a deployment exists.

## Baseline and constraints

Use the current checkout and [`audit/REPORT.md`](../audit/REPORT.md) as the initial evidence baseline. The report is historical, explicitly `STATUS: INCOMPLETE`, and records unknown payout intent, no supplied deployment address, and unresolved economics, operations, and compatibility questions. It records successful compile and test commands for its audit-session working tree, while repository guidance warns that recovered source defects remain unresolved and requires separate build and security validation. Reconcile the exact source revision and these conflicting build-state claims before implementation; do not alter the historical report as part of this documentation change.

The proposed economic direction is in [`V1_ECONOMIC_SPEC.md`](V1_ECONOMIC_SPEC.md): escrow principal, separately funded rewards, solvency invariants, and an immutable non-upgradeable V1. Numeric parameters, supply policy, stake limits, and testnet are still undecided. Any discovered live deployment triggers a separate compatibility and migration assessment before choosing implementation or migration steps.

## Phases and exit gates

### 1. Preserve and establish the baseline

Record the exact commit and working-tree state; inventory contracts, tests, deployment scripts, configuration, dependencies, and existing audit artifacts. Reproduce the claimed build and test outcomes in a controlled local setup and resolve the discrepancy with repository guidance about source defects. Preserve the historical audit unchanged.

**Exit gate:** a reviewed baseline record identifies the precise source revision, reproducible build/test status, known source defects, and whether any deployment or deployed bytecode has been discovered. If a deployment is found, stop V1 implementation planning until its compatibility and migration assessment is complete.

### 2. Approve economics and implement the minimal V1

Resolve and approve every open decision in the economic specification, including reward parameters, supply policy, stake limits, referral rules, administrative authority, and a supported testnet. Translate those decisions into explicit interfaces and contract behavior. Implement only the agreed V1 scope: escrowed principal, separately funded reward liabilities, minimal administration, and immutable non-upgradeable contracts. Add focused tests alongside behavior changes.

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
