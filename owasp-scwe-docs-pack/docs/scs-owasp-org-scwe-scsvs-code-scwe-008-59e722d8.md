---
title: "SCWE-008: Hardcoded Constants"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:22.257Z"
---
*Last updated: August 19, 2026*


# SCWE-008: Hardcoded Constants

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#relationships "Permanent link")

-   CWE-547: Use of Hard-coded, Security-relevant Constants [https://cwe.mitre.org/data/definitions/547.html](https://cwe.mitre.org/data/definitions/547.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#description "Permanent link")

Hardcoded constants refer to values that are embedded directly into the code and cannot be easily changed without modifying the code itself. These constants may include critical parameters, addresses, or settings that could be subject to change based on external factors or evolving needs. Hardcoding these values in the code introduces several issues:

-   **Lack of flexibility**: Once the contract is deployed, these hardcoded values cannot be changed without deploying a new version, leading to inefficiency and reduced adaptability.
-   **Security risks**: Hardcoded values may expose sensitive information or create vulnerabilities if they are not properly protected.
-   **Upgrade challenges**: Contracts with hardcoded constants cannot easily evolve to support new functionality or parameters without requiring costly redeployment.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#remediation "Permanent link")

-   **Use variables instead of constants**: Instead of hardcoding values, define them as variables that can be updated through administrative actions.
-   **Implement upgradeable contract patterns**: Use proxy contracts or other patterns that support upgrades to allow flexibility in modifying constants.
-   **External configuration**: Use off-chain storage for configuration values that can be updated without needing to deploy new contract versions.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#examples "Permanent link")

### Contract with Hardcoded Constants[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#contract-with-hardcoded-constants "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-3)contract HardcodedConstants {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-4)    address public owner = 0x1234567890abcdef1234567890abcdef12345678; // Hardcoded address    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-5)    uint public maxSupply = 1000000; // Hardcoded supply limit [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-7)    function setOwner(address newOwner) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-8)        owner = newOwner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-11)    function setMaxSupply(uint newMaxSupply) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-12)        maxSupply = newMaxSupply;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-0-14)}`

In this example, the `owner` address and `maxSupply` are hardcoded values that cannot be changed without redeploying the contract. This reduces flexibility and creates potential security risks.

### Improved Contract with External Configuration[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#improved-contract-with-external-configuration "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-3)contract ConfigurableContract {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-5)    uint public maxSupply; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-7)    constructor(address initialOwner, uint initialMaxSupply) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-8)        owner = initialOwner;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-9)        maxSupply = initialMaxSupply;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-12)    function setOwner(address newOwner) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-13)        owner = newOwner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-15)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-16)    function setMaxSupply(uint newMaxSupply) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-17)        maxSupply = newMaxSupply;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-18)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/#__codelineno-1-19)}`

In this improved example, the `owner` address and `maxSupply` are configurable through the constructor, allowing for more flexibility without the need for redeployment.
