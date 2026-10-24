---
title: "SCWE-009: Deprecated Variable and Function Usage"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:22.392Z"
---
*Last updated: August 19, 2026*


# SCWE-009: Deprecated Variable and Function Usage

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#relationships "Permanent link")

-   CWE-477: Use of Obsolete Function [https://cwe.mitre.org/data/definitions/477.html](https://cwe.mitre.org/data/definitions/477.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#description "Permanent link")

The use of deprecated variables and functions refers to employing code elements that are no longer recommended for use, either due to obsolescence, security concerns, or the introduction of better alternatives. Using such elements can cause issues, including reduced compatibility, poor maintainability, and security vulnerabilities. Specific concerns related to deprecated usage are:

-   **Security risks**: Deprecated functions may have known vulnerabilities or might not be patched.
-   **Compatibility issues**: Newer compiler versions and environments may not support deprecated code.
-   **Maintenance difficulties**: Continuing to use deprecated code increases the complexity of codebase management and prevents clean upgrades.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#remediation "Permanent link")

-   **Replace deprecated functions**: Always use the recommended and supported alternatives in the latest compiler versions.
-   **Update dependencies**: If relying on libraries that use deprecated elements, upgrade to versions that support current standards.
-   **Monitor for deprecation warnings**: Stay informed about deprecated functions in the Solidity language or external libraries and refactor the code when necessary.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#examples "Permanent link")

### Contract with Deprecated Function Usage[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#contract-with-deprecated-function-usage "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-3)contract DeprecatedUsage {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-5)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-7)    // Deprecated function, example using older Solidity versions    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-8)    function sendTransaction(address recipient, uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-9)        recipient.transfer(amount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-0-11)}`

In this example, the `transfer` function in Solidity's older versions is deprecated. Continuing to use such functions can cause issues with future compiler versions.

### Improved Contract without Deprecated Usage[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#improved-contract-without-deprecated-usage "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-3)contract UpdatedUsage {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-5)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-7)    // Replaced with call{value} — avoids 2300 gas limit of transfer/send    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-8)    function sendTransaction(address recipient, uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-9)        (bool success, ) = payable(recipient).call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-10)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/#__codelineno-1-12)}`

In this improved example, the contract uses `call{value}` instead of deprecated `transfer`/`send`, avoiding the 2300 gas limit that can cause DoS when the recipient is a contract (see SCWE-079).
