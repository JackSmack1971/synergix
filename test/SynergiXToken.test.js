const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("SynergiXToken", function () {
    let token;
    let staking;
    let owner;
    let admin;
    let user;

    const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
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

    it("initializes token metadata and assigns admin access", async function () {
        expect(await token.name()).to.equal("SynergiX Token");
        expect(await token.symbol()).to.equal("SNX");
        expect(await token.hasRole(role("ADMIN_ROLE"), admin.address)).to.equal(true);
        expect(await token.hasRole(role("STAKING_ROLE"), staking.address)).to.equal(true);
        expect((await token.totalSupply()).isZero()).to.equal(true);
    });

    it("only allows the configured staking contract to mint", async function () {
        const amount = ethers.utils.parseEther("100");
        await expectRevert(token.connect(user).mint(user.address, amount),
            `AccessControl: account ${user.address.toLowerCase()} is missing role ${role("STAKING_ROLE")}`);

        await token.connect(admin).grantRole(role("STAKING_ROLE"), user.address);
        await token.connect(user).mint(user.address, amount);
        expect((await token.balanceOf(user.address)).eq(amount)).to.equal(true);
    });

    it("allows staking to be wired once and only by an admin", async function () {
        await expectRevert(token.connect(owner).setStakingContract(user.address),
            `AccessControl: account ${owner.address.toLowerCase()} is missing role ${role("ADMIN_ROLE")}`);
        await expectRevert(token.connect(admin).setStakingContract(user.address), "Staking contract already set");
    });

    it("allows admin role management and rejects unauthorized changes", async function () {
        await token.connect(admin).grantAdminRole(user.address);
        expect(await token.hasRole(role("ADMIN_ROLE"), user.address)).to.equal(true);
        await token.connect(admin).revokeAdminRole(user.address);
        expect(await token.hasRole(role("ADMIN_ROLE"), user.address)).to.equal(false);

        await expectRevert(token.connect(user).grantRole(role("ADMIN_ROLE"), owner.address));
    });
});
