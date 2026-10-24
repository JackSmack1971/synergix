---
title: "SCWE-147: Permit or Meta-Transaction Signatures Without Expiration"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.807Z"
---
*Last updated: August 19, 2026*


# SCWE-147: Permit or Meta-Transaction Signatures Without Expiration

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#relationships "Permanent link")

-   CWE-347: Improper Verification of Cryptographic Signature
    [https://cwe.mitre.org/data/definitions/347.html](https://cwe.mitre.org/data/definitions/347.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#description "Permanent link")

Permit (EIP-2612) and meta-transaction signatures that omit a `deadline` or `expiry` parameter can be replayed indefinitely once obtained. An attacker who captures a valid signature (e.g., via phishing or a compromised frontend) can submit it at any future time. SCWE-105 covers domain separator and nonce; this weakness specifically addresses the absence of expiration.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#remediation "Permanent link")

-   Include a `deadline` (or `expiry`) in the signed message and enforce `require(block.timestamp <= deadline, "Expired")` when processing the signature.
-   Use EIP-712 structured data with a deadline field.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-3)contract MetaTx {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-4)    function execute(address signer, bytes32 hash, uint8 v, bytes32 r, bytes32 s) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-5)        require(ecrecover(hash, v, r, s) == signer, "Bad sig");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-6)        // No deadline: signature valid forever        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-7)        _execute(signer);    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-0-9)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-1-1)function execute(address signer, uint256 deadline, bytes32 hash, uint8 v, bytes32 r, bytes32 s) external {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-1-2)    require(block.timestamp <= deadline, "Expired");    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-1-3)    require(ecrecover(hash, v, r, s) == signer, "Bad sig");    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-1-4)    _execute(signer); [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/#__codelineno-1-5)}`

**Note:** The `hash` must be computed from EIP-712 structured data that includes the `deadline` field so the signature cannot be replayed after expiry.
