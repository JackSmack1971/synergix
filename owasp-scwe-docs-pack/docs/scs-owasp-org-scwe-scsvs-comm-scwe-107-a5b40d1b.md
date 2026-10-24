---
title: "SCWE-107: Missing Chain ID Validation in Cross-Chain Messages"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.004Z"
---
*Last updated: August 19, 2026*


# SCWE-107: Missing Chain ID Validation in Cross-Chain Messages

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#relationships "Permanent link")

-   CWE-345: Insufficient Verification of Data Authenticity
    [https://cwe.mitre.org/data/definitions/345.html](https://cwe.mitre.org/data/definitions/345.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#description "Permanent link")

Cross-chain handlers that accept payloads without checking the source `chainId` or endpoint domain allow replay of messages from other networks or forks. Attackers can re-trigger transfers, minting, or governance actions on unintended chains.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#remediation "Permanent link")

-   Bind every inbound message to an expected source chain/domain and trusted sender.
-   Include `chainId`/domain separators in signed payloads and verify them before execution.
-   Maintain replay protection (nonces) per (sourceChain, sourceSender).

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-0-3)contract BridgeReceiver {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-0-4)    function receiveMessage(bytes calldata data) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-0-5)        _execute(data); // no chainId/source validation    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-0-7)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-3)contract BridgeReceiver {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-4)    mapping(uint256 => mapping(address => uint256)) public nonce; // per (chainId, sender)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-5)    address public trustedSender;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-6)    uint256 public trustedChainId; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-8)    function receiveMessage(uint256 srcChainId, address src, uint256 n, bytes calldata data) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-9)        require(srcChainId == trustedChainId && src == trustedSender, "unauthorized source");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-10)        require(n == nonce[srcChainId][src]++, "replay");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-11)        _execute(data);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/#__codelineno-1-13)}`
