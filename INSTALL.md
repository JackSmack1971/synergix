# Install SynergiX development dependencies

## Prerequisites

- Node.js and npm. This install was performed with Node.js `v22.20.0` and npm `10.9.3`.
- Git, if you are cloning the repository.

The root `package.json` declares the Hardhat, ethers, OpenZeppelin, Mocha, and Chai development dependencies. `package-lock.json` pins the resolved dependency tree for repeatable installs.

## Clean install

From the repository root, run:

```sh
npm ci
```

`npm ci` installs the exact versions in `package-lock.json` and does not rewrite the lockfile. Use `npm install` when intentionally changing dependencies; review and commit the resulting `package.json` and `package-lock.json` changes together.

## Common project commands

```sh
npm run compile
npm test
```

Dependency installation does not imply that the current contracts compile or pass tests. The restored sources have known build defects, including a duplicate `SynergiXToken` declaration in `contracts/ISynergiXStaking.sol`; resolve those in a separately scoped change and validate before relying on compile or test results.

Deployment scripts can submit transactions and the checked-in network configuration contains placeholders. Do not run deployment commands until the network, credentials, and deployment configuration have been reviewed and supplied securely.
