---
title: "Unchecked External Calls in Smart Contracts"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:16.864Z"
---
# Unchecked External Calls in Smart Contracts

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#description "Permanent link")

Unchecked external calls occur when a smart contract makes an external call to another contract or address without verifying the call's outcome. In Ethereum, external calls may fail silently, and the calling contract may mistakenly proceed as if the call succeeded. This leads to state inconsistencies and potential exploitation. The issue is particularly risky in functions like delegatecall, send, or call, where the outcome must be explicitly checked.

**Example: Code Without Proper Access Control**

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-2)pragma solidity ^0.4.24; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-3)[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-4)contract Proxy {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-5)    address public owner; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-6)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-7)    constructor() public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-8)        owner = msg.sender;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-9)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-10)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-11)    function forward(address callee, bytes memory _data) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-12)        require(callee.delegatecall(_data)); // Unchecked: no validation of callee; delegatecall executes in caller context    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-13)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#__codelineno-0-14)}`

### Impact[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#impact "Permanent link")

-   When external calls fail and their results are unchecked, the contract can proceed under incorrect assumptions, leading to potential loss of funds or other unexpected behaviors.
-   Unverified external calls can lead to incorrect updates to the contract state, making it vulnerable to exploits and logical inconsistencies.
-   Attackers can manipulate such vulnerabilities to execute malicious code or withdraw funds multiple times.

### Remediation[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/overview/#remediation "Permanent link")

-   For low-level functions like `call`, `delegatecall`, and `staticcall`, always check the return value and handle failures with `require(success, "message")`.
-   For ETH transfers, prefer `call{value}("")` with explicit success checks over `transfer()` or `send()` (see SCWE-079); `transfer()` has a 2300 gas stipend and can cause DoS when the recipient is a contract.
-   Limit interactions with untrusted contracts and ensure robust validation before performing critical operations.
