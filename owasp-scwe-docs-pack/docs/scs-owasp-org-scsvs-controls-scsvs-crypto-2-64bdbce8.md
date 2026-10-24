---
title: "SCSVS-CRYPTO-2¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-2/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:57.253Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-CRYPTO-2.md "Edit this page")

# SCSVS-CRYPTO-2[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-2/#scsvs-crypto-2 "Permanent link")

## S6.2 Signature Verification[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-2/#s62-signature-verification "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-2/#control-objective "Permanent link")

Implement cryptographic techniques that ensure the secure verification of signatures and compliance with standards to maintain the integrity of authenticated transactions.

### S6.2.A Cryptographic Techniques for Authentication[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-2/#s62a-cryptographic-techniques-for-authentication "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S6.2.A1 | Ensure that cryptographic algorithms used for signature verification are secure and follow best practices. |  | ✓ | ✓ |  |

### S6.2.B Standard Compliance (e.g., EIP-712)[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-2/#s62b-standard-compliance-eg-eip-712 "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S6.2.B1 | Verify that ECDSA signature handling functions, such as ECDSA.recover and ECDSA.tryRecover, properly manage signature formats to prevent signature malleability, especially when handling both traditional 65-byte and EIP-2098 compact signatures. |  | ✓ | ✓ |  |
