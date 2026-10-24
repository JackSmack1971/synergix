---
title: "SCWE-135: ERC4626 Share Inflation via Donations"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:39.688Z"
---
*Last updated: August 19, 2026*


# SCWE-135: ERC4626 Share Inflation via Donations

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#relationships "Permanent link")

-   CWE-682: Incorrect Calculation
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#description "Permanent link")

ERC4626 vaults that do not guard against free-asset donations can skew `totalAssets` and share price. Attackers can donate assets to inflate share value and then mint shares cheaply before normalization, extracting value from existing holders.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#remediation "Permanent link")

-   Normalize share price on every deposit/mint using current `totalAssets`.
-   Optionally block unsolicited donations by reverting on direct transfers or sweeping them into reserves before new share mints.
-   Add tests for donation and price-per-share edge cases.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-0-1)// totalAssets() uses balanceOf; donations inflate it and skew share price [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-0-2)function mint(uint256 shares) external {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-0-3)    uint256 assets = previewMint(shares);    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-0-4)    asset.transferFrom(msg.sender, address(this), assets);    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-0-5)    _mint(msg.sender, shares); [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-0-6)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-1)uint256 private _accountedAssets; // internal balance; excludes direct transfers [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-3)function totalAssets() public view override returns (uint256) {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-4)    return _accountedAssets; // donations do not affect share price [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-5)} [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-6)[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-7)function deposit(uint256 assets, address receiver) public override returns (uint256 shares) {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-8)    uint256 before = asset.balanceOf(address(this));    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-9)    shares = super.deposit(assets, receiver);    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-10)    _accountedAssets += (asset.balanceOf(address(this)) - before); [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-11)} [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-12)[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-13)function withdraw(uint256 assets, address receiver, address owner) public override returns (uint256 shares) {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-14)    shares = super.withdraw(assets, receiver, owner);    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-15)    _accountedAssets -= assets; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/#__codelineno-1-16)}`
