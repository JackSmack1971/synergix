---
title: "SCWE-072: Use of Deprecated Solidity Functions"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.286Z"
---
*Last updated: August 19, 2026*


# SCWE-072: Use of Deprecated Solidity Functions

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#relationships "Permanent link")

-   CWE-676: Use of a Dangerous Function
    [https://cwe.mitre.org/data/definitions/676.html](https://cwe.mitre.org/data/definitions/676.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#description "Permanent link")

Some Solidity functions and features have been deprecated over time due to security risks, inefficiencies, or better alternatives being introduced in newer versions of Solidity. Using deprecated functions can expose contracts to known vulnerabilities and potential attacks. Examples include `suicide()`, which was replaced by `selfdestruct()`, and `sha3()`, which was replaced by `keccak256()`.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#remediation "Permanent link")

Always check the Solidity documentation to ensure that the functions you're using are not deprecated. If a function is deprecated, replace it with its recommended alternative to maintain the contract's security and ensure compatibility with future Solidity versions. **Note:** As of EIP-6049 (Solidity 0.8.24+), `selfdestruct` is deprecated and will be removed in a future EVM version.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#vulnerable-contract-example "Permanent link")

``[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-4)    function oldFunction() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-5)        // Using deprecated function `suicide`        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-6)        suicide(msg.sender);  // Deprecated, should be replaced with `selfdestruct`    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-0-8)}``

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#fixed-contract-example "Permanent link")

``[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-4)    function oldFunction() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-5)        // Correctly using the recommended alternative `selfdestruct` (deprecated per EIP-6049; prefer migration patterns)        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-6)        selfdestruct(payable(msg.sender));  // Replacing deprecated `suicide` with `selfdestruct`    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/#__codelineno-1-8)}``
