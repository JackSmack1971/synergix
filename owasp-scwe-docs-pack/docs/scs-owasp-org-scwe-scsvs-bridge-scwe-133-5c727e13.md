---
title: "SCWE-133: Missing Replay Nonce per Bridge Lane"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:37.818Z"
---
*Last updated: August 19, 2026*


# SCWE-133: Missing Replay Nonce per Bridge Lane

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#relationships "Permanent link")

-   CWE-294: Authentication Bypass by Capture-replay
    [https://cwe.mitre.org/data/definitions/294.html](https://cwe.mitre.org/data/definitions/294.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#description "Permanent link")

Bridge receivers that do not track nonces per source chain/sender allow the same message to be replayed, causing duplicate mints or withdrawals. Forked chains can also replay historical messages if lanes are not isolated.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#remediation "Permanent link")

-   Maintain monotonically increasing nonces per (sourceChain, sourceSender).
-   Reject messages with reused or out-of-order nonces.
-   Bind nonces into signed payloads or proofs to prevent tampering.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-0-1)function receive(bytes calldata payload) external {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-0-2)    _execute(payload); // no nonce tracking [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-0-3)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-1-1)mapping(uint256 => mapping(address => uint256)) public nonce; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-1-3)function receive(uint256 srcChain, address src, uint256 n, bytes calldata payload) external {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-1-4)    require(n == nonce[srcChain][src]++, "replay");    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-1-5)    _execute(payload); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/#__codelineno-1-6)}`
