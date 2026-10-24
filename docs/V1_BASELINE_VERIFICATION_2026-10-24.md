# SynergiX V1 Baseline Verification — 2026-10-24

**Purpose:** Record current-source build and existing Hardhat-suite evidence separately from the historical security report. This document does not amend or supersede [`audit/REPORT.md`](../audit/REPORT.md), approve economics, or lift the Phase 1 hold.

**Snapshot boundary:** These results describe the pre-remediation `8de8af76e3e9b42abc92abe56e2756f7368f267d` worktree before the current security fixes. For the later worktree, updated regressions, and fresh verification, see [`SECURITY_REMEDIATION_STATUS_2026-10-24.md`](SECURITY_REMEDIATION_STATUS_2026-10-24.md). The original counts and pending cases below are retained as baseline evidence.

## Revision and environment

- **Branch:** `fix/restore-solidity-sources`
- **HEAD:** `8de8af76e3e9b42abc92abe56e2756f7368f267d`
- **Source/test worktree:** `git diff -- contracts test` and the staged equivalent were empty at verification time; the local changes were documentation and `AGENTS.md` only.
- **Environment sampled:** `2026-10-24T00:25:57.0655653-04:00`; Microsoft Windows NT 10.0.22631.0; PowerShell 7.6.2; Node.js v22.20.0; npm 10.9.3; Hardhat 2.29.1; solc 0.8.26; EVM target Paris.
- **Phase 1 hold:** active. No economics-dependent contract changes were made.

## Build result

| Exact command | Exit/result | Scope |
|---|---|---|
| `npm run compile -- --force` | Exit 0 — `Compiled 35 Solidity files successfully (evm target: paris).` | Forced local compilation of the current checkout using the repository's local solc 0.8.26 override. This is build evidence only, not economic or security validation. |

## Default Hardhat suite

**Exact command:** `npm test`
**Underlying script:** `node scripts/hardhat.js test`
**Result:** exit 0; **15 passing, 2 pending, 0 failing**.

| File | Test case | Result |
|---|---|---|
| `test/poc/H-01.test.js` | shows a matured stake cannot end when daily data contains only the first appended record | PASS |
| `test/poc/positive-payout.test.js` | pays a matured stake once when day indexes 0 and 1 exist | PENDING — the test calls `this.skip()` when `endDayIndex > 1`; the default Hardhat clock is not epoch-aligned. |
| `test/poc/positive-payout.test.js` | shows an owner-supplied zero share denominator blocks an otherwise aligned claim | PENDING — the test calls `this.skip()` when `currentDayIndex > 100`; the default Hardhat clock exceeds this bound. |
| `test/poc/referral-validation.test.js` | pays the configured referral percentages once and rejects a two-account cycle | PASS |
| `test/poc/settings-edge-validation.test.js` | shows owner-set maxStakeDays 0 or 1 prevents valid stakes | PASS |
| `test/poc/stake-cap-validation.test.js` | rejects any value above the minimum because the token maximum equals the staking minimum | PASS |
| `test/poc/upgrade-validation.test.js` | rejects an unprivileged upgrade and preserves proxy state across an authorized same-layout upgrade | PASS |
| `test/poc/upgrade-validation.test.js` | confirms direct implementation initialization cannot upgrade or change proxy roles | PASS |
| `test/SynergiXStaking.test.js` | deploys as a constructor-based contract with the supplied token | PASS |
| `test/SynergiXStaking.test.js` | accepts a valid stake through the token entry point and escrows principal | PASS |
| `test/SynergiXStaking.test.js` | rejects stakes below the configured minimum and invalid durations | PASS |
| `test/SynergiXStaking.test.js` | enforces operator authorization on direct staking calls | PASS |
| `test/SynergiXStaking.test.js` | allows the owner to update bounded staking settings | PASS |
| `test/SynergiXToken.test.js` | initializes token metadata and assigns admin access | PASS |
| `test/SynergiXToken.test.js` | only allows the configured staking contract to mint | PASS |
| `test/SynergiXToken.test.js` | allows staking to be wired once and only by an admin | PASS |
| `test/SynergiXToken.test.js` | allows admin role management and rejects unauthorized changes | PASS |

No test failed in the default suite. The two pending results are conditional skips in the test code, not passing assertions.

## Epoch-aligned supplemental run

**Exact command:** `node scripts/hardhat.js --config hardhat.epoch.config.js test test/poc/positive-payout.test.js`
**Result:** exit 0; **2 passing, 0 pending, 0 failing**.

