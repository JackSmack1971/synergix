---
title: "SCWE-026: Insufficient Hash Verification"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.964Z"
---
*Last updated: August 19, 2026*


# SCWE-026: Insufficient Hash Verification

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#relationships "Permanent link")

-   CWE-347: Improper Verification of Cryptographic Signature
    [CWE-347 Link](https://cwe.mitre.org/data/definitions/347.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#description "Permanent link")

Insufficient hash verification refers to the failure to properly verify hashes, such as message hashes or transaction hashes. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of the contract's logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#remediation "Permanent link")

-   **Validate hashes:** Ensure all hashes are properly verified before processing.
-   **Use secure libraries:** Leverage well-audited libraries for hash verification.
-   **Test thoroughly:** Conduct extensive testing to ensure hash verification works as intended.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#examples "Permanent link")

-   **Insufficient Hash Verification**

    `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-0-3)contract InsufficientHashVerification {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-0-4)    function processHash(bytes32 hash) public {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-0-5)        // Process hash without verification    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-0-7)}`

-   **Sufficient Hash Verification**

    `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-3)contract SufficientHashVerification {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-4)    function processHash(bytes32 hash, bytes memory data) public {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-5)        require(keccak256(data) == hash, "Invalid hash");        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-6)        // Process hash    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/#__codelineno-1-8)}`


* * *
