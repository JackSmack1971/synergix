---
title: "SCWE-117: Proxy Implementation Selfdestruct Exposure"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.371Z"
---
*Last updated: August 19, 2026*


# SCWE-117: Proxy Implementation Selfdestruct Exposure

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#relationships "Permanent link")

-   CWE-284: Improper Access Control
    [https://cwe.mitre.org/data/definitions/284.html](https://cwe.mitre.org/data/definitions/284.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#description "Permanent link")

If the proxy’s implementation contract exposes `selfdestruct` (or `SELFDESTRUCT` reachable through a function), an attacker or careless admin can destroy the implementation. The proxy then points to a non-existent code address, bricking upgrades or locking funds.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#remediation "Permanent link")

-   Remove or disable `selfdestruct` in implementations; use `disableInitializers()` patterns.
-   Gate any destruct-like functionality behind timelock + multisig and migration plans.
-   Monitor implementation addresses and block upgrades that reduce code size to zero.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-0-3)contract Impl {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-0-4)    function kill() external {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-0-5)        selfdestruct(payable(msg.sender));    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-0-7)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-1-3)contract Impl {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-1-4)    // no selfdestruct path; migrations use new proxy with state copy [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/#__codelineno-1-5)}`
