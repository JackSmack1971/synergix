---
title: "SCWE-016: Insufficient Authorization Checks"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:30.216Z"
---
*Last updated: August 19, 2026*


# SCWE-016: Insufficient Authorization Checks

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#relationships "Permanent link")

-   CWE-862: Missing Authorization [https://cwe.mitre.org/data/definitions/862.html](https://cwe.mitre.org/data/definitions/862.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#description "Permanent link")

Insufficient authorization occurs when the contract does not verify whether a user has the appropriate permissions to perform specific actions. This vulnerability arises when there are missing or improperly implemented authorization checks, allowing unauthorized users to access functions they should not have access to.

Common causes of insufficient authorization include: - Missing access control modifiers or incorrect configuration. - Failure to validate roles before granting access to sensitive functions. - Poor handling of user permissions, which could lead to privilege escalation.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#remediation "Permanent link")

-   **Implement role-based access control (RBAC):** Define roles such as `admin`, `user`, etc., and assign permissions accordingly to ensure only authorized users can call restricted functions.
-   **Use access control modifiers:** Protect sensitive functions with appropriate modifiers (e.g., `onlyOwner`, `onlyAdmin`) to restrict access.
-   **Principle of least privilege:** Ensure each user only has access to the minimal set of actions they need to perform their role.
-   **Thorough testing:** Test for authorization vulnerabilities to ensure all restricted functions are properly secured.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#examples "Permanent link")

### Insufficient Authorization Example[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#insufficient-authorization-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-3)contract InsufficientAuthorization {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-6)    function withdraw(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-7)        // No checks for user roles, any address can withdraw funds        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-8)        balance -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-0-10)}`

### Fixed Authorization Example[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#fixed-authorization-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-3)contract FixedAuthorization {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-4)    uint public balance;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-7)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-8)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-11)    modifier onlyOwner() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-12)        require(msg.sender == owner, "Not authorized");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-13)        _;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-15)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-16)    function withdraw(uint amount) public onlyOwner {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-17)        balance -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-18)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/#__codelineno-1-19)}`

In the fixed example, the `onlyOwner` modifier ensures that only the contract owner can withdraw funds, thus preventing unauthorized users from performing sensitive operations like withdrawing assets.
