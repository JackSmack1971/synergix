---
title: "SCWE-131: Missing Domain Separation in Aggregate Signatures"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.074Z"
---
*Last updated: August 19, 2026*


# SCWE-131: Missing Domain Separation in Aggregate Signatures

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#relationships "Permanent link")

-   CWE-347: Improper Verification of Cryptographic Signature
    [https://cwe.mitre.org/data/definitions/347.html](https://cwe.mitre.org/data/definitions/347.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#description "Permanent link")

BLS/aggregate signature schemes that omit domain separation (e.g., chain id, contract, purpose) allow signature replay across domains. A valid signature for one network or message type can be reused elsewhere to authorize unintended actions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#remediation "Permanent link")

-   Include explicit domain separation tags in the signed message for every aggregate signature.
-   Verify domains on-chain and reject signatures from unknown domains.
-   Use well-reviewed libraries and EIP-712 style typed data for aggregate schemes.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#__codelineno-0-1)bytes32 message = keccak256(abi.encode(data)); // no domain tag`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/#__codelineno-1-1)bytes32 message = keccak256(abi.encode(DOMAIN_SEPARATOR, keccak256(data)));`
