---
title: "SC03:2026 Price Oracle Manipulation"
source_url: "https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:00.519Z"
---
# SC03:2026 Price Oracle Manipulation

## Vulnerability: Price Oracle Manipulation[¶](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#vulnerability-price-oracle-manipulation "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#description "Permanent link")

Price oracle manipulation describes any situation where a smart contract relies on price or valuation data that can be **directly or indirectly influenced by an attacker**, causing the protocol to make decisions based on incorrect values. Oracles are trust boundaries: the contract implicitly trusts that the price it receives reflects real-world or on-chain market conditions. When that trust is violated—whether by manipulation, staleness, or misconfiguration—protocol behavior is distorted.

This affects all contract types that consume price data: DeFi lending and borrowing (collateral valuation, liquidation), AMMs and DEXes (spot and TWAP-based pricing), yield vaults (NAV calculations, share valuation), liquid staking and derivatives (ETH/stake price feeds), NFT and token valuations (floor price oracles), and cross-chain bridges (asset pricing for mint/burn ratios). On non-EVM chains (e.g., Move, Solana), similar patterns apply wherever external price sources feed into on-chain logic.

Few areas to focus on:

-   **DEX-based oracles** (spot price, TWAP, geometric mean) and resistance to flash loans, JIT liquidity, or concentrated liquidity skew
-   **Off-chain and hybrid feeds** (Chainlink, Pyth, custom relayers) and assumptions about freshness, deviation, and multi-source aggregation
-   **Liquidity and market depth** of the underlying price source (thin pools vs. deep markets)
-   **Cross-chain and L2 pricing** (finality delays, sequencer ordering, message relay assumptions)

Attackers exploit:

-   **Spot price manipulation** via large trades, flash loans, or JIT liquidity in the same block
-   **TWAP manipulation** over short windows or during low-liquidity periods
-   **Stale or stuck data** when contracts do not enforce freshness or fallback behavior
-   **Deviation and outlier handling** when aggregation logic fails to reject manipulated inputs

### Example (Vulnerable Oracle Usage)[¶](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#example-vulnerable-oracle-usage "Permanent link")

`[](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-4)interface IPriceFeed {     [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-5)    function latestAnswer() external view returns (int256); [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-6)} [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-7)[](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-8)contract VulnerableOracleLending {     [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-9)    IPriceFeed public priceFeed; // single-point oracle    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-10)    mapping(address => uint256) public collateralEth;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-11)    mapping(address => uint256) public debtUsd; [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-12)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-13)    constructor(IPriceFeed _feed) {        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-14)        priceFeed = _feed;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-15)    } [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-16)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-17)    function depositCollateral() external payable {        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-18)        collateralEth[msg.sender] += msg.value;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-19)    } [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-20)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-21)    function borrow(uint256 amountUsd) external {        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-22)        int256 price = priceFeed.latestAnswer(); // no sanity checks, no delay        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-23)        require(price > 0, "bad price"); [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-24)        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-25)        uint256 collateralUsd = (collateralEth[msg.sender] * uint256(price)) / 1e8;        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-26)        // Allows borrowing up to 100% of collateral value – overly generous        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-27)        require(collateralUsd >= amountUsd, "insufficient collateral"); [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-28)        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-29)        debtUsd[msg.sender] += amountUsd;        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-30)        // transfer stablecoin (omitted)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-31)    } [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-0-32)}`

**Issues:**

-   Single oracle source, no aggregation or sanity checks.
-   No upper/lower bounds or deviation checks against past values.
-   Economic parameters (100% LTV) make even minor manipulations profitable.

### Example (Hardened Oracle Integration)[¶](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#example-hardened-oracle-integration "Permanent link")

