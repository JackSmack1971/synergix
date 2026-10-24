---
title: "SCWE-142: Extractable Value from Predictable Transaction Ordering"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.969Z"
---
*Last updated: August 19, 2026*


# SCWE-142: Extractable Value from Predictable Transaction Ordering

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#relationships "Permanent link")

-   CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
    [https://cwe.mitre.org/data/definitions/362.html](https://cwe.mitre.org/data/definitions/362.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#description "Permanent link")

Contracts that create predictable, orderable state changes expose value to block builders and searchers (MEV). Sandwich attacks, backrunning, and liquidation front-running are examples. When a user's transaction has a predictable effect (e.g., large swap moving price), an attacker can place transactions before and after to extract value. SCWE-037 covers front-running; this weakness addresses the broader MEV surface—design choices that make extraction easy.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#remediation "Permanent link")

-   Use private mempools or commit-reveal schemes for sensitive transactions.
-   Implement slippage protection (SCWE-090) and deadline parameters (SCWE-141).
-   Consider batch auctions, fair ordering, or MEV-aware design (e.g., CoW Protocol) where applicable.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-3)contract SimpleSwap {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-4)    function swap(uint256 amountIn, uint256 minOut) external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-5)        // Predictable: searcher sees large amountIn, sandwiches with buy-before and sell-after        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-6)        uint256 out = getAmountOut(amountIn);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-7)        require(out >= minOut, "Slippage");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-8)        transferOut(msg.sender, out);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-0-10)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-1-1)function swap(uint256 amountIn, uint256 minOut, uint256 deadline) external {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-1-2)    require(block.timestamp <= deadline, "Expired");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-1-3)    uint256 out = getAmountOut(amountIn);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-1-4)    require(out >= minOut, "Slippage");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-1-5)    transferOut(msg.sender, out); [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/#__codelineno-1-6)}`

**Fix:** User-supplied `deadline` and `minOut` limit MEV extraction. Use DEX aggregators or private order flow for additional protection.
