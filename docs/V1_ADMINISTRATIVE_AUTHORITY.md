# SynergiX V1 Administrative Authority and Custody Policy

**Status:** Proposed policy for accountable owner review — **no detailed rule in this document is approved**. Conditional architecture direction for escrowed principal, separately funded rewards, solvency, immutable versioned V1 contracts, and no administrator withdrawal of committed funds is recorded in [`V1_TOKENOMICS_DECISION_RECORD.md`](V1_TOKENOMICS_DECISION_RECORD.md); the directing user's identity and owner authority are unverified, so this is not attributable owner approval. This document evaluates candidate rules for TDR-02 and TDR-06–08 and their interactions with TDR-03–05 and TDR-09. It does not release the Phase 1 hold in [`V1_REMEDIATION_PLAN.md`](V1_REMEDIATION_PLAN.md).

**Version:** 0.2 draft, prepared 2026-10-24. This version identifies a proposal only; it has no accountable owner approval.

**Preferred candidate alignment:** schedule v1.4 proposes early exit with principal returned only and unpaid reward forfeited; paid referrals are zero. The recommended governance arrangement remains a 3-of-5 Safe with enforced 72-hour timelock, plus a separate 2-of-3 emergency Safe limited to new-stake pause for at most 72 hours. Signer thresholds, operational rules, custody, and all candidate parameters remain recommendations awaiting approval. No role may withdraw committed principal or reserved rewards.

No signer, owner, treasury, reserve, Safe, deployed address, signature, or operational configuration is established by this proposal. The proposed thresholds and numerical examples below are not approved parameters. The accountable owner must record each decision and evidence individually in the decision table at the end.

## Decision status and boundaries

| Topic | Present status | This document's treatment |
|---|---|---|
| Escrow principal returned at maturity; no mint substitute; administrators cannot withdraw committed funds | Conditional user direction only; identity and owner authority unverified | Preserve as a proposed design boundary; the detailed lifecycle below still needs attributable owner approval and implementation proof. |
| Stake limits: 100–100,000 SNX per position; 250,000 SNX per wallet; 16 active positions per wallet; 20M SNX globally | Open under TDR-06 | Evaluate as a candidate envelope; approve each bound and its address/accounting semantics separately. |
| Terms: 30/90/180 days | Open under TDR-04/TDR-06 | Evaluate as candidate terms; no reward rate or reward formula is implied. |
| Reward reserve, funding and liabilities | Conditional user direction recorded; identity/owner authority unverified. Details open under TDR-03–05/TDR-08–09 | Define measurable accounting and fail-closed behavior without choosing the reserve asset or reward schedule. |
| Governance, custody and emergency control | Open under TDR-07 | Evaluate 3-of-5 governance Safe, 72-hour timelock and separate 2-of-3 emergency Safe as proposals only. |
| Actual owner, signer identities, addresses, threshold deployment and chain | Not supplied / cannot verify | Blocking for Phase 4 configuration and any claim that governance is operational. Never fill with invented identities or addresses. |

## Candidate staking and withdrawal policy

### Candidate bounds for owner decision

The following candidate limits are internally compatible in the simple case of one EOA being the wallet identity: 16 positions each at the 100,000 SNX maximum imply at most 1.6M SNX per wallet, below the proposed 250,000 SNX wallet cap. The wallet cap is therefore the tighter aggregate bound; the position-count limit remains a separate operational/complexity bound. The 20M SNX global cap bounds aggregate principal but says nothing by itself about reward affordability. These observations do not prove the limits are desirable or sustainable.

| Candidate rule | Proposed value | Review and unresolved definition |
|---|---:|---|
| Minimum principal per position | 100 SNX | Consider whether transaction costs, decimals and user access justify this floor. |
| Maximum principal per position | 100,000 SNX | Must use integer base units and reject values outside the inclusive range atomically. |
| Maximum active principal per wallet | 250,000 SNX | Must define wallet identity. If positions are nontransferable, count by originating/beneficial address; a user can use multiple addresses, so this is not a person-level cap. Smart accounts, custody and address changes need explicit treatment. |
| Maximum active positions per wallet | 16 | Count open positions until principal has been paid and position closed. Define whether reward-only outstanding claims count; proposed answer: no, because they are separate liabilities. |
| Maximum active principal protocol-wide | 20,000,000 SNX | Sum outstanding principal, not reward reserve or lifetime deposits. Decrement only when principal is successfully returned. |
| Allowed fixed terms | 30, 90, 180 days | No arbitrary duration input. Do not infer reward rates or APR from terms. |

