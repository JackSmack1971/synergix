---
title: "SCWE-038: Insecure Use of Selfdestruct"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:30.834Z"
---
*Last updated: August 19, 2026*


# SCWE-038: Insecure Use of Selfdestruct

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#relationships "Permanent link")

-   CWE-732: Incorrect Permission Assignment for Critical Resource
    [CWE-732 Link](https://cwe.mitre.org/data/definitions/732.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#description "Permanent link")

Insecure use of selfdestruct refers to vulnerabilities that arise when the `selfdestruct` function is used without proper safeguards. This can lead to: - Unauthorized destruction of the contract. - Loss of funds or data. - Exploitation of vulnerabilities in contract logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#remediation "Permanent link")

-   **Restrict access:** Ensure only authorized addresses can call `selfdestruct`. Note: `selfdestruct` is deprecated per EIP-6049 (Solidity 0.8.24+); prefer migration patterns where possible.
-   **Implement circuit breakers:** Add mechanisms to halt operations in case of suspicious activity.
-   **Test thoroughly:** Conduct extensive testing to ensure `selfdestruct` is used securely.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#examples "Permanent link")

-   **Insecure Selfdestruct Usage**

    `[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-0-3)contract InsecureSelfdestruct {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-0-4)    function destroy() public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-0-5)        selfdestruct(payable(msg.sender)); // No access control    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-0-7)}`

-   **Secure Selfdestruct Usage**

    `[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-3)contract SecureSelfdestruct {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-4)    address public admin; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-6)    constructor(address _admin) {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-7)        admin = _admin;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-10)    modifier onlyAdmin() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-11)        require(msg.sender == admin, "Unauthorized");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-12)        _;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-14)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-15)    function destroy() public onlyAdmin {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-16)        selfdestruct(payable(admin)); // Restricted to admin    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/#__codelineno-1-18)}`


* * *
