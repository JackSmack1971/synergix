---
title: "SCWE-118: Unauthenticated Beacon Upgrade"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.497Z"
---
*Last updated: August 19, 2026*


# SCWE-118: Unauthenticated Beacon Upgrade

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#relationships "Permanent link")

-   CWE-306: Missing Authentication for Critical Function
    [https://cwe.mitre.org/data/definitions/306.html](https://cwe.mitre.org/data/definitions/306.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#description "Permanent link")

Beacon proxies rely on a beacon address that determines implementation. If the beacon upgrade function lacks proper access control or timelock, an attacker can point all proxies to malicious code, taking over state and funds.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#remediation "Permanent link")

-   Restrict beacon upgrades to multisig+timelock and emit events on change.
-   Validate new implementation bytecode (e.g., initializer disabled, interfaces intact).
-   Monitor beacon address changes on-chain with alerts.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-3)contract Beacon {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-4)    address public impl;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-5)    function upgradeTo(address newImpl) external { // no auth        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-6)        impl = newImpl;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-0-8)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-3)contract Beacon {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-4)    address public impl;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-5)    address public admin;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-6)    function upgradeTo(address newImpl) external {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-7)        require(msg.sender == admin, "not admin");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-8)        impl = newImpl;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/#__codelineno-1-10)}`
