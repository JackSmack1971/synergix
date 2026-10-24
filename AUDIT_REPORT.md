# SynergiX Security Audit and Remediation Gate

**Status: INCOMPLETE — the V1 payout architecture is owner-approved and implemented in a new contract; legacy H-01, numeric schedule approval, compatibility, and independent review remain open.**

## 1. Executive summary

Audited base revision `6496f7d666e95eb4707d3f81526cf46af0122f60` and the V1 implementation worktree on 2026-10-24. The user self-identified as owner `JackSmack1971` and gave durable in-session approval for position-based immutable entry terms, fixed simple rewards, separately prefunded liabilities, escrowed principal, keeper-independent settlement, and inclusive exact-timestamp maturity. The new `SynergiXStakingV1` implements that architecture with deployment-supplied immutable parameters. The legacy `SynergiXStaking` still contains H-01: current-only daily records can leave a matured claim reverting at a Unix-day array index. H-01 is verified by local PoC and remains open for legacy positions/deployment. Numeric rate/duration/stake bounds, referral policy, reserve loss behavior, governance/custody and chain remain unapproved. No Critical finding was validated. Coverage and Slither are unavailable.

The next V1 avoids the legacy temporal data model rather than attempting to repair its daily indexes. V1 stores each position's fixed reward and maturity timestamp at entry, checks full reward prefunding before accepting the position, and returns principal plus reward at or after maturity. The new contract has no admin or reserve withdrawal method. Legacy H-01 remains open because the new contract does not migrate or settle legacy positions; deployment/off-chain obligations have not been inventoried. This PR must not merge while H-01 remains open under the requested gate.

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

The token is UUPS-upgradeable while staking is constructor-based. Staking escrows principal on entry, but `stakeEnd` zeroes the position and mints payout instead of returning the escrowed principal; the intended economic model is unresolved. `dailyData` is append-only and zero-based, while payout reads it at Unix-day indexes. Referral eligibility and ancestry traversal scan unbounded arrays/chains. Existing tests cover selected role paths, settings bounds, callback reentrancy, false-return/fee-on-transfer behavior, referral cycles, same-layout upgrade behavior, and the H-01 reproducer. Gaps include full role matrices, no-return/rebasing/blacklisting token behavior, fuzz/property and invariant testing, reward solvency, broad payout boundary cases, deep traversal ceilings, and historical storage-layout compatibility. Public/external NatSpec is incomplete, notably interface functions and multiple staking entry points/setters.

### Verification evidence

- `npm test` — exit 0; 30 passing, 1 pending. H-01 PoC passed by asserting the legacy matured claim reverts. The pending legacy payout case passes with the epoch configuration below.
- `node scripts/hardhat.js --config hardhat.epoch.config.js test test/poc/positive-payout.test.js` — exit 0; 2 passing, including the aligned matured payout and zero-share rejection.
- V1-focused suite — 7 passing tests cover fixed-at-entry reward, reserve accounting/overcommit, bounds, exact timestamp maturity, delayed claim, false-return and fee-on-transfer intake/payout, and callback reentrancy.
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

### H-01 — Unix-day indexes can make ordinary matured claims revert

- **Severity:** High (conditional on a current-period schedule that has not been backfilled).
- **Location:** `contracts/SynergiXStaking.sol:222-231` computes Unix-day indexes and uses them directly as array indexes; `:413-420` appends one row at a time without an epoch offset or explicit day key. Claim path: `:153-175`; token wrapper: `contracts/SynergiXToken.sol:119-126`.
- **Checklist:** `SOL-AM-DOSA-1`, `SOL-Basics-Math-1`, `SOL-Defi-Staking-2`, `SOL-EC-13`; general mapping SCWE-083 (not an exact pattern match).
- **Impact:** A matured stake’s `stakeEnd` reverts before clearing the stake or paying the claimant. Escrow remains held and unavailable through that claim path. Impact amount is unknown.
- **Reachability/evidence:** An ordinary staker stakes and waits for maturity while the owner/keeper has appended only current-period rows. `npm test` executed the local H-01 PoC successfully; the assertion confirms `Invalid end day index.`
- **Counterargument:** Sequentially backfilling every historical day can make the direct Unix-day indexes exist. No deployment schedule was provided; the source has no base-day mapping or batch backfill. This limits certainty about deployed impact but does not remove the demonstrated ordinary schedule failure.
- **Recommendation:** Use the approved position-based V1 for new positions and do not reuse daily records. Separately identify any deployed or off-chain legacy positions and preserve an approved claim/migration path; do not silently replace legacy storage or payout semantics.
- **Status:** OPEN for legacy positions/deployment until compatibility and obligation inventory proves the daily-index path can be retired or safely resolved. The new V1 does not close H-01 for existing legacy positions.

