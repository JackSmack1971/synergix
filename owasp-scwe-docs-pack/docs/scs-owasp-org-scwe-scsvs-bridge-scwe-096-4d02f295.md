---
title: "SCWE-096: Missing Token Burn During Cross-Chain NFT Withdrawal"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:37.600Z"
---
*Last updated: August 19, 2026*


# SCWE-096: Missing Token Burn During Cross-Chain NFT Withdrawal

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#relationships "Permanent link")

-   CWE-345: Insufficient Verification of Data Authenticity
    [CWE-345 Link](https://cwe.mitre.org/data/definitions/345.html)
-   CWE-664: Improper Control of a Resource Through Its Lifetime
    [CWE-664 Link](https://cwe.mitre.org/data/definitions/664.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#description "Permanent link")

This weakness occurs when a cross-chain bridge allows withdrawals from Chain B to Chain A without properly burning or locking the corresponding token on the source chain (Chain B) before initiating the cross-chain transaction.

As a result, the same token can exist simultaneously on both chains, enabling a double-spend scenario where malicious actors can sell, transfer, or use the same token on multiple chains.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#remediation "Permanent link")

1.  Burn the NFT

    -   Call the `burn(tokenId)` function on the L2 NFT contract before sending the cross-chain withdrawal request.
    -   This ensures that the NFT no longer exists on L2 and cannot be reused, transferred, or sold.
2.  Alternatively, Lock the NFT (if burning isn’t possible)

    -   If NFTs are not meant to be permanently destroyed, implement a lock mechanism to freeze the token on L2 until the cross-chain withdrawal is completed successfully.
3.  Update Cross-Chain Workflow

    -   Enforce the burn/lock operation as part of the withdrawal process.
    -   Revert the entire transaction if the burn/lock fails.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#examples "Permanent link")

-   **Vulnerable Code (Not Burning Token Before Sending Cross Chain Message)**

    `[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-4)contract SourceChainNFTGateway {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-5)    mapping(address => mapping(uint256 => address)) public ownerOf; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-7)    function withdrawNFT(address l2Token, uint256 tokenId) external {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-8)        require(ownerOf[l2Token][tokenId] == msg.sender, "Not the owner"); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-9)        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-10)        // ❌ Send cross-chain message to Destination Chain (omitted for simplicity)        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-11)        // NFT is still available on Source Chain → double-spend possible    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-12)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-0-13)}`

-   **Safe Code (Burning Token Before Sending Cross Chain Message)**

    `[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-4)interface IL2NFT {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-5)    function burn(uint256 tokenId) external; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-6)} [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-7)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-8)contract SourceChainNFTGateway {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-9)    mapping(address => mapping(uint256 => address)) public ownerOf; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-11)    function withdrawNFT(address l2Token, uint256 tokenId) external {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-12)        require(ownerOf[l2Token][tokenId] == msg.sender, "Not the owner"); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-13)        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-14)        // ✅ Burn the NFT on Source Chain to prevent double-spend        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-15)        IL2NFT(l2Token).burn(tokenId); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-16)        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-17)        // Send cross-chain message to Destination Chain (omitted for simplicity)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-18)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/#__codelineno-1-19)}`
