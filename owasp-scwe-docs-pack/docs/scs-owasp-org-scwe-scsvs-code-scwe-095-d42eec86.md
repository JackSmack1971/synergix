---
title: "SCWE-095: Missing Destination Address Size Check"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:26.204Z"
---
*Last updated: August 19, 2026*


# SCWE-095: Missing Destination Address Size Check

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#relationships "Permanent link")

-   **CWE-20**: [Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#description "Permanent link")

This weakness occurs when a smart contract function accepts a `bytes32` parameter intended to represent an Ethereum address without validating its size. Ethereum addresses are 20 bytes, and using a `bytes32` type without proper checks can lead to incorrect address interpretation, potentially causing funds to be sent to unintended addresses.

This is especially risky in cross-chain, bridging, or interoperability contexts where address formats and padding conventions may vary. If the upper 12 bytes of the `bytes32` value are non-zero (or the value is otherwise malformed), naive casting to `address` can silently truncate or misinterpret the actual destination, leading to irreversible fund loss or misdirection.

## Impact[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#impact "Permanent link")

Failure to validate `bytes32` inputs that represent addresses may enable: - Accidental misdirection of funds to unintended addresses due to truncation.
\- Loss of funds in production deployments, as ETH/token transfers are irreversible.
\- Exploitation by attackers who craft inputs with malicious upper bits to redirect value.
\- Integration fragility in cross-chain workflows where address encoding/padding differs.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#remediation "Permanent link")

-   Avoid using `bytes32` to represent addresses when possible; prefer the native `address` type.
-   If `bytes32` is required for protocol compatibility, validate that the upper 12 bytes are zero before casting: ensure `uint256(destination) >> 160 == 0`.
-   Centralize the validation and conversion logic in a dedicated helper to prevent inconsistent handling.
-   Add unit tests and fuzzing to verify that malformed `bytes32` values are rejected.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#examples "Permanent link")

-   **❌ Vulnerable Code (Lack of address size validation)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-4)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-5)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-7)    // Deposit ETH    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-8)    function deposit() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-9)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-12)    // ❌ Vulnerable: destinationAddress is bytes32, not validated    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-13)    function withdraw(bytes32 destinationAddress, uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-14)        require(balances[msg.sender] >= amount, "Insufficient balance");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-15)        _debitFrom(msg.sender, amount);        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-16)        _send(destinationAddress, amount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-17)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-18)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-19)    // Internal debit    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-20)    function _debitFrom(address from, uint256 amount) internal {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-21)        balances[from] -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-22)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-23)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-24)    // Internal send    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-25)    function _send(bytes32 destinationAddress, uint256 amount) internal {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-26)        address payable dest = payable(address(uint160(uint256(destinationAddress))));        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-27)        (bool ok, ) = dest.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-28)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-29)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-0-30)}`

-   **✅ Safe Code (Validation of address size)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-4)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-5)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-7)    // Deposit ETH    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-8)    function deposit() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-9)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-12)    // ✅ Safe: Validates destinationAddress size    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-13)    function withdraw(bytes32 destinationAddress, uint256 amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-14)        require(balances[msg.sender] >= amount, "Insufficient balance");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-15)        require(uint256(destinationAddress) >> 160 == 0, "Invalid address: upper 12 bytes must be zero");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-16)        _debitFrom(msg.sender, amount);        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-17)        _send(destinationAddress, amount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-18)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-19)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-20)    // Internal debit    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-21)    function _debitFrom(address from, uint256 amount) internal {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-22)        balances[from] -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-23)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-24)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-25)    // Internal send    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-26)    function _send(bytes32 destinationAddress, uint256 amount) internal {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-27)        address payable dest = payable(address(uint160(uint256(destinationAddress))));        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-28)        (bool ok, ) = dest.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-29)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-30)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/#__codelineno-1-31)}`
