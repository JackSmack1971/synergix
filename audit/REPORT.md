STATUS: INCOMPLETE
Blocker: The full per-control OWASP test inventory, independent chain-state verification, and broad invariant/fuzz coverage remain incomplete. The owner attests that no legacy contracts or obligations exist; that statement has not been independently verified against every chain or off-chain record.

## 1. Executive summary

This source review covers base revision e13f7fceec35849bf2f85e390206138dacd7bd29 and the one-slice follow-up in this PR. It reviewed four production Solidity sources, local tests, the bundled OWASP reference pack, and prior static-analysis output. The owner attests that no contracts are deployed and no legacy holders, presales, written staking promises, or enforceable legacy obligations exist; the repository contains no deployment addresses, but the attestation is not independent chain-wide proof. H-01 remains a verified legacy source defect and is retired from new V1 scope under that owner decision. The V1 combined settlement failure is fixed by separate principal and reward claims, with regression coverage for reward transfer failure and reserve shortfall. No Critical or High active finding remains in this bounded slice; broader checklist, deployment and economic review remains incomplete.

Residual risks are privileged uncapped mint authority in the legacy token source, unresolved V1 numeric and administrative policy, possible token-level transfer restrictions, and incomplete broad security coverage. PR #7 is closed/merged at the audited base and has no submitted GitHub reviews; that prior merge is not treated as security approval.

## 2. Scope and assumptions

Audited base revision: e13f7fceec35849bf2f85e390206138dacd7bd29 (`origin/main`); final PR revision is recorded in the PR description. The owner attests no deployment or legacy obligations exist. No addresses, chain IDs, role-holder snapshot, or off-chain commitment ledger were independently available. Trust assumptions include privileged legacy token admins and staking owner/default-admin/operators. Compiler configuration includes legacy sources on solc 0.8.26 and V1 on solc 0.8.38; EVM target is Paris. Hardhat 2.29.1, ethers 5.8.0, OpenZeppelin 4.9.6 and the OpenZeppelin 5.7.0 alias were observed.

| File | LOC | Scope note |
|---|---:|---|
| contracts/SynergiXToken.sol | 189 | UUPS ERC20, role-gated minting, staking wrapper |
| contracts/SynergiXStaking.sol | 427 | Legacy custody, daily payout indexing, referrals, privileged settings |
| contracts/ISynergiXStaking.sol | 22 | Legacy staking interface |
| contracts/SynergiXStakingV1.sol | 217 | Immutable-parameter, prefunded position staking |

Tests and test token doubles are supporting evidence, not production audit scope. Excluded: frontend/off-chain operations, deployment configuration as proof of live state, key custody, bridges/oracles absent from source, and any claim about a deployed instance.

Baseline and focused evidence:

- At local revision 6496f7d: npm ls --depth=0 exited 0; npm test exited 0 with 23 passing and 1 pending; npm run compile -- --force exited 0 with 39 Solidity files compiled for Paris.
- At merged PR tree e13f7fc in a detached validation worktree: npm test exited 0 with 35 passing and 1 pending; npm run compile -- --force exited 0 with 55 Solidity files compiled for Paris. Hardhat warned that 0.8.38 is not fully supported and reported OpenZeppelin 4 assembly-annotation deprecations.
- Pre-change M-01 reproduction on a clean detached e13f7fc worktree: a temporary local test and test-token balance-reduction hook produced the expected combined-withdrawal revert with principal still covered; 1 passing. The temporary test and fixture edit were removed after capture.
- Final implementation worktree: `node scripts/hardhat.js test test/SynergiXStakingV1.test.js` exited 0 with 12 passing; `npm test` exited 0 with 36 passing and 1 pending; `npm run compile -- --force` exited 0 with 55 Solidity files compiled for Paris. The pending test is the legacy epoch-dependent positive payout case.
- Focused legacy PoC: node scripts/hardhat.js test test/poc/H-01.test.js exited 0, 1 passing. Epoch-aligned positive payout tests exited 0, 2 passing.
- Slither ran from the V1 worktree with --exclude-dependencies, analyzed 53 contracts with 102 detectors, and printed 40 results; the wrapper returned exit -1. Findings remain tool flags, not validated vulnerabilities. Coverage and stateful invariant fuzzing were not run.

## 3. Threat model and invariants

