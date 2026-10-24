---
title: "SCWE-070: Incorrect Constructor Name"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:20.790Z"
---
*Last updated: August 19, 2026*


# SCWE-070: Incorrect Constructor Name

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#relationships "Permanent link")

-   CWE-1001: Variable Shadowing
    [https://cwe.mitre.org/data/definitions/1001.html](https://cwe.mitre.org/data/definitions/1001.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#description "Permanent link")

In Solidity, the constructor is a special function used to initialize a contract's state variables when it is deployed. If a constructor is incorrectly named, it will not function as expected, leading to issues such as failing to initialize state variables or triggering unexpected behavior. The constructor must have the exact name of the contract and no return type.

If the constructor name is not correct, it will not be executed as intended, and the contract may not behave as expected, potentially leaving it in an uninitialized or inconsistent state.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#remediation "Permanent link")

Ensure that the constructor has the correct name, which must match the contract name and contain no return type. In newer versions of Solidity (0.4.22 and later), the constructor keyword is used instead of the contract name for constructor functions.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-6)    // In Solidity <0.4.22, constructor had to match contract name. In 0.5+, this is a regular function, not a constructor.    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-7)    function Example() public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-8)        value = 10;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-0-10)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-6)    // Correct constructor definition (Solidity >=0.4.22)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-7)    constructor() {  // Use "constructor" instead of the contract name        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-8)        value = 10;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/#__codelineno-1-10)}`
