---
title: "SCWE-045: Insecure Use of Modifiers"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:30.945Z"
---
*Last updated: August 19, 2026*


# SCWE-045: Insecure Use of Modifiers

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#relationships "Permanent link")

-   CWE-732: Incorrect Permission Assignment for Critical Resource
    [CWE-732 Link](https://cwe.mitre.org/data/definitions/732.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#description "Permanent link")

Insecure use of modifiers refers to vulnerabilities that arise when modifiers are used improperly. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of vulnerabilities in contract logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#remediation "Permanent link")

-   **Restrict access:** Ensure only authorized addresses can use the modifier.
-   **Validate inputs:** Ensure all inputs to the modifier are properly validated.
-   **Test thoroughly:** Conduct extensive testing to ensure modifiers are secure.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#examples "Permanent link")

-   **Insecure Modifier Usage (With Storage Bug)**

    `[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-3)contract InsecureModifier {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-4)    address public admin; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-6)    constructor(address _admin) {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-7)        admin = _admin; // ❌ Storage bug: Allows setting admin to zero address.    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-10)    modifier onlyAdmin() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-11)        require(admin == address(0), "Unauthorized"); // ❌ Wrong condition, only works if admin is zero!        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-12)        _;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-14)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-15)    function updateAdmin(address newAdmin) public onlyAdmin {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-16)        admin = newAdmin; // ❌ Can set admin to zero address, breaking access control.    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-17)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-18)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-19)    function updateBalance(uint newBalance) public onlyAdmin {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-20)        // Update balance    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-21)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-0-22)}`


**Why is this Insecure?** - Wrong Condition in `onlyAdmin()` - `require(admin == address(0), "Unauthorized");` only allows function execution when admin is zero. - This means no valid admin can ever execute admin functions! - If admin is ever non-zero, all `onlyAdmin` functions become unusable.

-   Loss of Control

    -   If admin is accidentally set to `address(0)`, anyone can now execute admin functions, breaking security
-   **Secure Modifier Usage**

    `[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-3)contract SecureModifier {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-4)    address public admin; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-6)    constructor(address _admin) {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-7)        require(_admin != address(0), "Invalid admin address"); // ✅ Proper validation        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-8)        admin = _admin;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-11)    modifier onlyAdmin() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-12)        require(msg.sender == admin, "Unauthorized"); // ✅ Correctly restricts access        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-13)        _;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-15)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-16)    function updateAdmin(address newAdmin) public onlyAdmin {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-17)        require(newAdmin != address(0), "New admin cannot be zero address"); // ✅ Prevents admin loss        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-18)        admin = newAdmin;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-19)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-20)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-21)    function updateBalance(uint newBalance) public onlyAdmin {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-22)        // Update balance securely    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-23)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/#__codelineno-1-24)}`


**Why is this Secure?** - Proper access control in `onlyAdmin()` - `require(msg.sender == admin, "Unauthorized");` ensures only the correct admin can execute admin functions. - Prevents privilege escalation - `updateAdmin()` prevents setting `admin = address(0)`, avoiding unintended loss of access.

* * *