Assets are SNX principal escrowed by legacy and V1 staking, V1 reward-reserve SNX, and token total supply. Actors include stakers/referrers, the legacy owner/default admin/operator, token ADMIN_ROLE and STAKING_ROLE holders, the V1 token selected at construction, and tokens that may call back or return nonstandard transfer results. Time affects maturity and legacy day indexing. No oracle, bridge, signature, AMM, or native-asset path was found in the reviewed sources.

| Invariant | Observation/test | Status | Evidence |
|---|---|---|---|
| Only STAKING_ROLE can mint through the token mint entry point | Role-gated mint and positive/negative tests | PASS | contracts/SynergiXToken.sol:94-96; test/SynergiXToken.test.js |
| A legacy matured claim remains reachable with only the current daily record | Claim indexes dailyData with Unix-day number; local PoC observes Invalid end day index | FAIL (historical source; owner attests no legacy deployment/obligations) | contracts/SynergiXStaking.sol:222-230; test/poc/H-01.test.js; owner addendum |
| Legacy aligned payout can close a stake once | Epoch-aligned test passes; principal remains escrowed while payout is minted | PASS | test/poc/positive-payout.test.js; contracts/SynergiXStaking.sol:153-179 |
| V1 principal and reward liabilities settle independently once after maturity | Focused tests cover both claim orders, zero reward, reserve shortfall and retry | PASS for tested cases | contracts/SynergiXStakingV1.sol; test/SynergiXStakingV1.test.js |
| Failed/reentrant token calls cannot duplicate or erase a V1 entitlement | Transfer failures roll back the attempted entitlement; callback guard tests pass | PASS for selected cases | contracts/SynergiXStakingV1.sol; test/SynergiXStakingV1.test.js |
| Effective proxy layout and roles match any deployed instance | No deployment data or historical storage comparison supplied | NOT TESTED | No address, bytecode, role snapshot, or upgrade history |

## 4. Findings

### H-01 — Unix-day indexes can block ordinary matured legacy claims (retired from V1 scope)

Severity: High source-level behavior; no active deployment impact per owner attestation.
Impact: A matured claimant's legacy stakeEnd reverts before closing the position or paying the claimant if the schedule is not fully backfilled.
Likelihood: Not applicable to current deployment scope per owner attestation; latent if legacy contracts are deployed.
Confidence: High in the demonstrated code-path failure; unknown for any deployed instance.
Calibration: [VERIFIED: PoC executed + output]
SCWE: SCWE-083, general edge-case mapping only; https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-083/.
SCSVS: SCSVS-DEFI-1; https://scs.owasp.org/SCSVS/controls/SCSVS-DEFI-1/.
Locations: contracts/SynergiXStaking.sol:222-230 computes Unix-day indexes and uses them directly as dailyData array indexes. The array is appended one record at a time at contracts/SynergiXStaking.sol:416-424 without a day key or epoch offset. The claim route is contracts/SynergiXStaking.sol:153-179 and the token wrapper is contracts/SynergiXToken.sol:119-126. The endDayIndex < dailyData.length guard does not map a current day to an array row.
Root cause: A Unix-day ordinal is used as a zero-based append-array position, while append history has no explicit epoch offset or day-key mapping.
Attack scenario: (1) A user stakes through the public token wrapper and waits until maturity. (2) The schedule contains only the current appended daily row, as reproduced locally. (3) The end index is the Unix-day count, which exceeds the one-row array length, and stakeEnd reverts with Invalid end day index. No attacker capital or privileged call is needed beyond an ordinary accepted stake; the owner/keeper schedule is an environmental precondition.
PoC: EXECUTED locally: node scripts/hardhat.js test test/poc/H-01.test.js exited 0, 1 passing. Output: the assertion observed Invalid end day index. The focused epoch-aligned test also exited 0 with 2 passing.
Falsification: An epoch-aligned fixture with rows at indexes 0 and 1 completes a payout, showing backfilled/aligned data can avoid this specific revert; it does not disprove the ordinary current-day failure.
Impact detail: The legacy position remains open and principal remains held by the legacy contract; legacy payout mints rather than transfers principal, and approved legacy settlement intent is unknown.
Recommendation: Do not deploy the legacy contracts. Preserve H-01 as a historical source defect; any future legacy deployment or discovered obligation requires a separate rights, payout and migration decision.
Disposition: RETIRED_FROM_V1_SCOPE based on owner attestation recorded in docs/V1_OWNER_DECISION_ADDENDUM_2026-10-24.md. This does not fix the legacy source or independently verify every chain/off-chain record.
Regression risk: Changing historical reward semantics may alter entitlements.
Status: OPEN