Bounds must be checked together with per-position and aggregate reward commitment limits under TDR-04/TDR-09. A stake that passes principal limits but cannot reserve its entire maximum reward liability must be refused atomically. Concurrent transactions must not exceed any aggregate limit.

### Entry-time entitlement and lifecycle

Candidate lifecycle, subject to individual owner approval:

1. At accepted entry, record the principal, chosen allowed term, entry timestamp, maturity timestamp, reward terms (if the reward schedule is approved), exact maximum reward liability reserved, and the staker/beneficiary address. Position terms are immutable thereafter.
2. Calculate maturity as `entryTimestamp + days * 86400` using checked integer arithmetic and Unix seconds. A position is mature when `block.timestamp >= maturityTimestamp`; there is no timezone or calendar-day interpretation. The exact block timestamp is the on-chain boundary.
3. Principal is an unconditional recorded liability from acceptance until successful repayment. Any reward formula is separately specified and reserved; reward schedule changes apply only to future entries and cannot change existing entitlements.
4. After maturity, the beneficiary may withdraw principal once. Candidate interface permits any caller to trigger payment to the recorded beneficiary, avoiding a keeper or beneficiary-transaction dependency; callers cannot redirect payment. Update the closed/withdrawn state and liability accounting atomically with the transfer. A failed token transfer reverts the full operation. Repeats revert and cannot pay twice.
5. Reward claims are separate from principal withdrawal and separate in accounting. The entitled beneficiary may claim only its recorded, vested/claimable amount, paid only from reward reserve. Candidate policy permits a third party to trigger payment only to the recorded beneficiary, with no caller fee. Whether reward claims are allowed before maturity depends on the approved reward schedule; no reward claim may draw on principal escrow.
6. Preferred candidate: early exit returns principal only and forfeits that position's unpaid reward. This is not approved. No administrator may accelerate, cancel, redirect, haircut, or rewrite an entitlement. Any early-exit implementation requires owner approval, user disclosure, reserve analysis, and security review.

**Required user disclosure if maturity-only withdrawal is approved:** principal is locked until its fixed maturity; the user cannot ordinarily exit early, even if they need liquidity, market conditions change, governance changes, or rewards are suspended. A pause, reserve incident, congestion, token transfer failure, or chain outage can delay on-chain execution. Once mature, principal withdrawal remains permissionless under the stated rule and must not depend on reward reserve availability or administrator action. This is a liquidity-risk disclosure, not a promise about transaction inclusion or asset value.

### Atomic refusal and accounting invariant

At stake acceptance, the contract must atomically verify all of the following before creating a position or moving tokens:

- caller/beneficiary and token transfer satisfy the approved asset assumptions;
- the position amount, wallet amount, position count, and global principal total remain within approved bounds;
- entry-time maturity and maximum reward liabilities are computable under approved integer arithmetic;
- sufficient uncommitted reward capacity exists for the full maximum commitment, including any approved referral component;
- principal is received in full and reward liability reservation succeeds in the same state transition.

If any check fails, the complete operation reverts: no tokens remain trapped, no position or referral attribution is created, and no principal/reward counters or events imply acceptance. Donations or unsolicited token transfers do not create user positions or reward commitments.

Maintain distinct ledgers for (a) outstanding principal liability, (b) reward reserve assets, (c) reserved maximum reward commitments, (d) accrued/claimable reward liabilities and (e) uncommitted reward capacity. Treasury assets are not reward reserve assets unless explicitly and observably transferred into the controlled reward-funding vault. Do not count the same asset in multiple categories.

## Objective reserve-discrepancy policy

### Trigger and immediate effects

The preferred trigger is a deterministic on-chain solvency predicate, not an administrator's opinion:

