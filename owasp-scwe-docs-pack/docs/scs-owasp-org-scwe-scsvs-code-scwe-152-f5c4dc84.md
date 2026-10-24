---
title: "SCWE-152: Misuse of Custom Errors Leading to Information Leakage or Wrong Revert Behavior"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:27.955Z"
---
*Last updated: August 19, 2026*


# SCWE-152: Misuse of Custom Errors Leading to Information Leakage or Wrong Revert Behavior

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#relationships "Permanent link")

-   CWE-209: Generation of Error Message Containing Sensitive Information
    [https://cwe.mitre.org/data/definitions/209.html](https://cwe.mitre.org/data/definitions/209.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#description "Permanent link")

Custom errors (Solidity 0.8.4+) save gas but can expose internal state if parameters include sensitive data (e.g., balances, private keys, internal addresses). Using the wrong error in a revert can also mislead integrators or hide the actual failure reason. Custom errors are part of the revert payload and can be decoded off-chain.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#remediation "Permanent link")

-   Avoid including sensitive data in custom error parameters.
-   Use generic error messages for external-facing reverts when the internal reason is confidential.
-   Ensure error selection matches the actual failure condition.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-3)contract Vault {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-4)    error InsufficientBalance(uint256 requested, uint256 available); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-6)    function withdraw(uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-7)        uint256 balance = balances[msg.sender];        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-8)        if (amount > balance) {            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-9)            revert InsufficientBalance(amount, balance);  // Exposes user balance        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-10)        }        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-11)        balances[msg.sender] -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-12)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-13)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-14)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-0-15)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-1)error InsufficientBalance(); [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-3)function withdraw(uint256 amount) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-4)    if (amount > balances[msg.sender]) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-5)        revert InsufficientBalance();    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-6)    }    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-7)    // ... [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/#__codelineno-1-8)}`
