---
title: "SCWE-136: Unbounded Proposal Execution Gas"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.725Z"
---
*Last updated: August 19, 2026*


# SCWE-136: Unbounded Proposal Execution Gas

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#description "Permanent link")

Governance proposals that execute arbitrary call lists without gas limits or batching can exceed block gas, making proposals unexecutable (DoS). Attackers can submit proposals with expensive calls to jam governance or brick queued actions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#remediation "Permanent link")

-   Enforce per-call and total gas limits; split proposals into bounded batches.
-   Allow graceful skipping of failed subcalls with clear status, or pre-validate gas cost.
-   Add simulation checks before queuing and block proposals that exceed safe gas budgets.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-0-1)function execute(bytes[] calldata calls) external {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-0-2)    for (uint i; i < calls.length; i++) {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-0-3)        target.call(calls[i]); // no gas limit    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-0-4)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-0-5)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-1-1)function execute(bytes[] calldata calls, uint256 gasPerCall) external {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-1-2)    for (uint i; i < calls.length; i++) {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-1-3)        (bool ok,) = target.call{gas: gasPerCall}(calls[i]);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-1-4)        require(ok, "subcall failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-1-5)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/#__codelineno-1-6)}`