```text
principal_shortfall = principal_escrow_balance < outstanding_principal_liability
reward_shortfall = reward_vault_balance < reserved_or_accrued_reward_liability
accounting_discrepancy = any independently computable liability/reserve invariant fails
```

Balance and liability values are in the reserve asset's base units, at the same transaction state. If principal and rewards use the same token contract, accounting partitions must still prevent reward payout from consuming principal coverage. Any failed invariant has an immediate fail-closed effect for new stake acceptance. An affected reward claim is payable only if the transfer can be made without violating reward liability coverage and principal coverage. Where a reward asset is insolvent or its balance cannot be trusted, suspend that asset's reward payments until recovery; do not suspend principal withdrawals because of a reward-only discrepancy.

Prefer a public, permissionless `report/check` path or invariant checks directly in affected entry/claim functions, with an event containing the measured balances, liabilities, asset and reason. It must not let the reporter choose a pause scope or beneficiary. Automatic enforcement is more reviewable than requiring an administrator to notice a shortfall. A privileged operator must not be able to clear an objectively true discrepancy by assertion.

| Operation | While principal coverage fails | While reward coverage fails | While only new-stake pause is active |
|---|---|---|---|
| New stake | Refuse atomically | Refuse atomically | Refuse |
| Matured principal withdrawal | Continue independently, up to available escrow; never require reward solvency or admin approval | Continue independently | Continue |
| Reward claim from affected reserve | N/A if principal asset issue only, unless it would worsen principal coverage | Suspend payment from affected asset until objective restoration | Continue only if fully covered and unaffected by the pause |
| Reward claim from unaffected, fully covered reserve | Permit if all accounting invariants remain true | Permit | Permit |
| Funding/top-up | Permit and record actual received amount | Permit and record actual received amount | Permit |
| Administrative treasury withdrawal | No committed asset withdrawal | No reserve or committed asset withdrawal | Governed delay applies; cannot bypass liabilities or approved purpose |

If escrow is actually deficient, not every mature principal claim may be payable. Continue independent claims from available escrow on a first-valid-transaction basis unless an approved, legally reviewed distribution mechanism is specified; do not promise pro-rata fairness from transaction ordering. A shortfall does not authorize administrators to confiscate or haircut remaining entitlements. Identify the affected positions and deficit through on-chain accounting and publish a reconciliation incident record.

### Restoration and resumption

Restore affected reward payments and new stakes only when all of these are true:

1. An on-chain check confirms actual reserve balances cover every corresponding outstanding liability, including full remaining commitments under the approved reservation model.
2. Any unexplained balance/liability discrepancy has a reproducible reconciliation record with transaction references and an identified root cause; a top-up alone does not erase an accounting error.
3. The fix, if any, is limited to an approved immutable-version replacement/migration path; no retroactive entitlement mutation is used.
4. The solvency predicate is rechecked at the transaction that clears the restriction, so a stale off-chain report cannot restore operations while underfunded.

The safest rule is automatic re-enablement once the predicate is true, or a permissionless clear function that succeeds only if the predicate is true. If owner review requires a governance acknowledgement for a confirmed exploit or accounting incident, governance may delay reopening new stakes, but it may not keep otherwise solvent matured principal withdrawals or unaffected fully funded reward claims paused. No emergency Safe may clear a reserve hold. The governance decision must be observable and cannot override a failing invariant.

## Privileged-action authorization and pause matrix

Proposed V1 is immutable and has no proxy upgrade, arbitrary mint, admin principal withdrawal, open-position editing, or discretionary reward-rate change. “Governance Safe” below is a candidate 3-of-5 Safe, not an existing or configured Safe. The 72-hour delay must be enforced on-chain by a timelock whose proposer/executor/admin paths cannot bypass it. A Safe signature alone must never execute a delayed action.

