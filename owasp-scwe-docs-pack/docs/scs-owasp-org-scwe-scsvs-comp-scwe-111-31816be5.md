---
title: "SCWE-111: Rebase Token Balance Drift"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:39.552Z"
---
*Last updated: August 19, 2026*


# SCWE-111: Rebase Token Balance Drift

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#relationships "Permanent link")

-   CWE-682: Incorrect Calculation
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#description "Permanent link")

Rebasing tokens change user balances over time. Protocols that track deposited amounts as fixed units (instead of shares) can become insolvent or let users withdraw more than their fair share after positive or negative rebases.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#remediation "Permanent link")

-   Track user positions using share-based accounting that scales with total supply.
-   Normalize balances on every interaction or use wrappers that expose a non-rebasing interface (e.g., wstETH).
-   Validate integrations against tokens with elastic supply and document unsupported assets.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-3)contract Savings {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-4)    IERC20 public rebasingToken;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-5)    mapping(address => uint256) public deposits; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-7)    function deposit(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-8)        rebasingToken.transferFrom(msg.sender, address(this), amount);        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-9)        deposits[msg.sender] += amount; // assumes static balance    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-3)contract Savings {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-4)    IERC20 public rebasingToken;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-5)    mapping(address => uint256) public shares;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-6)    uint256 public totalShares; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-8)    function deposit(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-9)        uint256 supply = rebasingToken.totalSupply();        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-10)        uint256 share = totalShares == 0 ? amount : amount * totalShares / supply;        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-11)        shares[msg.sender] += share;        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-12)        totalShares += share;        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-13)        rebasingToken.transferFrom(msg.sender, address(this), amount);    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/#__codelineno-1-15)}`
