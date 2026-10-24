---
title: "SC02:2026 Business Logic Vulnerabilities"
source_url: "https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:00.366Z"
---
# SC02:2026 Business Logic Vulnerabilities

## Vulnerability: Business Logic Vulnerabilities[¶](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#vulnerability-business-logic-vulnerabilities "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#description "Permanent link")

Business logic vulnerabilities describe any situation where a smart contract’s *intended* economic or functional behavior can be subverted even though individual low-level checks (e.g., type safety, reentrancy guards, access control) are correct. These are **design flaws** in how the system’s rules, incentives, state transitions, and invariants are modeled on-chain. Unlike low-level bugs (overflow, reentrancy), business logic flaws arise when the rules themselves are unsafe—the code “does what it says”, but what it says permits exploitable outcomes.

This applies across all smart contract domains: DeFi (lending, AMMs, vaults, yield strategies), NFTs (minting logic, royalties, marketplace mechanics), DAOs (voting, delegation, proposal execution), bridges (burn/mint asymmetry, liquidity rules), gaming (reward distribution, fairness), and cross-chain/L2 systems where multi-hop state transitions create emergent vulnerabilities.

Few areas to focus on:

-   **Invariant violations** across modules (e.g., vault ↔ strategy ↔ gauge, collateral ↔ debt, supply ↔ backing)
-   **Reward and fee logic** (double-counting, under/over-accrual, wrong beneficiary)
-   **Eligibility and limit checks** that are bypassable or inconsistently enforced (borrowing caps, mint limits, liquidation thresholds)
-   **Path-dependent state machines** that allow manipulative action sequences to reach impossible or inconsistent states
-   **Cross-module and cross-chain assumptions** (e.g., bridge liquidity, L2 finality, message ordering)

Attackers exploit:

-   **Arbitrage between inconsistent accounting** (vault vs. strategy, internal vs. external balance)
-   **Order-of-operations edge cases** (deposit/withdraw/claim sequences that break invariants)
-   **Eligibility bypasses** (e.g., claiming rewards without stake, liquidating healthy positions)
-   **Parameter manipulation** (interest curves, fees, collateral factors) that create economically irrational states

### Example (Vulnerable Lending Logic)[¶](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#example-vulnerable-lending-logic "Permanent link")

`[](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-4)contract VulnerableLending {     [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-5)    mapping(address => uint256) public collateral;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-6)    mapping(address => uint256) public debt;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-7)    uint256 public collateralFactorBps = 7500; // 75% [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-8)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-9)    function depositCollateral() external payable {        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-10)        collateral[msg.sender] += msg.value;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-11)    } [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-12)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-13)    // Vulnerable: calculates borrow capacity using the *new* amount, not total    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-14)    function borrow(uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-15)        uint256 allowed = (amount * collateralFactorBps) / 10_000;        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-16)        require(allowed >= amount, "not enough collateral"); // meaningless check [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-17)        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-18)        debt[msg.sender] += amount;        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-19)        // send tokens from pool (omitted)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-20)    } [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-0-21)}`

**Issues:**

-   `allowed` is computed from the *requested borrow amount*, not the user’s collateral balance.
-   The check `allowed >= amount` always holds for `collateralFactorBps >= 10_000`, and is otherwise simply a tautology when misused like this, failing to enforce any economic invariant.

### Example (Fixed: Invariant-Based Borrow Logic)[¶](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#example-fixed-invariant-based-borrow-logic "Permanent link")

`[](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-4)interface IPriceOracle {     [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-5)    function getCollateralPrice() external view returns (uint256); // 1e18 [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-6)} [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-7)[](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-8)contract SaferLending {     [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-9)    mapping(address => uint256) public collateral;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-10)    mapping(address => uint256) public debt;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-11)    uint256 public collateralFactorBps = 7500; // 75%    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-12)    IPriceOracle public oracle; [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-13)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-14)    constructor(IPriceOracle _oracle) {        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-15)        oracle = _oracle;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-16)    } [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-17)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-18)    function depositCollateral() external payable {        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-19)        require(msg.value > 0, "no collateral");        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-20)        collateral[msg.sender] += msg.value;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-21)    } [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-22)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-23)    function _maxBorrow(address user) internal view returns (uint256) {        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-24)        uint256 price = oracle.getCollateralPrice(); // e.g. ETH price in USD 1e18        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-25)        uint256 collateralUsd = (collateral[user] * price) / 1e18;        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-26)        return (collateralUsd * collateralFactorBps) / 10_000;    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-27)    } [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-28)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-29)    function borrow(uint256 amountUsd) external {        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-30)        uint256 maxBorrowUsd = _maxBorrow(msg.sender);        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-31)        require(debt[msg.sender] + amountUsd <= maxBorrowUsd, "exceeds limit"); [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-32)        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-33)        debt[msg.sender] += amountUsd;        [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-34)        // transfer stablecoin from pool (omitted)    [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-35)    } [](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#__codelineno-1-36)}`

