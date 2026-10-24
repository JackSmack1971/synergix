---
title: "SCWE-052: Transaction Order Dependence"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:20.475Z"
---
*Last updated: August 19, 2026*


# SCWE-052: Transaction Order Dependence

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#description "Permanent link")

Transaction Order Dependence (TOD) occurs when the outcome of a contract's execution depends on the order of transactions. Attackers can exploit this issue by submitting transactions in a specific order, manipulating the contract's state and gaining an unfair advantage, such as front-running or back-running other transactions. This can lead to unexpected behavior and resource consumption.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#remediation "Permanent link")

To mitigate TOD vulnerabilities, ensure that the contract's logic does not depend on transaction order. Use techniques like commit-reveal schemes or randomization to prevent attackers from predicting the transaction order and exploiting it.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-3)contract TODExample {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-4)    address public winner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-6)    function bid() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-7)        require(msg.value > 1 ether, "Bid too low");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-8)        winner = msg.sender;  // Dependent on transaction order    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-0-10)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-3)contract FixedTODExample {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-4)    address public winner;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-5)    uint public highestBid; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-7)    function bid() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-8)        require(msg.value > highestBid, "Bid too low");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-9)        highestBid = msg.value;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-10)        winner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/#__codelineno-1-12)}`
