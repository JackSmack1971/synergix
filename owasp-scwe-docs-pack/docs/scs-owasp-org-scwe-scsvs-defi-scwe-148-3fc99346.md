---
title: "SCWE-148: Gas Exhaustion via Unbounded Loops with External Calls"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.937Z"
---
*Last updated: August 19, 2026*


# SCWE-148: Gas Exhaustion via Unbounded Loops with External Calls

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#description "Permanent link")

Loops that iterate over user-controlled arrays and perform external calls (transfers, approvals, or other contract calls) in each iteration can exhaust gas when the array is large. Each external call consumes gas; unbounded loops cause the transaction to hit the block gas limit and revert, resulting in denial of service. SCWE-109 covers unbounded loops generally; this weakness focuses on loops that perform external calls.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#remediation "Permanent link")

-   Impose an upper bound on loop iterations or batch size.
-   Use pull-based patterns: let users claim individually instead of pushing to many addresses in one tx.
-   Process in chunks with pagination or checkpoints.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-3)contract Airdrop {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-4)    function distribute(address[] calldata recipients, uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-5)        for (uint256 i = 0; i < recipients.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-6)            (bool ok, ) = recipients[i].call{value: amount}("");            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-7)            require(ok, "Transfer failed");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-8)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-0-10)}`

**Why vulnerable:** Large `recipients.length` causes out-of-gas; one failed transfer reverts the entire batch.

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-1)uint256 public constant MAX_BATCH = 100; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-3)function distribute(address[] calldata recipients, uint256 amount) external {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-4)    require(recipients.length <= MAX_BATCH, "Batch too large");    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-5)    for (uint256 i = 0; i < recipients.length; i++) {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-6)        (bool ok, ) = recipients[i].call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-7)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/#__codelineno-1-9)}`