**Security Improvements:**

-   Borrow limits derive from **total collateral**, not just requested amounts.
-   Economic invariant: `debt[user] <= maxBorrow(user)` is enforced on every borrow.
-   Price oracle is explicitly integrated (and can be hardened per SC03).

### 2025 Case Studies[¶](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#2025-case-studies "Permanent link")

-   **Abracadabra (March 2025, $12.9M loss)**
    Flawed collateral accounting in GMX V2 CauldronV4 contracts. Attackers used a three-stage method: (1) made a deposit into GMX designed to fail, leaving tokens stuck in OrderAgent; (2) self-liquidated their position so the contract erased the position but failed to remove the associated order and collateral; (3) used the "ghost" collateral to borrow 6,260 ETH (~$12.9M). Economic invariants (collateral ↔ debt) were broken by the deposit-fail and liquidation path.
    Key lessons:
-   All economic invariants (e.g., minimum collateralization, max LTV) must be **provable and enforced** on every state transition.
-   Introducing new spell/strategy types must go through **formal review** of how they interact with the existing system.
-   [https://blog.solidityscan.com/abracadabra-hack-analysis-f2efcdee9c05](https://blog.solidityscan.com/abracadabra-hack-analysis-f2efcdee9c05)
-   [https://www.halborn.com/blog/post/explained-the-abracadabra-money-hack-march-2025](https://www.halborn.com/blog/post/explained-the-abracadabra-money-hack-march-2025)
-   [https://www.coindesk.com/business/2025/03/25/abracadabra-drained-of-usd13m-in-exploit-targeting-cauldrons-tied-to-gmx-liquidity-tokens](https://www.coindesk.com/business/2025/03/25/abracadabra-drained-of-usd13m-in-exploit-targeting-cauldrons-tied-to-gmx-liquidity-tokens)
-   [https://threesigma.xyz/blog/exploit/abracadabra-gmx-defi-exploit-explained](https://threesigma.xyz/blog/exploit/abracadabra-gmx-defi-exploit-explained)

-   **Yearn Finance (November 2025, $9M loss)**
    A design flaw in the yETH weighted stableswap pool's fixed-point iteration solver. By performing highly imbalanced add/remove liquidity operations, attackers forced the solver into a divergent regime, causing the product term (Π) to collapse to zero—converting the pool from a hybrid stableswap invariant to a constant-sum curve. This allowed minting ~2.35×10⁵⁶ yETH LP tokens without collateral and draining the pool. The vulnerability was **invariant collapse**, not reentrancy or low-level bugs.
    Key lessons:

-   Reward and fee distribution paths must be **simulation-tested** across adversarial scenarios.
-   Yield strategies should have **clear, testable invariants** (e.g., no user can claim more rewards than their fair share over time).
-   [https://defimon.xyz/blog/yearn-yeth-hack-november-2025](https://defimon.xyz/blog/yearn-yeth-hack-november-2025)
-   [https://www.cryptopolitan.com/yearn-finance-begins-clawback-after-9m-hack/](https://www.cryptopolitan.com/yearn-finance-begins-clawback-after-9m-hack/)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC02-BusinessLogicVulnerabilities/#best-practices-mitigations "Permanent link")

-   **Model protocol economics explicitly** (e.g., with adversarial simulations / agent-based models) rather than relying on intuition.
-   Express **core invariants in code and tests**:
-   “Total value withdrawn cannot exceed total deposits + realized yield”
-   “Rewards distribution is proportional to time-weighted stake”
-   “Liquidations never result in protocol loss under honest oracle data”
-   Use **formal verification and property-based fuzzing** for key accounting paths (vaults, strategies, reward distribution).
-   **Version and gate new strategies / spells**:
-   Roll out behind caps.
-   Monitor metrics and on-chain invariants before raising limits.
-   Ensure **governance and operations teams understand invariants**, not just auditors.
