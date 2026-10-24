---
title: "SCWE-101: Flash-Loan-Fueled Governance Manipulation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.455Z"
---
*Last updated: August 19, 2026*


# SCWE-101: Flash-Loan-Fueled Governance Manipulation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#relationships "Permanent link")

-   CWE-367: Time-of-Check Time-of-Use (TOCTOU) Race Condition
    [https://cwe.mitre.org/data/definitions/367.html](https://cwe.mitre.org/data/definitions/367.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#description "Permanent link")

If voting power is measured at execution time without historical snapshots or locking, an attacker can borrow a large balance via flash loan, pass a proposal, and return the loan in the same transaction. Governance decisions then depend on transient liquidity rather than long-term stake.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#remediation "Permanent link")

-   Use token balance snapshots at a fixed block for voting power.
-   Require vote escrow/locking or minimum voting period spanning multiple blocks.
-   Set quorum and proposal thresholds based on historical supply, not instantaneous balances.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-3)contract SimpleGov {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-4)    IERC20 public token;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-5)    mapping(uint256 => bool) public proposals; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-7)    function vote(uint256 id, bool support) external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-8)        require(token.balanceOf(msg.sender) > 1_000_000 ether, "low power");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-9)        if (support) { proposals[id] = true; }    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-2)import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol"; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-4)contract SnapshotGov {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-5)    ERC20Snapshot public token;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-6)    mapping(uint256 => uint256) public snapshotId; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-8)    function openProposal(uint256 id) external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-9)        snapshotId[id] = token.snapshot();    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-12)    function vote(uint256 id, bool support) external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-13)        uint256 power = token.balanceOfAt(msg.sender, snapshotId[id]);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-14)        require(power > 1_000_000 ether, "low power");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-15)        // record vote...    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/#__codelineno-1-17)}`
