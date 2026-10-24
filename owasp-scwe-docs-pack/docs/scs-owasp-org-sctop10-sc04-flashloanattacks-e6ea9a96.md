---
title: "SC04:2026 Flash Loan–Facilitated Attacks"
source_url: "https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:00.636Z"
---
# SC04:2026 Flash Loan–Facilitated Attacks

## Vulnerability: Flash Loan–Facilitated Attacks[¶](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#vulnerability-flash-loanfacilitated-attacks "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#description "Permanent link")

Flash loan–facilitated attacks describe exploits where an attacker uses **uncollateralized, same-transaction borrowing** (flash loans) to amplify an underlying vulnerability into a profitable, protocol-draining attack. Flash loans are not inherently vulnerable—they are a legitimate DeFi primitive—but they grant attackers arbitrarily large, transient capital within a single transaction. Any protocol that makes trust assumptions based on *capital at risk* or *historical position size* is exposed when an attacker can temporarily hold massive balances without putting their own funds at risk.

This affects all contract types that assume economic constraints or proportional exposure: lending protocols (governance vote weight, liquidation thresholds, collateral ratios), AMMs (share minting, arbitrage, oracle skew), yield vaults (deposit/withdraw/share accounting), governance (vote buying, flash-loan governance attacks), NFT and token valuation (floor price, collateral valuation), and cross-protocol composability where one contract’s state is influenced by another’s liquidity. On non-EVM chains, similar concepts exist (e.g., transient large positions within a single block or batch).

Few areas to focus on:

-   **Governance and voting** (flash-loan vote buying, snapshot manipulation)
-   **Oracle and pricing** (manipulating DEX/TWAP feeds with borrowed liquidity)
-   **Share and accounting logic** (rounding, proportional calculations that assume bounded input)
-   **Liquidation and collateral checks** (position size–dependent thresholds)
-   **Composability** (protocols that trust caller balance or pool state in a single transaction)

Attackers construct batched transactions that:

1.  Borrow large capital via flash loan (Aave, dYdX, Uniswap V3 flash, or equivalent).
2.  Manipulate protocol state, prices, or accounting using the borrowed funds.
3.  Extract profit (drain liquidity, take under-collateralized loans, skew governance).
4.  Repay the flash loan in the same transaction, keeping the profit.

When underlying weaknesses in business logic (SC02), oracles (SC03), arithmetic (SC07), or access control (SC01) exist, flash loans act as a **force multiplier**, turning small bugs into catastrophic exploits.

### Example (Vulnerable Use of Flash Loans with Rounding Bug)[¶](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#example-vulnerable-use-of-flash-loans-with-rounding-bug "Permanent link")

`[](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-4)interface IFlashLender {     [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-5)    function flashLoan(        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-6)        address receiver,        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-7)        uint256 amount,        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-8)        bytes calldata data    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-9)    ) external; [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-10)} [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-11)[](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-12)contract VulnerablePool {     [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-13)    uint256 public totalShares;    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-14)    uint256 public totalAssets; [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-15)    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-16)    mapping(address => uint256) public sharesOf; [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-17)    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-18)    // Vulnerable: naive share minting with truncation benefit to sender    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-19)    function deposit(uint256 assets) external {        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-20)        uint256 shares;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-21)        if (totalShares == 0) {            [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-22)            shares = assets;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-23)        } else {            [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-24)            shares = (assets * totalShares) / totalAssets;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-25)        } [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-26)        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-27)        totalAssets += assets;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-28)        totalShares += shares;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-29)        sharesOf[msg.sender] += shares;    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-30)    } [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-31)    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-32)    // No safeguard against flash-loan boosted deposit/withdraw loops [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-0-33)}`

**Issues:**

-   Rounding always truncates in favor of the protocol, but with repeated flash-loan-driven cycles, a mis-tuned formula or mis-accounted state can be turned into a net gain for an attacker.
-   No consideration for **max slippage, caps, or frequency** of operations, making repeated high-volume operations feasible.

### Example (Mitigated Design Considerations)[¶](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#example-mitigated-design-considerations "Permanent link")

