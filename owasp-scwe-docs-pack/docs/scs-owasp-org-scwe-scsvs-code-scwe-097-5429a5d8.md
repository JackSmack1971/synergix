---
title: "SCWE-097: Missing Explicit Function Visibility"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:26.321Z"
---
*Last updated: August 19, 2026*


# SCWE-097: Missing Explicit Function Visibility

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#relationships "Permanent link")

-   CWE-284: Improper Access Control
    [https://cwe.mitre.org/data/definitions/284.html](https://cwe.mitre.org/data/definitions/284.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#description "Permanent link")

When a function’s visibility is omitted in Solidity, it defaults to `public`, allowing any caller to invoke logic that may have been intended to be internal or private. This expands the attack surface, enabling unauthorized state changes, fund movements, or reentrancy entry points.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#remediation "Permanent link")

-   Explicitly declare visibility (`private`, `internal`, `public`, `external`) on every function.
-   Use linters/static analysis to enforce visibility declarations.
-   Restrict privileged logic with proper access modifiers and role checks.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-3)contract Vault {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-4)    uint256 public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-6)    function withdraw(uint256 amount) { // defaults to public        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-7)        balance -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-8)        payable(msg.sender).transfer(amount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-0-10)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-3)contract Vault {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-4)    uint256 public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-6)    function withdraw(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-7)        // add proper access control or business checks here        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-8)        balance -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-9)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-10)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/#__codelineno-1-12)}`
