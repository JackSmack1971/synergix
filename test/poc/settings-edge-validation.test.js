const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("Settings validation: invalid minimum stake duration setting", function () {
    it("shows owner-set maxStakeDays 0 or 1 prevents valid stakes", async function () {
        const [owner, admin, user] = await ethers.getSigners();
        const principal = ethers.utils.parseEther("1000000");

        const Token = await ethers.getContractFactory("SynergiXToken");
        const token = await upgrades.deployProxy(
            Token,
            [admin.address, ethers.constants.AddressZero],
            { initializer: "initialize" }
        );
        await token.deployed();

        const Staking = await ethers.getContractFactory("SynergiXStaking");
        const staking = await Staking.deploy(token.address);
        await staking.deployed();
        await token.connect(admin).setStakingContract(staking.address);
        await staking.connect(owner).grantStakingOperator(token.address);
        const stakingRole = ethers.utils.keccak256(ethers.utils.toUtf8Bytes("STAKING_ROLE"));
        await token.connect(admin).grantRole(stakingRole, admin.address);
        await token.connect(admin).mint(user.address, principal);
        await token.connect(user).approve(staking.address, principal);

        await staking.connect(owner).setMaxStakeDays(1);
        let oneDaySettingRejectedStake = false;
        try {
            await token.connect(user).stake(principal, 1);
        } catch (error) {
            oneDaySettingRejectedStake = Boolean(error);
        }
        expect(oneDaySettingRejectedStake).to.equal(true);

        await staking.connect(owner).setMaxStakeDays(0);
        let zeroDaySettingRejectedStake = false;
        try {
            await token.connect(user).stake(principal, 1);
        } catch (error) {
            zeroDaySettingRejectedStake = String(error.message).includes("Invalid stake days.");
        }
        expect(zeroDaySettingRejectedStake).to.equal(true);
    });
});
