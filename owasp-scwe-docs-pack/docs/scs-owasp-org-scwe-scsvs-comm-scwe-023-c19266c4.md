---
title: "SCWE-023: Lack of Communication Authenticity"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.241Z"
---
*Last updated: August 19, 2026*


# SCWE-023: Lack of Communication Authenticity

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#description "Permanent link")

Lack of communication authenticity refers to the failure to verify the authenticity of messages or transactions. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of the contract's logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#remediation "Permanent link")

-   **Use signatures:** Require signed messages for critical actions.
-   **Validate inputs:** Ensure all messages are properly validated before processing.
-   **Implement secure communication:** Use secure protocols and libraries for communication.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#examples "Permanent link")

-   **Lack of Authenticity**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-0-3)contract NoAuthenticity {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-0-4)    function processMessage(bytes memory message) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-0-5)        // Process message without authenticity check    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-0-7)}`

-   **Authentic Communication**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-3)import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol"; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-5)contract AuthenticCommunication {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-6)    using ECDSA for bytes32; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-8)    function processMessage(bytes memory message, bytes memory signature) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-9)        bytes32 messageHash = keccak256(message);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-10)        address signer = messageHash.recover(signature);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-11)        require(signer == msg.sender, "Invalid signature");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-12)        // Process message    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/#__codelineno-1-14)}`


* * *
