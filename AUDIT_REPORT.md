# SynergiX Security Audit and Remediation Gate

STATUS: INCOMPLETE
Blocker: This PR addresses one owner-approved V1 settlement invariant only. Numeric economics, administrative authority, full per-control checklist verification, and static analysis remain open. An independent reviewer approved the implementation diff at commit 5b0ce1fb3fe7cefba6829d93ce7d344fcea22469.

## 1. Executive summary

Audited base revision `e13f7fceec35849bf2f85e390206138dacd7bd29` (`origin/main`) on 2026-10-24. The owner has approved separate V1 principal and reward claims at maturity, principal priority after reserve loss, and attested that no contracts are deployed and no legacy holders or enforceable off-chain obligations exist; the decision and its limits are recorded in `docs/V1_OWNER_DECISION_ADDENDUM_2026-10-24.md`. Legacy H-01 remains a reproduced source defect but is retired from planned V1 work under that owner attestation; the legacy contracts must not be deployed. This slice addresses V1 failure isolation and principal solvency: reward failure must not block otherwise available principal, and reward claims cannot reduce balance below aggregate principal liabilities. Numeric economics, administrative authority, and deployment/release remain open. No Critical finding was validated. Coverage and Slither were unavailable.

V1 stores each position's fixed reward and maturity timestamp at entry and checks full reward prefunding before accepting the position. This change settles principal and reward independently, and reward payout checks that remaining balance covers aggregate principal liabilities. After reserve loss, rewards may wait until principal is withdrawn or funds are restored. Token-level restrictions that prevent all transfers can still block both claims. The legacy payout bug is not repaired because the owner attests there are no deployed legacy contracts or related obligations; it remains unsafe legacy source and is excluded from new V1 settlement.

## 2. Scope and assumptions

| File | Observed surface |
|---|---|
| `contracts/SynergiXToken.sol` | UUPS-upgradeable ERC20, role-based minting/admin, staking wrapper, transfer hook |
| `contracts/SynergiXStaking.sol` | Constructor-based staking, ERC20 custody, minted payouts/referrals, owner/operator roles, daily reward data |
| `contracts/ISynergiXStaking.sol` | Legacy external staking interface |
| `contracts/SynergiXStakingV1.sol` | New immutable-terms V1, escrow and prefunded reward liabilities |
| `contracts/test/SynergiXV1CallbackTokenMock.sol` | Test-only adversarial token double |

Trust assumptions: token `ADMIN_ROLE`, staking owner, staking `DEFAULT_ADMIN_ROLE`, and `STAKING_OPERATOR_ROLE` holders can materially affect upgrades, minting, settings, and reward records. Their identities and custody are unknown. The staking constructor accepts a token address; no deployment identity is supplied. `checklist.json` was loaded (370 entries) and applicable items were triaged against observed code. Inapplicable oracle, bridge, NFT, native-ETH, signature, and AMM controls were treated as not applicable to the inspected source; version-specific controls were checked against compiler and dependency versions, not assumed applicable.

Legacy project versions remain Hardhat 2.29.1, OpenZeppelin 4.9.6, ethers 5.8.0 and Solidity 0.8.26. The isolated V1 addition pins `solc` 0.8.38 and OpenZeppelin Contracts 5.7.0 under the npm alias `@openzeppelin/contracts-v5`; its pragma is exact `=0.8.38`. Legacy inheritance and storage behavior were left unchanged. Hardhat 2.29.1 warns that Solidity 0.8.38 is not fully supported; compilation and tests succeeded, but some stack traces may be limited. This slice deliberately does not migrate the existing ethers v5 / Hardhat 2 upgrade plugin stack to Hardhat 3.

### Current state and test gaps

The token is UUPS-upgradeable while legacy staking is constructor-based. Legacy `stakeEnd` clears a position and mints payout instead of returning escrowed principal; V1 terms are separately approved. Legacy `dailyData` is append-only and zero-based, while payout reads it at Unix-day indexes. Referral eligibility and ancestry traversal scan unbounded arrays/chains. Existing tests cover selected role paths, settings bounds, callback reentrancy, false-return/fee-on-transfer behavior, referral cycles, same-layout upgrade behavior, and H-01. V1 tests additionally cover no-return tokens, exact incoming/outgoing delivery, pause recovery, reentrancy during deposit and payout, zero-rounded reward, and configured amount/duration boundaries. Remaining gaps include adversarial `balanceOf`, negative rebasing, blacklisting/permanent pause, property/invariant fuzzing, historical storage-layout compatibility, full legacy role matrices, and deep traversal ceilings. Public/external NatSpec in legacy contracts remains incomplete.

