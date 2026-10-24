---
title: "SC06:2026 Unchecked External Calls"
source_url: "https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:00.958Z"
---
# SC06:2026 Unchecked External Calls

## Vulnerability: Unchecked External Calls[¶](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#vulnerability-unchecked-external-calls "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#description "Permanent link")

Unchecked external calls describe any situation where a smart contract invokes another contract or address (via `call`, `delegatecall`, `staticcall`, or high-level calls like `transfer`/`send`) **without fully accounting for** the callee’s behavior, return value, or reentrancy potential. The calling contract implicitly trusts that the callee will behave as expected—returning success, not re-entering, and not executing arbitrary logic. When that assumption is violated, the caller can be left in an inconsistent state or exploited.

This affects all contract types that perform external interactions: DeFi (token transfers, DEX swaps, vault deposits, flash loan callbacks), NFTs (transfers with hooks, marketplace payouts), DAOs (execution of proposal calldata), bridges (message relay, asset transfers), and composable protocols (arbitrary callbacks, ERC-777/ERC-721/ERC-1155 receiver hooks, ERC-4626 deposit/withdraw hooks). On non-EVM chains, analogous patterns exist (e.g., Move’s `vector::borrow`, Solana CPI) where cross-program invocations can re-enter or behave unexpectedly.

Few areas to focus on:

-   **Token transfers** (ERC-20, ERC-721, ERC-1155) and non-standard return values or reverting behavior
-   **Callback and hook interfaces** (ERC-777 `tokensReceived`, ERC-4626 `afterDeposit`/`beforeWithdraw`, `onFlashLoan`, `onERC721Received`)
-   **Low-level calls** (`call`, `delegatecall`, `callcode`) and gas/storage implications
-   **Composability flows** (vault calling strategy, strategy calling DEX) where reentrancy can cross multiple contracts

Attackers exploit:

-   **Reentrancy** by implementing malicious logic in callbacks or in tokens that hook into transfers (see SC08)
-   **Silent failures** when return values are ignored (e.g., non-returning ERC-20s) and state is left inconsistent
-   **Unexpected code execution** when calling user-supplied or protocol-configurable addresses

Unchecked external calls are rarely the *sole* root cause but are a **critical enabler** for reentrancy (SC08), business logic exploits (SC02), and accounting inconsistencies.

### Example (Vulnerable Unchecked Call Pattern)[¶](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#example-vulnerable-unchecked-call-pattern "Permanent link")

`[](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-4)interface IToken {     [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-5)    function transfer(address to, uint256 amount) external returns (bool); [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-6)} [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-7)[](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-8)contract VulnerablePayout {     [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-9)    IToken public token; [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-10)    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-11)    mapping(address => uint256) public rewards; [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-12)    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-13)    constructor(IToken _token) {        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-14)        token = _token;    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-15)    } [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-16)    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-17)    function claim() external {        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-18)        uint256 amount = rewards[msg.sender];        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-19)        require(amount > 0, "no rewards"); [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-20)        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-21)        // Vulnerable: does not check return value or reentrancy        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-22)        token.transfer(msg.sender, amount); [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-23)        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-24)        // State update after external call        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-25)        rewards[msg.sender] = 0;    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-26)    } [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-0-27)}`

**Issues:**

-   The `transfer` call’s return value is ignored; if transfer fails, rewards remain non-zero but the user did not receive tokens.
-   State is updated **after** the external call, opening reentrancy possibilities (if the token is malicious).

### Example (Hardened External Call Handling)[¶](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#example-hardened-external-call-handling "Permanent link")

`[](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-4)interface ISafeToken {     [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-5)    function transfer(address to, uint256 amount) external returns (bool); [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-6)} [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-7)[](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-8)contract SafePayout {     [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-9)    ISafeToken public immutable token;    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-10)    mapping(address => uint256) public rewards; [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-11)    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-12)    error NoRewards();    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-13)    error TransferFailed(); [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-14)    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-15)    constructor(ISafeToken _token) {        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-16)        token = _token;    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-17)    } [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-18)    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-19)    function claim() external {        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-20)        uint256 amount = rewards[msg.sender];        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-21)        if (amount == 0) revert NoRewards(); [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-22)        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-23)        // Move state change *before* external call to mitigate reentrancy on this variable        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-24)        rewards[msg.sender] = 0; [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-25)        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-26)        bool ok = token.transfer(msg.sender, amount);        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-27)        if (!ok) {            [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-28)            // revert and restore state if needed (not shown here for brevity)            [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-29)            revert TransferFailed();        [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-30)        }    [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-31)    } [](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#__codelineno-1-32)}`

**Security Improvements:**

-   State is updated **before** the external call, limiting simple reentrancy on `rewards`.
-   The token transfer’s return value is checked; failure results in a revert, preventing silent inconsistencies.

> Note: For full reentrancy protection, see SC08 and consider `ReentrancyGuard`, checks-effects-interactions, and pull-based patterns.

### 2025 Case Studies[¶](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#2025-case-studies "Permanent link")

-   **GMX (July 2025, $42M loss)**
    Unsafe external interactions and state updates after external calls allowed attackers to re-enter and manipulate accounting. The `executeDecreaseOrder` function transferred control to an attacker-supplied contract address during the refund process, enabling reentrancy. External call ordering, lack of proper checks, and reliance on assumptions about callee behavior amplified the impact.
-   [https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f](https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f)
-   [https://www.halborn.com/blog/post/explained-the-gmx-hack-july-2025](https://www.halborn.com/blog/post/explained-the-gmx-hack-july-2025)

-   **Arcadia Finance (July 2025, $3.5M loss)**
    The `SwapLogic._swapRouter()` and `RebalancerSpot` contracts allowed **arbitrary external calls** to user-supplied router addresses via `swapData` parameters, without validating the callee. The attacker registered a malicious contract as both the router and a whitelisted ArcadiaAccount, then used the router callback to spoof privileged execution contexts and invoke `setAssetManager()` / `flashAction()`. The protocol assumed the router would not have elevated permissions—an assumption not enforced in code. Unchecked callbacks and trust in external callee behavior enabled the drain.

-   [https://blog.solidityscan.com/arcadia-finance-hack-analysis-a03a722e554d](https://blog.solidityscan.com/arcadia-finance-hack-analysis-a03a722e554d)
-   [https://www.guardrail.ai/blog/arcadia-finance-hack-july-2025](https://www.guardrail.ai/blog/arcadia-finance-hack-july-2025)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC06-UncheckedExternalCalls/#best-practices-mitigations "Permanent link")

-   **Treat all external calls as untrusted**:
-   Even “standard” tokens or well-known protocols can be upgraded or replaced.
-   Assume they may re-enter or revert unexpectedly.
-   Use the **checks-effects-interactions** pattern:
-   Validate pre-conditions.
-   Update internal state.
-   Only then perform external calls.
-   Prefer **pull** over **push** for payments:
-   Allow users to withdraw rather than pushing funds to arbitrary addresses in loops.
-   Check return values and handle all failure modes:
-   Use libraries like OpenZeppelin’s `SafeERC20` to wrap token operations.
-   Be extremely careful with:
-   Low-level calls (`call`, `delegatecall`, `callcode`)
-   Arbitrary callbacks (e.g., hooks, onERC721Received, onFlashLoan callbacks)
