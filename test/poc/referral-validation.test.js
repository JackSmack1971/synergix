const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("Referral validation: reward issuance and cycle rejection", function () {
    it("pays the configured referral percentages once and rejects a two-account cycle", async function () {
        const [owner, admin, referrer, referred] = await ethers.getSigners();
        const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
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
        await token.connect(admin).grantRole(role("STAKING_ROLE"), admin.address);

        for (const account of [referrer, referred]) {
            await token.connect(admin).mint(account.address, principal);
            await token.connect(account).approve(staking.address, principal);
        }

        await token.connect(referrer).stake(principal, 1);
        await staking.connect(referred).setMyReferrer(referrer.address);
        await token.connect(referred).stake(principal, 1);

        expect(await staking.referrers(referred.address)).to.equal(referrer.address);
        expect((await token.balanceOf(referred.address)).eq(principal.div(100))).to.equal(true);
        expect((await token.balanceOf(referrer.address)).eq(principal.mul(2).div(100))).to.equal(true);

        let cycleRejected = false;
        try {
            await staking.connect(referrer).setMyReferrer(referred.address);
        } catch (error) {
            cycleRejected = String(error.message).includes("Circular referrer relationship detected.");
        }
        expect(cycleRejected).to.equal(true);
        expect(await staking.referrers(referrer.address)).to.equal(ethers.constants.AddressZero);
    });
});
