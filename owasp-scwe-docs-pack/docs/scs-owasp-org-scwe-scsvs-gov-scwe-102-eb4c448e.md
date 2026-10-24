---
title: "SCWE-102: Missing Checks-Effects-Interactions Pattern"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.574Z"
---
*Last updated: August 19, 2026*


# SCWE-102: Missing Checks-Effects-Interactions Pattern

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#relationships "Permanent link")

-   CWE-841: Improper Enforcement of Behavioral Workflow
    [https://cwe.mitre.org/data/definitions/841.html](https://cwe.mitre.org/data/definitions/841.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#description "Permanent link")

Calling external contracts before updating local state breaks the checks-effects-interactions (CEI) pattern. Attackers can reenter or observe stale state to perform double-withdrawals, bypass limits, or corrupt accounting.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#remediation "Permanent link")

-   Perform input validation and state updates before external calls.
-   Use reentrancy guards on functions that transfer value or call untrusted contracts.
-   Prefer pull-based withdrawals to avoid pushing funds inside complex flows.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-3)contract Payout {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-4)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-6)    function withdraw() external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-7)        (bool ok, ) = msg.sender.call{value: balances[msg.sender]}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-8)        require(ok, "send failed");       // external call first        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-9)        balances[msg.sender] = 0;         // state updated after    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-2)import "@openzeppelin/contracts/security/ReentrancyGuard.sol"; // OZ 5.x: utils/ReentrancyGuard.sol [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-4)contract Payout is ReentrancyGuard {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-5)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-7)    function withdraw() external nonReentrant {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-8)        uint256 amount = balances[msg.sender];        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-9)        balances[msg.sender] = 0;         // effects first        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-10)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-11)        require(ok, "send failed");       // interaction last    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/#__codelineno-1-13)}`
