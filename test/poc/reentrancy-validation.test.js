const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Reentrancy validation: token transfer callback", function () {
    it("blocks nested stakeStart from transferFrom and completes the outer stake once", async function () {
        const [owner, user] = await ethers.getSigners();
        const principal = ethers.utils.parseEther("1000000");

        const Token = await ethers.getContractFactory("ReentrantERC20Mock");
        const token = await Token.deploy();
        await token.deployed();

        const Staking = await ethers.getContractFactory("SynergiXStaking");
        const staking = await Staking.deploy(token.address);
        await staking.deployed();
        await token.setStaking(staking.address);
        await staking.connect(owner).grantStakingOperator(token.address);

        await token.mint(user.address, principal);
        await token.connect(user).approve(staking.address, principal);
        await staking.connect(owner).stakeStart(principal, 1, user.address);

        expect(await token.reentryRejected()).to.equal(true);
        expect((await staking.numStakes(user.address)).toNumber()).to.equal(1);
        expect((await token.balanceOf(user.address)).isZero()).to.equal(true);
        expect((await token.balanceOf(staking.address)).eq(principal)).to.equal(true);
    });
});
