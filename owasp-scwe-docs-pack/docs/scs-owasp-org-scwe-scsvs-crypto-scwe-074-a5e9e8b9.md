---
title: "SCWE-074: Hash Collisions with Multiple Variable Length Arguments"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.573Z"
---
*Last updated: August 19, 2026*


# SCWE-074: Hash Collisions with Multiple Variable Length Arguments

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#relationships "Permanent link")

-   CWE-347: Improper Verification of Cryptographic Signature
    [https://cwe.mitre.org/data/definitions/347.html](https://cwe.mitre.org/data/definitions/347.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#description "Permanent link")

When hashing multiple variable-length arguments, there is a potential risk of hash collisions, which can occur if two different sets of inputs produce the same hash output. This vulnerability is particularly relevant in situations where hashes are used as identifiers, signatures, or keys, and collisions may lead to incorrect behavior or security breaches, such as false validation of signatures or unexpected contract logic execution.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#remediation "Permanent link")

To prevent hash collisions, use a strong cryptographic hashing function like `keccak256` or `sha256`, and ensure that the inputs to the hash function are well-structured. Consider combining different sources of entropy (e.g., timestamps, nonces) and always verify the integrity of the data before trusting a hash.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-0-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-0-2)    function verifyData(bytes memory data1, bytes memory data2) public pure returns (bytes32) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-0-3)        // Vulnerable to hash collisions with multiple variable-length arguments        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-0-4)        return keccak256(abi.encodePacked(data1, data2));  // Possible collision risk    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-0-5)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-0-6)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-1-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-1-2)    function verifyData(bytes memory data1, bytes memory data2) public pure returns (bytes32) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-1-3)        // Safe way to hash multiple variable-length arguments        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-1-4)        return keccak256(abi.encode(data1, data2));  // More secure handling of variable-length inputs    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-1-5)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/#__codelineno-1-6)}`
