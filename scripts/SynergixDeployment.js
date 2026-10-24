// scripts/SynergixDeployment.js

const { ethers, upgrades } = require("hardhat");

async function main() {
    const [deployer] = await ethers.getSigners();
    const admin = deployer.address;

    const SynergiXToken = await ethers.getContractFactory("SynergiXToken");
    console.log("Deploying SynergiXToken proxy...");
    const token = await upgrades.deployProxy(SynergiXToken, [admin, ethers.constants.AddressZero], { initializer: "initialize" });
    await token.deployed();
    console.log("SynergiXToken deployed to:", token.address);

    const SynergiXStaking = await ethers.getContractFactory("SynergiXStaking");
    console.log("Deploying constructor-based SynergiXStaking...");
    const staking = await SynergiXStaking.deploy(token.address);
    await staking.deployed();
    console.log("SynergiXStaking deployed to:", staking.address);

    await (await token.setStakingContract(staking.address)).wait();
    await (await staking.grantStakingOperator(token.address)).wait();
    console.log("Token/staking roles configured.");
}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.error("Deployment failed:", error);
        process.exit(1);
    });
