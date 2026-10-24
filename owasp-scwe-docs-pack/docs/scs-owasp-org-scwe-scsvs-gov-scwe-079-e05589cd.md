---
title: "SCWE-079: Insecure Use of Transfer and Send"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.124Z"
---
*Last updated: August 19, 2026*


# SCWE-079: Insecure Use of Transfer and Send

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#description "Permanent link")

The use of `.transfer()` and `.send()` for Ether transfers in Solidity is insecure because they impose a fixed gas limit of 2300 gas. This restriction can cause transactions to fail unexpectedly when the receiving contract has complex logic that requires more gas. Additionally, it can result in a Denial of Service (DoS) vulnerability if the receiving contract cannot execute due to insufficient gas.

This issue is especially problematic in upgradable smart contracts or protocol interactions, where the gas requirements of a receiving contract might change over time.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#remediation "Permanent link")

Instead of `.transfer()` and `.send()`, use `.call{value: msg.value}("")`, which allows more flexible gas allocation and prevents DoS risks. Always check for the return value of `.call()` to ensure the transfer was successful.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-4)    function transferEther(address payable _to) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-5)        // Fixed gas limit of 2300 gas can cause unintended failures        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-6)        _to.transfer(msg.value);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-0-8)}`

**Problem**: - If `_to` is a contract that requires more than `2300 gas` (e.g., it has a fallback function with state changes), this transfer will fail. - The contract has no error handling, meaning the sender won't be aware of the failure.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-4)    function transferEther(address payable _to) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-5)        // Use call() for better gas flexibility and proper error handling        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-6)        (bool success, ) = _to.call{value: msg.value}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-7)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/#__codelineno-1-9)}`

**Why is this better?** - `.call{value: msg.value}("")` does not impose a gas limit, allowing the receiving contract to execute as needed. - It includes a `require(success, "Transfer failed");` check, ensuring failures are properly handled.
