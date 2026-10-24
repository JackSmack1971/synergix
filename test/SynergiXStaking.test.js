const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("SynergiXStaking", function () {
    let token;
    let staking;
    let owner;
    let admin;
    let user;

    const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
    const minimumStake = ethers.utils.parseEther("1000000");
    async function expectRevert(promise, message) {
        try { await promise; } catch (error) {
            const details = [error.message, error.reason, error.error && error.error.message].filter(Boolean).join(" ");
            if (message) expect(details).to.include(message);
            return;
        }
        expect.fail("Expected transaction to revert");
    }

    beforeEach(async function () {
        [owner, admin, user] = await ethers.getSigners();

        const Token = await ethers.getContractFactory("SynergiXToken");
        token = await upgrades.deployProxy(
            Token,
            [admin.address, ethers.constants.AddressZero],
            { initializer: "initialize" }
        );
        await token.deployed();

        const Staking = await ethers.getContractFactory("SynergiXStaking");
        staking = await Staking.deploy(token.address);
        await staking.deployed();

        await token.connect(admin).setStakingContract(staking.address);
        await token.connect(admin).grantRole(role("STAKING_ROLE"), admin.address);
        await staking.connect(owner).grantStakingOperator(token.address);
    });

    it("deploys as a constructor-based contract with the supplied token", async function () {
        expect(await staking.token()).to.equal(token.address);
        expect((await staking.shareRate()).eq(ethers.utils.parseEther("1"))).to.equal(true);
        expect(await staking.isLaunchBonusActive()).to.equal(true);
        expect(await staking.hasRole(role("STAKING_OPERATOR_ROLE"), owner.address)).to.equal(true);
    });

    it("accepts a valid stake through the token entry point and escrows principal", async function () {
        await token.connect(admin).mint(user.address, minimumStake);
        await token.connect(user).approve(staking.address, minimumStake);

        await token.connect(user).stake(minimumStake, 30);

        expect((await staking.numStakes(user.address)).eq(1)).to.equal(true);
        expect((await token.balanceOf(user.address)).isZero()).to.equal(true);
        expect((await token.balanceOf(staking.address)).eq(minimumStake)).to.equal(true);
        expect(await staking.stakeActive(0, user.address)).to.equal(true);
    });

    it("leaves balances and positions unchanged when transferFrom fails", async function () {
        await token.connect(admin).mint(user.address, minimumStake);

        await expectRevert(token.connect(user).stake(minimumStake, 30), "insufficient allowance");

        expect((await token.balanceOf(user.address)).eq(minimumStake)).to.equal(true);
        expect((await token.balanceOf(staking.address)).isZero()).to.equal(true);
        expect((await staking.numStakes(user.address)).isZero()).to.equal(true);
    });

    it("rejects stakes below the configured minimum and invalid durations", async function () {
        const belowMinimum = minimumStake.sub(1);
        await token.connect(admin).mint(user.address, minimumStake);
        await token.connect(user).approve(staking.address, minimumStake);

        await expectRevert(token.connect(user).stake(belowMinimum, 30), "Stake value must be at least 1 million SYN.");
        await expectRevert(token.connect(user).stake(minimumStake, 0), "Invalid staking duration");
    });

    it("enforces operator authorization on direct staking calls", async function () {
        await expectRevert(staking.connect(user).stakeStart(minimumStake, 30, user.address),
            `AccessControl: account ${user.address.toLowerCase()} is missing role ${role("STAKING_OPERATOR_ROLE")}`);
    });

    it("allows the owner to update bounded staking settings", async function () {
        await staking.connect(owner).setBurnRate(5);
        expect((await staking.burnRate()).eq(5)).to.equal(true);
        await expectRevert(staking.connect(owner).setBurnRate(101), "Burn rate must be between 0 and 100.");
        await expectRevert(staking.connect(user).setBurnRate(5));
    });
});
