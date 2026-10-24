---
title: "SCWE-145: Unvalidated Constructor Parameters"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.829Z"
---
*Last updated: August 19, 2026*


# SCWE-145: Unvalidated Constructor Parameters

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#description "Permanent link")

Constructors that accept critical parameters (owner, oracle, fee recipient, token addresses) without validation can deploy a contract in a broken or insecure state. Zero addresses, invalid values, or inconsistent configuration (e.g., fee > 100%) may be impossible to fix after deployment if there is no setter or upgrade path.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#remediation "Permanent link")

-   Validate all constructor parameters: zero address checks, range checks (e.g., fee <= 100%), and consistency checks.
-   Use `require` or custom errors to revert deployment with a clear message when validation fails.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-3)contract Staking {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-5)    address public rewardToken;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-6)    uint256 public feeBps; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-8)    constructor(address _owner, address _rewardToken, uint256 _feeBps) {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-9)        owner = _owner;           // No validation        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-10)        rewardToken = _rewardToken;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-11)        feeBps = _feeBps;         // Could be > 10000    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-12)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-0-13)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-1)constructor(address _owner, address _rewardToken, uint256 _feeBps) {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-2)    require(_owner != address(0), "Invalid owner");    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-3)    require(_rewardToken != address(0), "Invalid token");    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-4)    require(_feeBps <= 10000, "Fee too high");    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-5)    owner = _owner;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-6)    rewardToken = _rewardToken;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-7)    feeBps = _feeBps; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/#__codelineno-1-8)}`
