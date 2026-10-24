---
title: "SCWE-128: Insecure Multicall Context Forwarding"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.339Z"
---
*Last updated: August 19, 2026*


# SCWE-128: Insecure Multicall Context Forwarding

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#relationships "Permanent link")

-   CWE-841: Improper Enforcement of Behavioral Workflow
    [https://cwe.mitre.org/data/definitions/841.html](https://cwe.mitre.org/data/definitions/841.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#description "Permanent link")

Multicall-style aggregators that forward calls without guarding against reentrancy or context changes let attackers reorder actions within one tx (e.g., deposit then withdraw) or impersonate `msg.sender` when inner calls use `tx.origin` or cached sender state.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#remediation "Permanent link")

-   Apply reentrancy guards around multicall entrypoints.
-   Avoid caching `msg.sender` across calls; pass explicit sender/context to internal functions.
-   Restrict callable selectors/targets or enforce allowlists.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-0-1)function multicall(bytes[] calldata data) external {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-0-2)    for (uint i; i < data.length; i++) {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-0-3)        (bool ok, ) = address(this).delegatecall(data[i]);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-0-4)        require(ok, "fail");    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-0-5)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-0-6)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-1-1)function multicall(bytes[] calldata data) external nonReentrant {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-1-2)    for (uint i; i < data.length; i++) {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-1-3)        _dispatch(msg.sender, data[i]); // explicit context, no delegatecall loops    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-1-4)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/#__codelineno-1-5)}`
