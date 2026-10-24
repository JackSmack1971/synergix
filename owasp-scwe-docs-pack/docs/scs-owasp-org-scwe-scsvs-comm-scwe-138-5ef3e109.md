---
title: "SCWE-138: Reentrancy via ERC721/ERC1155 Safe Transfer Callbacks"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.575Z"
---
*Last updated: August 19, 2026*


# SCWE-138: Reentrancy via ERC721/ERC1155 Safe Transfer Callbacks

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#relationships "Permanent link")

-   CWE-841: Improper Enforcement of Behavioral Workflow
    [https://cwe.mitre.org/data/definitions/841.html](https://cwe.mitre.org/data/definitions/841.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#description "Permanent link")

ERC721 `safeTransferFrom` and ERC1155 `safeTransferFrom` invoke `onERC721Received` or `onERC1155Received` on the recipient contract. If the recipient is a contract that accepts NFTs and performs sensitive logic (e.g., withdrawals, state updates) inside these callbacks without reentrancy protection, an attacker can reenter the sender contract during the transfer and exploit stale state—similar to ERC777 hooks (SCWE-104) but for NFTs.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#remediation "Permanent link")

-   Add `nonReentrant` guards around functions that perform NFT transfers and any logic that could be reentered via the receiver callback.
-   Update state (e.g., balances, accounting) before calling `safeTransferFrom`.
-   Consider using `transferFrom` instead of `safeTransferFrom` when the recipient is trusted, to avoid callbacks.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-3)interface IERC721 {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-4)    function safeTransferFrom(address from, address to, uint256 tokenId) external; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-5)} [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-6)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-7)contract NFTVault {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-8)    mapping(address => uint256) public deposits;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-9)    IERC721 public nft; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-11)    function deposit(uint256 tokenId) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-12)        nft.safeTransferFrom(msg.sender, address(this), tokenId);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-13)        deposits[msg.sender]++;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-14)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-15)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-16)    function withdraw(uint256 tokenId) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-17)        require(deposits[msg.sender] > 0, "No deposit");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-18)        nft.safeTransferFrom(address(this), msg.sender, tokenId);  // Callback here—attacker reenters        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-19)        deposits[msg.sender]--;  // Too late: attacker already reentered and passed the check    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-20)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-0-21)}`

**Why vulnerable:** During `withdraw`, `safeTransferFrom` calls `onERC721Received` on the recipient before the state update. A malicious contract can reenter `withdraw` in that callback, pass the `deposits[msg.sender] > 0` check again, and withdraw a second NFT (double withdrawal).

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-2)import "@openzeppelin/contracts/security/ReentrancyGuard.sol"; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-4)contract NFTVault is ReentrancyGuard {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-5)    mapping(address => uint256) public deposits;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-6)    IERC721 public nft; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-8)    function withdraw(uint256 tokenId) external nonReentrant {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-9)        require(deposits[msg.sender] > 0, "No deposit");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-10)        deposits[msg.sender]--;        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-11)        nft.safeTransferFrom(address(this), msg.sender, tokenId);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/#__codelineno-1-13)}`

**Fix:** `nonReentrant` blocks reentry through the ERC721 receiver callback.
