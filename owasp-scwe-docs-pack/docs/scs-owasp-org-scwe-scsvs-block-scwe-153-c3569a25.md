---
title: "SCWE-153: Reliance on block.prevrandao for High-Value Randomness"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.863Z"
---
*Last updated: August 19, 2026*


# SCWE-153: Reliance on block.prevrandao for High-Value Randomness

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#relationships "Permanent link")

-   CWE-330: Use of Insufficiently Random Values
    [https://cwe.mitre.org/data/definitions/330.html](https://cwe.mitre.org/data/definitions/330.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#description "Permanent link")

Post-merge (Ethereum PoS), `block.difficulty` was replaced by `block.prevrandao`. Both are manipulable by validators: they can influence the value within protocol rules. Using `block.prevrandao` (or `block.difficulty`) for high-value randomness—lotteries, airdrops, winner selection—allows validators or sophisticated actors to predict or bias outcomes. SCWE-024 and SCWE-084 cover blockhash/timestamp; this weakness specifically addresses `block.prevrandao`.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#remediation "Permanent link")

-   Do not use `block.prevrandao` or `block.difficulty` for value-at-stake randomness.
-   Use Chainlink VRF, commit-reveal schemes, or other verifiable randomness sources.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-3)contract Lottery {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-4)    address[] public participants; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-6)    function pickWinner() external view returns (uint256) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-7)        return uint256(keccak256(abi.encodePacked(block.prevrandao, block.timestamp))) % participants.length;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#__codelineno-0-9)}`

**Why vulnerable:** `block.prevrandao` is manipulable by validators; they can influence the value to bias the outcome.

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/#fixed "Permanent link")

Use Chainlink VRF V2 or a commit-reveal scheme where participants commit hashes before the random value is known. See SCWE-024 for a Chainlink VRF example.
