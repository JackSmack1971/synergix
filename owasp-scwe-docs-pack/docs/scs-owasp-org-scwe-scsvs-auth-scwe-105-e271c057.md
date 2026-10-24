---
title: "SCWE-105: Permit Signature Replay via Missing Domain Separator or Nonce"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.320Z"
---
*Last updated: August 19, 2026*


# SCWE-105: Permit Signature Replay via Missing Domain Separator or Nonce

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#relationships "Permanent link")

-   CWE-347: Improper Verification of Cryptographic Signature
    [https://cwe.mitre.org/data/definitions/347.html](https://cwe.mitre.org/data/definitions/347.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#description "Permanent link")

Improper EIP-2612 permit implementations that omit chain-specific domain separators, do not increment nonces, or ignore expiration allow signatures to be replayed across chains or multiple times. Attackers can repeatedly approve spending or re-use permits on forked networks.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#remediation "Permanent link")

-   Build EIP-712 domain separators including `name`, `version`, `chainId`, and `verifyingContract`.
-   Maintain per-owner nonces and increment on every successful permit.
-   Enforce deadlines and reject expired signatures.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-2)contract Token {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-3)    mapping(address => uint256) public nonces; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-4)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-5)    function permit(address owner, address spender, uint256 value, bytes calldata sig) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-6)        // missing chainId/domain checks, nonce not incremented        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-7)        address signer = ecrecover(/* simplified */);        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-8)        require(signer == owner, "bad sig");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-9)        // allowance set here...    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-2)contract Token {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-3)    bytes32 public DOMAIN_SEPARATOR;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-4)    mapping(address => uint256) public nonces; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-7)        DOMAIN_SEPARATOR = keccak256(abi.encode(            [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-8)            keccak256("EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)"),            [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-9)            keccak256(bytes("Token")),            [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-10)            keccak256(bytes("1")),            [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-11)            block.chainid,            [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-12)            address(this)        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-13)        ));    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-15)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-16)    function permit(/* params */) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-17)        // verify typed data with nonce and deadline, then increment nonce        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-18)        nonces[owner] += 1;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-19)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/#__codelineno-1-20)}`
