---
title: "SCWE-046: Reentrancy Attacks"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:23.554Z"
---
*Last updated: August 19, 2026*


# SCWE-046: Reentrancy Attacks

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#relationships "Permanent link")

-   CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition
    [https://cwe.mitre.org/data/definitions/367.html](https://cwe.mitre.org/data/definitions/367.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#description "Permanent link")

Reentrancy attacks occur when a contract allows untrusted external calls during execution without properly updating state variables or implementing protections. This enables attackers to repeatedly call functions and manipulate the contract’s state before execution completes. Common issues include:

-   Making external calls before updating state variables.
-   Lack of mechanisms to prevent repeated or recursive calls.
-   Improper handling of external interactions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#remediation "Permanent link")

-   **Update state first:** Modify critical state variables before any external calls.
-   **Implement reentrancy guards:** Use tools like `nonReentrant` modifiers to block recursive calls.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#examples "Permanent link")

### Vulnerable Contract Example (Reentrancy)[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#vulnerable-contract-example-reentrancy "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-3)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-4)    mapping(address => uint) public balances; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-6)    function withdraw(uint _amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-7)        require(balances[msg.sender] >= _amount);        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-8)        (bool success, ) = msg.sender.call{value: _amount}(""); // Vulnerable: external call before state update (reentrancy)        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-9)        require(success, "Transfer failed");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-10)        balances[msg.sender] -= _amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-12)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-13)    function deposit() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-14)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-15)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-0-16)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-2)import "@openzeppelin/contracts/security/ReentrancyGuard.sol"; // OZ 5.x: utils/ReentrancyGuard.sol [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-4)contract Secure is ReentrancyGuard {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-5)    mapping(address => uint) public balances; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-7)    function withdraw(uint _amount) public nonReentrant {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-8)        require(balances[msg.sender] >= _amount, "Insufficient balance");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-9)        balances[msg.sender] -= _amount;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-10)        (bool success, ) = msg.sender.call{value: _amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-11)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-14)    function deposit() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-15)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/#__codelineno-1-17)}`