## 5. Centralization and trust risks

Token admin can authorize arbitrary UUPS implementation upgrades and administer token roles. Staking owner can alter settings, referral mappings, and daily reward inputs; default admin separately administers roles. Ownership transfer does not transfer AccessControl default-admin authority, as covered by a characterization test. Operators and admin can mint indirectly through staking paths if token `STAKING_ROLE` is assigned. These are privileged trust assumptions; no deployed role inventory or multisig/timelock evidence exists. The code has no timelock for critical changes. No new admin control is recommended until the TDR administrative authority decision is approved.

## 6. Invariant, test, and OWASP coverage

| Category | Control/test | Status | Evidence | Finding |
|---|---|---|---|---|
| legacy payout availability | Matured claim under current-only daily data | FAIL | H-01 PoC in `test/poc/H-01.test.js`; full suite asserts the revert | H-01 |
| V1 settlement | Fixed-entry reward, full reservation, maturity, duplicate claim, token edge and callback behavior | PARTIAL PASS | `test/SynergiXStakingV1.test.js`, 7 passing; numeric schedule and token/deployment identity remain unapproved | — |
| reward schedule | Aligned payout and boundary semantics | NOT TESTED | Positive payout test pending under default clock; no approved schedule semantics | H-01 |
| authorization | Selected token/admin/operator role paths | PARTIAL | `test/SynergiXToken.test.js`, `test/SynergiXStaking.test.js`, `test/poc/authorization-validation.test.js` | — |
| reentrancy | Callback reentry into `stakeStart` | PARTIAL | `test/poc/reentrancy-validation.test.js`; other cross-function callbacks not covered | — |
| ERC20 intake | False return and fee-on-transfer rejection | PARTIAL | `test/poc/erc20-interaction.test.js`; no-return/rebase/blacklist untested | — |
| upgradeability | UUPS authorization and same-layout state | PARTIAL | `test/poc/upgrade-validation.test.js`; historical/deployed layout unverified | — |
| gas/resource bounds | Referral ancestry and active-stake scan | PARTIAL | `test/poc/gas-traversal-profile.test.js` profiles finite sizes only | — |
| build | Forced local compile | PASS | `npm run compile -- --force`; 54 files, Solidity 0.8.38, Paris | — |
| coverage | Instrumented coverage | NOT TESTED | `solidity-coverage` not installed/configured | — |
| static analysis | Slither | NOT TESTED | `slither` unavailable | — |
| deployment | Chain, roles, proxy state, storage compatibility | NOT TESTED | No deployment facts supplied | — |

## 7. Discarded candidates and implementation decision

The owner approved replacing the legacy daily-index mechanism with a position-based V1. A separate immutable-terms implementation now exists; it does not migrate or rewrite legacy positions because deployment and off-chain obligations remain unverified. Numeric schedule terms and the existing Hardhat 2 development dependency advisories also remain open. No candidate was claimed disproven; deployment/release requires those gates to close.

**Selected slice:** introduce an immutable-terms V1 lifecycle that does not depend on daily keeper rows. Its constructor requires explicit token, rate, principal bounds, and duration bounds; no draft schedule values are defaults. Acceptance evidence includes exact receipt/payout checks, no underfunded position acceptance, one-time beneficiary withdrawal, inclusive timestamp maturity, delayed-claim fixed rewards, and reentrancy rejection. The owner’s approval is recorded in `docs/V1_TOKENOMICS_DECISION_RECORD.md`; numeric terms remain for an approved deployment schedule. The slice does not migrate or modify legacy positions. Legacy H-01 and 13 high development dependency advisories remain open, so do not merge under the requested gate.

## 8. Appendix

Primary local evidence: `contracts/SynergiXToken.sol`, `contracts/SynergiXStaking.sol`, `contracts/SynergiXStakingV1.sol`, `contracts/ISynergiXStaking.sol`, `checklist.json`, V1 decision documents, and the local tests named above. Pre-existing worktree changes were preserved. This report is not release approval and does not establish deployed-contract safety.
