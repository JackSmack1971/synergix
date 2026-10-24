---
title: "SCWE-056: Lack of Proper Signature Verification"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.463Z"
---
*Last updated: August 19, 2026*


# SCWE-056: Lack of Proper Signature Verification

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#relationships "Permanent link")

-   CWE-345: Insufficient Verification of Data Authenticity
    [https://cwe.mitre.org/data/definitions/345.html](https://cwe.mitre.org/data/definitions/345.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#description "Permanent link")

This vulnerability occurs when a smart contract fails to properly verify whether a signature was produced by an authorized entity. In Ethereum, contracts often use `ecrecover` to check signatures, but failing to validate who signed the message allows:

-   Unauthorized transactions, where attackers submit signatures from any key.
-   Replay attacks, where valid signatures are reused to repeat actions.
-   Malicious contract state manipulation, where attackers gain unauthorized access.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#remediation "Permanent link")

To mitigate this vulnerability, always implement proper signature verification using secure cryptographic methods. Use the `ecrecover` function to recover the signer’s address and ensure that the recovered address matches the expected address. Additionally, verify that the signature is valid for the intended message or transaction and that the signer is authorized to perform the action.

### Vulnerable Contract Example- (Lack of Signer Verification)[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#vulnerable-contract-example-lack-of-signer-verification "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-0-1)contract SignatureVerificationExample {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-0-2)    function authenticate(bytes32 message, uint8 v, bytes32 r, bytes32 s) public view returns (address) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-0-3)        address signer = ecrecover(message, v, r, s);        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-0-4)        return signer;  // No further validation of the signer or message    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-0-5)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-0-6)}`

\- Issue: The contract does not check if the recovered address matches an authorized signer. - Exploit: Any valid ECDSA signature can be used, even from an attacker’s key.

### Fixed Contract Example- (Proper Signature Verification)[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#fixed-contract-example-proper-signature-verification "Permanent link")

    `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-1)    pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-2)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-3)    import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-4)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-5)    contract SecureSignatureVerificationExample {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-6)        using ECDSA for bytes32; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-7)        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-8)        address public authorizedSigner; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-9)        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-10)        constructor(address _authorizedSigner) {            [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-11)            require(_authorizedSigner != address(0), "Invalid signer");            [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-12)            authorizedSigner = _authorizedSigner;        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-13)        } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-14)        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-15)        function authenticate(bytes32 message, bytes memory signature) public view returns (bool) {            [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-16)            address signer = message.toEthSignedMessageHash().recover(signature);            [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-17)            require(signer == authorizedSigner, "Unauthorized signer"); // Proper validation            [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-18)            return true;        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-19)        }    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/#__codelineno-1-20)    }`

\- Fix: The contract now explicitly checks that the recovered address matches `authorizedSigner`. - Outcome: Prevents attackers from submitting arbitrary signatures and ensures only authorized signatures are accepted.
