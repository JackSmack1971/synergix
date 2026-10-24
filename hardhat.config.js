require("@nomiclabs/hardhat-ethers");
require("@openzeppelin/hardhat-upgrades");

const { subtask } = require("hardhat/config");
const { TASK_COMPILE_SOLIDITY_GET_SOLC_BUILD } = require("hardhat/builtin-tasks/task-names");

// Use the locked local solc-js package; ordinary builds must not fetch a compiler.
subtask(TASK_COMPILE_SOLIDITY_GET_SOLC_BUILD).setAction(async ({ solcVersion }, _hre, runSuper) => {
    if (solcVersion === "0.8.38") {
        const solc = require("solc");
        return {
            compilerPath: require.resolve("solc/soljson.js"),
            isSolcJs: true,
            version: solcVersion,
            longVersion: solc.version()
        };
    }
    return runSuper();
});

const rinkebyAccounts = process.env.RINKEBY_PRIVATE_KEY
    ? [process.env.RINKEBY_PRIVATE_KEY]
    : [];
const mainnetAccounts = process.env.MAINNET_PRIVATE_KEY
    ? [process.env.MAINNET_PRIVATE_KEY]
    : [];

module.exports = {
    solidity: "0.8.38",
    networks: {
        rinkeby: {
            url: process.env.RINKEBY_RPC_URL || "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID",
            accounts: rinkebyAccounts
        },
        mainnet: {
            url: process.env.MAINNET_RPC_URL || "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
            accounts: mainnetAccounts
        }
        // Add other networks as needed
    }
};
