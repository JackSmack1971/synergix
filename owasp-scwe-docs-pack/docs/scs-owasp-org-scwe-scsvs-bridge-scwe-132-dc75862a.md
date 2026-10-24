---
title: "SCWE-132: Mismatched Token Decimals in Bridge Mint/Burn"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:37.712Z"
---
*Last updated: August 19, 2026*


# SCWE-132: Mismatched Token Decimals in Bridge Mint/Burn

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#relationships "Permanent link")

-   CWE-682: Incorrect Calculation
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#description "Permanent link")

Bridging tokens with differing decimals without normalization can over- or under-mint wrapped assets. Attackers can exploit decimal confusion to siphon value or lock funds when withdrawing back to the origin chain.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#remediation "Permanent link")

-   Normalize amounts to a canonical precision before mint/burn.
-   Store per-token decimal config and validate consistency during bridge operations.
-   Add tests for round-trip conversions across chains with varying decimals.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#__codelineno-0-1)// assumes 18 decimals on both sides; origin token has 6 [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#__codelineno-0-2)_mint(user, amount);`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#__codelineno-1-1)uint8 srcDec = 6; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#__codelineno-1-2)uint8 dstDec = 18; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#__codelineno-1-3)uint256 normalized = amount * 10**(dstDec - srcDec); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/#__codelineno-1-4)_mint(user, normalized);`
