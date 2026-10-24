---
title: "SCWE-067: Assert Violation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:24.809Z"
---
*Last updated: August 19, 2026*


# SCWE-067: Assert Violation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#relationships "Permanent link")

-   CWE-754: Improper Check for Unusual or Exceptional Conditions
    [https://cwe.mitre.org/data/definitions/754.html](https://cwe.mitre.org/data/definitions/754.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#description "Permanent link")

In Ethereum smart contracts, assertions (`assert`) are commonly used for internal consistency checks and to prevent erroneous states. However, if not used correctly, they can lead to unexpected behavior. When an `assert` statement fails, it reverts the entire transaction, and all changes made in the transaction are reverted. This can be problematic if it is used for conditions that can be expected during normal contract execution.

Using `assert` for conditions that can occur under normal circumstances (e.g., user inputs or contract logic) may cause unnecessary reverts and loss of gas. It’s important to reserve `assert` for critical errors, such as invariants and internal state checks that should never fail.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#remediation "Permanent link")

To avoid unnecessary assertion failures, use `require` for input validation and conditions that can reasonably fail. `assert` should only be used for internal error detection and state validation that should never happen, as it signals a critical issue if violated.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-3)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-7)        balance = 100;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-10)    function withdraw(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-11)        assert(balance >= amount);  // Assert violation on user input        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-12)        balance -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-0-14)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-3)contract Secure {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-7)        balance = 100;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-10)    function withdraw(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-11)        require(balance >= amount, "Insufficient balance");  // Use require for expected conditions        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-12)        balance -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/#__codelineno-1-14)}`
