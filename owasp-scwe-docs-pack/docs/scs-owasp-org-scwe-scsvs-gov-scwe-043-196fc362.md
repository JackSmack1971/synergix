---
title: "SCWE-043: Insecure Use of Fallback Functions"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:28.606Z"
---
*Last updated: August 19, 2026*


# SCWE-043: Insecure Use of Fallback Functions

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#relationships "Permanent link")

-   **CWE-250: Execution with Unnecessary Privileges**
    [CWE-250 Link](https://cwe.mitre.org/data/definitions/250.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#description "Permanent link")

Insecure use of fallback functions refers to vulnerabilities that arise when fallback functions are used improperly. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data due to unintended execution. - Exploitation of contract logic if the fallback function allows arbitrary interactions.

Fallback functions are triggered when a contract receives a call with no matching function signature. They can be used to handle Ether transfers or proxy unknown function calls. If misconfigured, they may enable unintended behaviors, such as unauthorized access or fund loss.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#remediation "Permanent link")

-   **Restrict logic execution in fallback functions**: Avoid placing critical execution logic inside fallback functions unless necessary.
-   **Separate Ether reception**: Use `receive()` explicitly to handle Ether transfers instead of overloading `fallback()`.
-   **Validate calls**: Ensure fallback functions do not execute unintended behavior. If required, use access control for specific use cases (e.g., controlled proxy calls).
-   **Use explicit function definitions**: Instead of relying on fallback functions for critical operations, define explicit functions with proper access control.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#examples "Permanent link")

### 🚨 **Insecure Fallback Function**[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#insecure-fallback-function "Permanent link")

#### *Problem: No access control or validation, allowing unintended execution.*[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#problem-no-access-control-or-validation-allowing-unintended-execution "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-0-3)contract InsecureFallback {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-0-4)    fallback() external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-0-5)        // No access control or validation    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-0-7)}`

\- This contract allows any call with an unknown function signature to trigger the fallback function, which could result in unintended behavior.

### Secure Fallback Function (Safe Handling of Ether)[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#secure-fallback-function-safe-handling-of-ether "Permanent link")

-   Solution: Explicitly handle Ether transfers using receive()

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-3)contract SecureFallback {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-4)    address public admin; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-6)    constructor(address _admin) {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-7)        admin = _admin;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-10)    // Explicitly define a receive function to safely accept Ether    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-11)    receive() external payable {} [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-12)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-13)    // Safe fallback function (does nothing if unintentionally called)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-14)    fallback() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-15)        // Optional: Log unexpected calls for security monitoring    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/#__codelineno-1-17)}`

This version properly separates Ether reception from fallback execution, preventing unintended behavior.

* * *
