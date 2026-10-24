---
title: "SCWE-104: Unprotected ERC777 Token Hooks"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.885Z"
---
*Last updated: August 19, 2026*


# SCWE-104: Unprotected ERC777 Token Hooks

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#relationships "Permanent link")

-   CWE-841: Improper Enforcement of Behavioral Workflow
    [https://cwe.mitre.org/data/definitions/841.html](https://cwe.mitre.org/data/definitions/841.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#description "Permanent link")

ERC777 tokens trigger `tokensReceived` hooks on recipients. Contracts that accept tokens without reentrancy protection or without blocking ERC777 hooks can be reentered during token transfers, enabling double-withdrawals or bypassing invariants.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#remediation "Permanent link")

-   Add `nonReentrant` guards around token transfer handlers and withdrawals.
-   Block unexpected token types or disable ERC777 acceptance by rejecting the ERC1820 interface.
-   Use pull-based withdrawals and avoid performing sensitive logic inside token receive hooks.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-2)interface IERC777 { function send(address,uint256,bytes calldata) external; } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-4)contract Rewards {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-5)    uint256 public totalPaid; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-7)    function claim(address token, uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-8)        IERC777(token).send(msg.sender, amount, ""); // ERC777 hook can reenter        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-9)        totalPaid += amount;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-2)import "@openzeppelin/contracts/security/ReentrancyGuard.sol"; // OZ 5.x: utils/ReentrancyGuard.sol [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-4)interface IERC20 {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-5)    function transfer(address to, uint256 amount) external returns (bool); [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-6)} [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-7)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-8)contract Rewards is ReentrancyGuard {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-9)    mapping(address => bool) public allowedTokens; // only non-ERC777 tokens    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-10)    uint256 public totalPaid; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-12)    function claim(address token, uint256 amount) external nonReentrant {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-13)        require(allowedTokens[token], "token not allowed"); // block ERC777        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-14)        totalPaid += amount;        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-15)        IERC20(token).transfer(msg.sender, amount);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/#__codelineno-1-17)}`
