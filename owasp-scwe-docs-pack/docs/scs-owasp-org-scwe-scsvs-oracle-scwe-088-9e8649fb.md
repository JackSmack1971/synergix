---
title: "SCWE-088: Improper Decimal Normalization in Price-Based Calculations"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.768Z"
---
*Last updated: August 19, 2026*


# SCWE-088: Improper Decimal Normalization in Price-Based Calculations

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#relationships "Permanent link")

-   **CWE-681**: [Incorrect Conversion between Numeric Types](https://cwe.mitre.org/data/definitions/681.html)
-   **CWE-682**: [Incorrect Calculation](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#description "Permanent link")

This issue arises when smart contracts perform arithmetic involving token values and price feeds without properly aligning decimal places across different sources (e.g. ERC-20 tokens with varying decimals and Chainlink oracles with fixed 8-decimal prices). Failing to normalize decimals before calculations can lead to severely inflated or deflated results, causing users to be overcharged, underpaid, or otherwise economically exploited.

## Impact[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#impact "Permanent link")

Smart contracts often rely on cross-asset conversions, such as paying fees in tokens or using collateralization logic involving price feeds. Improper decimal handling in these calculations may: - Lead to gross overcharging or underpayment. - Introduce systemic financial imbalances in vaults or accounting logic. - Enable economic exploits by arbitraging rounding errors or precision gaps. - Remain undetected during tests if decimals coincidentally align. This issue is especially critical when: - ERC-20 tokens with non-18 decimals (e.g., USDC = 6) are involved. - Chainlink oracles return 8-decimal fixed-point prices. - Arithmetic mixes native ETH values (in 18 decimals) with token values or prices.

* * *

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#remediation "Permanent link")

-   Always normalize decimals across all involved assets and feeds.
-   Use centralized utility functions for all price/token conversions.
-   Add sanity checks to detect outlier results (e.g., revert if output is >1000x expected range).
-   When possible, emit intermediate calculation steps for auditing.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#examples "Permanent link")

-   **❌ Vulnerable Code (Missing Decimal Normalization)**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-0-1)// Assume ETH/USD = 3000e8 (8 decimals), Token/USD = 1e8, and token has 6 decimals [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-0-2)uint256 tokenAmount = (ethAmountInWei * ethPriceInUsd) / tokenPriceInUsd; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-0-3)// Result is in 18-decimal scale, not adjusted for the 6-decimal USDC token`

-   **✅ Safe Code (With Proper Decimal Alignment)**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-1-1)uint8 tokenDecimals = IERC20(token).decimals(); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-1-3)uint256 rawAmount = (ethAmountInWei * ethPriceInUsd) / tokenPriceInUsd; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-1-4)uint256 adjustedAmount = rawAmount / (10 ** (18 - tokenDecimals)); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-1-5)// Now 'adjustedAmount' is in correct units for the target token`


## Realistic Exploit Example[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#realistic-exploit-example "Permanent link")

Assumptions:

##

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-1)Registrar fee = 0.01 ETH = 1e16 wei [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-3)ETH/USD price = 3000 * 1e8 = 300000000000 [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-4)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-5)USDC/USD price = 1 * 1e8 = 100000000 [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-6)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-7)USDC has 6 decimals [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-8)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-9)Faulty Calculation: [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-10)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-11)result = (1e16 * 300000000000) / 100000000 = 3e19 [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-12)return result / 1e6 = 3e13 (30 trillion base units = 30 million USDC) [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-13)Expected: [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-14)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-15)0.01 ETH * $3,000 = $30 [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-16)→ 30 * 1e6 = 30,000,000 USDC units [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-17)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-18)Overcharge: [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-19)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-20)Actual charged: 30,000,000 USDC [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-21)Expected: 30 USDC [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#__codelineno-2-22)Overcharge: 999,900x`

[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/#registrar-fee-001-eth-1e16-wei-ethusd-price-3000-1e8-300000000000-usdcusd-price-1-1e8-100000000-usdc-has-6-decimals-faulty-calculation-result-1e16-300000000000-100000000-3e19-return-result-1e6-3e13-30-trillion-base-units-30-million-usdc-expected-001-eth-3000-30-30-1e6-30000000-usdc-units-overcharge-actual-charged-30000000-usdc-expected-30-usdc-overcharge-999900x "Permanent link")
