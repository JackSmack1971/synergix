---
title: "SCWE-044: Insecure Use of Storage"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:28.719Z"
---
*Last updated: August 19, 2026*


# SCWE-044: Insecure Use of Storage

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#description "Permanent link")

Insecure use of storage refers to vulnerabilities that arise when storage variables are improperly managed. This can lead to: - Unauthorized access to sensitive data. - Loss of funds or data. - Exploitation of vulnerabilities in contract logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#remediation "Permanent link")

-   **Encrypt sensitive data:** Encrypt sensitive data before storing it.
-   **Validate inputs:** Ensure all storage updates are properly validated.
-   **Test thoroughly:** Conduct extensive testing to ensure storage is secure.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#examples "Permanent link")

-   **Insecure Storage Usage**

    `[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-3)contract InsecureStorage {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-6)    function updateBalance(uint newBalance) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-7)        balance = newBalance; // No validation    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-0-9)}`

-   **Secure Storage Usage**

    `[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-3)contract SecureStorage {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-6)    function updateBalance(uint newBalance) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-7)        require(newBalance > 0, "Invalid balance"); // Input validation        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-8)        balance = newBalance;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/#__codelineno-1-10)}`


* * *
