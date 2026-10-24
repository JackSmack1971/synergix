---
title: "SCWE-156: Missing Emergency Circuit Breaker for Critical Operations"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:30.095Z"
---
*Last updated: August 19, 2026*


# SCWE-156: Missing Emergency Circuit Breaker for Critical Operations

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#relationships "Permanent link")

-   CWE-693: Protection Mechanism Failure
    [https://cwe.mitre.org/data/definitions/693.html](https://cwe.mitre.org/data/definitions/693.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#description "Permanent link")

A circuit breaker is a threshold-based or condition-based halt mechanism that stops critical operations when anomalies are detected (e.g., TVL drop >X%, unusual withdrawal volume, oracle deviation). Unlike simple pausability (SCWE-014), a circuit breaker automatically or semi-automatically triggers based on predefined conditions, providing an additional safety layer during attacks or market stress.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#remediation "Permanent link")

-   Implement circuit breakers that halt deposits, withdrawals, or swaps when thresholds are exceeded.
-   Use oracle-based triggers (e.g., price deviation) or rate-limit triggers.
-   Ensure the circuit breaker can be reset by governance or after cooldown.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-3)contract LendingPool {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-4)    mapping(address => uint256) public balances;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-5)    uint256 public totalDeposits; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-7)    function deposit() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-8)        balances[msg.sender] += msg.value;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-9)        totalDeposits += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-12)    function withdraw(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-13)        require(balances[msg.sender] >= amount, "Insufficient");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-14)        balances[msg.sender] -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-15)        totalDeposits -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-16)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-17)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-18)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-0-19)}`

**Gap:** No circuit breaker. A flash loan or oracle attack could drain funds before anyone can pause.

### Mitigation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#mitigation "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-1)uint256 public maxWithdrawalPerTx = 100 ether; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-2)uint256 public lastWithdrawalTime; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-3)uint256 public constant WITHDRAWAL_COOLDOWN = 1 hours; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-5)function withdraw(uint256 amount) external {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-6)    require(amount <= maxWithdrawalPerTx, "Circuit breaker: amount too high");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-7)    require(block.timestamp >= lastWithdrawalTime + WITHDRAWAL_COOLDOWN, "Cooldown");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-8)    lastWithdrawalTime = block.timestamp;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-9)    // ... rest of logic [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/#__codelineno-1-10)}`
