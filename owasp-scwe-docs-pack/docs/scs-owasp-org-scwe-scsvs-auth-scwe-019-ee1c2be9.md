---
title: "SCWE-019: Insecure Signature Verification"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:30.587Z"
---
*Last updated: August 19, 2026*


# SCWE-019: Insecure Signature Verification

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#relationships "Permanent link")

-   CWE-347: Improper Verification of Cryptographic Signature [https://cwe.mitre.org/data/definitions/347.html](https://cwe.mitre.org/data/definitions/347.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#description "Permanent link")

Insecure signature verification occurs when a contract improperly verifies a cryptographic signature or fails to securely validate signatures, allowing attackers to forge or manipulate them. This vulnerability can allow unauthorized transactions or the bypassing of important security mechanisms, potentially leading to fraud, unauthorized access, or other attacks.

Common causes of insecure signature verification include: - Not validating the signer's address. - Using weak or outdated cryptographic libraries. - Failing to check signature validity before processing actions. - Incorrectly handling the signature format.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#remediation "Permanent link")

-   **Verify signatures properly:** Always verify that the signature matches the intended signer by using the `ecrecover` function for Ethereum addresses and comparing the result to the expected signer address.
-   **Use strong cryptographic methods:** Ensure the use of robust cryptographic techniques and libraries. Avoid using outdated or weak algorithms.
-   **Use secure signature formats:** Make sure that signature formats are validated properly (e.g., ensure proper handling of `v`, `r`, `s` values in Ethereum signatures).
-   **Implement checks before acting on the signature:** Always perform checks for valid signature and relevant parameters before executing any logic that could be influenced by the signature.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#examples "Permanent link")

### Insecure Signature Verification[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#insecure-signature-verification "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-3)contract InsecureSignatureExample {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-10)    // Insecure signature verification: does not properly validate the signature    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-11)    function executeTransaction(bytes32 hash, uint8 v, bytes32 r, bytes32 s) public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-12)        address signer = ecrecover(hash, v, r, s);  // Signature verification        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-13)        if (signer == owner) {            [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-14)            // Execute some sensitive action        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-15)        }    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-0-17)}`

In the insecure version, the contract checks if the signature corresponds to the owner but does not properly validate or handle potential issues with the signature, such as its format or correctness.

### Fixed Signature Verification[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#fixed-signature-verification "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-3)contract SecureSignatureExample {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-10)    // Secure signature verification: properly checks signature and signer    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-11)    function executeTransaction(bytes32 hash, uint8 v, bytes32 r, bytes32 s) public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-12)        address signer = ecrecover(hash, v, r, s);        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-13)        require(signer == owner, "Invalid signature");  // Ensure valid signature before proceeding        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-14)        // Execute some sensitive action    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-15)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/#__codelineno-1-16)}`

In the fixed version, we use the `require()` function to ensure the signature matches the owner's address, thereby improving security by preventing unauthorized access or actions.
