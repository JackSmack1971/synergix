---
title: "SCWE-119: Shared Proxy Admin and Logic Owner Key"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.610Z"
---
*Last updated: August 19, 2026*


# SCWE-119: Shared Proxy Admin and Logic Owner Key

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#relationships "Permanent link")

-   CWE-284: Improper Access Control
    [https://cwe.mitre.org/data/definitions/284.html](https://cwe.mitre.org/data/definitions/284.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#description "Permanent link")

Using the same key to control both the proxy admin (upgrade rights) and logic contract owner concentrates power. A single key compromise allows hostile upgrades and privileged function abuse with no separation of duties.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#remediation "Permanent link")

-   Separate roles: proxy admin under multisig+timelock; logic owner under different multisig.
-   Use role-based access (e.g., OZ AccessControl) and distinct keys for operational vs. upgrade actions.
-   Document and monitor role boundaries; rotate keys periodically.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-3)contract Proxy {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-4)    address public admin; // same key for upgrades and logic owner    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-5)    address public implementation; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-7)    modifier onlyAdmin() { require(msg.sender == admin, "not admin"); _; } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-8)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-9)    function upgrade(address impl) external onlyAdmin { implementation = impl; }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-10)    function setParam(uint256 x) external onlyAdmin { /* ... */ } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-3)contract Proxy {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-4)    address public proxyAdmin;   // timelock + multisig; upgrade rights only    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-5)    address public logicOwner;  // separate multisig; operational params only    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-6)    address public implementation; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-8)    modifier onlyProxyAdmin() { require(msg.sender == proxyAdmin, "not proxy admin"); _; }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-9)    modifier onlyLogicOwner() { require(msg.sender == logicOwner, "not logic owner"); _; } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-11)    function upgrade(address impl) external onlyProxyAdmin { implementation = impl; }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-12)    function setParam(uint256 x) external onlyLogicOwner { /* ... */ } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/#__codelineno-1-13)}`
