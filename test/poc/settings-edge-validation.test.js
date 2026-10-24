const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

async function expectRevert(promise, message) {
    try {
        await promise;
    } catch (error) {
        expect(error.message).to.include(message);
        return;
    }
    expect.fail("Expected transaction to revert");
}

describe("Settings validation: max stake duration lower bound", function () {
    it("rejects maxStakeDays 0 or 1 and keeps valid stakes available", async function () {
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

        await expectRevert(
            staking.connect(owner).setMaxStakeDays(1),
            "Must allow at least two stake days."
        );
        await expectRevert(
            staking.connect(owner).setMaxStakeDays(0),
            "Must allow at least two stake days."
        );
        expect(Number(await staking.maxStakeDays())).to.equal(5555);
        await expectRevert(staking.calcStakeShares(principal, 0), "Invalid stake days.");
        await expectRevert(staking.calcStakeShares(principal, 5556), "Invalid stake days.");

        await token.connect(user).stake(principal, 1);
        expect((await staking.numStakes(user.address)).toNumber()).to.equal(1);
    });
});
