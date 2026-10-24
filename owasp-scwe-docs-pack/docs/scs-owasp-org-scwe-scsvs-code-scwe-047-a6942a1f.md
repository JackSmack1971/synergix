---
title: "SCWE-047: Integer Overflows and Underflows"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:23.797Z"
---
*Last updated: August 19, 2026*


# SCWE-047: Integer Overflows and Underflows

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#relationships "Permanent link")

-   CWE-190: Integer Overflow or Wraparound
    [https://cwe.mitre.org/data/definitions/190.html](https://cwe.mitre.org/data/definitions/190.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#description "Permanent link")

Integer overflows and underflows occur when arithmetic operations exceed the bounds of the integer data type, causing the value to "wrap around" to an unexpected number.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#remediation "Permanent link")

-   **Use Solidity 0.8.0 or later:** Leverage the compiler’s built-in overflow and underflow checks.
-   **Apply SafeMath libraries:** Use libraries like OpenZeppelin’s `SafeMath` for versions before 0.8.0.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#examples "Permanent link")

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-3)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-4)    uint8 public totalSupply; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-6)    function addTokens(uint8 _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-7)        totalSupply += _value; // May overflow    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-10)    function subtractTokens(uint8 _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-11)        totalSupply -= _value; // May underflow    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-12)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-0-13)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-3)contract Secure {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-4)    uint8 public totalSupply; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-6)    function addTokens(uint8 _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-7)        totalSupply += _value; // Built-in overflow check in 0.8+    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-10)    function subtractTokens(uint8 _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-11)        totalSupply -= _value; // Built-in underflow check in 0.8+    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/#__codelineno-1-13)}`
