---
title: "SCWE-002: Excessive Contract Complexity"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:19.063Z"
---
*Last updated: August 19, 2026*


# SCWE-002: Excessive Contract Complexity

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#relationships "Permanent link")

-   CWE-710: Improper Adherence to Coding Standards
    [https://cwe.mitre.org/data/definitions/710.html](https://cwe.mitre.org/data/definitions/710.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#description "Permanent link")

Excessive contract complexity refers to situations where the design or implementation of a smart contract becomes overly complicated, making it difficult to understand, audit, and maintain. Such complexity increases the likelihood of introducing bugs and vulnerabilities that may not be apparent during development or testing. It often arises from:

-   Overuse of complex inheritance structures or external libraries.
-   Too many functions, interdependencies, and conditions within the contract.
-   Unnecessarily convoluted logic that could be simplified.

The more complex the code, the higher the chance that mistakes are made, especially if future developers or auditors need to interact with the contract. Complexity can lead to hidden vulnerabilities that may be exploited over time.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#remediation "Permanent link")

-   **Refactor and simplify the code**: Break down complex functions into smaller, easier-to-understand components.
-   **Limit inheritance depth**: Use inheritance judiciously and prefer composition over deep inheritance chains.
-   **Use clear and descriptive names**: Functions, variables, and events should have self-explanatory names that indicate their purpose.
-   **Avoid redundant logic**: Consolidate repeated logic into reusable functions or libraries.
-   **Ensure modularity**: Split the contract into manageable modules that focus on specific tasks, improving readability and maintainability.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#examples "Permanent link")

### Excessive Complexity[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#excessive-complexity "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-3)contract ComplexContract {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-4)    uint public balance;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-7)    function ComplexFunction1(uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-8)        // Complex logic with many conditions        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-9)        if (value > 10) {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-10)            // do something        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-11)        }        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-12)        // Multiple nested functions and too many conditions        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-13)        for (uint i = 0; i < value; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-14)            if (i % 2 == 0) {                [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-15)                // nested loop            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-16)            }        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-17)        }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-18)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-19)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-20)    function ComplexFunction2(address addr) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-21)        // Complex logic with external dependencies        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-22)        SomeLibrary.someFunction(addr);    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-23)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-0-24)}`

### Simplified Version[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#simplified-version "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-3)contract SimpleContract {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-4)    uint public balance;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-7)    function deposit(uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-8)        balance += value;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-11)    function withdraw(uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-12)        require(balance >= value, "Insufficient funds");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-13)        balance -= value;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-14)        // Note: Simplified example — internal accounting only. For ETH vaults, add payable(msg.sender).call{value: value}("") and require(success).    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-15)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/#__codelineno-1-16)}`
