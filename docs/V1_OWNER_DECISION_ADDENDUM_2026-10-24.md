# V1 owner decision addendum — 2026-10-24

**Source revision:** `e13f7fceec35849bf2f85e390206138dacd7bd29` (`origin/main`).
**Decision-maker:** JackSmack1971, project owner per the existing in-session owner attestation in `docs/V1_TOKENOMICS_DECISION_RECORD.md`. This addendum records the owner's statements in this conversation; it is not a wallet signature or external identity verification.

## Legacy deployment and obligations

The owner states that the contracts have not been deployed and confirms there are no existing holders, presales, written staking promises, or other enforceable obligations tied to the legacy contracts. No project deployment address is present in the inspected repository sources or deployment records. The absence of a deployment is an owner attestation supported by repository evidence, not an independent chain-wide proof. On this basis, legacy H-01 is retired from the planned V1 remediation scope and retained as a historical source defect. The legacy contracts must not be deployed as a substitute for V1.

## PAY-07 — independent principal and reward claims

The owner selects separate principal withdrawal and reward claim operations for a matured V1 position. A failed or unavailable reward transfer must not make the principal entitlement unclaimable when the token can transfer the principal amount. Each entitlement can be settled at most once by its beneficiary at or after the recorded maturity timestamp. A failed claim leaves that entitlement and its liability unchanged for a later retry.

This decision does not select a reward rate, duration, stake bound, reserve cap, early-exit policy, token behavior beyond the existing exact-transfer assumptions, or reserve-loss recovery mechanism. A token pause, blacklist, or failure affecting all transfers can still prevent principal transfer; this slice does not claim to override token-level restrictions.

## Implementation authorization and boundary

The owner authorizes this single source-and-test slice on a branch based on the stated source revision: split matured V1 principal and reward settlement, add regression coverage for each independent entitlement and reward shortfall, and update the security evidence. This is not authorization to deploy, migrate, merge, select numeric economics, or release the contracts.
