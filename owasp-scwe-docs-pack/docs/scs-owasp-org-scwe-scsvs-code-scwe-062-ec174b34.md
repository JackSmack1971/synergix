---
title: "SCWE-062: Dead Code"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:24.475Z"
---
*Last updated: August 19, 2026*


# SCWE-062: Dead Code

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#relationships "Permanent link")

-   CWE-561: Dead Code
    [https://cwe.mitre.org/data/definitions/561.html](https://cwe.mitre.org/data/definitions/561.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#description "Permanent link")

Code with no effects or Dead Code- refers to segments of a smart contract that are never executed or do not alter the contract's state or output. This can lead to unnecessary gas consumption, complicate the contract’s logic, and potentially confuse developers. Dead code often appears as leftover code from previous iterations or functions that are no longer in use but have not been removed. Removing such code improves contract efficiency and readability.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#remediation "Permanent link")

To mitigate this vulnerability, ensure that all functions, variables, and logic in the smart contract have a purpose and contribute to the contract’s behavior. Unused code should be removed to reduce complexity, save gas, and improve maintainability.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-3)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-6)    // Dead code, never called or used    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-7)    function unusedFunction() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-8)        uint x = 5;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-9)        uint y = 10;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-10)        uint result = x + y;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-12)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-13)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-14)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-15)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-0-16)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-3)contract Fixed {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/#__codelineno-1-9)}`