| Callable action / path | Who may authorize/call | Delay / scope | During emergency new-stake pause | During reserve discrepancy | Proposed decision status |
|---|---|---|---|---|---|
| Create stake | Any user for self (or approved smart account) | No admin approval; checks all limits and reserve predicate atomically | Refuse | Refuse if relevant solvency predicate fails | Candidate policy; bounds open |
| Matured principal withdrawal | Beneficiary or any caller; destination fixed to beneficiary | Permissionless after maturity; no timelock | Always available | Continue independently from available escrow | Required path for owner approval; architecture principle supports it |
| Claim approved reward | Beneficiary or any caller; destination fixed to beneficiary | No admin approval; claim amount bounded by recorded entitlement and reserve | Available if fully funded and unaffected | Suspend only the affected undercovered reward asset/path | Accounting and reward timing open |
| Fund reward vault | Any approved token transfer/funder; no privileged role needed to add assets | No delay for inbound funding; amount actually received is recorded | Available | Available | Funding source/asset open |
| Pause new staking (emergency) | Candidate separate 2-of-3 Emergency Safe | Immediate; on-chain expiry no later than 72 hours from activation; only blocks new positions | This action creates the pause; it cannot block withdrawals/claims | Cannot clear or widen a reserve restriction | Proposed; identities/configuration open |
| Lift emergency pause early | Governance through timelock, or automatic expiry | Timelock applies to governance early-lift; expiry is automatic at 72h | Permitted; does not clear reserve invariant | Does not clear reserve restriction | Proposed; interaction needs owner approval |
| Extend/restart emergency pause | Emergency Safe cannot extend an active pause or restart it to evade continuous 72h limit. Governance may impose a new pause after 72h through the 72h governance timelock. | No emergency repeat path | New governance action subject to delay | Cannot alter discrepancy state | Proposed; confirm whether governance pause is desired |
| Set future-only parameters, if any | Governance Safe via timelock | Minimum 72-hour enforced delay; immutable V1 preference is no mutable economics. Only a pre-approved allowlist and bounded ranges may be exposed. | Cannot alter pause, existing positions or withdrawals | Cannot clear failing solvency predicates; no new stake while deficient | Open; default candidate is no such action |
| Treasury disbursement | Treasury controlled vault only through governance Safe + enforced timelock; recipient/purpose/amount fixed in queued operation | At least 72 hours from final operation hash; no alternate owner/guardian/ Safe route; cancel is allowed, bypass execution is not | Unaffected only if no conflict with pause incident; cannot touch user liabilities/reserve | Prohibit any transfer that would reduce reserve coverage or principal coverage | Candidate controls; asset budget and permitted purpose open |
| Reward reserve transfer out | No role for committed/reserved assets. Excess withdrawal only if an approved excess rule exists and post-transfer invariant remains covered; candidate default is no withdrawal path. | If ever allowed, governance timelock plus objective on-chain excess check; never emergency | Cannot affect principal or claims | Refuse while any relevant discrepancy exists | Open; safest proposed default is disabled |
| Change treasury/reward-vault controller or timelock config | Governance Safe through current enforced timelock; no self-service bypass | At least 72 hours, with old configuration still controlling execution | Cannot broaden emergency scope | Cannot clear/transfer liabilities | Open; strongly prefer immutable controller configuration in V1 |
| Rotate governance/emergency signers | Governance Safe through timelock with threshold met by the currently configured Safe | At least 72 hours; validate replacement Safe and threshold before execution | No effect on user exits | No effect on reserve predicate | Open; requires identified, independently verified replacement custody |
| Recover lost signer access | Only through preconfigured, delayed governance Safe recovery path; no unilateral admin recovery | Timelock applies; if quorum is lost, no privileged recovery is possible absent a separately approved mechanism | Emergency Safe cannot recover governance control | Cannot alter liabilities or claims | Blocking decision; no recovery guardian is assumed |
| Deployer-role handoff / renounce | Current deployer may only transfer residual setup authority to the verified governance/timelock addresses, then renounce all temporary roles. Must be one-way and logged. | Before user funds/production use; governance delay if after launch | Cannot use deployer role to pause/withdraw | Cannot override invariant | Required deployment gate; actual deployer/address unknown |
| Mint, upgrade, withdraw principal, edit open position, redirect beneficiary, cancel entitlement, haircut entitlement | No caller or role exists in proposed immutable V1 | Not available | Not available | Not available | Prohibited by proposed policy; architecture forbids committed asset extraction |

### Privileged-action verification crosswalk

This table maps every privileged or custody-sensitive action above to the proposed economic criteria and the security/adversarial evidence needed. It describes draft controls; it does not grant or approve any role.

