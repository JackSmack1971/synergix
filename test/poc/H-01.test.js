const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("PoC STAKE-01: Unix-day reward index blocks ordinary matured claims", function () {
    it("shows a matured stake cannot end when daily data contains only the first appended record", async function () {
        const [owner, admin, user] = await ethers.getSigners();
        const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
        const minimumStake = ethers.utils.parseEther("1000000");

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
        await token.connect(admin).mint(user.address, minimumStake);
        await token.connect(user).approve(staking.address, minimumStake);

        // One append creates index 0; it does not create an entry for today's Unix day.
        await staking.connect(owner).addDailyData(1, 0);
        await token.connect(user).stake(minimumStake, 1);

        const stake = await staking.stakes(user.address, 0);
        const endDayIndex = stake.endTimestamp.div(86400);
        expect(endDayIndex.gt(0)).to.equal(true);
        await ethers.provider.send("evm_setNextBlockTimestamp", [stake.endTimestamp.toNumber()]);
        await ethers.provider.send("evm_mine", []);

        let revertText = "";
        try {
            await token.connect(user).stakeEnd(0);
        } catch (error) {
            revertText = [error.message, error.reason].filter(Boolean).join(" ");
        }
        expect(revertText).to.include("Invalid end day index.");
    });
});
