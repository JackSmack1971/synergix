---
title: "SCWE-151: Add/Remove Liquidity Without Minimum Output Validation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:39.063Z"
---
*Last updated: August 19, 2026*


# SCWE-151: Add/Remove Liquidity Without Minimum Output Validation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#description "Permanent link")

Adding or removing liquidity in AMMs (e.g., Uniswap, Curve) without enforcing a minimum amount of LP tokens or underlying assets received can expose users to sandwich attacks or unfavorable execution. Similar to swap slippage (SCWE-090), LP operations can be front-run: an attacker manipulates the pool before the user's add/remove, then reverses after. Without `amountMin` or equivalent checks, users may receive far less than expected.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#remediation "Permanent link")

-   Accept `amountMin` (or `minLPTokens`, `minAmounts`) from users and enforce it when adding/removing liquidity.
-   Use deadline parameters (SCWE-141) in addition to slippage protection.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-3)interface IUniswapV2Router {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-4)    function addLiquidity(address tokenA, address tokenB, uint256 amountADesired, uint256 amountBDesired, uint256 amountAMin, uint256 amountBMin, address to, uint256 deadline) external returns (uint256 amountA, uint256 amountB, uint256 liquidity); [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-5)} [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-6)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-7)contract LiquidityManager {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-8)    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-9)        IUniswapV2Router(router).addLiquidity(            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-10)            tokenA, tokenB,            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-11)            amountA, amountB,            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-12)            0, 0,  // amountAMin, amountBMin = 0: no slippage protection            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-13)            msg.sender,            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-14)            block.timestamp        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-15)        );    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-0-17)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-1-1)function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB, uint256 amountAMin, uint256 amountBMin, uint256 deadline) external {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-1-2)    require(block.timestamp <= deadline, "Expired");    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-1-3)    IUniswapV2Router(router).addLiquidity(tokenA, tokenB, amountA, amountB, amountAMin, amountBMin, msg.sender, deadline); [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/#__codelineno-1-4)}`
