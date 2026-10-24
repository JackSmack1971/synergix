---
title: "SCWE-059: Insufficient Gas Griefing"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.152Z"
---
*Last updated: August 19, 2026*


# SCWE-059: Insufficient Gas Griefing

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#description "Permanent link")

Insufficient gas griefing occurs when an attacker intentionally sends a transaction with insufficient gas to force the contract to fail. This can lead to resource consumption issues and potential denial of service for the contract or other users. If a contract relies on external calls or interacts with other contracts and does not properly handle gas estimation, it may be vulnerable to such attacks.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#remediation "Permanent link")

To mitigate this vulnerability, ensure that gas estimation and proper gas limits are handled when performing contract calls, especially when interacting with other contracts. Additionally, use mechanisms to handle failures gracefully, such as revert messages and checks for sufficient gas before initiating important operations.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-3)contract GasGriefing {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-10)    function transferFunds(address payable recipient, uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-11)        require(msg.sender == owner, "Not the owner");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-12)        recipient.transfer(amount);  // Potential for griefing with insufficient gas    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-0-14)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-3)contract GasGriefingSafe {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-10)    function transferFunds(address payable recipient, uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-11)        require(msg.sender == owner, "Not the owner");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-12)        (bool success, ) = recipient.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-13)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/#__codelineno-1-15)}`