| Action | TDR | ECON criteria | Security invariants | Required adversarial verification |
|---|---|---|---|---|
| User creates stake (permissionless, custody-sensitive) | 01, 03, 04, 05, 06, 09 | ECON-01/03/05/08/11/12 | SEC-04/05/07/09 | Concurrent reserve/principal boundary, referral expansion, reentrancy, fee-on-transfer, and atomic rejection. |
| Beneficiary or caller returns matured principal | 02, 06, 08 | ECON-01/02/04/06/12 | SEC-02/04/08/09 | Duplicate, reentrant, wrong-destination, pause, reward-reserve depletion, and token-transfer failure. |
| Beneficiary or caller claims approved reward | 03, 04, 05, 08, 09 | ECON-03/04/05/06/08/11/12 | SEC-02/04/07/09 | Same-timestamp claims, reserve race, referral rounding, payout failure, and principal coverage after each serialized transition. |
| Fund reward vault | 03, 07, 08 | ECON-03/05/12 | SEC-01/04/09 | Unauthorized funder; false-return, fee-on-transfer, callback, and reverting asset; actual received balance must match credit. |
| Pause new staking | 07, 08 | ECON-06/10/12 | SEC-01/02/08 | Unauthorized caller, pause expiry, repeat/extension attempts, and matured-principal/funded-claim liveness. |
| Lift, expire, extend, or restart pause | 07, 08 | ECON-06/10/12 | SEC-01/02/08 | Timelock bypass, premature lift, emergency renewal, governance restart, and pause-state race. |
| Set future-only parameters | 04, 06, 07 | ECON-08/09/10/12 | SEC-01/02/07/08 | Unauthorized/malformed value, timelock bypass, boundary value, and proof existing positions remain unchanged. |
| Treasury disbursement | 01, 03, 07, 08 | ECON-03/04/05/06/07/12 | SEC-01/02/03/09 | Compromised quorum, alternate Safe module/controller path, queued-operation mutation, and reserve/principal coverage after execution. |
| Withdraw excess reward reserve | 03, 07, 08, 09 | ECON-03/04/05/06/12 | SEC-01/02/07/09 | Concurrent stake/claim race, stale excess calculation, discrepancy state, and post-transfer reserve predicate. Default proposal is no withdrawal path. |
| Change vault controller or timelock configuration | 07 | ECON-09/10/12 | SEC-01/02/03/08 | Direct owner, guardian, module, delegate-call, or emergency bypass; verify old controller remains effective through the delay. |
| Rotate governance/emergency signers | 07 | ECON-09/10/12 | SEC-01/02/08 | Threshold takeover, signer replacement validation, malicious module, and role-separation failure. |
| Recover lost signer access | 07 | ECON-09/10/12 | SEC-01/02/08 | Lost-quorum and collusion scenarios; no recovery authority may seize principal or rewrite entitlements. |
| Deployer-role handoff / renounce | 07 | ECON-09/10/12 | SEC-01/02/03 | Incomplete handoff, residual deployer authority, wrong custody destination, or renounce-before-safe-handoff. |
| Mint, upgrade, withdraw principal, edit positions, redirect beneficiaries, cancel or haircut entitlements | 01, 02, 07, 09 | ECON-01/02/04/06/07/09/12 | SEC-01/02/03/08 | Enumerate every role, proxy, token, vault, and direct-call bypass; prove no privileged path can create supply, extract committed assets, or alter existing terms. |

The ECON/SEC identifiers resolve to the acceptance and invariant oracles in [`V1_TOKENOMICS_DECISION_RECORD.md`](V1_TOKENOMICS_DECISION_RECORD.md) and [`V1_INVARIANT_TEST_MATRIX.md`](V1_INVARIANT_TEST_MATRIX.md). Until approved roles and a V1 implementation exist, each verification row remains pending.

The pause is deliberately narrow: it stops creation of new positions only. It does not pause matured principal return, cannot pause token transfers globally, cannot change terms, and cannot grant mint/upgrade/withdrawal authority. The reserve-solvency guard is a separate objective restriction on new stakes and affected reward payments; it does not authorize an administrator to block independent matured principal withdrawals.

