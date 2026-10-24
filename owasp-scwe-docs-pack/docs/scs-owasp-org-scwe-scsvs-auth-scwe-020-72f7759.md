---
title: "SCWE-020: Absence of Time-Locked Functions"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:30.712Z"
---
*Last updated: August 19, 2026*


# SCWE-020: Absence of Time-Locked Functions

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#relationships "Permanent link")

-   CWE-840: Business Logic Errors [https://cwe.mitre.org/data/definitions/840.html](https://cwe.mitre.org/data/definitions/840.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#description "Permanent link")

Absence of time-locked functions occurs when smart contracts do not implement mechanisms to delay certain critical functions or actions based on time conditions. This can result in the contract allowing actions that should be restricted or postponed for a certain period, such as emergency fund withdrawals or sensitive administrative actions. Without time-locking mechanisms, malicious actors or faulty logic could trigger these actions at the wrong time, leading to undesired outcomes.

Time-locking is commonly used in scenarios like: - Delaying admin or owner functions to prevent immediate misuse. - Ensuring withdrawal or fund transfer happens only after a predefined delay. - Enabling emergency actions only after a certain time or under specific conditions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#remediation "Permanent link")

-   **Implement time-locked functions:** Ensure that critical functions, especially those related to fund transfers or administrative actions, are protected by a time lock, delaying their execution until an appropriate time has passed.
-   **Use block timestamps:** Leverage block timestamps or block numbers to control the execution of functions.
-   **Limit emergency access:** If implementing emergency mechanisms, ensure that there are time delays before they can be invoked, to reduce the chance of misuse.
-   **Review time-based logic regularly:** Verify the correctness of time-based logic to ensure that the system behaves as intended.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#examples "Permanent link")

### Absence of Time-Locked Function[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#absence-of-time-locked-function "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-3)contract NoTimeLock {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-5)    uint public funds; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-7)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-8)        owner = msg.sender;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-9)        funds = 1000;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-12)    // Critical function without time-lock    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-13)    function withdrawFunds(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-14)        require(msg.sender == owner, "Not the owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-15)        funds -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-0-17)}`

In this example, the contract lacks any time-lock mechanism, allowing the owner to withdraw funds at any time, which could be dangerous if mishandled.

### Time-Locked Function Implementation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#time-locked-function-implementation "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-3)contract TimeLockExample {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-5)    uint public funds;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-6)    uint public lastWithdrawalTime;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-7)    uint public withdrawalDelay = 1 weeks; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-9)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-10)        owner = msg.sender;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-11)        funds = 1000;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-12)        lastWithdrawalTime = block.timestamp;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-14)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-15)    // Critical function with time-lock    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-16)    function withdrawFunds(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-17)        require(msg.sender == owner, "Not the owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-18)        require(block.timestamp >= lastWithdrawalTime + withdrawalDelay, "Time lock not expired"); [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-19)        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-20)        lastWithdrawalTime = block.timestamp;        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-21)        funds -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-22)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/#__codelineno-1-23)}`

In the fixed version, a time-lock mechanism is implemented, ensuring that the owner can only withdraw funds after a certain delay (e.g., one week). This provides an added layer of security, particularly in cases where emergency withdrawals or administrative actions are necessary but should not be immediate.
