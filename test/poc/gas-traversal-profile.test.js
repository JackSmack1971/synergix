const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

const principal = ethers.utils.parseEther("1000000");
const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));

async function deploySystem() {
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
    await token.connect(admin).setStakingContract(staking.address);
    await token.connect(admin).grantRole(role("STAKING_ROLE"), admin.address);
    await staking.connect(owner).grantStakingOperator(token.address);
    return { owner, admin, token, staking };
}

async function giveStake(token, staking, admin, account, count = 1) {
    await token.connect(admin).mint(account.address, principal.mul(count));
    await token.connect(account).approve(staking.address, principal.mul(count));
    for (let i = 0; i < count; i++) {
        await token.connect(account).stake(principal, 1);
    }
}

describe("Gas profile: referral and active-stake scans", function () {
    it("measures referral ancestry growth while retaining cycle checks", async function () {
        const { admin, token, staking } = await deploySystem();
        const signers = await ethers.getSigners();
        const users = signers.slice(2, 15);

        for (const user of users) {
            await giveStake(token, staking, admin, user);
        }

        const gasByDepth = {};
        for (let depth = 1; depth < users.length; depth++) {
            const tx = await staking.connect(users[depth]).setMyReferrer(users[depth - 1].address);
            const receipt = await tx.wait();
            if ([1, 4, 8, 12].includes(depth)) {
                gasByDepth[depth] = receipt.gasUsed.toNumber();
            }
        }

        console.log("Referral ancestry gas by depth:", JSON.stringify(gasByDepth));
        expect(gasByDepth[12]).to.be.greaterThan(gasByDepth[1]);

        let cycleRejected = false;
        try {
            await staking.connect(users[0]).setMyReferrer(users[12].address);
        } catch (error) {
            cycleRejected = String(error.message).includes("Circular referrer relationship detected.");
        }
        expect(cycleRejected).to.equal(true);
    });

    it("measures active-stake scan growth when the only active stake is last", async function () {
        const { admin, token, staking } = await deploySystem();
        const signers = await ethers.getSigners();
        const referrers = signers.slice(2, 6);
        const candidates = signers.slice(6, 10);
        const expiredCounts = [1, 4, 8, 12];

        for (let i = 0; i < referrers.length; i++) {
            await giveStake(token, staking, admin, referrers[i], expiredCounts[i]);
        }

        await ethers.provider.send("evm_increaseTime", [86402]);
        await ethers.provider.send("evm_mine", []);

        for (const referrer of referrers) {
            await giveStake(token, staking, admin, referrer);
        }

        const gasByStakeCount = {};
        for (let i = 0; i < referrers.length; i++) {
            const tx = await staking.connect(candidates[i]).setMyReferrer(referrers[i].address);
            const receipt = await tx.wait();
            gasByStakeCount[expiredCounts[i] + 1] = receipt.gasUsed.toNumber();
        }

        console.log("Active-stake scan gas by stake count:", JSON.stringify(gasByStakeCount));
        expect(gasByStakeCount[13]).to.be.greaterThan(gasByStakeCount[2]);
    });
});
