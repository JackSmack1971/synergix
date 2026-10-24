---
title: "SCWE-031: Insecure use of Block Variables"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.380Z"
---
*Last updated: August 19, 2026*


# SCWE-031: Insecure use of Block Variables

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#relationships "Permanent link")

-   **CWE-682: Incorrect Calculation**
    [https://cwe.mitre.org/data/definitions/682.html](https://cwe.mitre.org/data/definitions/682.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#description "Permanent link")

In blockchain networks like Ethereum, block variables `(block.timestamp, block.number, block.difficulty` / `block.prevrandao` post-merge, etc.) provide information about the current state of the blockchain. However, these values are not fully deterministic and can be manipulated by validators (or miners on PoW chains), leading to vulnerabilities in smart contracts.

Block timestamps are not guaranteed to be accurate or consistent, and validators (or miners on PoW chains) can influence them within a certain range. This can cause issues when contracts depend on precise timing for critical functionality, such as token distribution, access control, or other time-sensitive events.

Potential issues that arise from insecure timestamp usage include:

-   Timestamp Manipulation: Validators (or miners on PoW) can slightly alter `block.timestamp` to influence time-sensitive logic (e.g., auctions, token distributions, staking rewards).
-   Predictable Randomness: Using `block.number` or `block.difficulty` as a source of randomness allows attackers to predict and manipulate outcomes.
-   Exploitable Access Control: Contracts that rely on block timestamps for permissions or actions may be bypassed if timestamps are adjusted.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#remediation "Permanent link")

-   **Avoid timestamp-based conditions**: Where possible, use block numbers instead of timestamps. Block numbers are more reliable and less subject to manipulation.
-   **Use Oracles**: For time-sensitive contracts, consider using trusted oracles to provide external time data.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#examples "Permanent link")

### Insecure Block Timestamp Usage- Timestamp-Based Deadlines[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#insecure-block-timestamp-usage-timestamp-based-deadlines "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-3)contract TimestampExample {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-4)    uint public deadline; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-6)    function setDeadline(uint _deadline) public {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-7)        deadline = _deadline;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-10)    function checkDeadline() public view returns (string) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-11)        if (block.timestamp > deadline) {            [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-12)            return "Deadline passed";        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-13)        } else {            [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-14)            return "Deadline not passed";        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-15)        }    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-0-17)}`

In the above example, `block.timestamp` is used to compare with the deadline. This creates a potential vulnerability as validators (or miners on PoW) can manipulate the block timestamp within a predefined window (~15 seconds).

### Fixed Block Timestamp Usage[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#fixed-block-timestamp-usage "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-3)contract SafeTimestampExample {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-4)    uint public deadline;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-5)    uint public blockNumber; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-7)    function setDeadline(uint _deadline) public {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-8)        deadline = _deadline;        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-9)        blockNumber = block.number;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-12)    function checkDeadline() public view returns (string) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-13)        if (block.number > blockNumber + 1000) { // Assuming a reasonable number of blocks for a deadline            [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-14)            return "Deadline passed";        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-15)        } else {            [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-16)            return "Deadline not passed";        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-17)        }    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-18)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-1-19)}`

In this fixed version, the contract uses `block.number` instead of `block.timestamp`. This makes the contract less susceptible to timestamp manipulation, as block numbers are more reliable and consistent.

### Insecure Lottery Using block.timestamp[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#insecure-lottery-using-blocktimestamp "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-2)[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-3)contract InsecureLottery {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-4)    address[] public players; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-5)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-6)    function enter() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-7)        require(msg.value > 0.01 ether, "Minimum ETH required"); [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-8)        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-9)        players.push(msg.sender);    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-10)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-11)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-12)    function pickWinner() public {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-13)        uint index = uint(block.timestamp) % players.length; // Insecure: Predictable outcome        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-14)        (bool ok, ) = payable(players[index]).call{value: address(this).balance}("");        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-15)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-16)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-2-17)}`

Issue: - Predictability: Since `block.timestamp` is manipulable within a small range, validators (or miners on PoW chains) can influence the winner selection. - Attack Vector: A validator (or miner on PoW) could reorder transactions to ensure a specific outcome

### Secure Alternative (Commit-Reveal)[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#secure-alternative-commit-reveal "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-2)[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-3)contract SecureLottery {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-4)    mapping(address => bytes32) public commits;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-5)    mapping(address => bytes32) public revealed;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-6)    address[] public players; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-7)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-8)    function commit(bytes32 hash) external payable {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-9)        require(msg.value > 0.01 ether, "Minimum ETH required");        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-10)        require(commits[msg.sender] == bytes32(0), "Already committed");        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-11)        commits[msg.sender] = hash;        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-12)        players.push(msg.sender);    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-13)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-14)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-15)    function reveal(bytes32 secret) external {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-16)        require(keccak256(abi.encodePacked(secret)) == commits[msg.sender], "Invalid reveal");        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-17)        revealed[msg.sender] = secret;    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-18)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-19)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-20)    function pickWinner() external {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-21)        bytes32 combined = bytes32(0);        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-22)        for (uint i = 0; i < players.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-23)            require(revealed[players[i]] != bytes32(0), "All must reveal");            [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-24)            combined = keccak256(abi.encodePacked(combined, revealed[players[i]]));        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-25)        }        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-26)        uint index = uint(combined) % players.length;        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-27)        (bool ok, ) = payable(players[index]).call{value: address(this).balance}("");        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-28)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-29)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/#__codelineno-3-30)}`

Fixes: - Uses commit-reveal: each player commits a hash, then reveals; combined secrets determine the winner. - `block.prevrandao` and `block.timestamp` are **not safe** for value-at-stake randomness — use VRF (e.g., Chainlink) or commit-reveal.

* * *
