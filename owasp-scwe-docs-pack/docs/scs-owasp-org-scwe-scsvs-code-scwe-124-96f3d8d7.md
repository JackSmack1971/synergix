---
title: "SCWE-124: Inconsistent Rounding Direction in Financial Math"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:27.107Z"
---
*Last updated: August 19, 2026*


# SCWE-124: Inconsistent Rounding Direction in Financial Math

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#relationships "Permanent link")

-   CWE-682: Incorrect Calculation
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#description "Permanent link")

Using mixed rounding strategies (floor vs. ceil vs. truncation) across mint/burn/withdraw logic causes value drift. Attackers can cycle operations to accumulate dust gains or trigger unfair liquidations due to asymmetry.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#remediation "Permanent link")

-   Define and document a single rounding direction per invariant (e.g., always round in favor of the protocol or user).
-   Centralize math helpers and reuse them across all financial paths.
-   Add property-based tests to ensure invariant preservation under rounding.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-0-3)shares = amount * totalShares / totalAssets;      // truncates [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-0-4)assets = shares * totalAssets / totalShares + 1;  // rounds up`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-1-3)// consistently round down (or up) and state it explicitly [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-1-4)shares = amount * totalShares / totalAssets; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/#__codelineno-1-5)assets = shares * totalAssets / totalShares;`
