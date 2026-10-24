---
title: "SCWE-137: Read-Only Reentrancy via View Function State Staleness"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:27.337Z"
---
*Last updated: August 19, 2026*


# SCWE-137: Read-Only Reentrancy via View Function State Staleness

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#relationships "Permanent link")

-   CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition
    [https://cwe.mitre.org/data/definitions/367.html](https://cwe.mitre.org/data/definitions/367.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#description "Permanent link")

Read-only reentrancy occurs when a `view` or `pure` function is called during an external callback (e.g., from a lending protocol reading collateral, or an integrator querying state). The view function returns stale state because the contract's effects have not yet been applied—the callback happens mid-transaction, before state updates complete. External protocols that rely on this state for critical decisions (e.g., liquidations, pricing, health checks) can be exploited to drain funds or bypass invariants.

This is distinct from classic reentrancy (SCWE-046): no state-modifying function is reentered, but the *read* of inconsistent state by external callers during a callback causes the vulnerability.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#remediation "Permanent link")

-   Apply `nonReentrant` guards to functions that make external calls, even if the caller only reads state—external protocols may call back into view functions.
-   Use a "read-your-writes" pattern: ensure view functions reflect in-flight state or document that they are unsafe during callbacks.
-   Integrators should not rely on view functions of contracts that perform external calls without reentrancy guards.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-3)contract LendingPool {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-4)    mapping(address => uint256) public balances;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-5)    mapping(address => uint256) public borrowed; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-7)    function deposit() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-8)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-11)    function withdraw(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-12)        require(balances[msg.sender] >= amount, "Insufficient");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-13)        balances[msg.sender] -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-14)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-15)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-17)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-18)    function getHealthFactor(address user) external view returns (uint256) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-19)        return (balances[user] * 1e18) / (borrowed[user] + 1);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-20)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-0-21)}`

**Why vulnerable:** During `withdraw`, the recipient's callback can invoke `getHealthFactor(user)` (e.g., from an integrator or liquidation bot). The victim's state may be mid-update or the integrator may rely on cached/stale values from the victim or dependent contracts. External protocols making decisions based on such reads can allow unhealthy borrows or incorrect liquidations.

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-2)import "@openzeppelin/contracts/security/ReentrancyGuard.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-4)contract LendingPool is ReentrancyGuard {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-5)    mapping(address => uint256) public balances;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-6)    mapping(address => uint256) public borrowed; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-8)    function withdraw(uint256 amount) external nonReentrant {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-9)        require(balances[msg.sender] >= amount, "Insufficient");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-10)        balances[msg.sender] -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-11)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-12)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/#__codelineno-1-14)}`

**Fix:** `nonReentrant` prevents external callbacks from reentering or being used while state is mid-update, so view functions cannot be called in an inconsistent state during the callback.