### Verification evidence

- `npm test` — exit 0; 34 passing, 1 pending. H-01 PoC passed by asserting the legacy matured claim reverts. The pending legacy payout case passes with the epoch configuration below.
- `node scripts/hardhat.js --config hardhat.epoch.config.js test test/poc/positive-payout.test.js` — exit 0; 2 passing, including the aligned matured payout and zero-share rejection.
- V1-focused suite — 11 passing tests cover fixed-at-entry reward, reserve accounting/overcommit, bounds, exact timestamp maturity, delayed claim, no-return/false-return/fee-on-transfer behavior, temporary pause recovery, zero-rounded reward, and callback reentrancy.
- `npm run compile -- --force` — exit 0; 54 Solidity files compiled for Paris using local Solidity 0.8.38. Hardhat emitted its compiler-support warning and legacy OpenZeppelin 4.9 assembly annotation warnings.
- `npm audit` — 36 development-tree findings (19 low, 4 moderate, 13 high; 0 critical). `npm audit --omit=dev` — 0 runtime dependency findings. High findings trace to the existing Hardhat 2 / ethers v5 / upgrades-plugin toolchain; remediation requires a separate major toolchain migration and remains a merge blocker under the requested no-open-High rule.
- Coverage — not configured/installed (`solidity-coverage` unavailable).
- Slither — unavailable in the environment; no static-analysis result claimed.
- GitHub/PR discovery — `gh` could not connect to `api.github.com` in the restricted network. PR and mergeability state are unknown.

## 3. Threat model and checklist application

Legacy assets include escrowed SNX principal and newly minted staking/referral rewards; V1 assets are the constructor-selected ERC20 principal and explicitly funded reward reserve. Actors are stakers/referrers, legacy owner/default admin/operators/token admin, and the immutable V1 asset. Core invariants: V1 principal can be withdrawn once by its recorded beneficiary at/after maturity; reward is fixed at entry and reserved before stake acceptance; legacy schedule rows remain correctly mapped only under the legacy model; V1 external token failure cannot create an unbacked position; no V1 admin role can change terms or withdraw liabilities. Legacy payout/deployment state and V1 numeric deployment configuration remain unknown or unapproved.

Checklist triage (IDs are the exact IDs from the supplied `checklist.json`):

- **Attacker’s mindset / availability:** `SOL-AM-DOSA-1..6`, `SOL-AM-DA-1`, `SOL-AM-GA-1..2`, `SOL-AM-MA-1..2`, `SOL-AM-ReentrancyAttack-1..2`, `SOL-AM-RP-1`. H-01 is validated; scans are unbounded; `balanceOf` is used only for exact receipt-delta validation, not as liability accounting. Reentrancy has a focused callback test, not full cross-function coverage.
- **Access control / centralization:** `SOL-Basics-AC-2`, `SOL-Basics-AC-4..7`, `SOL-Basics-Function-9`, `SOL-CR-2..7`, `SOL-Basics-PU-4..10`, `SOL-Timelock-1`. Selected role checks are tested. Ownership and AccessControl administration diverge; privileged settings and daily data are immediately mutable; no timelock is present. These are material governance risks, but roles’ actual holders are unknown.
- **Math / staking / payments:** `SOL-Basics-Math-1..12`, `SOL-Basics-Payment-1..7`, `SOL-Defi-General-1..3`, `SOL-Defi-General-8..9`, `SOL-Defi-Staking-1..3`, `SOL-EC-13`. Checked arithmetic is used; payout still has unresolved division/index and epoch boundaries. No native-ETH flow exists. Exact deposit receipt is enforced, excluding fee-on-transfer behavior; arbitrary decimals/rebasing semantics are not supported/documented. There is no user-directed escrow withdrawal; payout currently mints.
- **External calls / tokens:** `SOL-EC-1`, `SOL-EC-3..4`, `SOL-EC-6..7`, `SOL-EC-9`, `SOL-Token-FE-1..16`. SafeERC20 is used for principal intake and exact balance delta is checked. Token callbacks are guarded in stake entry; tests cover one nested `stakeStart`. No ERC777/NFT/permit/approval integration exists in the staking flow. False-return and fee-on-transfer failures have tests; no-return, adversarial `balanceOf`, blacklist, pause, rebasing, and arbitrary-revert cases remain gaps.
- **Privilege and proxy:** `SOL-Basics-Initialization-1..3`, `SOL-Basics-PU-1..10`, `SOL-CR-4..7`. Token implementation initialization is disabled and proxy authorization/same-layout state retention have tests. Historical layout and deployed state are unverified. Immediate UUPS upgrades depend on admin trust; no delay is enforced.
- **Not applicable by source search:** oracle controls `SOL-Defi-Oracle-1..14` and `SOL-AM-PMA-1` (no price feed or pricing ratio); bridge/cross-chain controls (no bridge calls/interfaces); NFT controls `SOL-Token-NfE1-*` (no NFT state); signature controls (no signatures); native payment controls `SOL-Basics-Payment-3,6,7` (no native asset path). AMM swap/slippage and lending/liquidation checklists are not applicable (no such mechanism). Compiler-specific historical bug IDs were screened against the current Solidity 0.8.38 build and local source; no matching legacy language feature was identified, but this is not a compiler security certification.

