# Repository Guidelines

## Project Structure & Module Organization

- `contracts/` contains the Solidity files `SynergiXToken.sol`, `SynergiXStaking.sol`, and `ISynergiXStaking.sol`.
- `test/` contains Hardhat tests, split by contract (`SynergiXToken.test.js` and `SynergiXStaking.test.js`).
- `scripts/` contains deployment and maintenance scripts; `hardhat.config.js` configures the development network and compiler.
- `audit/REPORT.md` records the current security review and its limitations.
- `owasp-scwe-docs-pack/` is a bundled security reference corpus. Keep generated/reference content separate from contract source changes.

## Build, Test, and Development Commands

Install dependencies with `npm install`. Use the package scripts from the repository root:

- `npm test` runs the Hardhat test suite against the local network.
- `npm run compile` compiles the Solidity contracts.
- `npx hardhat test test/SynergiXStaking.test.js` runs one contract's test file.

Deployment scripts target configured networks and may submit transactions. Review the target network and configuration before running `npm run deploy` or `npm run deploy:mainnet`.

## Coding Style & Naming Conventions

Follow the existing Solidity and JavaScript style: use four spaces for indentation, descriptive names, and keep related contract behavior together. Solidity contracts and interfaces use PascalCase; functions and state variables use camelCase. Name tests after the contract or behavior under test, ending in `.test.js`. Keep changes focused and avoid unrelated formatting churn.

## Testing Guidelines

Tests use Hardhat with Mocha and Chai. Add or update tests in `test/` for behavior changes, including access control, staking/reward paths, and expected revert cases when relevant. Run `npm test` and `npm run compile` before submitting; there is no separate coverage threshold configured in `package.json`.

## Commit & Pull Request Guidelines

The available history does not show a consistent commit-message format. Use a short imperative summary, for example `Fix staking reward calculation`. Pull requests should explain the behavior changed, note contract or storage-layout implications, list validation commands and results, and link the related issue when one exists. Include screenshots only when a change has a visual component.

## Security & Configuration

Never commit private keys, API credentials, or populated `.env` files. Use local environment variables for deployment credentials. Treat contract and upgrade changes as security-sensitive: describe access-control and storage-layout effects in the pull request and test the affected paths.

The files under `contracts/` were restored from the Solidity blobs identified by their saved GitHub pages. The current `ISynergiXStaking.sol` still contains a duplicate `SynergiXToken` contract instead of only the expected staking interface, and the recovered sources have unresolved build defects. Do not treat this contract set as compilable or fully audited; see `audit/REPORT.md`. Resolve those source defects in a separately scoped change with build and security validation.
