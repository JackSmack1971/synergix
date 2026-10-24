---
title: "SCWE-150: Storage Slot Collision When Upgrading Implementation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.949Z"
---
*Last updated: August 19, 2026*


# SCWE-150: Storage Slot Collision When Upgrading Implementation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#relationships "Permanent link")

-   CWE-682: Incorrect Calculation
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#description "Permanent link")

When upgrading a proxy's implementation, the new implementation's storage layout must be compatible with the proxy's storage. Appending variables in the implementation without accounting for the proxy's own storage (e.g., admin, implementation address) can cause slot collisions. Similarly, inherited contracts that add state variables can overwrite slots used by the base or proxy. SCWE-099 covers same-contract layout; this addresses cross-contract layout (proxy + implementation, inheritance chain).

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#remediation "Permanent link")

-   Use a single storage contract or follow a consistent storage layout convention (e.g., EIP-1967).
-   Reserve gaps (`uint256[50] private __gap`) in base contracts for future expansion.
-   Run storage layout diff tools before upgrading.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-1)// Proxy [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-2)contract Proxy {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-3)    address public implementation;  // slot 0    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-4)    address public admin;           // slot 1 [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-5)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-6)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-7)// Implementation V2 - assumes it "owns" slots from 0 [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-8)contract ImplV2 {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-9)    address public owner;      // slot 0 - COLLIDES with proxy's implementation    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-10)    uint256 public newValue;   // slot 1 - COLLIDES with proxy's admin [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-1-1)contract ImplV2 {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-1-2)    // Storage in implementation must not overlap proxy slots    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-1-3)    // Use EIP-1967 or append after reserved slots    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-1-4)    bytes32 private constant IMPLEMENTATION_SLOT = 0x360894...;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-1-5)    // Implementation state starts after proxy slots    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-1-6)    uint256 public newValue; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/#__codelineno-1-7)}`
