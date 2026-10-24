---
title: "SCWE-116: Missing Supply Cap Enforcement"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.618Z"
---
*Last updated: August 19, 2026*


# SCWE-116: Missing Supply Cap Enforcement

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#relationships "Permanent link")

-   CWE-693: Protection Mechanism Failure
    [https://cwe.mitre.org/data/definitions/693.html](https://cwe.mitre.org/data/definitions/693.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#description "Permanent link")

Tokens or lending systems without hard supply caps allow privileged accounts or flawed logic to mint unlimited units, inflating supply and draining collateralized protocols. Lack of caps also breaks price assumptions in AMMs and oracles.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#remediation "Permanent link")

-   Define immutable max supply and enforce it on every mint path.
-   Separate minting roles with multi-sig and timelock; emit events for mint changes.
-   Include cap checks in upgrades and cross-chain minting/bridging logic.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-3)contract Token {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-5)    uint256 public totalSupply; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-7)    function mint(address to, uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-8)        require(msg.sender == owner, "not owner");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-9)        totalSupply += amount; // no cap        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-10)        // mint tokens...    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-0-12)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-3)contract Token {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-5)    uint256 public totalSupply;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-6)    uint256 public constant MAX_SUPPLY = 1_000_000 ether; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-8)    function mint(address to, uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-9)        require(msg.sender == owner, "not owner");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-10)        require(totalSupply + amount <= MAX_SUPPLY, "cap exceeded");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-11)        totalSupply += amount;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-12)        // mint tokens...    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/#__codelineno-1-14)}`
