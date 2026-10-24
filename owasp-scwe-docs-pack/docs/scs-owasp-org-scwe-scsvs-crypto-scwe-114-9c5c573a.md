---
title: "SCWE-114: ECDSA Nonce Reuse"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.824Z"
---
*Last updated: August 19, 2026*


# SCWE-114: ECDSA Nonce Reuse

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#relationships "Permanent link")

-   CWE-323: Reusing a Nonce, Key Pair in Encryption
    [https://cwe.mitre.org/data/definitions/323.html](https://cwe.mitre.org/data/definitions/323.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#description "Permanent link")

Reusing the same ECDSA nonce (`k`) across signatures (or using predictable nonces) leaks the private key. Contracts that accept off-chain signatures for permits, meta-txs, or governance can be compromised if signing infrastructure mismanages nonces.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#remediation "Permanent link")

-   Use battle-tested libraries/wallets that generate unique, random or RFC6979 deterministic nonces per message.
-   Monitor and rotate keys if nonce reuse is suspected; support key revocation on-chain.
-   Avoid custom signing code or manual nonce management in scripts.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-0-1)// Off-chain signer reuses k for two messages: [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-0-2)// sig1 = (r, s1) with k [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-0-3)// sig2 = (r, s2) with same k => private key can be recovered`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-1)// Off-chain: Use libraries/wallets that follow RFC6979; never reuse k. [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-2)// On-chain: Support key rotation so compromised keys can be revoked. [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-3)mapping(address => bool) public revokedSigners; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-5)function execute(bytes calldata payload, bytes calldata sig) external {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-6)    address signer = _recoverSigner(payload, sig);    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-7)    require(!revokedSigners[signer], "key revoked");    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-8)    // ... [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/#__codelineno-1-9)}`
