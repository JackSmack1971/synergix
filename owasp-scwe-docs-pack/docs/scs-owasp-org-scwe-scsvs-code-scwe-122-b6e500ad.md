---
title: "SCWE-122: Calldata Length Not Validated Before Decode"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:26.819Z"
---
*Last updated: August 19, 2026*


# SCWE-122: Calldata Length Not Validated Before Decode

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#description "Permanent link")

Functions that `abi.decode` calldata without first checking expected length can revert unpredictably or read malformed inputs. Attackers can craft short calldata to trigger reverts that lock functionality or bypass logic that runs before decode.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#remediation "Permanent link")

-   Validate `msg.data.length` against expected sizes (including selector).
-   Prefer Solidity typed arguments but still guard against undersized calldata on low-level entrypoints.
-   Reject unexpected trailing data when strict parsing is required.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-0-3)function execute(bytes calldata data) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-0-4)    (address to, uint256 amount) = abi.decode(data, (address, uint256));    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-0-5)    // ... [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-0-6)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-1-3)function execute(bytes calldata data) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-1-4)    require(data.length == 64, "bad length"); // selector handled elsewhere    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-1-5)    (address to, uint256 amount) = abi.decode(data, (address, uint256)); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/#__codelineno-1-6)}`
