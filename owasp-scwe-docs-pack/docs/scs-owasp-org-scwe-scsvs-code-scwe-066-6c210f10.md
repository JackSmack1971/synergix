---
title: "SCWE-066: Incorrect Handling of Bitwise Operations"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:24.681Z"
---
*Last updated: August 19, 2026*


# SCWE-066: Incorrect Handling of Bitwise Operations

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#relationships "Permanent link")

-   **CWE-682: Incorrect Calculation**
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#description "Permanent link")

Bitwise operations (e.g., `&`, `|`, `^`, `<<`, `>>`) can be efficient alternatives to arithmetic operations but are prone to errors if not used correctly. Misusing bitwise shifts can cause unintended value changes, integer overflows, or precision loss. Solidity lacks native overflow checks for bitwise shifts, making incorrect handling particularly dangerous in financial calculations or cryptographic functions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#remediation "Permanent link")

-   Ensure bitwise shifts do not exceed the size of the data type (e.g., shifting a `uint8` left by 8+ bits).
-   Validate input ranges before performing shifts to prevent overflow or precision loss.
-   Avoid unnecessary bitwise operations in financial calculations unless explicitly needed.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#vulnerable-contract-example "Permanent link")

``[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-4)    function shiftLeft(uint8 input) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-5)        return input << 8;  // ❌ Shifting beyond `uint8` capacity leads to zero    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-8)    function bitwiseAnd(uint8 a, uint8 b) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-9)        return a & b;  // ❌ Without proper validation, this could lead to unintended masking    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-0-11)}``

**Why is this vulnerable?**

-   `input << 8` shifts a `uint8` completely out of range, resulting in a value of `0`.
-   `a & b` can unintentionally mask critical bits if inputs are not properly validated.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#fixed-contract-example "Permanent link")

``[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-3)contract SecureExample {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-4)    function safeShiftLeft(uint8 input) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-5)        require(input < 32, "Shift too large");  // ✅ Validate shift range        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-6)        return input << 2;  // ✅ Safe shift within `uint8` bounds    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-9)    function safeBitwiseAnd(uint8 a, uint8 b) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-10)        require(a > 0 && b > 0, "Invalid input");  // ✅ Ensure inputs are meaningful        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-11)        return a & b;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/#__codelineno-1-13)}``

**Why is this safe?**

-   Restricts shift values to prevent unexpected overflows.
-   Ensures bitwise operations do not unintentionally modify values in an unintended way.
-   Protects contract logic from potential manipulation through poorly validated inputs.

**By correctly handling bitwise operations, developers can avoid unintended computation errors and ensure mathematical correctness in smart contracts.**
