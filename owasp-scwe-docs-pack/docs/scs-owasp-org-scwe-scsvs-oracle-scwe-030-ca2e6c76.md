---
title: "SCWE-030: Insecure Oracle Data Updates"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.425Z"
---
*Last updated: August 19, 2026*


# SCWE-030: Insecure Oracle Data Updates

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#description "Permanent link")

Insecure oracle data updates refer to the failure to properly validate or secure updates to oracle data. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of the contract's logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#remediation "Permanent link")

-   **Validate updates:** Ensure all oracle data updates are properly validated.
-   **Restrict access:** Restrict update permissions to trusted addresses.
-   **Implement timelocks:** Add delays to oracle updates to allow for review.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#examples "Permanent link")

-   **Insecure Oracle Updates**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-0-3)contract InsecureOracleUpdates {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-0-4)    function updatePrice(address oracle, uint newPrice) public {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-0-5)        Oracle(oracle).updatePrice(newPrice); // No validation    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-0-7)}`

-   **Secure Oracle Updates**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-3)contract SecureOracleUpdates {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-4)    address public admin; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-6)    constructor(address _admin) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-7)        admin = _admin;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-10)    modifier onlyAdmin() {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-11)        require(msg.sender == admin, "Unauthorized");        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-12)        _;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-14)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-15)    function updatePrice(address oracle, uint newPrice) public onlyAdmin {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-16)        Oracle(oracle).updatePrice(newPrice); // Restricted to admin    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/#__codelineno-1-18)}`
