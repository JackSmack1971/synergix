---
title: "SCWE-121: Swallowed Revert Reasons"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:26.640Z"
---
*Last updated: August 19, 2026*


# SCWE-121: Swallowed Revert Reasons

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#relationships "Permanent link")

-   CWE-388: Error Handling
    [https://cwe.mitre.org/data/definitions/388.html](https://cwe.mitre.org/data/definitions/388.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#description "Permanent link")

Ignoring revert data (e.g., using `require(ok)` without bubbling reason) hides the root cause of failures. Protocols may proceed under incorrect assumptions, misprice risk, or block user funds without actionable errors.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#remediation "Permanent link")

-   Bubble revert reasons from external calls (`(bool ok, bytes memory data)`, then `assembly { revert(add(data,32), mload(data)) }` when `!ok`).
-   Standardize error handling with custom errors and propagate upstream.
-   Emit diagnostics when external calls fail to aid monitoring.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-0-3)(bool ok, ) = target.call(payload); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-0-4)require(ok, "call failed"); // hides real reason`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-3)(bool ok, bytes memory data) = target.call(payload); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-4)if (!ok) {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-5)    assembly {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-6)        revert(add(data, 32), mload(data))    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/#__codelineno-1-8)}`
