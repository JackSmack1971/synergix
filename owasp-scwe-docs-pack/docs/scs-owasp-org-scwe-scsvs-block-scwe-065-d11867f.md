---
title: "SCWE-065: Block Values as a Proxy for Time"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.501Z"
---
*Last updated: August 19, 2026*


# SCWE-065: Block Values as a Proxy for Time

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#description "Permanent link")

Using block values (such as `block.timestamp`, `block.number`, or `block.difficulty` / `block.prevrandao` post-merge) as a proxy for time in Ethereum smart contracts can be problematic. Block values are determined by validators (or miners on PoW chains) and can be manipulated within certain limits, making them unreliable for time-sensitive logic. Relying on these values for critical decisions like deadlines or expiration dates can result in unexpected behaviors, such as manipulations by validators (or miners on PoW chains) or unintended contract states.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#remediation "Permanent link")

To mitigate this vulnerability, account for the manipulation bounds of block values. `block.timestamp` can vary by ~15 seconds per block; design deadlines and time checks with this tolerance in mind. Time oracles are uncommon; the standard approach is to use `block.timestamp` with appropriate buffers. Where precision is critical, consider commit-reveal or multi-block confirmation.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-1)contract TimeSensitive {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-2)    uint public deadline; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-4)    constructor(uint _deadline) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-5)        deadline = _deadline;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-8)    function hasExpired() public view returns (bool) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-9)        return block.timestamp > deadline;  // Relies on block.timestamp    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-0-11)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-3)contract TimeSensitive {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-4)    uint public constant DEADLINE_BUFFER = 15; // seconds — accounts for block.timestamp manipulation    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-5)    uint public deadline; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-7)    constructor(uint _deadline) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-8)        // Set deadline with buffer so expiry is robust to ~15s timestamp variance        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-9)        deadline = _deadline + DEADLINE_BUFFER;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-12)    function hasExpired() public view returns (bool) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-13)        return block.timestamp > deadline;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/#__codelineno-1-15)}`

**Mitigation:** Add a buffer when setting deadlines to account for the ~15 second manipulation window of `block.timestamp`. Avoid relying on sub-minute precision.
