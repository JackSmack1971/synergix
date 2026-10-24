---
title: "SCWE-010: Shadowing Variables and Functions"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:22.514Z"
---
*Last updated: August 19, 2026*


# SCWE-010: Shadowing Variables and Functions

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#relationships "Permanent link")

-   **CWE-1109: Use of Same Variable for Multiple Purposes**
    [CWE-1109](https://cwe.mitre.org/data/definitions/1109.html)
    Description: This weakness occurs when a variable is used for multiple purposes in a way that causes confusion, bugs, or unintentional side effects. In the context of smart contracts, shadowing variables leads to such misuse, as it causes ambiguity between different scopes.

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#description "Permanent link")

Shadowing variables or functions is a scenario where a local variable or function shares the same name as one in a larger or outer scope. This can cause ambiguity and lead to unexpected behavior or bugs, as the inner variable or function hides the outer one. This problem is especially tricky in Solidity due to its inheritance model, where a child contract might unintentionally override parent contract variables or functions.

### Key issues:[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#key-issues "Permanent link")

-   **Ambiguity**: The developer might not be aware that a variable or function is being hidden.
-   **Unintentional logic errors**: It may lead to the wrong variable being accessed, or the wrong function being called.
-   **Difficulty in debugging**: Shadowing makes the code harder to understand and trace, especially in complex contracts or when inheritance is involved.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#remediation "Permanent link")

-   **Use unique and descriptive names**: Always use unique names for variables and functions to avoid shadowing. Use clear, descriptive names for contract variables and functions.
-   **Avoid redeclaring variables in nested scopes**: Ensure that variables or functions in inner scopes don’t conflict with those in outer scopes.
-   **Static analysis tools**: Use static analysis tools to detect and warn about shadowing issues.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#examples "Permanent link")

### Example of Shadowing Variables and Functions[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#example-of-shadowing-variables-and-functions "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-3)contract ShadowingExample {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-6)    // This function shadows the 'balance' variable    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-7)    function deposit(uint balance) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-8)        // Local variable 'balance' now shadows the contract's balance variable        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-9)        balance += balance;  // This operation affects the local 'balance', not the contract's state variable    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-11)} [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-12)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-13)contract Test {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-14)    ShadowingExample example; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-15)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-16)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-17)        example = new ShadowingExample();    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-18)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-19)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-20)    function testDeposit() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-21)        example.deposit(100);  // Calling the deposit function on the example contract    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-22)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-0-23)}`

In the above example, the parameter `balance` in the `deposit` function shadows the contract’s state variable `balance`. This causes confusion, and the operation `balance += balance`; modifies the local variable instead of the contract state variable, leading to unexpected behavior.

### Fixed Code[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-3)contract ShadowingExample {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-4)    uint public balance; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-6)    // The parameter is renamed to avoid shadowing the state variable 'balance'    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-7)    function deposit(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-8)        balance += amount;  // Correctly updates the contract's state variable    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-10)} [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-11)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-12)contract Test {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-13)    ShadowingExample example; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-14)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-15)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-16)        example = new ShadowingExample();    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-18)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-19)    function testDeposit() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-20)        example.deposit(100);  // Calling the deposit function on the example contract    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-21)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/#__codelineno-1-22)}`

In the optimized version, the function parameter is renamed from `balance` to `amount` to avoid shadowing the state variable. This clears up the ambiguity and ensures the function operates on the contract's state variable, not the local variable.