`[](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-4)contract SaferPool {     [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-5)    uint256 public totalShares;    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-6)    uint256 public totalAssets;    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-7)    uint256 public lastUpdateBlock; [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-8)    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-9)    mapping(address => uint256) public sharesOf; [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-10)    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-11)    error TooFrequentInteraction(); [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-12)    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-13)    modifier rateLimited() {        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-14)        // Simple example: limit high-impact operations to once per block        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-15)        if (lastUpdateBlock == block.number) revert TooFrequentInteraction();        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-16)        _;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-17)        lastUpdateBlock = block.number;    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-18)    } [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-19)    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-20)    function deposit(uint256 assets) external rateLimited {        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-21)        require(assets > 0, "zero assets"); [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-22)        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-23)        uint256 shares;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-24)        if (totalShares == 0) {            [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-25)            shares = assets;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-26)        } else {            [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-27)            // Use rounding that errs in favor of the protocol and is formally analyzed            [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-28)            shares = (assets * totalShares + totalAssets - 1) / totalAssets;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-29)        } [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-30)        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-31)        totalAssets += assets;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-32)        totalShares += shares;        [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-33)        sharesOf[msg.sender] += shares;    [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-34)    } [](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#__codelineno-1-35)}`

**Security Improvements:**

-   Introduces **basic rate limiting** to reduce susceptibility to rapid flash-loan loops.
-   Uses a more conservative, explicitly documented rounding strategy.
-   Encourages formal analysis of share/accounting formulas and invariants.

> Note: Real protocols should use stronger defense-in-depth mechanisms rather than relying solely on per-block limits.

### 2025 Case Studies[¶](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#2025-case-studies "Permanent link")

-   **Bunni (September 2025, $8.4M loss)**
    A rounding error in the withdrawal function was amplified by flash loans. Attackers flash-borrowed 3M USDT, pushed the pool's spot price to extremes (USDC active balance to 28 wei), then executed 44 chained tiny withdrawals exploiting rounding—decreasing USDC balance by 85.7% while only burning 84.4% of liquidity. Flash loans enabled the capital scale required.
-   [https://www.halborn.com/blog/post/explained-the-bunni-hack-september-2025](https://www.halborn.com/blog/post/explained-the-bunni-hack-september-2025)
-   [https://blog.bunni.xyz/posts/exploit-post-mortem/](https://blog.bunni.xyz/posts/exploit-post-mortem/)
-   [https://cryptorank.io/news/feed/27dc8-bunni-hit-by-8-4m-flash-loan-exploit-rounding-error-blamed](https://cryptorank.io/news/feed/27dc8-bunni-hit-by-8-4m-flash-loan-exploit-rounding-error-blamed)

-   **zkLend (February 2025, $9.5M loss)**
    A rounding error in the `mint()` function (integer division rounding down) allowed attackers to inflate the lending\_accumulator via repeated deposits/withdrawals. Flash loans scaled the position—turning small per-iteration precision gains into a ~$9.5M drain. Flash loans were the **force multiplier**.

-   [https://blog.solidityscan.com/zklend-hack-analysis-e494cb794f71](https://blog.solidityscan.com/zklend-hack-analysis-e494cb794f71)
-   [https://www.halborn.com/blog/post/explained-the-zklend-hack-february-2025](https://www.halborn.com/blog/post/explained-the-zklend-hack-february-2025)
-   [https://zircon.tech/blog/the-9-5m-zklend-hack-another-defi-security-wake-up-call/](https://zircon.tech/blog/the-9-5m-zklend-hack-another-defi-security-wake-up-call/)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC04-FlashLoanAttacks/#best-practices-mitigations "Permanent link")

-   **Assume flash loans exist**: design economic and accounting logic on the assumption that arbitrarily large, transient capital is available to attackers.
-   **Rate limit sensitive operations**:
-   Per-block or per-epoch limits on rebasing, rebalancing, or high-impact state transitions.
-   Dynamic fees that increase with the magnitude/frequency of actions.
-   **Cap exposure per interaction**:
-   Set maximum slippage, max position sizes, and borrowing caps.
-   Limit how much state can change in a single transaction.
-   **Simulate flash loan scenarios**:
-   Include flash-loan-style tests in QA and audits.
-   Use fuzzing to discover profitable multi-call sequences.
-   **Combine with strong oracles and logic**:
-   Flash loans are usually the *multiplier*; underlying issues (SC02, SC03, SC07) must be fixed at the root.
