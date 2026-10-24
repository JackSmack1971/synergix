---
title: "SCWE-140: Ether Locked Due to Missing Withdrawal Path"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.841Z"
---
*Last updated: August 19, 2026*


# SCWE-140: Ether Locked Due to Missing Withdrawal Path

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#relationships "Permanent link")

-   CWE-404: Improper Resource Shutdown or Release
    [https://cwe.mitre.org/data/definitions/404.html](https://cwe.mitre.org/data/definitions/404.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#description "Permanent link")

Contracts can receive ETH via `receive()`, `fallback()`, `selfdestruct` from another contract, or accidental sends. If the contract has no function to withdraw or forward this ETH, the funds become permanently locked. This can occur when a contract was not designed to hold ETH, when the withdrawal function is restricted to a role that no longer exists, or when the contract lacks a rescue/withdraw mechanism for unexpected inflows.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#remediation "Permanent link")

-   Implement a withdrawal or rescue function for authorized roles to recover stuck ETH.
-   If the contract should not accept ETH, use `receive() external payable { revert("ETH not accepted"); }`.
-   Document how unexpected ETH (e.g., from `selfdestruct`) is handled.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-3)contract TokenSale {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-4)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-6)    function buyTokens() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-7)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-10)    function withdrawTokens() external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-11)        uint256 amount = balances[msg.sender];        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-12)        balances[msg.sender] = 0;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-13)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-14)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-15)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-0-16)}`

**Why vulnerable:** If ETH is sent via `selfdestruct` or a plain transfer, it increases `address(this).balance` but not any user's `balances`. That ETH cannot be withdrawn by anyone and is locked.

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-3)contract TokenSale {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-5)    uint256 public totalDeposits;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-6)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-8)    constructor() { owner = msg.sender; } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-10)    function buyTokens() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-11)        balances[msg.sender] += msg.value;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-12)        totalDeposits += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-14)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-15)    function withdrawTokens() external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-16)        uint256 amount = balances[msg.sender];        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-17)        balances[msg.sender] = 0;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-18)        totalDeposits -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-19)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-20)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-21)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-22)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-23)    function rescueStuckETH() external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-24)        require(msg.sender == owner, "Not owner");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-25)        uint256 excess = address(this).balance - totalDeposits;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-26)        require(excess > 0, "No excess");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-27)        (bool ok, ) = owner.call{value: excess}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-28)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-29)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/#__codelineno-1-30)}`

**Fix:** Track `totalDeposits` and only rescue ETH in excess of user deposits (e.g., from `selfdestruct`). `withdrawTokens` lets users claim their deposits; `rescueStuckETH` recovers only excess ETH.
