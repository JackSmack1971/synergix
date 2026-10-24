---
title: "SCWE-021: Unsecured Data Transmission"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.044Z"
---
*Last updated: August 19, 2026*


# SCWE-021: Unsecured Data Transmission

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#relationships "Permanent link")

-   CWE-319: Cleartext Transmission of Sensitive Information
    [CWE-319 Link](https://cwe.mitre.org/data/definitions/319.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#description "Permanent link")

Unsecured data transmission refers to the transmission of sensitive information, such as private keys or user data, without encryption. This can lead to: - Interception of sensitive data by malicious actors. - Exploitation of vulnerabilities in the contract. - Loss of funds or data.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#remediation "Permanent link")

-   **Use encryption:** Encrypt sensitive data before transmission.
-   **Leverage secure protocols:** Use HTTPS or other secure communication protocols.
-   **Avoid transmitting sensitive data:** Minimize the transmission of sensitive data whenever possible.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#examples "Permanent link")

-   **Unsecured Data Transmission**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-0-3)contract UnsecuredData {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-0-4)    function transmitData(bytes memory data) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-0-5)        // Transmit data without encryption    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-0-7)}`

-   **Secured Data Transmission**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-1-3)contract SecuredData {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-1-4)    function transmitData(bytes memory encryptedData) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-1-5)        // Transmit encrypted data    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-1-6)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/#__codelineno-1-7)}`


* * *
