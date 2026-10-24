---
title: "SCWE-055: Missing Protection against Signature Replay Attacks"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.341Z"
---
*Last updated: August 19, 2026*


# SCWE-055: Missing Protection against Signature Replay Attacks

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#relationships "Permanent link")

-   CWE-294: Authentication Bypass by Capture-replay
    [https://cwe.mitre.org/data/definitions/294.html](https://cwe.mitre.org/data/definitions/294.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#description "Permanent link")

Signature replay attacks occur when a valid signature from a previous transaction is reused in a different context, such as a different transaction or contract call. Without proper protection, an attacker can capture and replay a signature, potentially bypassing authentication checks and causing unauthorized actions or transactions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#remediation "Permanent link")

To prevent signature replay attacks, include additional checks that ensure the signature is valid for a specific transaction or context. This can be done by incorporating unique identifiers like a nonce, timestamp, or a unique transaction hash into the signature to bind it to a specific use. Always verify that the signature is only valid for the intended action.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-1)contract ReplayAttackExample {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-2)    mapping(address => uint256) public nonces; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-4)    function authenticate(bytes32 message, uint8 v, bytes32 r, bytes32 s) public {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-5)        address signer = ecrecover(message, v, r, s);        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-6)        require(signer == msg.sender, "Invalid signature");        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-7)        // No protection against replay attacks; attacker can reuse the same signature    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-0-9)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#fixed-contract-example "Permanent link")

  `[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-1)  pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-2)  [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-3)  import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-4)  [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-5)  contract SecureReplayProtectionExample {      [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-6)      using ECDSA for bytes32; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-7)      [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-8)      mapping(address => uint256) public nonces; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-9)      [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-10)      function authenticate(bytes32 message, bytes memory signature) public {          [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-11)          uint256 nonce = nonces[msg.sender]++;          [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-12)          bytes32 messageWithContext = keccak256(abi.encodePacked(message, nonce, block.chainid));          [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-13)          address signer = messageWithContext.toEthSignedMessageHash().recover(signature);          [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-14)          require(signer == msg.sender, "Invalid signature");      [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-15)      }  [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/#__codelineno-1-16)  }`

**Fixes Implemented:** - Binds signature to a nonce (ensuring it's only usable once). - Includes `chainId` (prevents cross-chain replay attacks). - Uses OpenZeppelin’s ECDSA library (avoids signature malleability risks).

* * *
