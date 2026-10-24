---
title: "SCWE-129: Single EOA Admin Without Rotation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.556Z"
---
*Last updated: August 19, 2026*


# SCWE-129: Single EOA Admin Without Rotation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#relationships "Permanent link")

-   CWE-284: Improper Access Control
    [https://cwe.mitre.org/data/definitions/284.html](https://cwe.mitre.org/data/definitions/284.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#description "Permanent link")

Relying on a single externally owned account (EOA) as contract admin creates a single point of failure. Key compromise, loss, or coercion can lead to irreversible upgrades, pauses, or fund drains with no recovery.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#remediation "Permanent link")

-   Use multisig (>=2-of-3) with hardware keys and timelocks for admin roles.
-   Document and test key rotation and recovery procedures.
-   Limit admin powers by role (upgrade vs. ops) and enforce separation of duties.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-3)contract Gov {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-4)    address public admin; // single EOA — key loss or compromise = no recovery [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-6)    modifier onlyAdmin() { require(msg.sender == admin, "not admin"); _; }    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-7)    function upgrade(address impl) external onlyAdmin { /* ... */ } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-0-8)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-3)contract Gov {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-4)    IMultisig public admin;     // 2-of-3 multisig with hardware keys    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-5)    ITimelock public timelock;  // 48h delay for upgrades [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-7)    function proposeUpgrade(address impl) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-8)        require(admin.isOwner(msg.sender), "not owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-9)        timelock.schedule(impl);    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-10)    }    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-11)    function executeUpgrade() external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-12)        timelock.execute(); // only after delay; supports key rotation    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/#__codelineno-1-14)}`
