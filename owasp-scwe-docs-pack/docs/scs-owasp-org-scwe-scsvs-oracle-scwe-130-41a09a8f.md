---
title: "SCWE-130: Admin-Write Oracle Without Delay"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.141Z"
---
*Last updated: August 19, 2026*


# SCWE-130: Admin-Write Oracle Without Delay

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#relationships "Permanent link")

-   CWE-346: Origin Validation Error
    [https://cwe.mitre.org/data/definitions/346.html](https://cwe.mitre.org/data/definitions/346.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#description "Permanent link")

Price feeds that allow an admin to push arbitrary values immediately (no delay or quorum) let insiders force liquidations, manipulate collateralization, or drain AMMs. Even trusted operators can be compromised.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#remediation "Permanent link")

-   Require multi-sig + timelock for manual price pushes; emit events for monitoring.
-   Use decentralized oracles with aggregation/quorum instead of single-writer feeds.
-   Enforce bounds/deviation checks against reference feeds and reject outliers.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-0-1)function setPrice(uint256 p) external onlyOwner {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-0-2)    price = p; // immediate effect [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-0-3)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-1-1)function queuePrice(uint256 p) external onlyGuardian {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-1-2)    queued = Price({val:p, eta:block.timestamp + delay}); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-1-3)} [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-1-4)function execute() external {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-1-5)    require(block.timestamp >= queued.eta, "too early");    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-1-6)    price = queued.val; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/#__codelineno-1-7)}`
