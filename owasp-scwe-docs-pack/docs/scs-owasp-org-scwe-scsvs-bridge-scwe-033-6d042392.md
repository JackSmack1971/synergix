---
title: "SCWE-033: Chain Split Risks"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:37.110Z"
---
*Last updated: August 19, 2026*


# SCWE-033: Chain Split Risks

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#description "Permanent link")

Chain split risks refer to vulnerabilities that arise when a blockchain splits into multiple chains, such as during a hard fork. This can lead to: - Confusion or inconsistencies in contract logic. - Loss of funds or data. - Exploitation of vulnerabilities in cross-chain operations.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#remediation "Permanent link")

-   **Handle chain splits:** Implement logic to handle potential chain splits.
-   **Use chain identifiers:** Include chain identifiers in cross-chain communications.
-   **Test thoroughly:** Conduct extensive testing to ensure contract logic is robust.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#examples "Permanent link")

-   **Vulnerable to Chain Splits**

    `[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-0-3)contract ChainSplitVulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-0-4)    function processTransaction(bytes memory data) public {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-0-5)        // Process transaction without chain split handling    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-0-7)}`

-   **Protected Against Chain Splits**

    `[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-3)contract ChainSplitProtected {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-4)    uint public chainId; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-6)    constructor(uint _chainId) {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-7)        chainId = _chainId;    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-10)    function processTransaction(bytes memory data, uint transactionChainId) public {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-11)        require(transactionChainId == chainId, "Invalid chain ID");        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-12)        // Process transaction    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/#__codelineno-1-14)}`


* * *
