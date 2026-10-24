---
title: "SCWE-007: Presence of Unused Variables"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:22.128Z"
---
*Last updated: August 19, 2026*


# SCWE-007: Presence of Unused Variables

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#relationships "Permanent link")

-   CWE-563: Assignment to Variable with No Effect [https://cwe.mitre.org/data/definitions/563.html](https://cwe.mitre.org/data/definitions/563.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#description "Permanent link")

The presence of unused variables in smart contracts refers to variables that are declared but never utilized in the contract logic. These variables consume storage or memory space unnecessarily, potentially wasting gas when deployed or executed. This situation often arises due to incomplete code, forgotten variables, or code that was intended for future use but never implemented. The presence of such variables increases the attack surface by making it harder to understand the contract and opens up potential vulnerabilities.

Some common risks include: - Wasted gas due to storage and memory consumption. - Increased complexity and difficulty in understanding contract behavior. - Potential confusion for auditors or future developers working on the contract.

Unused variables can also hide logic errors or indicate that parts of the contract are not functioning as intended.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#remediation "Permanent link")

-   **Remove Unused Variables:** Ensure that any variables that are not required for the contract’s functionality are removed.
-   **Code Review and Refactoring:** Regularly review and refactor the code to eliminate dead or unnecessary variables.
-   **Automated Static Analysis Tools:** Use static analysis tools to detect unused variables and other unnecessary code patterns.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#examples "Permanent link")

### Contract with Unused Variables[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#contract-with-unused-variables "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-3)contract UnusedVariables {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-4)    uint public balance;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-5)    uint public unusedVariable; // This variable is not used anywhere [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-7)    function deposit(uint amount) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-8)        require(msg.value == amount, "ETH amount mismatch");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-9)        balance += amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-12)    function withdraw(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-13)        balance -= amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-14)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-0-15)}`

In the example above, the `unusedVariable` is declared but never used within the contract. This is a waste of storage space and can confuse anyone reading or auditing the code.

### Fixed Code with Unused Variables Removed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#fixed-code-with-unused-variables-removed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-3)contract FixedUnusedVariables {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-6)    function deposit(uint amount) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-7)        require(msg.value == amount, "ETH amount mismatch");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-8)        balance += amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-11)    function withdraw(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-12)        require(balance >= amount, "Insufficient balance");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-13)        balance -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-14)        (bool success, ) = msg.sender.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-15)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/#__codelineno-1-17)}`

The improved contract removes the unnecessary `unusedVariable`, reducing the complexity and improving gas efficiency.
