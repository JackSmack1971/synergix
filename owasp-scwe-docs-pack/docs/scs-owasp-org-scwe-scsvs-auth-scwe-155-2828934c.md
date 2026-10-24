---
title: "SCWE-155: Single Point of Failure in Administrative Key Management"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.923Z"
---
*Last updated: August 19, 2026*


# SCWE-155: Single Point of Failure in Administrative Key Management

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#relationships "Permanent link")

-   CWE-284: Improper Access Control
    [https://cwe.mitre.org/data/definitions/284.html](https://cwe.mitre.org/data/definitions/284.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#description "Permanent link")

Contracts that rely on a single administrative key (EOA or contract) without multisig, timelock, or key rotation create a single point of failure. Compromise of that key (phishing, malware, physical theft) gives full control; loss of the key (e.g., no backup) can permanently lock critical functions. SCWE-129 covers single EOA admin; this weakness focuses on the *risk* of single-key design and the absence of mitigations.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#remediation "Permanent link")

-   Use multisig wallets (e.g., Gnosis Safe) for administrative actions.
-   Implement timelocks for sensitive operations (SCWE-020).
-   Plan for key rotation or recovery mechanisms.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-3)contract Treasury {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-6)    function withdraw(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-7)        require(msg.sender == owner, "Not owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-8)        (bool ok, ) = owner.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-9)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-0-11)}`

**Risk:** Single `owner` key; no multisig, no timelock. Compromise or loss permanently affects the treasury.

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-1)contract Treasury {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-2)    address public owner;  // In production: use multisig (e.g., Gnosis Safe)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-3)    uint256 public constant TIMELOCK = 2 days;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-4)    uint256 public pendingAmount;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-5)    uint256 public unlockTime; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-7)    function proposeWithdraw(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-8)        require(msg.sender == owner, "Not owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-9)        pendingAmount = amount;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-10)        unlockTime = block.timestamp + TIMELOCK;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-12)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-13)    function executeWithdraw() external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-14)        require(msg.sender == owner, "Not owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-15)        require(block.timestamp >= unlockTime, "Timelock");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-16)        uint256 amount = pendingAmount;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-17)        pendingAmount = 0;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-18)        (bool ok, ) = owner.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-19)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-20)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/#__codelineno-1-21)}`

**Fix:** Timelock adds a delay so large withdrawals can be contested. Use a multisig for `owner` in production.
