---
title: "SCWE-110: Fee-On-Transfer Token Misaccounting"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:39.432Z"
---
*Last updated: August 19, 2026*


# SCWE-110: Fee-On-Transfer Token Misaccounting

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#relationships "Permanent link")

-   CWE-682: Incorrect Calculation
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#description "Permanent link")

Assuming an ERC20 transfer moves the full requested amount fails with fee-on-transfer or deflationary tokens. Protocols that credit users for the requested amount instead of the received amount can be drained or mis-account balances.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#remediation "Permanent link")

-   Measure token balances before and after transfers to calculate the actual received amount.
-   Maintain allowlists/blocks for incompatible tokens or handle fee-on-transfer explicitly.
-   Validate that accounting uses the net amount when updating shares or debts.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-3)contract Vault {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-4)    IERC20 public token;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-5)    mapping(address => uint256) public deposits; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-7)    function deposit(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-8)        token.transferFrom(msg.sender, address(this), amount);        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-9)        deposits[msg.sender] += amount; // credits full amount even if fee applied    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-3)contract Vault {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-4)    IERC20 public token;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-5)    mapping(address => uint256) public deposits; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-7)    function deposit(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-8)        uint256 beforeBal = token.balanceOf(address(this));        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-9)        token.transferFrom(msg.sender, address(this), amount);        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-10)        uint256 received = token.balanceOf(address(this)) - beforeBal;        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-11)        deposits[msg.sender] += received; // credit net amount    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/#__codelineno-1-13)}`