This is a focused checklist mapping, not a claim that every one of the 370 prompts is a separately verified control. Items not explicitly enumerated above were screened for applicability by mechanism; no oracle, bridge, NFT, signature, AMM, native-payment, or lending code was found. Unavailable deployment state, unapproved economics, and incomplete adversarial coverage remain `NOT TESTED`.

## 4. Findings

### H-01 — Unix-day indexes can make ordinary matured claims revert (historical; retired for V1)

- **Severity:** High (conditional on a current-period schedule that has not been backfilled).
- **Location:** `contracts/SynergiXStaking.sol:222-231` computes Unix-day indexes and uses them directly as array indexes; `:413-420` appends one row at a time without an epoch offset or explicit day key. Claim path: `:153-175`; token wrapper: `contracts/SynergiXToken.sol:119-126`.
- **Checklist:** `SOL-AM-DOSA-1`, `SOL-Basics-Math-1`, `SOL-Defi-Staking-2`, `SOL-EC-13`; general mapping SCWE-083 (not an exact pattern match).
- **Impact:** A matured stake’s `stakeEnd` reverts before clearing the stake or paying the claimant. Escrow remains held and unavailable through that claim path. Impact amount is unknown.
- **Reachability/evidence:** An ordinary staker stakes and waits for maturity while the owner/keeper has appended only current-period rows. `npm test` executed the local H-01 PoC successfully; the assertion confirms `Invalid end day index.`
- **Counterargument:** Sequentially backfilling every historical day can make the direct Unix-day indexes exist. No deployment schedule was provided; the source has no base-day mapping or batch backfill. This limits certainty about deployed impact but does not remove the demonstrated ordinary schedule failure.
- **Recommendation:** Use the approved position-based V1 for new positions and do not reuse daily records. Separately identify any deployed or off-chain legacy positions and preserve an approved claim/migration path; do not silently replace legacy storage or payout semantics.
- **Status:** Retired from this V1 remediation scope based on the owner attestation in `docs/V1_OWNER_DECISION_ADDENDUM_2026-10-24.md`. The legacy source still has the defect; do not deploy the legacy contracts. This is not an on-chain independent verification of the owner's statement.

### M-01 — Reward transfer failure also blocks principal settlement

- **Severity:** Medium, conditional on a reward shortfall or reward-only transfer failure while enough tokens remain to return principal.
- **Location:** Base `contracts/SynergiXStakingV1.sol:187-215` reads the combined payout and performs one transfer; the function updates both liabilities together. The relevant guard rejects the entire settlement if the token cannot deliver the combined amount.
- **Checklist:** `SOL-Defi-Staking-2`, `SOL-EC-13`, `SOL-AM-DOSA-1`.
- **Impact:** A matured beneficiary cannot recover principal through the only settlement function if reward delivery fails even when the principal amount remains transferable.
- **Reachability/evidence:** A local regression reduces the contract's test-token balance by the reserved reward while leaving principal covered. The updated V1 implementation returns principal, leaves reward liability outstanding when reward payment fails, and permits reward retry after funds are restored. This models an external reserve shortfall; it does not assert that the selected production token can rebase or confiscate balances.
- **Counterargument:** V1 fully reserves rewards, has no admin withdrawal, and explicitly rejects fee-on-transfer behavior, so a shortfall is outside the expected token model. The owner nevertheless selected explicit failure isolation, and arbitrary ERC20 reserve loss or reward-only transfer failure must not couple the two entitlements.
- **Recommendation:** Keep separate at-most-once principal and reward claims; apply checks-effects-interactions and exact transfer validation independently to each.
- **Status:** Addressed in this slice; focused and full-suite verification pending.

