---
title: "SCWE-025: Improper Cryptographic Key Management"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.840Z"
---
*Last updated: August 19, 2026*


# SCWE-025: Improper Cryptographic Key Management

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#relationships "Permanent link")

-   CWE-310: Cryptographic Issues
    [CWE-310 Link](https://cwe.mitre.org/data/definitions/310.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#description "Permanent link")

Improper cryptographic key management refers to the failure to securely generate, store, or use cryptographic keys. This can lead to: - Unauthorized access to sensitive data. - Exploitation of the contract's logic. - Loss of funds or data.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#remediation "Permanent link")

-   **Use secure key management:** Leverage secure key management systems or libraries.
-   **Avoid hardcoding keys:** Never hardcode cryptographic keys in the contract.
-   **Regularly rotate keys:** Periodically update cryptographic keys to reduce risks.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#examples "Permanent link")

-   **Improper Key Management**

    `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-0-3)contract ImproperKeyManagement {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-0-4)    bytes32 private key = keccak256("insecure-key"); // Hardcoded key [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-0-5)}`

-   **Proper Key Management**

    `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-3)contract ProperKeyManagement {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-4)    bytes32 private key; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-6)    constructor(bytes32 _key) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-7)        key = _key; // Configurable key    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/#__codelineno-1-9)}`
