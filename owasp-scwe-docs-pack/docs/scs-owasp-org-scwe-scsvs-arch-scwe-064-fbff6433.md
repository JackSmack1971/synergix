---
title: "SCWE-064: Incorrect Inheritance Order"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:20.658Z"
---
*Last updated: August 19, 2026*


# SCWE-064: Incorrect Inheritance Order

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#relationships "Permanent link")

-   CWE-1001: Variable Shadowing
    [https://cwe.mitre.org/data/definitions/1001.html](https://cwe.mitre.org/data/definitions/1001.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#description "Permanent link")

Incorrect inheritance order in Solidity can lead to unintended behavior, especially when multiple base contracts define similar variables or functions. Solidity’s linearization of the inheritance order can result in one contract unintentionally overriding or shadowing variables or functions defined in a parent contract, leading to confusion, errors, and potential vulnerabilities.

In Solidity, the order of inheritance matters. If the inheritance hierarchy is not properly structured, the wrong version of a variable or function may be called, causing bugs or security issues.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#remediation "Permanent link")

To mitigate this vulnerability, carefully review and order the inheritance structure. Ensure that parent contracts are inherited in a logical sequence and that any variables or functions are not unintentionally shadowed or overridden. Consider following a clear and consistent inheritance pattern.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-3)contract BaseA {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-9)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-10)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-11)contract BaseB {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-12)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-13)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-14)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-15)        value = _value + 1;  // Different implementation    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-17)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-18)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-19)contract Child is BaseB, BaseA {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-20)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-21)        value = _value + 2;  // Shadows value from BaseA or BaseB    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-22)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-0-23)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-3)contract BaseA {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-9)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-10)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-11)contract BaseB {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-12)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-14)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-15)        value = _value + 1;  // Different implementation    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-17)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-18)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-19)contract Child is BaseA, BaseB {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-20)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-21)        value = _value + 2;  // Calls setValue from BaseA or BaseB intentionally    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-22)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/#__codelineno-1-23)}`