### Timelock and treasury bypass requirements

The candidate 72-hour governance timelock is meaningful only if contract execution enforces it. Before implementation/deployment review, verify all of the following from exact source and deployed configuration:

- Every governance-controlled treasury transfer, controller change and allowed mutable parameter change passes through the same enforced delay; direct Safe ownership, fallback handlers, modules, delegate calls, guardians, alternate owners, or emergency roles cannot execute around it.
- The operation hash binds target, value, calldata, predecessor, salt, and chain context. Changing any field requires a new queue and a fresh 72-hour wait.
- Cancellation may prevent execution; no actor can shorten, skip, or retroactively satisfy the delay. Execution checks the queued timestamp and current operation state.
- Treasury and reward funding vaults are distinct custody/accounting domains. A treasury transfer into the reward vault is a new, observable funding event; it does not create authority to withdraw user liabilities back out.
- No vault administrator can transfer principal escrow or reserved reward assets. A proposed excess-recovery path, if approved, must prove post-transfer solvency on-chain at execution, after all concurrent commitments and claims are accounted for.
- Timelock proposer/executor/admin roles are enumerated. Their initial assignment and all later changes are delayed or permanently fixed; no bootstrap owner remains able to call the target directly.

## Proposed custody model and deployment blockers

| Custody item | Candidate arrangement | Evidence still required before Phase 4 |
|---|---|---|
| Governance | 3-of-5 Safe; control of a 72-hour timelock | Safe address, chain ID, exact five signer identities and addresses, threshold/configuration inspection, module/guard/fallback inventory, timelock address/code/config, independent verification and recorded transaction evidence. |
| Emergency | Separate 2-of-3 Safe; only new-stake pause for a maximum 72 hours | Safe address distinct from governance Safe, three named signer identities and addresses, code-level permission proving it can call only the bounded pause, expiry behavior, no renewal route, independent config verification. |
| Treasury vault | Controlled treasury custody, spending only through governance Safe + timelock | Address, asset balances, approved purposes/limits/beneficiaries, signer and operational process, on-chain enforcement and reserve separation. |
| Reward-funding vault | Separately accounted reward funding; receives only approved funding; no committed-fund withdrawal | Address and asset, funding authority/source, liability accounting, signer access, proof its controller cannot extract reserve or principal; reconcile on-chain balances against liabilities. |
| Principal escrow | Immutable staking contract accounting; no administrator withdrawal selector | Reviewed source/bytecode and address, actual token behavior, principal liability reconciliation, no upgrade/admin escape path, withdrawal behavior verified on approved network. |
| Deployer/bootstrap | Temporary setup authority only | Actual deployer identity/address, complete grant inventory, proof all final roles point to verified governance/timelock/emergency addresses, temporary role revocation/renunciation transaction and post-handoff verification. |

Actual signers must be identifiable people/entities with authority to accept their role, not anonymous placeholder labels. Require unique, hardware-backed signing devices, independently stored recovery material, geographically/organizationally separated custodians where practical, and no shared seed phrase or single person controlling threshold. Record device custody and signer replacement process without publishing secret material. Do not put private keys, seed phrases or recovery shares in this repository.

Lost-key procedures must be approved before deployment. The proposed governance Safe can rotate a lost signer only while the remaining signers still meet the existing threshold and then only after the timelock. A lost quorum has no safe unilateral recovery route under this proposal. The owner must choose either (a) accept unrecoverable governance and deploy a new immutable version under an approved migration, or (b) approve a narrowly scoped recovery mechanism with its own independent threshold, delay, expiry, and threat analysis. The Emergency Safe is not a governance recovery mechanism. No person may claim recovery capability without verified configured code and custody evidence.

Phase 4 must verify network and chain ID, Safe addresses and exact owners/thresholds, signer identity-to-address attestations, hardware-custody procedure, timelock code and delay, vault controllers and balances, deployed bytecode/source match, role grants, deployer handoff, and test transactions for pause expiry and user withdrawal. The preferred BASE network mentioned elsewhere remains only a preference; this document does not select a network or authorize deployment.

## Interactions with decision records