Both pending cases above passed with `hardhat.epoch.config.js`, which sets the initial Hardhat timestamp to `1970-01-01T00:00:00.000Z`. The first verifies the legacy payout and duplicate-claim rejection with daily indexes 0 and 1. The second reproduces a claim revert when owner-supplied daily data has a zero share denominator. These results characterize current legacy code under the test's clock assumptions; they do not validate V1 economics.

## Reconciliation to the current source revision

The tests and source files were unchanged from HEAD during these checks. The suite therefore applies to revision `8de8af76e3e9b42abc92abe56e2756f7368f267d`, not merely to historical results recorded for another audit-session working tree. The working directory had documentation and `AGENTS.md` edits, but no staged or unstaged changes under `contracts/` or `test/`.

The suite establishes selected legacy behaviors: one stake escrows principal; access roles gate selected calls; current referral minting and a two-account cycle check work; several configuration boundaries behave as expected; selected UUPS checks pass; and the payout-index failure reproduces. It does not establish that the contracts satisfy the approved architectural principles or any owner-approved tokenomics, because those economics are not implemented in this source set.

## V1 invariant coverage gaps

The `ECON-*` identifiers refer to [`V1_TOKENOMICS_DECISION_RECORD.md`](V1_TOKENOMICS_DECISION_RECORD.md). No current test constitutes complete executable coverage of the V1 invariant set. The following cases have limited legacy analogues; all others lack an executable V1 test.

| V1 invariant | Current executable evidence | Coverage conclusion |
|---|---|---|
| ECON-01 — escrowed principal always covers aggregate outstanding principal | `SynergiXStaking.test.js` checks one user's balance and staking-contract balance after one deposit. | **Partial only.** No multi-position stateful liability invariant, withdrawal sequence, or aggregate model. |
| ECON-02 — principal returned at most once | The aligned payout test checks duplicate legacy claim rejection in the supplemental epoch run; default suite marks it pending. | **Partial legacy analogue only.** Current legacy claim mints principal plus interest instead of returning escrowed principal; no V1 withdrawal implementation. |
| ECON-03 — reward reserve covers all base and referral liabilities | Current rewards/referrals are minted; there is no separately accounted reward reserve. | **Absent.** No reserve-liability model or property test. |
| ECON-04 — rewards cannot consume assets owed as principal | No separate reward reserve is implemented; payouts mint. | **Absent.** No interleaved reserve/principal solvency test. |
| ECON-05 — reject an underfunded reward commitment atomically | No prefunded reward commitment mechanism exists. | **Absent.** No reserve boundary or atomicity oracle. |
| ECON-06 — reward exhaustion cannot block matured principal withdrawal | No reserve exhaustion path or principal-return withdrawal exists. | **Absent.** No exhaustion/withdrawal isolation test. |
| ECON-07 — no post-genesis supply increase under fixed supply | Token tests explicitly show a caller with `STAKING_ROLE` can mint. | **Absent for V1; current behavior conflicts with the preferred fixed-supply principle.** No total-supply invariant. |
| ECON-08 — arithmetic and liability bounds match approved parameters | Tests cover selected stake-cap and `maxStakeDays` edges; no approved V1 parameters or reward reference model exist. | **Partial legacy edge checks only.** No stateful/property fuzzing across reward, referral, rounding, and liability boundaries. |
| ECON-09 — open positions retain their entry terms | A settings test confirms owner changes to settings; it does not compare existing positions before and after changes. | **Absent.** No immutable-position-terms property. |
| ECON-10 — pause policy preserves allowed withdrawals and funded claims | Current token has a private pause flag but no public pause setter; no pause matrix test exists. | **Absent.** Emergency controls and withdrawal policy remain open. |
| ECON-11 — referral traversal is bounded and liabilities remain covered | Referral test rejects a two-account cycle and checks current 1%/2% minting. | **Partial legacy checks only.** No maximum-depth, gas bound, referral cap, or reserve accounting test. |
| ECON-12 — rejected operations leave all economic state unchanged | Individual revert checks exist, but they do not snapshot and compare the full set of balances, positions, liabilities, reserve, supply, and events across operation classes. | **Partial only.** No broad atomicity invariant or stateful reference-model test. |

## Hold-point disposition

The Phase 1 hold remains active. This baseline result does not authorize implementation that depends on the open supply, reward, staking, referral, governance, emergency-control, or withdrawal decisions. The historical [`audit/REPORT.md`](../audit/REPORT.md) was not changed; its `STATUS: INCOMPLETE` and findings remain intact. The forced compile and current test runs are new, revision-specific evidence, not a replacement security audit.
