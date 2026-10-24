---
title: "SCWE-141: Lack of Deadline Validation in Time-Sensitive External Calls"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:27.453Z"
---
*Last updated: August 19, 2026*


# SCWE-141: Lack of Deadline Validation in Time-Sensitive External Calls

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#description "Permanent link")

Time-sensitive external calls (e.g., DEX swaps, limit orders) that use only `block.timestamp` as a deadline—or no user-supplied deadline—can be front-run or executed at unfavorable times. A user signs a transaction expecting execution within a short window, but miners/validators can delay inclusion. Without a `deadline` parameter, the transaction may execute when prices have moved adversely. SCWE-090 covers slippage; this weakness addresses the absence of explicit deadline validation.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#remediation "Permanent link")

-   Accept a `deadline` parameter from users and enforce `require(block.timestamp <= deadline, "Expired")` before executing time-sensitive logic.
-   Never rely solely on `block.timestamp` for user-intended time bounds without a user-supplied deadline.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-3)interface IRouter {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-4)    function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to, uint256 deadline) external returns (uint256[] memory); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-5)} [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-6)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-7)contract Swapper {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-8)    IRouter public router; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-10)    function swap(address[] calldata path, uint256 amountIn, uint256 minOut) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-11)        router.swapExactTokensForTokens(            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-12)            amountIn,            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-13)            minOut,            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-14)            path,            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-15)            msg.sender,            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-16)            block.timestamp  // No user deadline: tx can be delayed and executed at bad time        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-17)        );    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-18)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-0-19)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-1-1)function swap(address[] calldata path, uint256 amountIn, uint256 minOut, uint256 deadline) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-1-2)    require(block.timestamp <= deadline, "Expired");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-1-3)    router.swapExactTokensForTokens(amountIn, minOut, path, msg.sender, deadline); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/#__codelineno-1-4)}`
