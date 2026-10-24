---
title: "SCWE-069: Shadowing State Variables"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.152Z"
---
*Last updated: August 19, 2026*


# SCWE-069: Shadowing State Variables

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#relationships "Permanent link")

-   CWE-1001: Variable Shadowing
    [https://cwe.mitre.org/data/definitions/1001.html](https://cwe.mitre.org/data/definitions/1001.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#description "Permanent link")

Shadowing occurs when a state variable in a derived contract uses the same name as one in the base contract. This can lead to confusion and unexpected behavior, as the derived contract will hide the state variable from the base contract, potentially causing errors in contract logic or making it harder to maintain and audit the code.

It is essential to avoid naming state variables in derived contracts the same as those in base contracts to ensure that the intended state is correctly accessed and modified.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#remediation "Permanent link")

To avoid state variable shadowing, use unique names for state variables in derived contracts or explicitly refer to the base contract variable using `super`. This will ensure that the correct state variable is accessed and manipulated as intended.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-3)contract Base {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-7)        balance = 100;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-9)} [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-10)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-11)contract Derived is Base {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-12)    uint public balance;  // Shadows state variable from Base contract [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-13)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-14)    function updateBalance(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-15)        balance = amount;  // Refers to Derived's balance, not Base's balance    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-0-17)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-3)contract Base {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-7)        balance = 100;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-9)} [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-10)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-11)contract Derived is Base {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-12)    uint public newBalance;  // Unique name for Derived contract [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-14)    function updateBalance(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-15)        newBalance = amount;  // Updates Derived's balance without shadowing    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/#__codelineno-1-17)}`
