---
title: "SCWE-120: Missing Return Data Length Validation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:26.433Z"
---
*Last updated: August 19, 2026*


# SCWE-120: Missing Return Data Length Validation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#relationships "Permanent link")

-   CWE-697: Incorrect Comparison
    [https://cwe.mitre.org/data/definitions/697.html](https://cwe.mitre.org/data/definitions/697.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#description "Permanent link")

Low-level calls that decode return values without checking `returndatasize` can read zeroed or truncated data. Attackers can craft contracts that return short payloads so callers mis-interpret success flags, prices, or balances.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#remediation "Permanent link")

-   Verify `returndatasize` matches expected length before decoding.
-   Prefer high-level interfaces that perform ABI decoding checks.
-   Revert on unexpected return sizes and log anomalies.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-0-3)(bool ok, bytes memory data) = token.staticcall(abi.encodeWithSignature("balanceOf(address)", user)); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-0-4)uint256 bal = abi.decode(data, (uint256)); // assumes length >= 32`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-1-3)(bool ok, bytes memory data) = token.staticcall(abi.encodeWithSignature("balanceOf(address)", user)); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-1-4)require(ok && data.length == 32, "bad returndata"); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/#__codelineno-1-5)uint256 bal = abi.decode(data, (uint256));`
