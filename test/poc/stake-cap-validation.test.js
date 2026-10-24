const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("Stake cap validation: public staking amount range", function () {
    it("rejects any value above the minimum because the token maximum equals the staking minimum", async function () {
        const [owner, admin, user] = await ethers.getSigners();
        const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
        const minimum = ethers.utils.parseEther("1000000");

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
        await token.connect(admin).mint(user.address, minimum.mul(2));
        await token.connect(user).approve(staking.address, minimum.mul(2));

        await token.connect(user).stake(minimum, 1);
        expect((await staking.numStakes(user.address)).eq(1)).to.equal(true);

        let aboveMinimumRejected = false;
        try {
            await token.connect(user).stake(minimum.add(1), 1);
        } catch (error) {
            aboveMinimumRejected = String(error.message).includes("Stake value exceeds maximum limit");
        }
        expect(aboveMinimumRejected).to.equal(true);
    });
});
