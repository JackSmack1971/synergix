const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("Authorization validation: ownership and default-admin separation", function () {
    it("shows transferring staking ownership does not transfer AccessControl authority", async function () {
        const [deployer, tokenAdmin, nextOwner, operator] = await ethers.getSigners();
        const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));

        const Token = await ethers.getContractFactory("SynergiXToken");
        const token = await upgrades.deployProxy(
            Token,
            [tokenAdmin.address, ethers.constants.AddressZero],
            { initializer: "initialize" }
        );
        await token.deployed();

        const Staking = await ethers.getContractFactory("SynergiXStaking");
        const staking = await Staking.deploy(token.address);
        await staking.deployed();

        await staking.connect(deployer).transferOwnership(nextOwner.address);

        expect(await staking.owner()).to.equal(nextOwner.address);
        expect(await staking.hasRole(ethers.constants.HashZero, deployer.address)).to.equal(true);
        expect(await staking.hasRole(ethers.constants.HashZero, nextOwner.address)).to.equal(false);

        await staking.connect(nextOwner).setMaxStakeDays(5000);

        let ownerHelperFailed = false;
        try {
            await staking.connect(nextOwner).grantStakingOperator(operator.address);
        } catch (error) {
            ownerHelperFailed = String(error.message).includes("missing role");
        }
        expect(ownerHelperFailed).to.equal(true);

        await staking.connect(deployer).grantRole(role("STAKING_OPERATOR_ROLE"), operator.address);
        expect(await staking.hasRole(role("STAKING_OPERATOR_ROLE"), operator.address)).to.equal(true);
    });
});
