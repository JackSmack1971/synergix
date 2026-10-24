---
title: "SCWE-098: Initialization Front-Running in Upgradeable Contracts"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.156Z"
---
*Last updated: August 19, 2026*


# SCWE-098: Initialization Front-Running in Upgradeable Contracts

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#relationships "Permanent link")

-   CWE-284: Improper Access Control
    [https://cwe.mitre.org/data/definitions/284.html](https://cwe.mitre.org/data/definitions/284.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#description "Permanent link")

Proxy-based contracts ship without constructors; if the initializer is callable by anyone, an attacker can front-run deployment and seize ownership, set trusted roles, or lock upgrades. This permanently compromises the implementation behind the proxy.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#remediation "Permanent link")

-   Protect initializer functions with access control and `initializer`/`reinitializer` guards.
-   Invoke initialization atomically during deployment or via a deploy-time call data payload.
-   Use `disableInitializers()` on the implementation contract to prevent accidental takeover.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-2)import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol"; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-4)contract UpgradeableVault is Initializable {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-7)    function initialize(address _owner) public initializer {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-8)        owner = _owner; // anyone can front-run and become owner    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-0-10)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-2)import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol"; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-4)contract UpgradeableVault is Initializable {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-7)    function initialize(address _owner, address deployer) public initializer {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-8)        require(msg.sender == deployer, "only deployer");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-9)        owner = _owner;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/#__codelineno-1-11)}`

Deployer (or factory) deploys the proxy and calls `initialize(owner, address(this))` in the same transaction — no window for front-running.
