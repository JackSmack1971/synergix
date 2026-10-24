---
title: "SCWE-027: Vulnerable Cryptographic Algorithms"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.083Z"
---
*Last updated: August 19, 2026*


# SCWE-027: Vulnerable Cryptographic Algorithms

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#relationships "Permanent link")

-   **CWE-327:** Use of a Broken or Risky Cryptographic Algorithm
    [CWE-327 Link](https://cwe.mitre.org/data/definitions/327.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#description "Permanent link")

Vulnerable cryptographic algorithms refer to the use of outdated or insecure cryptographic algorithms, such as MD5 or SHA-1. This can lead to: - Exploitation of the contract’s logic. - Loss of funds or data. - Reduced trust in the contract’s security.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#remediation "Permanent link")

-   **Use secure algorithms:** Leverage modern cryptographic algorithms like SHA-256 or Keccak-256.
-   **Avoid deprecated algorithms:** Do not use algorithms known to be insecure.
-   **Test thoroughly:** Conduct extensive testing to ensure cryptographic security.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#examples "Permanent link")

-   **Vulnerable Algorithm**

    `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-0-3)contract VulnerableAlgorithm {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-0-4)    function hashData(bytes memory data) public pure returns (bytes32) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-0-5)        return sha256(data); // Insecure algorithm    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-0-7)}`

-   **Secure Algorithm**

    `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-1-3)contract SecureAlgorithm {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-1-4)    function hashData(bytes memory data) public pure returns (bytes32) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-1-5)        return keccak256(data); // Secure algorithm    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-1-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/#__codelineno-1-7)}`


* * *
