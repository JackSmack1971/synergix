const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("SynergiXStakingV1", function () {
    const annualRateBps = 1000;
    const minimumStake = ethers.utils.parseEther("10");
    const maximumStake = ethers.utils.parseEther("1000");
    const minimumDuration = 3600;
    const maximumDuration = 30 * 24 * 60 * 60;
    const stakeAmount = ethers.utils.parseEther("100");

    let token;
    let staking;
    let admin;
    let funder;
    let user;
    let other;

    function expectedReward(amount, durationSeconds) {
        return amount
            .mul(annualRateBps)
            .mul(durationSeconds)
            .div(10_000 * 365 * 24 * 60 * 60);
    }

    async function expectRevert(promise, errorName) {
        try {
            await promise;
        } catch (error) {
            expect(error.message).to.include(errorName);
            return;
        }
        expect.fail(`Expected ${errorName} revert`);
    }

    async function deployStaking(asset = token) {
        const Factory = await ethers.getContractFactory("SynergiXStakingV1");
        const instance = await Factory.deploy(
            asset.address,
            annualRateBps,
            minimumStake,
            maximumStake,
            minimumDuration,
            maximumDuration
        );
        await instance.deployed();
        return instance;
    }

    async function fundReserve(instance, asset = token, amount) {
        await asset.connect(admin).mint(funder.address, amount);
        await asset.connect(funder).approve(instance.address, amount);
        await instance.connect(funder).fundRewards(amount);
    }

    beforeEach(async function () {
        [admin, funder, user, other] = await ethers.getSigners();
        const Token = await ethers.getContractFactory("SynergiXToken");
        token = await upgrades.deployProxy(
            Token,
            [admin.address, ethers.constants.AddressZero],
            { initializer: "initialize" }
        );
        await token.deployed();
        await token.connect(admin).grantRole(
            ethers.utils.keccak256(ethers.utils.toUtf8Bytes("STAKING_ROLE")),
            admin.address
        );
        staking = await deployStaking();
    });

    it("stores entry-fixed simple rewards and reserves them atomically", async function () {
        const duration = 30 * 24 * 60 * 60;
        const reward = expectedReward(stakeAmount, duration);
        await fundReserve(staking, token, reward);
        await token.connect(admin).mint(user.address, stakeAmount);
        await token.connect(user).approve(staking.address, stakeAmount);

        await staking.connect(user).stake(stakeAmount, duration);

        const position = await staking.positions(1);
        expect(position.beneficiary).to.equal(user.address);
        expect(position.principal.eq(stakeAmount)).to.equal(true);
        expect(position.fixedReward.eq(reward)).to.equal(true);
        expect(position.withdrawn).to.equal(false);
        expect((await staking.totalPrincipalLiability()).eq(stakeAmount)).to.equal(true);
        expect((await staking.totalReservedRewardLiability()).eq(reward)).to.equal(true);
        expect((await staking.availableRewardReserve()).isZero()).to.equal(true);
        expect((await token.balanceOf(staking.address)).eq(stakeAmount.add(reward))).to.equal(true);
    });

    it("rejects unfunded or out-of-range positions without changing balances", async function () {
        await token.connect(admin).mint(user.address, stakeAmount);
        await token.connect(user).approve(staking.address, stakeAmount);

        await expectRevert(
            staking.connect(user).stake(stakeAmount, maximumDuration),
            "InsufficientRewardReserve"
        );
        await expectRevert(
            staking.connect(user).stake(minimumStake.sub(1), minimumDuration),
            "AmountOutOfRange"
        );
        await expectRevert(
            staking.connect(user).stake(stakeAmount, minimumDuration - 1),
            "DurationOutOfRange"
        );

        expect((await token.balanceOf(user.address)).eq(stakeAmount)).to.equal(true);
        expect((await staking.totalPrincipalLiability()).isZero()).to.equal(true);
        expect((await staking.nextPositionId()).eq(1)).to.equal(true);
    });

    it("does not accept commitments that exceed the remaining funded reward reserve", async function () {
        const duration = maximumDuration;
        const reward = expectedReward(stakeAmount, duration);
        await fundReserve(staking, token, reward);
        await token.connect(admin).mint(user.address, stakeAmount.mul(2));
        await token.connect(user).approve(staking.address, stakeAmount.mul(2));

        await staking.connect(user).stake(stakeAmount, duration);
        await expectRevert(
            staking.connect(user).stake(stakeAmount, duration),
            "InsufficientRewardReserve"
        );

        expect((await staking.totalPrincipalLiability()).eq(stakeAmount)).to.equal(true);
        expect((await staking.totalReservedRewardLiability()).eq(reward)).to.equal(true);
        expect((await staking.availableRewardReserve()).isZero()).to.equal(true);
        expect((await token.balanceOf(user.address)).eq(stakeAmount)).to.equal(true);
        expect((await staking.nextPositionId()).eq(2)).to.equal(true);
    });

    it("settles at the inclusive boundary and keeps reward fixed after maturity", async function () {
        const duration = minimumDuration;
        const reward = expectedReward(stakeAmount, duration);
        await fundReserve(staking, token, reward.mul(2));
        await token.connect(admin).mint(user.address, stakeAmount.mul(2));
        await token.connect(user).approve(staking.address, stakeAmount.mul(2));
        const stakeReceipt = await (await staking.connect(user).stake(stakeAmount, duration)).wait();
        const stakeBlock = await ethers.provider.getBlock(stakeReceipt.blockNumber);
        const position = await staking.positions(1);
        const maturity = position.maturityTimestamp.toNumber();
        expect(maturity).to.equal(stakeBlock.timestamp + duration);
        await staking.connect(user).stake(stakeAmount, duration);
        const delayedMaturity = (await staking.positions(2)).maturityTimestamp.toNumber();

        await expectRevert(staking.connect(other).withdraw(1), "NotBeneficiary");
        await ethers.provider.send("evm_setNextBlockTimestamp", [maturity]);
        await staking.connect(user).withdraw(1);

        expect((await token.balanceOf(user.address)).eq(stakeAmount.add(reward))).to.equal(true);
        expect((await token.balanceOf(other.address)).isZero()).to.equal(true);
        expect((await staking.positions(1)).withdrawn).to.equal(true);
        await expectRevert(staking.connect(user).withdraw(1), "PositionAlreadyWithdrawn");

        await ethers.provider.send("evm_setNextBlockTimestamp", [delayedMaturity + 7 * 24 * 60 * 60]);
        await staking.connect(user).withdraw(2);
        expect((await token.balanceOf(user.address)).eq(stakeAmount.mul(2).add(reward.mul(2)))).to.equal(true);
        expect((await staking.totalPrincipalLiability()).isZero()).to.equal(true);
        expect((await staking.totalReservedRewardLiability()).isZero()).to.equal(true);
        expect((await staking.availableRewardReserve()).isZero()).to.equal(true);
    });

    it("rejects fee-on-transfer and false-returning token behavior atomically", async function () {
        const Mock = await ethers.getContractFactory("SynergiXV1CallbackTokenMock");
        const mock = await Mock.deploy();
        await mock.deployed();
        const instance = await deployStaking(mock);
        const duration = maximumDuration;
        const reward = expectedReward(stakeAmount, duration);
        await mock.mint(funder.address, reward);
        await mock.connect(funder).approve(instance.address, reward);
        await instance.connect(funder).fundRewards(reward);
        await mock.mint(user.address, stakeAmount);
        await mock.connect(user).approve(instance.address, stakeAmount);

        await mock.configureTransferBehavior(false, 100);
        await expectRevert(
            instance.connect(user).stake(stakeAmount, duration),
            "UnsupportedTokenBehavior"
        );
        expect((await instance.totalPrincipalLiability()).isZero()).to.equal(true);
        expect((await instance.availableRewardReserve()).eq(reward)).to.equal(true);
        expect((await mock.balanceOf(user.address)).eq(stakeAmount)).to.equal(true);

        await mock.configureTransferBehavior(true, 0);
        await expectRevert(
            instance.connect(user).stake(stakeAmount, duration),
            "SafeERC20FailedOperation"
        );
        expect((await instance.totalPrincipalLiability()).isZero()).to.equal(true);
        expect((await instance.nextPositionId()).eq(1)).to.equal(true);
    });

    it("supports no-return ERC20 transfers through OpenZeppelin SafeERC20", async function () {
        const Mock = await ethers.getContractFactory("SynergiXV1CallbackTokenMock");
        const mock = await Mock.deploy();
        await mock.deployed();
        const instance = await deployStaking(mock);
        const duration = maximumDuration;
        const reward = expectedReward(stakeAmount, duration);
        await mock.configureNoReturn(true);
        await mock.mint(funder.address, reward);
        await mock.connect(funder).approve(instance.address, reward);
        await instance.connect(funder).fundRewards(reward);
        await mock.mint(user.address, stakeAmount);
        await mock.connect(user).approve(instance.address, stakeAmount);
        await instance.connect(user).stake(stakeAmount, duration);

        const position = await instance.positions(1);
        await ethers.provider.send("evm_setNextBlockTimestamp", [position.maturityTimestamp.toNumber()]);
        await instance.connect(user).withdraw(1);

        expect((await mock.balanceOf(user.address)).eq(stakeAmount.add(reward))).to.equal(true);
        expect((await instance.totalPrincipalLiability()).isZero()).to.equal(true);
        expect((await instance.totalReservedRewardLiability()).isZero()).to.equal(true);
    });

    it("accepts the configured amount and duration boundaries", async function () {
        const minReward = expectedReward(minimumStake, minimumDuration);
        const maxReward = expectedReward(maximumStake, maximumDuration);
        await fundReserve(staking, token, minReward.add(maxReward));
        await token.connect(admin).mint(user.address, minimumStake.add(maximumStake));
        await token.connect(user).approve(staking.address, minimumStake.add(maximumStake));

        await staking.connect(user).stake(minimumStake, minimumDuration);
        await staking.connect(user).stake(maximumStake, maximumDuration);

        expect((await staking.positions(1)).principal.eq(minimumStake)).to.equal(true);
        expect((await staking.positions(2)).principal.eq(maximumStake)).to.equal(true);
        expect((await staking.totalPrincipalLiability()).eq(minimumStake.add(maximumStake))).to.equal(true);
        expect((await staking.totalReservedRewardLiability()).eq(minReward.add(maxReward))).to.equal(true);
    });

    it("allows a zero-rounded reward without consuming reserve", async function () {
        const Factory = await ethers.getContractFactory("SynergiXStakingV1");
        const zeroRewardStaking = await Factory.deploy(
            token.address,
            1,
            1,
            1,
            1,
            1
        );
        await zeroRewardStaking.deployed();
        await token.connect(admin).mint(user.address, 1);
        await token.connect(user).approve(zeroRewardStaking.address, 1);

        await zeroRewardStaking.connect(user).stake(1, 1);

        expect((await zeroRewardStaking.positions(1)).fixedReward.isZero()).to.equal(true);
        expect((await zeroRewardStaking.totalReservedRewardLiability()).isZero()).to.equal(true);
    });

    it("keeps a mature position open if the token cannot deliver the exact payout", async function () {
        const Mock = await ethers.getContractFactory("SynergiXV1CallbackTokenMock");
        const mock = await Mock.deploy();
        await mock.deployed();
        const instance = await deployStaking(mock);
        const duration = maximumDuration;
        const reward = expectedReward(stakeAmount, duration);
        await mock.mint(funder.address, reward);
        await mock.connect(funder).approve(instance.address, reward);
        await instance.connect(funder).fundRewards(reward);
        await mock.mint(user.address, stakeAmount);
        await mock.connect(user).approve(instance.address, stakeAmount);
        const receipt = await (await instance.connect(user).stake(stakeAmount, duration)).wait();
        const block = await ethers.provider.getBlock(receipt.blockNumber);
        const position = await instance.positions(1);

        await mock.configureTransferBehavior(false, 100);
        await ethers.provider.send("evm_setNextBlockTimestamp", [position.maturityTimestamp.toNumber()]);
        await expectRevert(
            instance.connect(user).withdraw(1),
            "UnsupportedTokenBehavior"
        );

        const stillOpen = await instance.positions(1);
        expect(stillOpen.withdrawn).to.equal(false);
        expect((await instance.totalPrincipalLiability()).eq(stakeAmount)).to.equal(true);
        expect((await instance.totalReservedRewardLiability()).eq(reward)).to.equal(true);
        expect((await mock.balanceOf(instance.address)).eq(stakeAmount.add(reward))).to.equal(true);
        expect(block.timestamp).to.be.lessThan(position.maturityTimestamp.toNumber());
    });

    it("rolls back paused payout and allows withdrawal after transfers resume", async function () {
        const Mock = await ethers.getContractFactory("SynergiXV1CallbackTokenMock");
        const mock = await Mock.deploy();
        await mock.deployed();
        const instance = await deployStaking(mock);
        const duration = maximumDuration;
        const reward = expectedReward(stakeAmount, duration);
        await mock.mint(funder.address, reward);
        await mock.connect(funder).approve(instance.address, reward);
        await instance.connect(funder).fundRewards(reward);
        await mock.mint(user.address, stakeAmount);
        await mock.connect(user).approve(instance.address, stakeAmount);
        await instance.connect(user).stake(stakeAmount, duration);
        const position = await instance.positions(1);

        await ethers.provider.send("evm_setNextBlockTimestamp", [position.maturityTimestamp.toNumber()]);
        await mock.setTransfersPaused(true);
        await expectRevert(instance.connect(user).withdraw(1), "transfers paused");
        expect((await instance.positions(1)).withdrawn).to.equal(false);
        expect((await instance.totalPrincipalLiability()).eq(stakeAmount)).to.equal(true);

        await mock.setTransfersPaused(false);
        const reentry = instance.interface.encodeFunctionData("fundRewards", [1]);
        await mock.configureCallback(instance.address, reentry);
        await instance.connect(user).withdraw(1);

        expect(await mock.callbackAttempted()).to.equal(true);
        expect(await mock.callbackSucceeded()).to.equal(false);
        expect((await mock.balanceOf(user.address)).eq(stakeAmount.add(reward))).to.equal(true);
        expect((await instance.totalPrincipalLiability()).isZero()).to.equal(true);
    });

    it("blocks callback reentrancy without duplicating a position", async function () {
        const Mock = await ethers.getContractFactory("SynergiXV1CallbackTokenMock");
        const mock = await Mock.deploy();
        await mock.deployed();
        const instance = await deployStaking(mock);
        const duration = maximumDuration;
        const reward = expectedReward(stakeAmount, duration);
        await mock.mint(funder.address, reward);
        await mock.connect(funder).approve(instance.address, reward);
        await instance.connect(funder).fundRewards(reward);
        await mock.mint(user.address, stakeAmount);
        await mock.connect(user).approve(instance.address, stakeAmount);
        const reentry = instance.interface.encodeFunctionData("stake", [stakeAmount, duration]);
        await mock.configureCallback(instance.address, reentry);

        await instance.connect(user).stake(stakeAmount, duration);

        expect(await mock.callbackAttempted()).to.equal(true);
        expect(await mock.callbackSucceeded()).to.equal(false);
        expect((await instance.nextPositionId()).eq(2)).to.equal(true);
        expect((await instance.totalPrincipalLiability()).eq(stakeAmount)).to.equal(true);
        expect((await mock.balanceOf(instance.address)).eq(stakeAmount.add(reward))).to.equal(true);
    });
});
