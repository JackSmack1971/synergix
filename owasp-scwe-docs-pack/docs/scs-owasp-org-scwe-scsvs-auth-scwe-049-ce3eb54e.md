---
title: "SCWE-049: Unprotected Ether Withdrawal"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:31.069Z"
---
*Last updated: August 19, 2026*


# SCWE-049: Unprotected Ether Withdrawal

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#relationships "Permanent link")

-   CWE-732: Incorrect Permission Assignment for Critical Resource
    [https://cwe.mitre.org/data/definitions/732.html](https://cwe.mitre.org/data/definitions/732.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#description "Permanent link")

Unprotected Ether withdrawal occurs when a smart contract allows withdrawal of Ether (ETH) without sufficient access control or proper authorization mechanisms. This vulnerability exposes the contract to unauthorized or malicious users, enabling them to drain funds without any checks on the withdrawal request.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#remediation "Permanent link")

To prevent this vulnerability, implement strong access control mechanisms like the `onlyOwner` modifier or a more flexible role-based access control (RBAC) system. Ensure that only authorized users (e.g., the contract owner or specific users) can initiate Ether withdrawals. Always verify user permissions before allowing access to critical contract functions.

## Impact[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#impact "Permanent link")

An attacker can exploit this vulnerability to withdraw Ether from the contract, leading to potential financial loss. This could result in a total loss of funds if no protective measures are in place, exposing the contract and its users to significant risks.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-1)contract EtherWallet {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-2)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-4)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-5)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-8)    function withdraw(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-9)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-10)        require(ok, "Transfer failed");  // No access control    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-0-12)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-1)contract EtherWallet {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-2)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-3)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-4)    modifier onlyOwner() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-5)        require(msg.sender == owner, "Not the owner");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-6)        _;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-9)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-10)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-12)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-13)    function withdraw(uint amount) public onlyOwner {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-14)        (bool ok, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-15)        require(ok, "Transfer failed");  // Access control added    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/#__codelineno-1-17)}`
