---
title: "SCWE-071: Uninitialized Storage Pointer"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:20.915Z"
---
*Last updated: August 19, 2026*


# SCWE-071: Uninitialized Storage Pointer

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#relationships "Permanent link")

-   CWE-457: Use of Uninitialized Variable
    [https://cwe.mitre.org/data/definitions/457.html](https://cwe.mitre.org/data/definitions/457.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#description "Permanent link")

An uninitialized storage pointer in Solidity refers to a variable that has been declared but not assigned a value before being used. This can result in unpredictable behavior, as the variable might point to unintended locations in the contract's storage, potentially exposing sensitive data or allowing attackers to exploit the uninitialized pointer. This is a critical issue because Solidity does not automatically initialize storage variables, leaving them with default values that may be unsafe.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#remediation "Permanent link")

Always initialize storage pointers to avoid potential vulnerabilities. Ensure that all variables, especially storage pointers, are properly assigned a value before being used. This prevents accessing uninitialized or garbage data from the contract’s storage.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-4)    uint[] public data; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-6)    // Uninitialized storage pointer, could lead to unexpected behavior    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-7)    function addData(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-8)        data.push(_value);        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-9)        uint[] storage uninitializedPointer;  // Pointer is uninitialized        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-10)        uninitializedPointer.push(10);  // Accessing uninitialized storage pointer    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-0-12)}`

**Why is this vulnerable?** - `uninitializedPointer` is a storage pointer but is not assigned a reference to valid storage. - Writing to `uninitializedPointer.push(10);` could overwrite unintended storage locations.

**Potential outcomes:** - Corrupting storage layout (e.g., overwriting contract variables). - Unexpected behaviors due to storage reallocation.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-3)contract Example {       [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-4)      uint[] public data; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-5)      [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-6)      function addData(uint _value) public {          [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-7)          data.push(_value);          [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-8)          uint[] storage initializedPointer = data;  // ✅ Properly initialized storage pointer          [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-9)          initializedPointer.push(10);  // ✅ Safely interacts with the intended storage      [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-10)      }  [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/#__codelineno-1-11)  }`

**Why is this safe?** - `initializedPointer` explicitly references `data`, ensuring that it does not point to an arbitrary storage slot. - Prevents unintended overwrites of contract state. - Ensures expected behavior and protects contract integrity.