| TDR | Interaction captured here | Still open |
|---|---|---|
| TDR-02 | Entry snapshot, fixed maturity, exactly-once permissionless principal return, no admin extraction | Exact owner approval, asset transfer assumptions, pause/recovery and legacy obligations |
| TDR-03 | Separate reserve/funding vault and full prefunding before promise | Asset, funding source, accounting and actual custody |
| TDR-04 | Position reward terms immutable; reward claim separate | Rate/formula, timing, rounding, maximum liability, claim timing |
| TDR-05 | Referral reward, if approved, is part of same atomic fully funded commitment and same liability limits | Include/exclude, eligibility, beneficiary and cap |
| TDR-06 | Candidate amount/count/duration bounds; maturity-only exits and explicit liquidity-risk disclosure | Approve/revise each candidate bound and exact wallet semantics |
| TDR-07 | Candidate governance/emergency Safes, timelock, narrow pause, no admin extraction | Names, addresses, thresholds, custody, mutable actions, recovery and handoff |
| TDR-08 | Objective balance/liability triggers, atomic refusal, affected reward suspension, objective recovery | Reserve asset and final accounting oracle; owner approval of incident/resumption operations |
| TDR-09 | Full base plus referral liability reserved atomically; no shared headroom overcommitment | Cap and detailed concurrent liability formula |

## Owner decisions and approval evidence

No approvals are inferred from the conditional architecture approval, legacy code/tests, a repository commit, or this proposal. Record each disposition separately; `OPEN` is the current state for every row below.

| Decision | Proposed disposition for review | Approver / role | Date | Rationale / evidence reference | Approved version | Status |
|---|---|---|---|---|---|---|
| D-01 Position minimum / maximum (100 / 100,000 SNX) | Evaluate candidate bounds; approve or replace | Not supplied | — | Required: economic owner decision plus integer-unit boundary examples | — | OPEN |
| D-02 Wallet aggregate / active position cap (250,000 SNX / 16) | Evaluate; define wallet identity and position counting | Not supplied | — | Required: address/account semantics, multi-address limitation, test oracle | — | OPEN |
| D-03 Protocol principal cap (20M SNX) | Evaluate active-liability cap | Not supplied | — | Required: concurrency and reward stress scenarios under TDR-04/09 | — | OPEN |
| D-04 Terms and maturity rule (30/90/180 days; `timestamp + days*86400`) | Evaluate fixed entry-time maturity and exact boundary | Not supplied | — | Required: owner approval and lifecycle/boundary examples | — | OPEN |
| D-05 Early exit returns principal only; unpaid reward forfeited; exactly-once principal return | Candidate policy | Not supplied | — | Required: owner approval, user terms, reserve and ECON-01/02/06/10 mapping | — | OPEN |
| D-06 Atomic reserve refusal and reserve discrepancy behavior | Proposed objective triggers, affected reward suspension, new-stake stop, principal-withdrawal independence | Not supplied | — | Required: TDR-03/08 asset/accounting oracle, recovery record and adversarial review | — | OPEN |
| D-07 Governance Safe / timelock (3-of-5 / 72 hours) | Evaluate candidate controls | Not supplied | — | Required: named accountable signers, address/config evidence, no-bypass proof and permitted action list | — | OPEN |
| D-08 Emergency Safe (separate 2-of-3; new-stake pause <=72 hours) | Evaluate narrow temporary pause | Not supplied | — | Required: named signers, exact on-chain expiry/no-renew rule and no broader permissions | — | OPEN |
| D-09 Treasury/reward vaults, recovery, signer custody and deployer handoff | No actual arrangement approved | Not supplied | — | Required: vault purpose/balances, hardware custody, lost-key decision, role handoff evidence | — | BLOCKING / OPEN |
| D-10 Chain and deployed configuration | Defer to Phase 4; BASE is preference only | Not supplied | — | Required: network/chain ID, addresses, bytecode/config and independent verification | — | DEFERRED; BLOCKS DEPLOYMENT |

The Phase 1 hold remains active until an accountable owner approves the needed economic schedule and this administrative policy, with attributable approvals and reconciliation against the owner ledger. TDR-10 remains deferred to Phase 4. No approval, custody, or deployed state is claimed here.
