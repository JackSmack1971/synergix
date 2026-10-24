---
title: "SC09:2026 Integer Overflow and Underflow"
source_url: "https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:01.394Z"
---
# SC09:2026 Integer Overflow and Underflow

## Vulnerability: Integer Overflow and Underflow[¶](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#vulnerability-integer-overflow-and-underflow "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#description "Permanent link")

Integer overflow and underflow describe situations where arithmetic operations produce values outside the representable range of the operand type. In Solidity 0.8+, arithmetic is **checked by default** and reverts on overflow/underflow. However, explicit `unchecked` blocks, assembly, or custom libraries can disable these checks. On non-EVM platforms (e.g., Move, Sui, Solana, Rust-based chains), default overflow semantics differ—some wrap silently, some abort—and incorrect assumptions or flawed custom checks can lead to wrapped values, miscomputed balances, and broken invariants.

This affects all contract types that perform arithmetic: DeFi (pool invariants, balances, interest, shares), NFTs (supply, token IDs), bridges (amounts, sequence numbers), and any logic involving large or user-controlled numeric inputs. The impact is especially severe when overflow/underflow breaks economic invariants (e.g., k = x \* y in AMMs) or enables balance manipulation.

Few areas to focus on:

-   **EVM/Solidity** (use of `unchecked`, assembly, pre-0.8 codebases)
-   **Non-EVM chains** (Move, Sui, Aptos, Solana, etc.) and their default overflow semantics
-   **Multiplication and exponentiation** (high risk of overflow with large operands)
-   **Subtraction and decrement** (underflow when subtrahend > minuend)
-   **Casting and type conversion** (downcasting uint256 to uint128, etc.)

Attackers exploit:

-   **Unchecked blocks** in Solidity where overflow/underflow is assumed impossible but edge cases exist
-   **Non-EVM semantics** where silent wrap or custom checks can be bypassed
-   **Large or crafted inputs** that trigger overflow in multiplication or addition chains
-   **Invariant-breaking values** (e.g., overflow producing a small k that passes naive checks)

### Example 1: Solidity Pre-0.8 Overflow (EVM)[¶](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#example-1-solidity-pre-08-overflow-evm "Permanent link")

In Solidity versions **before 0.8.0**, arithmetic overflow and underflow occurred **silently**—no revert, no error. Values wrapped around (e.g., `uint8` 255 + 1 = 0). Solidity 0.8.0+ fixes this by default; overflow/underflow reverts unless explicitly wrapped in `unchecked`.

**Vulnerable (Solidity 0.7.x):**

`[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-2)pragma solidity ^0.7.6; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-4)contract VulnerableToken {     [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-5)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-6)    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-7)    function transfer(address to, uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-8)        // UNDERFLOW: if balances[msg.sender] < amount, wraps to huge value        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-9)        balances[msg.sender] -= amount;  // Silent underflow!        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-10)        balances[to] += amount;          // Silent overflow possible    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-11)    } [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-0-12)}`

**Fixed (Option A—SafeMath for 0.7.x):**

`[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-2)pragma solidity ^0.7.6; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-4)import "@openzeppelin/contracts/utils/math/SafeMath.sol"; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-5)[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-6)contract SafeToken {     [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-7)    using SafeMath for uint256;    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-8)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-9)    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-10)    function transfer(address to, uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-11)        balances[msg.sender] = balances[msg.sender].sub(amount);  // Reverts on underflow        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-12)        balances[to] = balances[to].add(amount);                   // Reverts on overflow    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-13)    } [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-1-14)}`

**Fixed (Option B—Upgrade to Solidity 0.8+):**

`[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-3)[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-4)contract SafeToken {     [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-5)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-6)    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-7)    function transfer(address to, uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-8)        balances[msg.sender] -= amount;  // Reverts on underflow (checked by default)        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-9)        balances[to] += amount;          // Reverts on overflow    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-10)    } [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-2-11)}`

**Key takeaway:** Solidity 0.8.0+ provides built-in overflow/underflow checks. Use `unchecked` only when you have strong guarantees; otherwise prefer checked arithmetic.

* * *

### Example 2: Cetus Protocol—Sui/Move (Non-EVM)[¶](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#example-2-cetus-protocolsuimove-non-evm "Permanent link")

On **May 22, 2025**, Cetus Protocol (largest DEX on Sui) lost ~$223M due to a flawed overflow check in the `integer-mate` library. In **Move**, addition and multiplication abort on overflow, but **left shift (`<<`) does NOT abort**—it truncates silently. The protocol used a custom `checked_shlw` to guard a `<< 64` shift; the guard was wrong.

**Root cause:** `checked_shlw` in `math_u256.move` used an incorrect threshold. It should reject values with any non-zero bits in the top 64 bits (i.e., `n >= 1 << 192`). The implementation used `n > (0xFFFFFFFFFFFFFFFF << 192)` instead, which is wrong and allowed values ≥ 2^192 to pass, then overflow on `n << 64`.

**Vulnerable `checked_shlw` (integer-mate, Sui Move):**

