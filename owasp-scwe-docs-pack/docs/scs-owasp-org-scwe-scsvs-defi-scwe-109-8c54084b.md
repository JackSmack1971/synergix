---
title: "SCWE-109: Unbounded Loops on Untrusted Input"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.511Z"
---
*Last updated: August 19, 2026*


# SCWE-109: Unbounded Loops on Untrusted Input

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#relationships "Permanent link")

-   CWE-834: Excessive Iteration
    [https://cwe.mitre.org/data/definitions/834.html](https://cwe.mitre.org/data/definitions/834.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#description "Permanent link")

Iterating over user-controlled arrays or mappings without bounds lets attackers submit large inputs that exhaust gas, causing denial of service. Functions like batch withdrawals, reward distribution, or liquidations may become permanently unusable.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#remediation "Permanent link")

-   Impose upper bounds on loop iterations or batch sizes.
-   Use pagination/iterative processing with checkpoints.
-   Avoid on-chain iteration over untrusted lists; rely on off-chain aggregation with verifiable proofs (Merkle leaves).

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-3)contract Distributor {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-4)    function airdrop(address[] calldata users) external {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-5)        for (uint256 i = 0; i < users.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-6)            (bool ok, ) = payable(users[i]).call{value: 1 ether}("");            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-7)            require(ok, "Transfer failed"); // can run out of gas with large arrays        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-8)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-0-10)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-3)contract Distributor {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-4)    uint256 public last; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-6)    function airdrop(address[] calldata users, uint256 max) external {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-7)        uint256 end = last + max;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-8)        if (end > users.length) end = users.length;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-9)        for (uint256 i = last; i < end; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-10)            (bool ok, ) = payable(users[i]).call{value: 1 ether}("");            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-11)            require(ok, "Transfer failed");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-12)        }        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-13)        last = end;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/#__codelineno-1-15)}`
