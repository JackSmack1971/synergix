---
title: "SCWE-154: Calldata Decode Without Length Check"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:28.092Z"
---
*Last updated: August 19, 2026*


# SCWE-154: Calldata Decode Without Length Check

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#description "Permanent link")

Decoding calldata or bytes with `abi.decode` without first verifying the input length can cause unexpected reverts. In modern Solidity (0.4.22+), `abi.decode` with data shorter than expected reverts due to bounds checking; malformed or incorrectly typed data can produce wrong values. SCWE-122 covers calldata length validation; this weakness addresses the broader pattern of decoding without length checks.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#remediation "Permanent link")

-   Validate `data.length >= expectedLength` before `abi.decode`.
-   Use `abi.decode` with the correct type and ensure the encoded data matches.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-3)contract Decoder {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-4)    function decodeAndUse(bytes calldata data) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-5)        (address recipient, uint256 amount) = abi.decode(data, (address, uint256));        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-6)        // If data is too short, decode reverts; malformed data can produce wrong values        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-7)        transfer(recipient, amount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-0-9)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-1-1)function decodeAndUse(bytes calldata data) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-1-2)    require(data.length >= 32 + 32, "Invalid data length");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-1-3)    (address recipient, uint256 amount) = abi.decode(data, (address, uint256));    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-1-4)    transfer(recipient, amount); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/#__codelineno-1-5)}`
