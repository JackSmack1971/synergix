---
title: "SCWE-106: Unauthenticated Meta-Transactions"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.441Z"
---
*Last updated: August 19, 2026*


# SCWE-106: Unauthenticated Meta-Transactions

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#relationships "Permanent link")

-   CWE-347: Improper Verification of Cryptographic Signature
    [https://cwe.mitre.org/data/definitions/347.html](https://cwe.mitre.org/data/definitions/347.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#description "Permanent link")

Meta-transaction forwarders that relay calls without verifying the signer, nonce, chain, or expiry let relayers execute arbitrary actions on behalf of victims. Missing replay protection allows the same signed request to be executed multiple times.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#remediation "Permanent link")

-   Verify EIP-712 typed data signatures against the declared signer.
-   Track and increment per-signer nonces; enforce deadlines and chainId.
-   Restrict trusted forwarders and sanitize `msg.sender`/`msg.data` assumptions in downstream calls.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-3)contract Forwarder {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-4)    function relay(address target, bytes calldata data) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-5)        (bool ok, ) = target.call(data); // no signature or nonce check        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-6)        require(ok, "call failed");    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-0-8)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-3)contract Forwarder {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-4)    mapping(address => uint256) public nonces; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-6)    function relay(address target, bytes calldata data, uint256 nonce, uint256 deadline, bytes calldata sig) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-7)        require(block.timestamp <= deadline, "expired");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-8)        bytes32 digest = keccak256(abi.encode(target, data, nonce, block.chainid, deadline));        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-9)        address signer = ECDSA.recover(digest, sig);        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-10)        require(nonce == nonces[signer]++, "bad nonce");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-11)        (bool ok, ) = target.call(data);        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-12)        require(ok, "call failed");    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/#__codelineno-1-14)}`