### M-01 — Reward payout failure can block or consume principal coverage

Severity: Medium, conditional on a reward shortfall or reward-only transfer failure while principal remains transferable.
Impact: The original `withdraw` transfers `principal + reward` together; a reward failure blocks principal return. A first split-claim implementation also allowed partial reserve loss to be consumed by successive reward claims, leaving principal undercollateralized. The final diff rejects a reward claim unless remaining balance will cover all principal liabilities.
Likelihood: Low under the intended fully reserved, exact-transfer token model; conditional on reserve loss or token-specific reward transfer restriction.
Confidence: High for the original combined-payout reproduction and the partial-shortfall counterexample.
Calibration: [VERIFIED: pre-change reproduction, independent review counterexample, and final regression output]
SCWE: SCWE-083, general edge-case mapping only; https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-083/.
SCSVS: SCSVS-DEFI-1; https://scs.owasp.org/SCSVS/controls/SCSVS-DEFI-1/.
Locations: Base `contracts/SynergiXStakingV1.sol:187-215` combines both liabilities in one transfer. Searched the base source with `rg -n 'principal.*reward|withdraw\\(' contracts/SynergiXStakingV1.sol`; no guard exists to preserve principal independently, and no separate principal claim path was found. Final `claimReward` enforces aggregate principal coverage before transfer at `contracts/SynergiXStakingV1.sol:240-244`.
Root cause: Combined settlement couples principal return to reward delivery; without a principal-coverage invariant, independent reward transfers can consume assets backing other positions' principal after partial reserve loss.
Attack scenario: (1) Two matured positions each hold principal 100 and reward 10. (2) External loss reduces token balance from 220 to 210 while principal liability is 200. (3) Without a guard, two successive reward claims reduce balance to 190, so the remaining principal claim fails. The owner has now selected ECON-04 principal priority; final code blocks the second reward claim until principal is returned or assets restored.
PoC: Base reproduction on e13f7fc passed by observing `insufficient balance` while the staking balance equaled principal; temporary test was removed. Independent review reproduced the two-position partial-loss counterexample on intermediate head effab999. Final `test/SynergiXStakingV1.test.js` adds that scenario and asserts `PrincipalCoverageRequired`, successful principal returns, and reward retry after reserve restoration.
Falsification: With full reserve and exact-transfer token, both entitlements settle; this does not disprove shortfall behavior. The principal-coverage check prevents the reviewed partial-loss counterexample but cannot recover external losses.
Impact detail: The owner selected that reward claims may remain unavailable after a reserve loss while principal is outstanding; token-level restrictions affecting all transfers can still block both operations.
Recommendation: Preserve separate, at-most-once claims and enforce ECON-04 before each reward transfer.
Regression risk: The settlement ABI and position tuple changed. The owner states V1 is not deployed; no on-chain storage migration is required for the current scope. Existing integrations must use the new function names. TDR-08 loss behavior is clarified for principal priority in the owner addendum.
Status: OPEN

## 5. Centralization and trust risks

The token ADMIN_ROLE can grant roles and authorize UUPS upgrades; STAKING_ROLE can mint arbitrary amounts without an on-chain cap (contracts/SynergiXToken.sol:89-96,168-175). The legacy staking owner can supply daily reward rows, alter settings and referral mappings, and administer operator roles (contracts/SynergiXStaking.sol:201-300,362-424). These are privileged economic controls, not independently validated unprivileged exploits. The owner attests there is no deployment; role holders, multisig and timelock are not independently verified.

The legacy maturity flow mints the calculated payout and leaves escrowed principal in staking. The owner states there are no legacy deployments or obligations; this decision does not approve that behavior for future deployment. V1 is separate and has no migration path. No administrative rescue or migration operation is authorized.

## 6. Invariant, test, and OWASP coverage

The bundled OWASP pack was present; its manifest identifies an OWASP SCS corpus fetched 2026-10-24. Current edition pages include SCSVS and SCSTG sources and SC Top 10 2026; archived 2025 pages are distinct. Coverage below is a focused source-backed sample, not a complete per-control inventory. The full set of applicable controls/tests remains NOT TESTED pending a complete mapping.