`[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-1)// integer-mate/sui/sources/math_u256.move [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-2)// VULNERABLE: incorrect overflow threshold [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-3)public fun checked_shlw(n: u256): (u256, bool) {     [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-4)    let mask = 0xFFFFFFFFFFFFFFFF << 192;  // WRONG! Produces wrong threshold    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-5)    if (n > mask) {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-6)        (0, true)   // Should signal overflow    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-7)    } else {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-8)        ((n << 64), false)  // Overflow occurs here for n >= 2^192—Move truncates silently    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-9)    } [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-3-10)}`

**Fixed `checked_shlw`:**

`[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-1)// FIXED: correct overflow check—reject if any bits in top 64 bits [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-2)public fun checked_shlw(n: u256): (u256, bool) {     [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-3)    // Correct: shifting left by 64 overflows if n >= 2^192    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-4)    if (n >= 1 << 192) {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-5)        (0, true)   // Overflow—abort path    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-6)    } else {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-7)        ((n << 64), false)    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-8)    } [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-4-9)}`

**Where it was used:** The CLMM function `get_delta_a` in `clmm_math.move` computed token A required for a liquidity position. It called:

`[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-5-1)let (numerator, overflowing) = math_u256::checked_shlw(     [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-5-2)    full_math_u128::full_mul(liquidity, sqrt_price_diff) [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-5-3)); [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-5-4)assert!(!overflowing);  // Assertion passed incorrectly due to flawed check`

With `liquidity ≈ 2^113` and `sqrt_price_diff ≈ 2^79`, the product was `≈ 2^192 + ε`. The flawed `checked_shlw` allowed it through; `n << 64` overflowed and truncated to a tiny value. The protocol then computed that only **1 unit** of token A was needed to mint massive liquidity (~10^37 units), enabling the drain.

**Attack flow (simplified):** Flash swap → open narrow tick position → call `add_liquidity` with crafted liquidity parameter → undercharged (1 token) while credited huge liquidity → remove liquidity → drain pools → repay flash swap.

* * *

### Example 3: Solidity 0.8+ with `unchecked` (Explicit Opt-Out)[¶](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#example-3-solidity-08-with-unchecked-explicit-opt-out "Permanent link")

Even on Solidity 0.8+, `unchecked` disables checks. Use only when overflow/underflow is provably impossible:

`[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-3)[](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-4)contract UncheckedExample {     [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-5)    function bad(uint256 x, uint256 y) external pure returns (uint256) {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-6)        unchecked {            [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-7)            return x * y;  // Can overflow; no revert        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-8)        }    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-9)    } [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-10)    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-11)    function good(uint256 x) external pure returns (uint256) {        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-12)        unchecked {            [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-13)            return x - 1;  // Safe only if caller ensures x >= 1        [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-14)        }    [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-15)    } [](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#__codelineno-6-16)}`

**Avoid `unchecked`** for user-controlled or unbounded inputs unless you have formal reasoning or tests proving safety.

* * *

### 2025 Case Study: Cetus (May 2025, $223M loss)[¶](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#2025-case-study-cetus-may-2025-223m-loss "Permanent link")

Cetus Protocol on Sui was exploited via a flawed `checked_shlw` in the shared `integer-mate` library. The function was meant to prevent u256 overflow when shifting left by 64 bits during CLMM liquidity calculations. The overflow check used the wrong threshold (`0xFFFFFFFFFFFFFFFF << 192` instead of `1 << 192`), allowing values ≥ 2^192 to pass. In Move, left shift does not abort on overflow—it truncates. The truncated numerator caused `get_delta_a` to return that only 1 token was required to mint enormous liquidity. Attackers repeated this across pools using flash swaps, draining ~$223M. Key lessons: (1) Move shift operations do not abort on overflow; (2) custom overflow guards must be rigorously verified; (3) shared math libraries are high-risk and need formal analysis.
\- [https://dedaub.com/blog/the-cetus-amm-200m-hack-how-a-flawed-overflow-check-led-to-catastrophic-loss/](https://dedaub.com/blog/the-cetus-amm-200m-hack-how-a-flawed-overflow-check-led-to-catastrophic-loss/) - [https://www.cyfrin.io/blog/inside-the-223m-cetus-exploit-root-cause-and-impact-analysis](https://www.cyfrin.io/blog/inside-the-223m-cetus-exploit-root-cause-and-impact-analysis) - [https://www.halborn.com/blog/post/explained-the-cetus-hack-may-2025](https://www.halborn.com/blog/post/explained-the-cetus-hack-may-2025) - [https://blog.verichains.io/p/cetus-protocol-hacked-analysis](https://blog.verichains.io/p/cetus-protocol-hacked-analysis)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC09-IntegerOverflowUnderflow/#best-practices-mitigations "Permanent link")

-   On Solidity/EVM:
-   **Avoid `unchecked`** arithmetic unless you have strong reasons and tests proving safety.
-   Use explicit checks and custom errors for critical invariants.
-   Favor well-reviewed math libraries (for fixed-point, exponentiation, etc.).
-   On non-EVM environments (e.g., Move, Rust-based chains):
-   Understand the language’s **default overflow semantics**.
-   Use safe arithmetic constructs or libraries where available.
-   Add **assertions and invariants** around critical arithmetic.
-   Test with **extreme value ranges**:
-   Minimum and maximum values for all numeric types.
-   Fuzz tests that target edge cases (near boundaries where overflow/underflow is likely).
