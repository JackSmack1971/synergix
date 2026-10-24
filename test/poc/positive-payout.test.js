const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("Payout validation: correctly aligned daily data", function () {
    async function expectRevert(promise, message) {
        try {
            await promise;
        } catch (error) {
            expect(error.message).to.include(message);
            return;
        }
        expect.fail("Expected transaction to revert");
    }

    it("pays a matured stake once when day indexes 0 and 1 exist", async function () {
        const [owner, admin, user] = await ethers.getSigners();
        const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
        const principal = ethers.utils.parseEther("1000000");
        const interest = ethers.BigNumber.from(123);

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
        await token.connect(admin).grantRole(role("STAKING_ROLE"), admin.address);

        const shares = await staking.calcStakeShares(principal, 1);
        await staking.connect(owner).addDailyData(shares, 0);
        await staking.connect(owner).addDailyData(shares, interest);
        await token.connect(admin).mint(user.address, principal);
        await token.connect(user).approve(staking.address, principal);
        await token.connect(user).stake(principal, 1);

        const stake = await staking.stakes(user.address, 0);
        const endDayIndex = stake.endTimestamp.div(86400);
        if (endDayIndex.gt(1)) this.skip();
        expect(endDayIndex.eq(1)).to.equal(true);

        let earlyClaimFailed = false;
        try {
            await token.connect(user).stakeEnd(0);
        } catch (error) {
            earlyClaimFailed = String(error.message).includes("Stake has not ended yet.");
        }
        expect(earlyClaimFailed).to.equal(true);

        await ethers.provider.send("evm_setNextBlockTimestamp", [stake.endTimestamp.toNumber()]);
        await ethers.provider.send("evm_mine", []);
        await token.connect(user).stakeEnd(0);

        expect((await token.balanceOf(user.address)).eq(principal.add(interest))).to.equal(true);
        expect((await staking.stakes(user.address, 0)).stakeValue.isZero()).to.equal(true);
        expect((await token.balanceOf(staking.address)).eq(principal)).to.equal(true);

        let doubleClaimFailed = false;
        try {
            await token.connect(user).stakeEnd(0);
        } catch (error) {
            doubleClaimFailed = String(error.message).includes("Stake has already been ended.");
        }
        expect(doubleClaimFailed).to.equal(true);
    });

    it("rejects owner-supplied daily data with zero total shares", async function () {
        const [owner, admin] = await ethers.getSigners();

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
        await expectRevert(
            staking.connect(owner).addDailyData(0, 123),
            "Total stake shares must be greater than zero."
        );
        await staking.connect(owner).addDailyData(1, 0);
        expect((await staking.dailyData(0)).totalSShares.eq(1)).to.equal(true);
    });
});
