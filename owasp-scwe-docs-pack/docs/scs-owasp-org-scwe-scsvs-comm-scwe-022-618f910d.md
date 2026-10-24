---
title: "SCWE-022: Message Replay Vulnerabilities"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.132Z"
---
*Last updated: August 19, 2026*


# SCWE-022: Message Replay Vulnerabilities

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#relationships "Permanent link")

-   CWE-294: Authentication Bypass by Capture-replay
    [CWE-294 Link](https://cwe.mitre.org/data/definitions/294.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#description "Permanent link")

Message replay vulnerabilities occur when an attacker can reuse a valid message or transaction to perform unauthorized actions. This can lead to: - Unauthorized access to sensitive functions. - Loss of funds or data. - Exploitation of the contract's logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#remediation "Permanent link")

-   **Use nonces:** Include a unique nonce in each message to prevent reuse.
-   **Validate timestamps:** Ensure messages are only valid for a limited time.
-   **Implement replay protection:** Use established libraries or mechanisms to prevent replay attacks.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#examples "Permanent link")

-   **Vulnerable to Replay Attacks**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-0-3)contract ReplayVulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-0-4)    function processMessage(bytes memory message) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-0-5)        // Process message without replay protection    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-0-7)}`

-   **Protected Against Replay Attacks**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-3)contract ReplayProtected {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-4)    mapping(bytes32 => bool) public usedMessages; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-6)    function processMessage(bytes memory message, uint nonce, uint chainId) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-7)        bytes32 messageHash = keccak256(abi.encodePacked(message, nonce, chainId));        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-8)        require(!usedMessages[messageHash], "Message already used");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-9)        usedMessages[messageHash] = true;        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-10)        // Process message    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/#__codelineno-1-12)}`


* * *
