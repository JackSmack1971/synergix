---
title: "SCWE-149: Transfers to Addresses That Cannot Receive Funds"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.709Z"
---
*Last updated: August 19, 2026*


# SCWE-149: Transfers to Addresses That Cannot Receive Funds

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#relationships "Permanent link")

-   CWE-755: Improper Handling of Exceptional Conditions
    [https://cwe.mitre.org/data/definitions/755.html](https://cwe.mitre.org/data/definitions/755.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#description "Permanent link")

Sending ETH or tokens to addresses that cannot receive them (e.g., contracts with no `receive`/`fallback`, or that revert on receive) causes the transfer to fail. In push-based distributions (e.g., airdrops, reward payouts), if one recipient cannot receive, the entire transaction reverts—leading to denial of service for all recipients. Pull-based patterns avoid this by letting users claim individually.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#remediation "Permanent link")

-   Prefer pull-based over push-based distributions.
-   If push-based is required, use `try/catch` to skip failing recipients and track failures, or validate recipients (e.g., reject contracts that don't implement a receiver interface).

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-3)contract RewardDistributor {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-4)    function distribute(address[] calldata users, uint256[] calldata amounts) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-5)        for (uint256 i = 0; i < users.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-6)            (bool ok, ) = users[i].call{value: amounts[i]}("");            [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-7)            require(ok, "Transfer failed");  // One failure reverts entire batch        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-8)        }    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-0-10)}`

### Fixed (Pull-based)[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#fixed-pull-based "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-1)mapping(address => uint256) public pendingRewards; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-3)function claim() external {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-4)    uint256 amount = pendingRewards[msg.sender];    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-5)    require(amount > 0, "Nothing to claim");    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-6)    pendingRewards[msg.sender] = 0;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-7)    (bool ok, ) = msg.sender.call{value: amount}("");    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-8)    require(ok, "Transfer failed"); [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/#__codelineno-1-9)}`
