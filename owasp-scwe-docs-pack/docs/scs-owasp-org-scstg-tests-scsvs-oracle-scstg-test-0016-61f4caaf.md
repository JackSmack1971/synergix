---
title: "SCSTG-TEST-0016: Testing Arithmetic and Logic Security"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:17.588Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016.md "Edit this page")

# SCSTG-TEST-0016: Testing Arithmetic and Logic Security

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#description "Permanent link")

Preventing arithmetic overflow and underflow is critical for maintaining the integrity and security of smart contracts. If a contract performs arithmetic operations without proper safeguards, it is vulnerable to overflow and underflow issues, which can be exploited by attackers to manipulate contract behavior, causing unexpected results or loss of funds.

* * *

### **Test 1: Ensure Safe Math Operations are Used**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#test-1-ensure-safe-math-operations-are-used "Permanent link")

#### Vulnerable Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-3)contract UnsafeMath {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-4)    uint256 public balance; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-6)    function addFunds(uint256 _amount) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-7)        balance += _amount;  // Possible overflow if balance + _amount exceeds max uint256 value    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-0-9)}`

#### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#why-its-vulnerable "Permanent link")

The contract does not use a safe math library to perform arithmetic operations. If the balance exceeds uint256's maximum value (2^256 - 1), an overflow occurs.
This can result in unexpected contract behavior or a reset of the balance value, allowing attackers to manipulate the contract.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-3)contract SafeMath {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-4)    using SafeMath for uint256;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-5)    uint256 public balance; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-6)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-7)    function addFunds(uint256 _amount) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-8)        balance = balance.add(_amount);  // Safe addition using SafeMath to prevent overflow    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-9)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-1-10)}`

#### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#how-to-check "Permanent link")

-   **Code Review:** Check that all arithmetic operations use libraries such as SafeMath (for older versions) or rely on Solidity 0.8’s built-in overflow checks.
-   **Testing:** Use edge cases such as adding large values to check if the contract prevents overflow.

* * *

### **Test 2: Verify Correct Use of Fixed-Point Arithmetic**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#test-2-verify-correct-use-of-fixed-point-arithmetic "Permanent link")

#### Vulnerable Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#vulnerable-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-3)contract FixedPointExample {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-4)    uint256 public totalSupply; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-6)    function calculateReward(uint256 _rewardPercentage) public view returns (uint256) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-7)        return totalSupply * _rewardPercentage / 100;  // Simple calculation without considering fixed-point precision    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-2-9)}`

#### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#why-its-vulnerable_1 "Permanent link")

The function performs division without accounting for fixed-point precision. This could result in rounding errors, especially for small percentage values.
Using integer division directly leads to truncation, causing inaccuracies in reward calculations.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#fixed-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-3)contract FixedPointExample {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-4)    uint256 public totalSupply;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-5)    uint256 constant FIXED_POINT = 1e18;  // Set a scaling factor for fixed-point precision [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-6)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-7)    function calculateReward(uint256 _rewardPercentage) public view returns (uint256) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-8)        return (totalSupply * _rewardPercentage * FIXED_POINT) / 100 / FIXED_POINT;  // Proper fixed-point arithmetic    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-9)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#__codelineno-3-10)}`

#### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ORACLE/SCSTG-TEST-0016/#how-to-check_1 "Permanent link")

-   **Code Review:** Verify that fixed-point arithmetic is implemented using appropriate scaling factors (e.g., 1e18) to avoid precision loss.
-   **Dynamic Testing:** Test the function with small values for `_rewardPercentage` and check that the result is accurate, verifying that there is no unexpected rounding behavior.
