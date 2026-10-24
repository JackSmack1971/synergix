---
title: "SCWE-125: Missing Post-Operation Health Check"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.722Z"
---
*Last updated: August 19, 2026*


# SCWE-125: Missing Post-Operation Health Check

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#relationships "Permanent link")

-   CWE-754: Improper Check for Unusual or Exceptional Conditions
    [https://cwe.mitre.org/data/definitions/754.html](https://cwe.mitre.org/data/definitions/754.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#description "Permanent link")

Lending/borrowing protocols that do not re-evaluate health factors after actions (borrow, withdraw, leverage) allow users to exit with unhealthy positions. Attackers can drain collateral or avoid liquidation by skipping post-operation solvency checks.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#remediation "Permanent link")

-   Recompute health factor after every state-changing action and revert if below threshold.
-   Lock price/oracle reads during the operation to avoid mid-tx manipulation.
-   Add invariant/fuzz tests to ensure every path enforces solvency.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-0-1)function borrow(uint256 amount) external {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-0-2)    _issueDebt(msg.sender, amount);    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-0-3)    // no health check after debt increase [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-0-4)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-1-1)function borrow(uint256 amount) external {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-1-2)    _issueDebt(msg.sender, amount);    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-1-3)    require(_health(msg.sender) >= MIN_HF, "insolvent"); [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/#__codelineno-1-4)}`
