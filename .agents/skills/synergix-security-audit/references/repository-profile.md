# SynergiX project fingerprint and historical leads

**Origin:** User-supplied draft `AGENTS.md` (not a live repository read). Every item below is an inspection target, **not** an established fact or independently reproduced vulnerability. A commit and current tree must be inspected before relying on any item. Do not transpose observations to similarly named repositories.

## Expected identity (confirm at target revision)

- Hardhat with JavaScript Mocha/Chai tests and ethers v5.
- Claimed UUPS-upgradeable `SynergiXToken` (ERC20, AccessControl roles `ADMIN_ROLE`, `STAKING_ROLE`) and `SynergiXStaking` (staking/referrals/rewards, role `STAKING_OPERATOR_ROLE`), plus `ISynergiXStaking`.
- Expected `contracts/`, `scripts/SynergixDeployment.js`, `test/SynergiXToken.test.js`, `test/SynergiXStaking.test.js`, `hardhat.config.js`.
- Historically reported versions: `@openzeppelin/contracts` and `@openzeppelin/contracts-upgradeable` `^4.8.4`; `@openzeppelin/hardhat-upgrades` `^1.21`; Hardhat `^2.12`; Solidity setting `0.8.0`. Exact resolved dependency versions and compiler must be rechecked. Keep any local changes to dependencies out of audit scope.

## Historical repo defects to confirm/refute

1. `contracts/SynergiXToken.sol` reportedly starts `<!DOCTYPE html>` and contains a saved GitHub HTML page (~512 KB); `SynergiXStaking.sol` (~639 KB) and `ISynergiXStaking.sol` (~512 KB) were **not read**. If actual source is HTML, stop security conclusions and ask for Solidity source. Filename/size alone is insufficient proof.
2. `package.json` reportedly points its `upgrade` script to absent `scripts/UpgradeSynergixContracts.js`.
3. `hardhat.config.js` reportedly contains `0xYourPrivateKey` placeholders, Rinkeby configuration, and no dotenv handling, whereas README describes an env-based variant. Treat strings as placeholders, not usable secrets; do not execute deployment scripts.
4. `initialize` calls reportedly diverge: deploy `staking.initialize([])`, tests `[owner.address]`, README `[AddressZero]`. Check real signature and actual call sites before alleging any flaw. Deployment script reportedly uses placeholder `admin`, then deployer calls `token.grantRole(...)`.
5. Tests reportedly use `anyValue` without an import and refer to absent `SynergiXTokenV2`; test pass state is unknown.
6. Exact Solidity compiler `0.8.0` may be incompatible with some installed OpenZeppelin `^0.8.1` pragmas; verify via installed package source and compilation rather than assuming failure.

## Useful commands, subject to availability and safety

- `git status --short && git rev-parse HEAD`
- `npx hardhat compile`; `npx hardhat test`; `npx hardhat test test/SynergiXStaking.test.js`; `npx hardhat test --grep 'referral'`
- If installed, `slither .`; record version, exit status, and do not promote static alerts without independent analysis.
- PoCs: `test/poc/<ID>.test.js`; run `npx hardhat test test/poc/<ID>.test.js` **only on local Hardhat network**. Check configuration for external RPC/fork actions before running; no live transactions.
