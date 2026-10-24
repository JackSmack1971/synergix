---
title: "SCWE-004: Uncaught Exceptions"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:19.344Z"
---
*Last updated: August 19, 2026*


# SCWE-004: Uncaught Exceptions

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#relationships "Permanent link")

-   CWE-703: Improper Check or Handling of Exceptional Conditions
    [https://cwe.mitre.org/data/definitions/703.html](https://cwe.mitre.org/data/definitions/703.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#description "Permanent link")

Uncaught exceptions occur when a smart contract fails to properly handle errors, leading to unintended behaviors, lost funds, or denial of service (DoS). In Solidity, low-level calls such as `call()`, `delegatecall()`, and `send()` return a boolean instead of reverting automatically, requiring explicit checks. Ignoring return values or using `assert()` instead of `require()` can result in vulnerabilities that attackers can exploit.

Common issues with uncaught exceptions: - Ignoring return values of `call()`, `delegatecall()`, `send()` - Unchecked external contract calls - Incorrect use of `assert()` instead of `require()` - Failure to catch errors in `try/catch` blocks

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#remediation "Permanent link")

-   **Check Return Values:** Always verify the return values of low-level calls to ensure execution succeeded.
-   **Use `require()` for Input Validation:** `require()` should be used for checking user input, while `assert()` should only be used for invariants.
-   **Implement Try/Catch:** Use `try/catch` when interacting with external contracts to prevent silent failures.
-   **Use Safe Libraries:** Utilize OpenZeppelin’s `SafeERC20` for secure token transfers.
-   **Minimize External Dependencies:** Avoid relying on external contract behavior unless necessary.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#examples "Permanent link")

### Example 1: Uncaught Exception:[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#example-1-uncaught-exception "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-0-3)contract UncheckedCall {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-0-4)    function execute(address target, bytes memory data) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-0-5)        target.call{value: msg.value}(data); // ❌ No success check    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-0-7)}`

In the above example, `call()` returns a boolean indicating success, but it is ignored, which can lead to silent failures.

### Refactored to Handle Exceptions Properly:[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#refactored-to-handle-exceptions-properly "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-3)contract SafeCall {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-4)    function execute(address target, bytes memory data) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-5)        (bool success, bytes memory returnData) = target.call{value: msg.value}(data);        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-6)        require(success, "Call execution failed"); // ✅ Handle failure    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-1-8)}`

In this improved version, the contract checks whether `call()` was successful, preventing execution from continuing on failure.

### Example 2: Bad Practice (Using assert() Instead of require())[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#example-2-bad-practice-using-assert-instead-of-require "Permanent link")

-   Problem: Using assert() for input validation instead of require().

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-3)contract WrongAssertion {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-4)    function withdraw(uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-5)        assert(amount > 0); // ❌ Assert should not be used for input validation        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-6)        // Withdraw logic here    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-7)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-2-8)}`

Why is this vulnerable? - `assert()` is meant for invariants, not input validation. - If `assert()` fails, it consumes all remaining gas and does not return gas to the caller.

### Better Practice (Fixing Input Validation)[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#better-practice-fixing-input-validation "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-3)contract CorrectValidation {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-4)    function withdraw(uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-5)        require(amount > 0, "Invalid amount"); // ✅ Proper validation        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-6)        // Withdraw logic here    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-7)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-3-8)}`

\- Now, a proper `require()` statement prevents execution if amount is invalid.

### Example 3: Bad Practice (Failure to Catch Errors in Try/Catch)[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#example-3-bad-practice-failure-to-catch-errors-in-trycatch "Permanent link")

-   Problem: Not using try/catch for external contract calls.

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-3)interface ExternalContract {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-4)    function riskyFunction() external; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-5)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-6)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-7)contract NoErrorHandling {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-8)    function callExternal(address contractAddr) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-9)        ExternalContract(contractAddr).riskyFunction(); // ❌ No error handling    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-10)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-4-11)}`

Why is this vulnerable? - If riskyFunction() fails, the transaction completely reverts. - There is no way to recover or take alternative action.

### Better Practice (Using Try/Catch for External Calls)[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#better-practice-using-trycatch-for-external-calls "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-3)interface ExternalContract {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-4)    function riskyFunction() external; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-5)} [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-6)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-7)contract SafeExternalCall {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-8)    function callExternal(address contractAddr) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-9)        try ExternalContract(contractAddr).riskyFunction() {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-10)            // ✅ Success case        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-11)        } catch {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-12)            revert("External call failed"); // ✅ Catch and handle failure        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-13)        }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-14)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/#__codelineno-5-15)}`

\- Now, errors are properly caught, and alternative actions can be taken.
