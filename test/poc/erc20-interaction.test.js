const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ERC20 interaction validation: exact principal receipt", function () {
    async function deployFixture() {
        const [owner, user] = await ethers.getSigners();
        const principal = ethers.utils.parseEther("1000000");

        const Token = await ethers.getContractFactory("ReentrantERC20Mock");
        const token = await Token.deploy();
        await token.deployed();

        const Staking = await ethers.getContractFactory("SynergiXStaking");
        const staking = await Staking.deploy(token.address);
        await staking.deployed();
        await token.setStaking(staking.address);
        await staking.connect(owner).grantStakingOperator(owner.address);
        await staking.connect(owner).grantStakingOperator(token.address);
        await token.mint(user.address, principal);
        await token.connect(user).approve(staking.address, principal);

        return { owner, user, principal, token, staking };
    }

    it("rejects fee-on-transfer deposits without recording or retaining partial principal", async function () {
        const { owner, user, principal, token, staking } = await deployFixture();
        await token.setTransferFeeBps(100);

        let rejected = false;
        try {
            await staking.connect(owner).stakeStart(principal, 1, user.address);
        } catch (error) {
            rejected = String(error.message).includes("Unexpected token amount received.");
        }
        expect(rejected).to.equal(true);

        expect((await token.balanceOf(user.address)).eq(principal)).to.equal(true);
        expect((await token.balanceOf(staking.address)).isZero()).to.equal(true);
        expect((await staking.numStakes(user.address)).isZero()).to.equal(true);
        expect((await token.totalSupply()).eq(principal)).to.equal(true);
    });

    it("rejects a false-returning transferFrom without changing stake state", async function () {
        const { owner, user, principal, token, staking } = await deployFixture();
        await token.setReturnFalseFrom(true);

        let rejected = false;
        try {
            await staking.connect(owner).stakeStart(principal, 1, user.address);
        } catch (error) {
            rejected = String(error.message).includes("SafeERC20: ERC20 operation did not succeed");
        }
        expect(rejected).to.equal(true);

        expect((await token.balanceOf(user.address)).eq(principal)).to.equal(true);
        expect((await token.balanceOf(staking.address)).isZero()).to.equal(true);
        expect((await staking.numStakes(user.address)).isZero()).to.equal(true);
        expect((await token.totalSupply()).eq(principal)).to.equal(true);
    });
});
