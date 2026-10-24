---
title: "SCWE-143: Critical Address Parameters Not Validated for Zero Address"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:27.569Z"
---
*Last updated: August 19, 2026*


# SCWE-143: Critical Address Parameters Not Validated for Zero Address

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#description "Permanent link")

Critical address parameters (owner, oracle, fee recipient, token address) that are not validated for `address(0)` can brick the contract or cause funds to be sent to the burn address. Assigning `address(0)` as owner prevents any owner-only actions; using it as a recipient loses funds permanently. SCWE-091 covers zero *value* in token transfers; this weakness addresses zero *address*.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#remediation "Permanent link")

-   Validate `require(addr != address(0), "Zero address")` for all critical address parameters in constructors and setters.
-   Use custom errors for gas efficiency where appropriate.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-3)contract Vault {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-5)    address public feeRecipient; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-7)    constructor(address _owner, address _feeRecipient) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-8)        owner = _owner;           // No check: address(0) bricks contract        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-9)        feeRecipient = _feeRecipient;  // No check: fees sent to burn address    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-12)    function collectFees() external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-13)        uint256 fees = address(this).balance;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-14)        (bool ok, ) = feeRecipient.call{value: fees}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-15)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-0-17)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-1-1)constructor(address _owner, address _feeRecipient) {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-1-2)    require(_owner != address(0), "Invalid owner");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-1-3)    require(_feeRecipient != address(0), "Invalid fee recipient");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-1-4)    owner = _owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-1-5)    feeRecipient = _feeRecipient; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/#__codelineno-1-6)}`