| Category | Control/test | Status | Evidence | Finding |
|---|---|---|---|---|
| DeFi staking | SCWE-083 Failure to Handle Edge Cases; SCSVS-DEFI-1 | FAIL | contracts/SynergiXStaking.sol:222-230; executed H-01 PoC | H-01 |
| V1 payout isolation | Principal and reward claim independently under reward shortfall | PASS | contracts/SynergiXStakingV1.sol:193-265; focused regression tests | M-01 |
| Principal solvency | Reward claims cannot reduce balance below aggregate principal liabilities | PASS | contracts/SynergiXStakingV1.sol:240-244; multi-position partial-shortfall regression | M-01 |
| Architecture/upgrade | SCSVS-ARCH-2; SCSTG-TEST-0007 | NOT TESTED | contracts/SynergiXToken.sol:18,89; test/poc/upgrade-validation.test.js; deployed layout absent | — |
| Authorization | SCSVS-AUTH-2; selected mint path | PASS | contracts/SynergiXToken.sol:89-96; test/SynergiXToken.test.js | — |
| External token | SCSVS-COMP-2; SCSTG-TEST-0012 | NOT TESTED | SafeERC20 and exact-receipt checks at contracts/SynergiXStaking.sol:116-128; rebasing/blacklist behavior not tested | — |
| Reentrancy | SC Top 10 SC08:2026; SCSVS-CODE-3 | NOT TESTED | contracts/SynergiXStaking.sol:116,153; contracts/SynergiXStakingV1.sol:145,187; selected callback paths only | — |
| Economic/business logic | SCSTG-TEST-0015; SCSTG-TEST-0016 | NOT TESTED | No approved legacy payout schedule; no stateful reference-model or fuzz run | — |
| Unbounded work | SCWE-109 | NOT TESTED | Referral and active-position scans lack a proven maximum; finite gas profiles only | — |
| Deployment and upgrade state | SCSVS-ARCH-2 | NOT TESTED | No chain/address/implementation/role snapshot | — |
| Compiler | SCSTG-TEST-0010; SC Top 10 SC09:2026 | NOT TESTED | Forced compile succeeded; Slither compiler-range flag is unvalidated and returned exit -1 | — |

Source URLs for the mapped controls: https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/; https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-2/; https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-2/; https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-3/; https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/; https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0004/; https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/; https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/; https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/; https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/; https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/; https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/.

## 7. Discarded candidates

- Privileged unlimited mint: confirmed capability at contracts/SynergiXToken.sol:94-96, but only callable by STAKING_ROLE and role administration is privileged. No cap or approved supply rule is established for the legacy contract, so this is recorded as a centralization/economic decision risk rather than an unprivileged vulnerability.
- V1 atomic principal-plus-reward settlement: owner has now selected separate principal and reward claims for PAY-07; M-01 is addressed in this PR. Numeric terms remain open but are constructor supplied and unchanged here.
- Unbounded referral ancestry and active-position loops: finite profiles show growth but do not establish a reachable gas-exhaustion threshold. Retained as NOT TESTED, not a validated finding.
- Slither alerts: arbitrary-from transferFrom, stale-balance/reentrancy, divide-before-multiply, strict equality, timestamp, compiler range and test-mock alerts were not validated as defects. Slither output alone is insufficient; the security guard, trusted-token assumptions and scope need case-specific review.

## 8. Appendix

Call path summary: token stake -> legacy staking stakeStart -> exact ERC20 transferFrom -> position append -> optional referral mint; token stakeEnd -> legacy stakeEnd -> dailyData lookup -> clear position -> mint payout. V1 stake -> reserve and principal transfers -> immutable position; V1 maturity -> beneficiary-only principal withdrawal and reward claim, each with independent liability and exact-transfer checks.

OWASP references are from the local pack manifest dated 2026-10-24; cited source URLs are the pack's recorded source URLs. The report validator checks structure only and cannot validate exploit semantics. Commands and observed results are recorded in Sections 2 and 4. Not performed: independent chain/deployment verification, full applicable SCSVS/SCSTG item inventory, stateful invariant fuzzing, the full ERC20 adversarial matrix, historical proxy storage comparison, and external legal/economic review. The implementation PR remains open pending independent review and required hosted checks; merge was not authorized.