## 5. Centralization and trust risks

Token admin can authorize arbitrary UUPS implementation upgrades and administer token roles. Staking owner can alter settings, referral mappings, and daily reward inputs; default admin separately administers roles. Ownership transfer does not transfer AccessControl default-admin authority, as covered by a characterization test. Operators and admin can mint indirectly through staking paths if token `STAKING_ROLE` is assigned. These are privileged trust assumptions; no deployed role inventory or multisig/timelock evidence exists. The code has no timelock for critical changes. No new admin control is recommended until the TDR administrative authority decision is approved.

## 6. Invariant, test, and OWASP coverage

| Category | Control/test | Status | Evidence | Finding |
|---|---|---|---|---|
| legacy payout availability | Matured claim under current-only daily data | FAIL | H-01 PoC in `test/poc/H-01.test.js`; full suite asserts the revert | H-01 |
| V1 settlement | Fixed-entry reward, full reservation, maturity, duplicate claim, token edge and callback behavior | PARTIAL PASS | `test/SynergiXStakingV1.test.js`, 11 passing; numeric schedule and token/deployment identity remain unapproved | — |
| reward schedule | Aligned payout and boundary semantics | NOT TESTED | Positive payout test pending under default clock; no approved schedule semantics | H-01 |
| authorization | Selected token/admin/operator role paths | PARTIAL | `test/SynergiXToken.test.js`, `test/SynergiXStaking.test.js`, `test/poc/authorization-validation.test.js` | — |
| reentrancy | Callback reentry during V1 deposit and payout | PARTIAL | `test/SynergiXStakingV1.test.js`; legacy cross-function callbacks and production token behavior not covered | — |
| ERC20 intake and payout | False-return, fee-on-transfer, no-return, pause rollback/recovery, exact transfer behavior | PARTIAL | `test/poc/erc20-interaction.test.js`, `test/SynergiXStakingV1.test.js`; production rebase/blacklist/token-admin behavior untested | — |
| upgradeability | UUPS authorization and same-layout state | PARTIAL | `test/poc/upgrade-validation.test.js`; historical/deployed layout unverified | — |
| gas/resource bounds | Referral ancestry and active-stake scan | PARTIAL | `test/poc/gas-traversal-profile.test.js` profiles finite sizes only | — |
| build | Forced local compile | PASS | `npm run compile -- --force`; 54 files, Solidity 0.8.38, Paris | — |
| coverage | Instrumented coverage | NOT TESTED | `solidity-coverage` not installed/configured | — |
| static analysis | Slither | NOT TESTED | `slither` unavailable | — |
| deployment | Chain, roles, proxy state, storage compatibility | NOT TESTED | No deployment facts supplied | — |

## 7. Discarded candidates and implementation decision

The owner attests that there are no deployed legacy contracts or enforceable legacy obligations, so H-01 is preserved as a historical defect rather than patched. Numeric schedule terms and administrative authority remain open and are not changed by this slice. No claim is made about release readiness or deployment authorization.

## 8. Appendix

Primary evidence: `contracts/SynergiXToken.sol`, `contracts/SynergiXStaking.sol`, `contracts/SynergiXStakingV1.sol`, `contracts/ISynergiXStaking.sol`, `checklist.json` (370 items; SHA-256 `f33ad4227e866f97372b291eaa88951c52d72a241aca51da5ca3038680168cce`), the owner decision addendum, and named tests. The tracked base is GitHub default-branch commit `e13f7fceec35849bf2f85e390206138dacd7bd29`; this feature branch records one follow-up slice. PR #7 is closed/merged at that base and has no submitted GitHub review; its prior state is not an approval of this change. This report is pre-merge evidence, not release approval or a safety certification.

**Selected slice:** separate matured V1 principal withdrawal and reward claim operations. Acceptance criteria: each is beneficiary-only, mature-only and independently at-most-once; failure of either operation preserves its own liability and does not block success of the other when the token can transfer the relevant amount; both claim orders work; zero reward settles once without a token transfer; and reentrancy/transfer failure cannot duplicate or erase either entitlement.

**Independent review:** APPROVE on implementation commit `5b0ce1fb3fe7cefba6829d93ce7d344fcea22469`; reviewer confirmed the ECON-04 guard closes the partial-loss counterexample and independently ran its targeted regression. **Pre-merge status:** not ready; hosted CI and required human reviews are absent, and explicit merge authorization is required.
