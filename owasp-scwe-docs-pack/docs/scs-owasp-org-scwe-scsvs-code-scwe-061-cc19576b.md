---
title: "SCWE-061: Outdated Compiler Version"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:24.355Z"
---
*Last updated: August 19, 2026*


# SCWE-061: Outdated Compiler Version

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#relationships "Permanent link")

-   CWE-1103: Use of Outdated or Insecure Software
    [https://cwe.mitre.org/data/definitions/1103.html](https://cwe.mitre.org/data/definitions/1103.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#description "Permanent link")

Using an outdated compiler version can expose a smart contract to vulnerabilities that have already been patched in newer versions. Compiler versions often include security fixes, optimizations, and new features that are crucial for the safety and performance of contracts.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#remediation "Permanent link")

To mitigate this vulnerability, always use the most up-to-date stable version of the Solidity compiler. Ensure that your development environment is regularly updated to incorporate the latest security patches, optimizations, and features provided by newer versions of the compiler.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-1)pragma solidity 0.4.24;  // Outdated compiler version [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-3)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-0-9)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-1)pragma solidity 0.8.4;  // Updated compiler version for better security and performance [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-3)contract Fixed {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/#__codelineno-1-9)}`
