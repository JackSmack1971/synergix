---
title: "SCWE-054: Signature Malleability"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.218Z"
---
*Last updated: August 19, 2026*


# SCWE-054: Signature Malleability

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#relationships "Permanent link")

-   CWE-345: Insufficient Verification of Data Authenticity
    [https://cwe.mitre.org/data/definitions/345.html](https://cwe.mitre.org/data/definitions/345.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#description "Permanent link")

Signature malleability refers to the ability to modify a valid signature without changing its validity. This can occur when signatures are not properly verified or when certain components of a signature (like the `v`, `r`, and `s` values) can be altered while still producing a valid signature.

Attackers can modify a signature’s `s` value or flip `v` between 27 and 28, generating different valid signatures for the same message. This can lead to:

-   Replay attacks, where transactions can be re-executed with modified signatures.
-   Transaction hijacking, where a valid signature is altered to redirect funds or manipulate contract state.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#remediation "Permanent link")

To mitigate signature malleability, ensure that the signature verification process is robust. Use secure cryptographic libraries that properly handle signature validation, such as ECDSA or EdDSA with additional checks to prevent malleability. When verifying signatures, consider using a canonical format for signature components to avoid malleability.

### Vulnerable Contract Example- (Allows Signature Malleability)[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#vulnerable-contract-example-allows-signature-malleability "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-0-1)contract MalleableSignatureExample {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-0-2)    function verifySignature(bytes32 message, uint8 v, bytes32 r, bytes32 s) public pure returns (bool) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-0-3)        address signer = ecrecover(message, v, r, s);  // Signature malleability risk        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-0-4)        return signer != address(0);    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-0-5)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-0-6)}`

\- This contract does not restrict `s` values, allowing malleable signatures. - Issue: The contract does not check if `s` is in the lower half of the `curve (s < secp256k1n/2)`, allowing multiple valid signatures for the same message.

### Fixed Contract Example- Prevents Signature Malleability)[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#fixed-contract-example-prevents-signature-malleability "Permanent link")

  `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-1)  pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-2)  [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-3)  import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-4)  [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-5)  contract SecureSignatureExample {      [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-6)      using ECDSA for bytes32; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-7)      [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-8)      function verifySignature(bytes32 message, bytes memory signature) public pure returns (address) {          [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-9)          return message.toEthSignedMessageHash().recover(signature);      [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-10)      }  [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/#__codelineno-1-11)  }`

-   Fix: Uses `OpenZeppelin’s ECDSA library`, which ensures `s` is in the lower half and restricts `v` to 27 or 28.
-   Outcome: Prevents attackers from modifying valid signatures to create alternate, equally valid ones.
