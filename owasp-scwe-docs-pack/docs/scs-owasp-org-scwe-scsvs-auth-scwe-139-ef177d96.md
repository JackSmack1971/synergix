---
title: "SCWE-139: Single-Step Ownership Transfer Without Confirmation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.688Z"
---
*Last updated: August 19, 2026*


# SCWE-139: Single-Step Ownership Transfer Without Confirmation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#relationships "Permanent link")

-   CWE-670: Always-Incorrect Control Flow Implementation
    [https://cwe.mitre.org/data/definitions/670.html](https://cwe.mitre.org/data/definitions/670.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#description "Permanent link")

A single-step `transferOwnership(newOwner)` immediately assigns ownership to the new address. If the wrong address is used (typo, burn address `address(0)`, or a contract that cannot receive ownership), the contract can be permanently locked—no one can perform owner-only actions or correct the mistake. A two-step process (propose → accept) allows the intended recipient to confirm and prevents accidental loss of control.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#remediation "Permanent link")

-   Implement a two-step ownership transfer: `transferOwnershipPending(newOwner)` sets a pending owner, and `acceptOwnership()` (callable only by the pending owner) completes the transfer.
-   Validate that `newOwner != address(0)` and consider rejecting contract addresses if the owner must be an EOA for operational reasons.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-3)contract Ownable {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-10)    function transferOwnership(address newOwner) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-11)        require(msg.sender == owner, "Not owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-12)        owner = newOwner;  // Single step: typo or address(0) permanently locks contract    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-0-14)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-3)contract Ownable {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-5)    address public pendingOwner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-7)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-8)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-11)    function transferOwnership(address newOwner) external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-12)        require(msg.sender == owner, "Not owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-13)        require(newOwner != address(0), "Zero address");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-14)        pendingOwner = newOwner;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-15)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-16)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-17)    function acceptOwnership() external {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-18)        require(msg.sender == pendingOwner, "Not pending owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-19)        owner = pendingOwner;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-20)        delete pendingOwner;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-21)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/#__codelineno-1-22)}`
