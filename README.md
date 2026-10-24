# SynergiX

SynergiX is a Solidity token and staking prototype. The current checkout is **not release-ready**: [`audit/REPORT.md`](audit/REPORT.md) remains incomplete, the H-01 payout-history defect is unresolved, and the V1 economic and administrative decisions in [`docs/V1_TOKENOMICS_DECISION_RECORD.md`](docs/V1_TOKENOMICS_DECISION_RECORD.md) are still awaiting owner approval. The current contract behavior below is a source description, not an approved product or deployment specification.

## Current contract architecture

- `SynergiXToken` is an ERC-20 UUPS implementation intended to run behind a proxy. Its initializer assigns `ADMIN_ROLE` and `DEFAULT_ADMIN_ROLE`. It can initialize with no staking address and then wire one staking contract once through `setStakingContract`. That call grants the staking contract `STAKING_ROLE` (which can mint) and `TRUSTED_CONTRACT_ROLE`.
- `SynergiXStaking` is **not upgradeable**. It is deployed with a token address in its constructor and combines `Ownable`, `AccessControl`, and `ReentrancyGuard`. At construction, the deployer receives ownership, `DEFAULT_ADMIN_ROLE`, and `STAKING_OPERATOR_ROLE`.
- Ownership and AccessControl membership are separate: `transferOwnership` does not transfer `DEFAULT_ADMIN_ROLE` or `STAKING_OPERATOR_ROLE`. The approved role handoff procedure is still open.
- Staking uses `SafeERC20` and records a position only when its token balance increases by the exact requested principal. False-returning and fee-on-transfer deposits are rejected.
- The current deployment script deploys the token proxy first, deploys staking directly, wires the two contracts, and grants the token contract `STAKING_OPERATOR_ROLE` in staking. It does not transfer the deployer's token admin roles or staking ownership/admin/operator roles to a multisig.
- The token's UUPS upgrades are authorized by `ADMIN_ROLE`. Staking has no UUPS implementation or repository upgrade script. The old `npm run upgrade` entry referred to a missing script and has been removed.

The token implementation locks its standalone implementation storage against initialization. This does not remove proxy upgrade authority or make an existing deployment immutable.

## Legacy behavior and unresolved rules

The current source has a 1,000,000 SNX minimum in staking and a 1,000,000 SNX maximum in the token wrapper, so the public amount range is exactly one amount. The token wrapper allows 1–365 days, while staking's owner-controlled maximum defaults to 5,555 days. The staking bonus threshold is 150,000,000 SNX, above the public amount maximum. These are observed source values, not approved product parameters.

Matured `stakeEnd` currently mints principal plus calculated interest while the original principal remains in the staking contract. Referral rewards are also minted (2% to the referrer and 1% to the referred staker). These legacy mechanics do not establish approved payout, funding, supply, referral, or burn policy.

`dailyData` is appended as a zero-based array while payout calculation indexes it using Unix-day numbers. A one-row history therefore does not make an ordinary matured stake claimable. This H-01 defect remains open. New daily records with zero total shares and `maxStakeDays` settings below 2 are rejected by the current working-tree changes, but that does not repair any already-recorded history or a deployed instance.

## Build and tests

Install locked dependencies with:

```sh
npm ci
```

Compile and run the local Hardhat suite:

```sh
npm run compile -- --force
npm test
```

The default clock skips one epoch-sensitive positive payout case. Run both payout cases and related regression checks with the repository's epoch-aligned local configuration:

```sh
node scripts/hardhat.js --config hardhat.epoch.config.js test test/poc/positive-payout.test.js test/poc/H-01.test.js test/poc/settings-edge-validation.test.js test/poc/referral-validation.test.js test/poc/stake-cap-validation.test.js test/poc/upgrade-validation.test.js
```

Passing these checks is not a security signoff. See the incomplete audit and the separate [remediation evidence](docs/SECURITY_REMEDIATION_STATUS_2026-10-24.md).

## Deployment and network configuration

[`scripts/SynergixDeployment.js`](scripts/SynergixDeployment.js) submits deployment transactions on the selected Hardhat network. `npm run deploy` uses Hardhat's local default network; `npm run deploy:mainnet` explicitly targets mainnet and can submit public-chain transactions. The script makes its caller the token admin and staking owner/admin/operator. Review the target network and role holders before any use. This repository does not establish that a deployment exists or identify any deployed addresses.

The current Hardhat configuration contains legacy `rinkeby` and `mainnet` entries with placeholder RPC defaults. Those entries do not establish a supported network; testnet selection is deferred in the V1 plan. Do not run deployment or upgrade operations until the economic schedule, administrative authority, target chain, and any existing deployment have been reviewed and separately authorized.

## Repository map

- `contracts/` — token, staking contract, staking interface, and `contracts/test/` mocks used only by adversarial tests
- `test/` — Hardhat tests and focused security regression cases
- `scripts/` — deployment and local Hardhat launcher
- `docs/` — proposed V1 economics/remediation documents and new verification records
- `audit/REPORT.md` — historical security report; its incomplete status and evidence are preserved