`[](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-4)interface IAggregatorV3 {     [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-5)    function latestRoundData()        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-6)        external        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-7)        view        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-8)        returns (            [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-9)            uint80 roundId,            [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-10)            int256 answer,            [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-11)            uint256 startedAt,            [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-12)            uint256 updatedAt,            [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-13)            uint80 answeredInRound        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-14)        ); [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-15)} [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-16)[](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-17)contract RobustOracleLending {     [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-18)    IAggregatorV3 public immutable priceFeed;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-19)    mapping(address => uint256) public collateralEth;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-20)    mapping(address => uint256) public debtUsd; [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-21)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-22)    uint256 public constant MAX_DELAY = 1 hours;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-23)    uint256 public constant COLLATERAL_FACTOR_BPS = 7500; // 75% [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-24)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-25)    constructor(IAggregatorV3 _feed) {        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-26)        priceFeed = _feed;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-27)    } [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-28)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-29)    function _getSafePrice() internal view returns (uint256) {        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-30)        (, int256 answer, , uint256 updatedAt, uint80 answeredInRound) =            [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-31)            priceFeed.latestRoundData();        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-32)        require(answer > 0, "bad answer");        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-33)        require(updatedAt != 0 && block.timestamp - updatedAt <= MAX_DELAY, "stale price");        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-34)        require(answeredInRound != 0, "incomplete round");        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-35)        return uint256(answer);    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-36)    } [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-37)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-38)    function depositCollateral() external payable {        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-39)        require(msg.value > 0, "no collateral");        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-40)        collateralEth[msg.sender] += msg.value;    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-41)    } [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-42)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-43)    function borrow(uint256 amountUsd) external {        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-44)        uint256 price = _getSafePrice();        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-45)        uint256 collateralUsd = (collateralEth[msg.sender] * price) / 1e8;        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-46)        uint256 maxBorrow = (collateralUsd * COLLATERAL_FACTOR_BPS) / 10_000;        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-47)        require(debtUsd[msg.sender] + amountUsd <= maxBorrow, "exceeds limit"); [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-48)        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-49)        debtUsd[msg.sender] += amountUsd;        [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-50)        // transfer stablecoin (omitted)    [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-51)    } [](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#__codelineno-1-52)}`

**Security Improvements:**

-   Uses a price feed interface with **round metadata** to reject stale or incomplete data.
-   Applies conservative **collateral factors** and explicit borrowing limits.
-   Encapsulates price fetch and validation in `_getSafePrice`, making reasoning and testing easier.

In 2025, pure oracle-only mega-exploits were less frequent, but oracle manipulation was often one component in **multi-vector attacks**.

### 2025 Case Studies[¶](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#2025-case-studies "Permanent link")

-   **NGP Token (September 2025, ~$2M loss)**
    The protocol's `getPrice()` function relied solely on DEX pair (Uniswap V2/PancakeSwap) reserve balances to calculate token price. Attackers used a flash loan to swap large amounts and manipulate reserves, skewing the oracle to show artificially low values, then bypassed purchase limits and cooldown protections to drain ~$2M. Oracle manipulation was the **root cause**.
-   [https://blog.solidityscan.com/ngp-token-hack-analysis-414b6ca16d96](https://blog.solidityscan.com/ngp-token-hack-analysis-414b6ca16d96)
-   [https://hacken.io/insights/ngp-hack-explained/](https://hacken.io/insights/ngp-hack-explained/)
-   [https://coincentral.com/flash-loan-exploit-drains-2-million-from-ngp-token-on-bnb-chain/](https://coincentral.com/flash-loan-exploit-drains-2-million-from-ngp-token-on-bnb-chain/)

-   **GMX (July 2025, $42M loss)**
    While the primary root cause was reentrancy in `executeDecreaseOrder`, the attack flow involved **price feed manipulation** in conjunction: the attacker manipulated global average short price for Bitcoin downward (~57×), then used a flash loan to purchase GLP at artificially low prices and redeem at inflated prices. Oracle/pricing was a key **enabler** of the exploit.

-   [https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f](https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f)
-   [https://www.halborn.com/blog/post/explained-the-gmx-hack-july-2025](https://www.halborn.com/blog/post/explained-the-gmx-hack-july-2025)
-   [https://blog.verichains.io/p/gmx-42m-exploit-root-cause-analysis](https://blog.verichains.io/p/gmx-42m-exploit-root-cause-analysis)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC03-PriceOracleManipulation/#best-practices-mitigations "Permanent link")

-   **Aggregate multiple sources**:
-   Use median/mean of several DEXs / oracles.
-   Reject outliers and anomalous deviations.
-   **Time-based defenses**:
-   Use TWAPs over sufficient windows to resist short-lived manipulations.
-   Reject prices older than a maximum staleness threshold.
-   **Liquidity-aware design**:
-   Avoid basing core prices on **illiquid pools**.
-   Cap impact of a single pool/feed on global pricing.
-   **Fail-safe behavior**:
-   On suspicious or unavailable data, **halt sensitive operations** (borrowing, liquidations).
-   Use circuit breakers and rate limiting on parameter changes.
-   **Monitoring & alerting**:
-   Track price deviations between your oracle and reference markets.
-   Set automated alerts for out-of-band movements or stuck oracles.
