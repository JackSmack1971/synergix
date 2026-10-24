---
title: "SCWE-050: Unprotected SELFDESTRUCT Instruction"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.192Z"
---
*Last updated: August 19, 2026*


# SCWE-050: Unprotected SELFDESTRUCT Instruction

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#relationships "Permanent link")

-   CWE-732: Incorrect Permission Assignment for Critical Resource
    [https://cwe.mitre.org/data/definitions/732.html](https://cwe.mitre.org/data/definitions/732.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#description "Permanent link")

The `SELFDESTRUCT` instruction in Ethereum allows a contract to destroy itself and send its remaining Ether balance to a specified address. If this instruction is not properly protected with access controls, an attacker could trigger it, causing the contract to self-destruct and possibly transferring all the funds to an unauthorized address. This can result in the total loss of funds or disruption of contract functionality.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#remediation "Permanent link")

To mitigate this vulnerability, it is crucial to protect the `SELFDESTRUCT` instruction with proper access control mechanisms. Only authorized users, such as the contract owner or admin, should be allowed to call the `SELFDESTRUCT` function. Consider using modifiers like `onlyOwner` or a role-based access control system to enforce permission checks before allowing this critical operation. **Note:** `selfdestruct` is deprecated per EIP-6049 (Solidity 0.8.24+); prefer migration patterns where possible.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-1)contract Destructible {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-2)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-4)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-5)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-8)    // Unprotected SELFDESTRUCT allowing anyone to call it    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-9)    function destruct() public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-10)        selfdestruct(payable(msg.sender));  // No access control    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-0-12)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-1)contract Destructible {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-2)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-3)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-4)    modifier onlyOwner() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-5)        require(msg.sender == owner, "Not the owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-6)        _;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-9)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-10)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-12)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-13)    // Only the owner can call SELFDESTRUCT    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-14)    function destruct() public onlyOwner {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-15)        selfdestruct(payable(msg.sender));  // Access control added    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/#__codelineno-1-17)}`
