---
title: "SC06:2025 Unchecked External Calls"
source_url: "https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:02.686Z"
---
# SC06:2025 Unchecked External Calls

## Vulnerability: Unchecked External Calls[¶](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#vulnerability-unchecked-external-calls "Permanent link")

### Description:[¶](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#description "Permanent link")

Unchecked external calls refer to a security flaw where a contract makes an external call to another contract or address without properly checking the outcome of that call. In Ethereum, when a contract calls another contract, the called contract can fail silently without throwing an exception. If the calling contract doesn’t check the return value, it might incorrectly assume the call was successful, even if it wasn't. This can lead to inconsistencies in the contract state and vulnerabilities that attackers can exploit.

### Example (Vulnerable contract):[¶](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#example-vulnerable-contract "Permanent link")

`[](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-2)pragma solidity ^0.4.24; [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-4)contract Solidity_UncheckedExternalCall {     [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-5)    address public owner; [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-6)    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-7)    constructor() public {        [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-8)        owner = msg.sender;    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-9)    } [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-10)    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-11)    function forward(address callee, bytes memory _data) public {        [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-12)        require(callee.delegatecall(_data));    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-13)    } [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-0-14)}`

### Impact:[¶](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#impact "Permanent link")

-   Unchecked external calls can result in failed transactions, causing the intended operations to not be completed successfully. This can lead to the loss of funds, as the contract may proceed under the false assumption that the transfer was successful. Additionally, it can create an incorrect contract state, making the contract vulnerable to further exploits and inconsistencies in its logic.

### Remediation:[¶](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#remediation "Permanent link")

-   Always check the return value of low-level calls (`call`, `delegatecall`, `staticcall`) and `send()` — do not assume success. Use `require(success, "message")` after `(bool success, ) = target.call{...}(...)`.
-   For ETH transfers, prefer `call{value}("")` with explicit success checks over `transfer()` or `send()` (see SCWE-079); `transfer()` has a 2300 gas stipend and can cause DoS when the recipient is a contract.

### Example (Fixed version):[¶](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#example-fixed-version "Permanent link")

`[](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-2)pragma solidity ^0.8.0;  [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-4)contract Solidity_UncheckedExternalCall {     [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-5)    address public owner; [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-6)    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-7)    constructor() {        [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-8)        owner = msg.sender;    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-9)    } [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-10)    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-11)    function forward(address callee, bytes memory _data) public {        [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-12)        // Ensure that delegatecall succeeds        [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-13)        (bool success, ) = callee.delegatecall(_data);        [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-14)        require(success, "Delegatecall failed");  // Check the return value to handle failure    [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-15)    } [](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#__codelineno-1-16)}`

### Examples of Smart Contracts That Fell Victim to Unchecked External Call Attacks:[¶](https://scs.owasp.org/sctop10/archive/2025/SC06-UncheckedExternalCalls/#examples-of-smart-contracts-that-fell-victim-to-unchecked-external-call-attacks "Permanent link")

1.  [Punk Protocol Hack](https://github.com/PunkFinance/punk.protocol/blob/master/contracts/models/CompoundModel.sol) : A Comprehensive [Hack Analysis](https://blog.solidityscan.com/security-issues-with-delegate-calls-4ae64d775b76)
