---
title: "SCWE-036: Inadequate Gas Limit Handling"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:37.924Z"
---
*Last updated: August 19, 2026*


# SCWE-036: Inadequate Gas Limit Handling

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [CWE-400 Link](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#description "Permanent link")

Inadequate gas limit handling occurs when a contract fails to manage gas constraints efficiently, leading to performance bottlenecks and denial-of-service (DoS) risks. Poor gas handling can result in: - Unoptimized execution: Unnecessary gas-heavy computations increasing costs. - DoS vulnerabilities: Transactions failing due to excessive gas usage, blocking operations. - Inefficient batch processing: Overloaded loops or storage updates causing out-of-gas (OOG) errors.

Unlike **SCWE-032**, which focuses on the protocol-level block gas limit, this issue arises due to poor gas management at the smart contract level.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#remediation "Permanent link")

-   **Optimize gas usage:** Minimize gas consumption in contract operations.
-   **Avoid unbounded loops:** Ensure loops have a fixed upper limit.
-   **Test thoroughly:** Conduct extensive testing to ensure operations stay within gas limits.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#examples "Permanent link")

-   **Inadequate Gas Handling**

    `[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-3)contract InefficientProcessing {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-4)    mapping(address => uint) public balances; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-6)    function batchTransfer(address[] memory recipients, uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-7)        for (uint i = 0; i < recipients.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-8)            balances[recipients[i]] += amount; // Gas-intensive operation        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-9)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-0-11)}`


**Issue:** Processes large arrays in a single transaction, which can fail due to out-of-gas errors.

Why is this a problem? - If recipients.length is too large, the transaction fails. - Attackers can exploit this by submitting large recipient lists, causing a DoS attack.

-   **Adequate Gas Handling**

    `[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-3)contract GasOptimizedProcessing {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-4)    mapping(address => uint) public balances; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-6)    function batchTransfer(address[] memory recipients, uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-7)        uint i = 0;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-8)        while (i < recipients.length && gasleft() > 50000) { // Stop before out of gas            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-9)            balances[recipients[i]] += amount;            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-10)            i++;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-11)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/#__codelineno-1-13)}`

    ✔️ Fix: Uses gasleft() to gracefully exit before running out of gas, ensuring some transfers complete. Why is this better? ✅ Prevents complete transaction failure by handling only as many iterations as gas allows. ✅ Reduces DoS risk by allowing partial execution instead of reverting everything. ✅ Enables retrying to complete all operations over multiple calls.

* * *
