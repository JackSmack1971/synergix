---
title: "SCWE-018: Use of tx.origin for Authorization"
source_url: "https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:30.456Z"
---
*Last updated: August 19, 2026*


# SCWE-018: Use of tx.origin for Authorization

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#relationships "Permanent link")

-   **CWE-346**: Origin Validation Error
    [https://cwe.mitre.org/data/definitions/346.html](https://cwe.mitre.org/data/definitions/346.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#description "Permanent link")

The use of `tx.origin` for authorization is a security vulnerability in which a smart contract checks the origin of the transaction to determine if a user is authorized to perform an action. This approach is flawed because `tx.origin` can be exploited by an attacker through a chain of transactions, allowing unauthorized users to interact with the contract. An attacker could trick the contract into performing an action on behalf of the victim by utilizing another contract in the transaction chain.

**Key Issues**: - Allows unauthorized transactions by using the `tx.origin` variable instead of `msg.sender`. - Vulnerable to phishing and reentrancy attacks, where attackers can use contracts to impersonate the victim. - Mismanagement of roles and improper transaction flow handling.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#remediation "Permanent link")

-   **Use `msg.sender` instead of `tx.origin`**: Always rely on `msg.sender` for authentication and authorization, as it correctly represents the immediate sender of the current call.
-   **Strict validation checks**: Ensure that authorization checks are done on the direct sender of the transaction, i.e., `msg.sender`, and not the originator.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#examples "Permanent link")

### Vulnerable Contract (Using `tx.origin` for Authorization)[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#vulnerable-contract-using-txorigin-for-authorization "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-3)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-10)    function restrictedAction() public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-11)        require(tx.origin == owner, "Only the owner can perform this action");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-12)        // Action code here    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-0-14)}`

In the vulnerable contract, the authorization check uses `tx.origin` to validate the caller. This is a problem because if the contract is called via another contract, `tx.origin` will return the original transaction sender (not the immediate caller), which opens up the contract to attacks such as phishing. The attacker can create a contract that interacts with the vulnerable contract on behalf of the victim.

### Fixed Contract (Using msg.sender for Authorization)[¶](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#fixed-contract-using-msgsender-for-authorization "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-3)contract Secure {     [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-10)    function restrictedAction() public {        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-11)        require(msg.sender == owner, "Only the owner can perform this action");        [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-12)        // Action code here    [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/#__codelineno-1-14)}`

In the fixed contract, `msg.sender` is used instead of `tx.origin`. This ensures that the contract checks the immediate sender of the call, which prevents attacks where malicious contracts impersonate the victim.
