---
title: "SCWE-144: Bypassable Contract Existence Check via extcodesize"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:27.686Z"
---
*Last updated: August 19, 2026*


# SCWE-144: Bypassable Contract Existence Check via extcodesize

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#relationships "Permanent link")

-   CWE-697: Incorrect Comparison
    [https://cwe.mitre.org/data/definitions/697.html](https://cwe.mitre.org/data/definitions/697.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#description "Permanent link")

Using `extcodesize(addr) > 0` to detect whether an address is a contract fails during construction. When code runs inside a constructor, `extcodesize(address(this))` returns 0 because the contract's code is not yet deployed. An attacker can deploy a contract whose constructor calls the victim—the victim sees `extcodesize(caller) == 0` and treats the caller as an EOA, bypassing contract-specific restrictions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#remediation "Permanent link")

-   Do not rely on `extcodesize` to distinguish EOAs from contracts.
-   If contract-only or EOA-only logic is required, use a different mechanism (e.g., trusted registry, explicit opt-in) or accept that constructor calls cannot be distinguished.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-3)contract TokenGating {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-4)    mapping(address => bool) public allowed; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-6)    function claim() external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-7)        require(extcodesize(msg.sender) == 0, "Contracts not allowed");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-8)        allowed[msg.sender] = true;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-11)    function extcodesize(address account) internal view returns (uint256 size) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-12)        assembly { size := extcodesize(account) }    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-0-14)}`

**Why vulnerable:** An attacker deploys `Attacker` whose constructor calls `claim()`. During the constructor, `extcodesize(Attacker) == 0`, so the check passes and the contract receives the claim.

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-3)contract TokenGating {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-4)    mapping(address => bool) public allowed;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-5)    mapping(address => bool) public claimed; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-7)    function claim() external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-8)        require(allowed[msg.sender], "Not allowed");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-9)        require(!claimed[msg.sender], "Already claimed");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-10)        claimed[msg.sender] = true;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/#__codelineno-1-12)}`

**Fix:** Use an allowlist instead of `extcodesize`. Access control is based on explicit registration, not EOA vs contract detection.
