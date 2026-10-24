---
title: "SCWE-099: Storage Layout Collision on Upgrade"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.261Z"
---
*Last updated: August 19, 2026*


# SCWE-099: Storage Layout Collision on Upgrade

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#relationships "Permanent link")

-   CWE-664: Improper Control of a Resource Through its Lifetime
    [https://cwe.mitre.org/data/definitions/664.html](https://cwe.mitre.org/data/definitions/664.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#description "Permanent link")

Upgradeable contracts rely on stable storage slots. Reordering, removing, or inserting state variables (or changing inheritance order) between versions causes storage collisions when the proxy reuses the same slots, corrupting balances, roles, or configuration.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#remediation "Permanent link")

-   Freeze variable ordering; only append new variables.
-   Reserve gaps (`uint256[50] private __gap;`) to allow future expansion.
-   Use automated storage layout diffing and follow upgrade-safe patterns (e.g., OZ Upgradeable tooling).

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-3)contract V1 {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-4)    address public owner;   // slot 0    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-5)    uint256 public balance; // slot 1 [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-6)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-7)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-8)contract V2 is V1 {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-9)    uint256 public balance; // reuses slot 1, corrupts state    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-10)    address public treasury; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-3)contract V1 {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-4)    address public owner;   // slot 0    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-5)    uint256 public balance; // slot 1    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-6)    uint256[48] private __gap; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-7)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-8)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-9)contract V2 is V1 {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-10)    uint256 public treasuryFee; // slot 2 (after gap) [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/#__codelineno-1-11)}`
