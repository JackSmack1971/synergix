---
title: "SCWE-090: Missing Slippage Protection in Automated Token Swaps"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.660Z"
---
*Last updated: August 19, 2026*


# SCWE-090: Missing Slippage Protection in Automated Token Swaps

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#relationships "Permanent link")

-   CWE-20: Improper Input Validation [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#description "Permanent link")

This weakness occurs when smart contracts execute token swaps through DEX routers (e.g., Uniswap, PancakeSwap, SushiSwap) with the amountOutMin parameter set to 0 or a hardcoded static value. This disables slippage protection and allows trades to execute regardless of adverse price movement. As a result, users or protocols may receive significantly fewer tokens than expected, especially under high volatility, front-running, or sandwich attack conditions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#remediation "Permanent link")

-   Always validate amountOutMin based on live price quotes (e.g., using on-chain oracles or pre-trade estimates).
-   Allow users to configure slippage tolerance (0.5%, 1%, etc.), and enforce it in contract logic.
-   Never hardcode 0 or static values for amountOutMin.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#examples "Permanent link")

-   **Vulnerable Code (Missing Slippage Protection)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-1)function swapTokens(address tokenIn, address tokenOut, uint256 amountIn) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-2)    IERC20(tokenIn).approve(address(uniswapRouter), amountIn); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-4)    address[] memory path = new address[](2);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-5)    path[0] = tokenIn;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-6)    path[1] = tokenOut; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-8)    // ❌ amountOutMin is set to 0 → no protection against slippage    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-9)    uniswapRouter.swapExactTokensForTokens(        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-10)        amountIn,        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-11)        0, // Vulnerable: accepts any output amount        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-12)        path,        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-13)        msg.sender,        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-14)        block.timestamp    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-15)    ); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-0-16)}`

-   **Safe Code (With Slippage Protection)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-1)function swapTokensWithSlippage(     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-2)    address tokenIn,    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-3)    address tokenOut,    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-4)    uint256 amountIn,    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-5)    uint256 minAmountOut [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-6)) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-7)    IERC20(tokenIn).approve(address(uniswapRouter), amountIn); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-9)    address[] memory path = new address[](2);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-10)    path[0] = tokenIn;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-11)    path[1] = tokenOut; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-12)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-13)    // ✅ Enforces user-provided slippage tolerance    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-14)    uniswapRouter.swapExactTokensForTokens(        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-15)        amountIn,        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-16)        minAmountOut, // Safe: requires a minimum output        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-17)        path,        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-18)        msg.sender,        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-19)        block.timestamp    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-20)    ); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/#__codelineno-1-21)}`
