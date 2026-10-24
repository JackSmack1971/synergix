---
title: "SC07:2026 Arithmetic Errors (Rounding & Precision)"
source_url: "https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:01.105Z"
---
# SC07:2026 Arithmetic Errors (Rounding & Precision)

## Vulnerability: Arithmetic Errors (Rounding & Precision Loss)[¶](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#vulnerability-arithmetic-errors-rounding-precision-loss "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#description "Permanent link")

Arithmetic errors (rounding and precision loss) describe any situation where a smart contract performs integer-based calculations that produce incorrect or exploitable results due to truncation, scaling, or unit conversion. Smart contracts are limited to integer arithmetic; any division, fixed-point scaling, or conversion between units can lose precision, introduce asymmetric rounding, or—when combined with unchecked blocks or non-EVM semantics—cause overflow/underflow (see SC09).

This affects all contract types that compute numeric values: DeFi (share minting/burning, LP tokens, interest accrual, swap outputs, AMM invariant updates), yield vaults and ERC-4626 (asset/share conversions), rebasing tokens, reward distribution, and NFT/token economics. On non-EVM chains (e.g., Move, Rust-based), integer semantics and available precision differ; similar risks apply wherever arithmetic drives economic outcomes.

Few areas to focus on:

-   **Share and LP token calculations** (deposit/withdraw formulas, rounding direction)
-   **Interest and reward accrual** (compounding, time-weighted averages)
-   **Swap and AMM math** (constant product, concentrated liquidity, output calculations)
-   **Fixed-point and scaling** (1e18, 1e8 conventions, cross-token conversions)
-   **Rebasing and proportional distribution** (per-user vs. global accounting)

Attackers exploit:

-   **Rounding bias** (e.g., rounding that favors depositor or protocol under adversarial sequences)
-   **Repeated small gains** via flash loans (SC04) or high-frequency interactions
-   **Edge cases** (zero total supply, first depositor, extreme ratios) where formulas break down
-   **Precision loss** in multi-step computations that accumulates across operations

When combined with flash loans (SC04) or business logic flaws (SC02), arithmetic errors can be amplified into protocol-draining exploits.

### Example (Vulnerable Share Calculation)[¶](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#example-vulnerable-share-calculation "Permanent link")

`[](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-4)contract VulnerableShares {     [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-5)    uint256 public totalAssets;    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-6)    uint256 public totalShares; [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-7)    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-8)    mapping(address => uint256) public balanceOf; [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-9)    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-10)    function deposit(uint256 assets) external {        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-11)        require(assets > 0, "zero"); [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-12)        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-13)        uint256 shares;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-14)        if (totalShares == 0) {            [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-15)            shares = assets;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-16)        } else {            [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-17)            // Rounds down and may favor the depositor under certain edge states            [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-18)            shares = (assets * totalShares) / totalAssets;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-19)        } [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-20)        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-21)        totalAssets += assets;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-22)        totalShares += shares;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-23)        balanceOf[msg.sender] += shares;    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-24)    } [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-0-25)}`

**Issues:**

-   Rounding always truncates; under adversarial sequences of deposits/withdrawals, this can be gamed.
-   No invariant tests to ensure that total share value remains consistent across edge cases.

### Example (More Robust Arithmetic & Invariant-Aware Design)[¶](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#example-more-robust-arithmetic-invariant-aware-design "Permanent link")

`[](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-4)contract SaferShares {     [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-5)    uint256 public totalAssets;    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-6)    uint256 public totalShares; [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-7)    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-8)    mapping(address => uint256) public balanceOf; [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-9)    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-10)    error ZeroAmount();    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-11)    error InvalidState(); [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-12)    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-13)    function deposit(uint256 assets) external {        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-14)        if (assets == 0) revert ZeroAmount(); [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-15)        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-16)        uint256 shares;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-17)        if (totalShares == 0 || totalAssets == 0) {            [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-18)            // Explicitly define initial conditions            [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-19)            shares = assets;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-20)        } else {            [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-21)            // Use rounding strategy intentionally (up or down) and test it            [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-22)            shares = (assets * totalShares + totalAssets - 1) / totalAssets; // round up        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-23)        } [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-24)        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-25)        uint256 newTotalAssets = totalAssets + assets;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-26)        if (newTotalAssets < totalAssets) revert InvalidState(); // overflow guard [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-27)        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-28)        totalAssets = newTotalAssets;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-29)        totalShares += shares;        [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-30)        balanceOf[msg.sender] += shares;    [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-31)    } [](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#__codelineno-1-32)}`

**Security Improvements:**

-   Explicitly handles initial states and avoids division by zero.
-   Uses a clearly documented rounding strategy (`round up` in this example).
-   Adds overflow checks and custom errors for clarity.

> Real-world protocols should pair such logic with formal reasoning and invariants (e.g., through formal verification or property-based tests).

### 2025 Case Studies[¶](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#2025-case-studies "Permanent link")

-   **zkLend (February 2025, $9.5M loss)**
    A rounding error in the `mint()` function—integer division rounding down—caused a mismatch between recorded and actual values. A withdrawal that should have burned 1.5 tokens rounded down to 1.0, allowing attackers to artificially inflate the lending\_accumulator via repeated deposits/withdrawals and drain ~$9.5M.
-   [https://blog.solidityscan.com/zklend-hack-analysis-e494cb794f71](https://blog.solidityscan.com/zklend-hack-analysis-e494cb794f71)
-   [https://www.halborn.com/blog/post/explained-the-zklend-hack-february-2025](https://www.halborn.com/blog/post/explained-the-zklend-hack-february-2025)

-   **Bunni (September 2025, $8.4M loss)**
    Precision bugs in the withdrawal function's rounding logic. Developers assumed rounding down the idle balance would be "safe," but repeated operations created an exploitable loophole—the attacker decreased USDC balance by 85.7% while only burning 84.4% of liquidity, enabling disproportionate value extraction.

-   [https://www.halborn.com/blog/post/explained-the-bunni-hack-september-2025](https://www.halborn.com/blog/post/explained-the-bunni-hack-september-2025)
-   [https://blog.bunni.xyz/posts/exploit-post-mortem/](https://blog.bunni.xyz/posts/exploit-post-mortem/)
-   [https://cryptotimes.io/2025/09/05/bunni-reveals-code-flaw-behind-8-4-million-exploit](https://cryptotimes.io/2025/09/05/bunni-reveals-code-flaw-behind-8-4-million-exploit)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC07-ArithmeticErrors/#best-practices-mitigations "Permanent link")

-   **Use safe math patterns** (Solidity 0.8+ has built-in checks, but logic around them still matters).
-   Clearly document and test your **rounding strategy**:
-   Decide whether rounding should favor the protocol or users.
-   Prove that repeated interactions cannot create “free value”.
-   Rely on **well-reviewed math libraries** for complex operations:
-   Fixed-point math (e.g., 1e18 scaling)
-   High-precision exponentiation or logarithms
-   Incorporate **invariant checks**:
-   E.g., `totalAssets` vs. sum of user balances, or share/value consistency after operations.
-   Use **fuzz testing and differential testing** to discover edge cases around small/large values and repeated operations.
