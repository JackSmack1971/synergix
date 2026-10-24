---
title: "SCWE-060: Floating Pragma"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:24.226Z"
---
*Last updated: August 19, 2026*


# SCWE-060: Floating Pragma

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#relationships "Permanent link")

-   CWE-703: Improper Check for Unusual or Exceptional Conditions
    [https://cwe.mitre.org/data/definitions/703.html](https://cwe.mitre.org/data/definitions/703.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#description "Permanent link")

The use of floating pragmas (e.g., `^0.8.0`) in smart contract development can lead to unexpected issues when new versions of the Solidity compiler are released. Floating versions allow the contract to automatically use newer versions of the compiler within the specified range, which may introduce breaking changes, unexpected bugs, or security vulnerabilities. To avoid this, it is important to specify fixed versions to ensure the contract works reliably and consistently across different environments.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#remediation "Permanent link")

To mitigate this vulnerability, always specify a fixed compiler version in the contract to avoid using floating pragmas. This ensures that the contract is compiled using a known and tested version of the compiler, preventing unexpected behavior from new, untested releases.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-1)pragma solidity ^0.8.0;  // Floating version allows for any 0.8.x version [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-3)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-0-9)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-1)pragma solidity 0.8.4;  // Fixed version ensures no unexpected updates [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-3)contract Fixed {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-4)    uint public value; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-6)    function setValue(uint _value) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-7)        value = _value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/#__codelineno-1-9)}`
