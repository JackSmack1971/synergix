---
title: "SCWE-103: ERC20 Approval Double-Spend (Allowance Race)"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.759Z"
---
*Last updated: August 19, 2026*


# SCWE-103: ERC20 Approval Double-Spend (Allowance Race)

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#relationships "Permanent link")

-   CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization (Race Condition)
    [https://cwe.mitre.org/data/definitions/362.html](https://cwe.mitre.org/data/definitions/362.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#description "Permanent link")

Changing an ERC20 allowance from value `X` to `Y` with a single `approve` call allows a spender to front-run and spend `X` before the change, then spend `Y` after, effectively double-spending. Integrations that do not use `increaseAllowance`/`decreaseAllowance` are exposed.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#remediation "Permanent link")

-   Follow the allowance reset pattern: set allowance to `0`, then set the new value.
-   Prefer `increaseAllowance`/`decreaseAllowance` or EIP-2612 `permit` with nonces.
-   For critical flows, pull tokens via `transferFrom` after verifying allowance updates.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-2)interface IERC20 { function approve(address,uint256) external returns (bool); } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-4)contract DApp {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-5)    IERC20 public token; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-7)    function changeSpender(address spender, uint256 newAmount) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-8)        token.approve(spender, newAmount); // can be front-run    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-0-10)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-2)import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-3)import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol"; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-5)contract DApp {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-6)    using SafeERC20 for IERC20;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-7)    IERC20 public token; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-9)    function changeSpender(address spender, uint256 newAmount) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-10)        token.safeApprove(spender, 0);      // reset first; SafeERC20 handles non-standard tokens (e.g. USDT)        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-11)        token.safeApprove(spender, newAmount);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/#__codelineno-1-13)}`
