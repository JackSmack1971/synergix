---
title: "SC08:2026 Reentrancy Attacks"
source_url: "https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:01.232Z"
---
# SC08:2026 Reentrancy Attacks

## Vulnerability: Reentrancy Attacks[¶](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#vulnerability-reentrancy-attacks "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#description "Permanent link")

Reentrancy describes any situation where a smart contract performs an external call (to another contract or address), and the callee can **call back into** the original contract before the first invocation has completed and state has been fully updated. If the caller is not designed to be reentrancy-safe, the callback can observe stale state and exploit it—e.g., withdrawing more than the caller’s balance, double-counting rewards, or manipulating accounting across complex multi-step flows.

This affects all contract types that perform external calls: DeFi (token transfers, DEX swaps, vault deposits/withdrawals, flash loan callbacks), NFTs (transfers with ERC-721/ERC-1155 receiver hooks, marketplace payouts), DAOs (proposal execution that invokes external contracts), bridges (message relay, asset transfers), and composable protocols (ERC-777 hooks, ERC-4626 deposit/withdraw hooks). Reentrancy can be **single-function** (same function called recursively), **cross-function** (callback into a different function), or **cross-contract** (callback traverses multiple contracts). On non-EVM chains, analogous patterns exist wherever cross-program invocations can recurse.

Few areas to focus on:

-   **Classic withdraw-before-update** (state change after external call)
-   **Callback and hook interfaces** (ERC-777, ERC-721/1155 receivers, ERC-4626, flash loan callbacks)
-   **Cross-function reentrancy** (read-your-writes assumptions between functions)
-   **Read-only reentrancy** (view functions or oracles reading state during a callback)
-   **Cross-contract and multi-module** reentrancy (vault → strategy → DEX flows)

Attackers exploit:

-   **Malicious tokens or receivers** that re-enter on transfer/hook callbacks
-   **Flash loan callbacks** that execute attacker logic before repayment
-   **Complex call graphs** where state is inconsistent mid-transaction across modules

### Example (Vulnerable Reentrancy Pattern)[¶](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#example-vulnerable-reentrancy-pattern "Permanent link")

`[](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-4)interface IToken {     [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-5)    function transfer(address to, uint256 amount) external returns (bool); [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-6)} [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-7)[](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-8)contract VulnerableVault {     [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-9)    IToken public immutable token;    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-10)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-11)    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-12)    constructor(IToken _token) {        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-13)        token = _token;    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-14)    } [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-15)    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-16)    function deposit(uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-17)        // Assume token already transferred in for brevity        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-18)        balances[msg.sender] += amount;    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-19)    } [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-20)    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-21)    function withdraw(uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-22)        require(balances[msg.sender] >= amount, "insufficient"); [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-23)        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-24)        // External call before state update – reentrancy window        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-25)        token.transfer(msg.sender, amount); [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-26)        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-27)        balances[msg.sender] -= amount;    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-28)    } [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-0-29)}`

**Issues:**

-   An attacker using a malicious token / proxy can re-enter `withdraw` from within the `transfer` call, repeatedly withdrawing based on the unchanged `balances[msg.sender]`.

### Example (Reentrancy-Safe Withdraw)[¶](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#example-reentrancy-safe-withdraw "Permanent link")

`[](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-4)import "@openzeppelin/contracts/security/ReentrancyGuard.sol"; [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-5)[](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-6)interface ITokenSafe {     [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-7)    function transfer(address to, uint256 amount) external returns (bool); [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-8)} [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-9)[](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-10)contract SafeVault is ReentrancyGuard {     [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-11)    ITokenSafe public immutable token;    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-12)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-13)    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-14)    error InsufficientBalance();    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-15)    error TransferFailed(); [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-16)    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-17)    constructor(ITokenSafe _token) {        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-18)        token = _token;    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-19)    } [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-20)    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-21)    function deposit(uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-22)        // Assume token already transferred in for brevity        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-23)        balances[msg.sender] += amount;    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-24)    } [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-25)    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-26)    function withdraw(uint256 amount) external nonReentrant {        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-27)        uint256 bal = balances[msg.sender];        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-28)        if (bal < amount) revert InsufficientBalance(); [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-29)        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-30)        // Effects first        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-31)        balances[msg.sender] = bal - amount; [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-32)        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-33)        // Then interaction        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-34)        bool ok = token.transfer(msg.sender, amount);        [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-35)        if (!ok) revert TransferFailed();    [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-36)    } [](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#__codelineno-1-37)}`

**Security Improvements:**

-   Uses `nonReentrant` modifier from OpenZeppelin’s `ReentrancyGuard`.
-   Applies **checks-effects-interactions** pattern to minimize reentrancy windows.
-   Checks transfer return value and reverts on failure.

### 2025 Case Study[¶](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#2025-case-study "Permanent link")

-   **GMX (July 2025, $42M loss)**
    GMX V1 contracts were exploited via a classic yet sophisticated reentrancy vector in `executeDecreaseOrder`. The function accepted the attacker's smart contract address as a parameter; when it transferred control to that address during the refund process, the attacker re-entered and manipulated global average short prices, AUM, and GLP valuations. State updates after external calls and lack of reentrancy guards enabled the drain. The vulnerability was introduced in 2022 as an unaudited patch.
-   [https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f](https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f)
-   [https://www.halborn.com/blog/post/explained-the-gmx-hack-july-2025](https://www.halborn.com/blog/post/explained-the-gmx-hack-july-2025)
-   [https://blog.verichains.io/p/gmx-42m-exploit-root-cause-analysis](https://blog.verichains.io/p/gmx-42m-exploit-root-cause-analysis)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/#best-practices-mitigations "Permanent link")

-   Use **`ReentrancyGuard`** or similar reentrancy locks on stateful functions that:
-   Modify balances or internal accounting.
-   Perform external calls that could re-enter the contract.
-   Follow **checks-effects-interactions**:
-   Check preconditions.
-   Apply all state changes.
-   Only then call external contracts.
-   Treat **ERC-777 hooks, ERC-4626 hooks, and other callbacks** as reentrancy vectors.
-   Carefully review:
-   Cross-function interactions (e.g., `deposit` calling `withdraw` internally).
-   Multi-contract systems where reentrancy may occur across modules, not just within a single contract.
-   Include reentrancy-focused **fuzzing and unit tests**, especially where external calls are involved.
