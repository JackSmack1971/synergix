const { expect } = require("chai");
const { ethers, upgrades } = require("hardhat");

describe("Upgrade validation: UUPS authorization and basic storage retention", function () {
    it("rejects an unprivileged upgrade and preserves proxy state across an authorized same-layout upgrade", async function () {
        const [deployer, admin, user] = await ethers.getSigners();
        const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
        const amount = ethers.utils.parseEther("77");

        const Token = await ethers.getContractFactory("SynergiXToken");
        const token = await upgrades.deployProxy(
            Token,
            [admin.address, ethers.constants.AddressZero],
            { initializer: "initialize" }
        );
        await token.deployed();
        await token.connect(admin).grantRole(role("STAKING_ROLE"), admin.address);
        await token.connect(admin).mint(user.address, amount);

        await upgrades.validateUpgrade(token.address, Token);
        const nextImplementation = await Token.deploy();
        await nextImplementation.deployed();

        let unauthorizedUpgradeFailed = false;
        try {
            await token.connect(user).upgradeTo(nextImplementation.address);
        } catch (error) {
            unauthorizedUpgradeFailed = String(error.message).includes("missing role");
        }
        expect(unauthorizedUpgradeFailed).to.equal(true);

        await token.connect(admin).upgradeTo(nextImplementation.address);
        const upgradedToken = Token.attach(token.address);
        expect((await upgradedToken.balanceOf(user.address)).eq(amount)).to.equal(true);
        expect((await upgradedToken.totalSupply()).eq(amount)).to.equal(true);
        expect(await upgradedToken.hasRole(role("ADMIN_ROLE"), admin.address)).to.equal(true);
        expect(await upgradedToken.staking()).to.equal(ethers.constants.AddressZero);
        expect(await upgrades.erc1967.getImplementationAddress(token.address)).to.equal(nextImplementation.address);
    });

    it("locks the standalone implementation against initialization", async function () {
        const [deployer, admin, attacker] = await ethers.getSigners();
        const role = (name) => ethers.utils.keccak256(ethers.utils.toUtf8Bytes(name));
        const Token = await ethers.getContractFactory("SynergiXToken");
        const proxy = await upgrades.deployProxy(
            Token,
            [admin.address, ethers.constants.AddressZero],
            { initializer: "initialize" }
        );
        await proxy.deployed();

        const implementation = await Token.deploy();
        await implementation.deployed();
        const standalone = Token.attach(implementation.address);

        let directInitializationRejected = false;
        try {
            await standalone.connect(attacker).initialize(attacker.address, ethers.constants.AddressZero);
        } catch (error) {
            directInitializationRejected = String(error.message).includes("already initialized");
        }
        expect(directInitializationRejected).to.equal(true);
        expect(await standalone.hasRole(role("ADMIN_ROLE"), attacker.address)).to.equal(false);
        expect(await upgrades.erc1967.getImplementationAddress(proxy.address)).to.not.equal(implementation.address);
        expect(await proxy.hasRole(role("ADMIN_ROLE"), admin.address)).to.equal(true);
        expect(await proxy.hasRole(role("ADMIN_ROLE"), attacker.address)).to.equal(false);
    });
});
