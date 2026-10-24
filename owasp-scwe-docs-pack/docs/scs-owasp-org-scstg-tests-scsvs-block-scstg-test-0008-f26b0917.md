---
title: "SCSTG-TEST-0008: Efficient Loop and Function Design"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:18.015Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008.md "Edit this page")

# SCSTG-TEST-0008: Efficient Loop and Function Design

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#description "Permanent link")

Inefficient loop and function designs in smart contracts can result in excessive gas consumption, leading to out-of-gas errors and potential denial-of-service (DoS) vulnerabilities. Smart contract security auditors must ensure that all loops and functions are optimized to operate within Ethereum's block gas limit.

### **Test 1: Detecting Unbounded Loops**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#test-1-detecting-unbounded-loops "Permanent link")

#### **Objective**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#objective "Permanent link")

Identify and mitigate the use of unbounded loops in contract code, as they are vulnerable to excessive gas usage.

#### **Vulnerable Code Example**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#vulnerable-code-example "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-3)contract UnboundedLoopExample {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-4)    uint[] public data; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-6)    function processAll() public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-7)        for (uint i = 0; i < data.length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-8)            // This operation scales with the size of the array            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-9)            data[i] = data[i] + 1;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-10)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-11)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-0-12)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#why-its-vulnerable "Permanent link")

The loop iterates over the entire `data` array, which could grow indefinitely.
\- For large arrays, gas consumption may exceed the block gas limit, causing the transaction to fail.
\- Attackers could exploit this by filling the array, making the function unusable for legitimate users.

### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#how-to-check "Permanent link")

-   **Code Review:** Look for `for` or `while` loops operating on dynamic arrays or mappings without size constraints.
-   **Dynamic Input Testing:** Test the function with a large dataset to simulate its behavior near the gas limit.
-   **Review Documentation:** Ensure the contract specifies constraints on data growth and function usage.

### **Fixed Code Example**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#fixed-code-example "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-3)contract BoundedLoopExample {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-4)    uint[] public data; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-6)    function processBatch(uint start, uint end) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-7)        require(end <= data.length, "End index out of bounds");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-8)        for (uint i = start; i < end; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-9)            data[i] = data[i] + 1;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-10)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-11)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-1-12)}`

* * *

### **Test 2: Identifying Inefficient Nested Loops**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#test-2-identifying-inefficient-nested-loops "Permanent link")

#### **Objective**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#objective_1 "Permanent link")

-   Detect and address inefficient nested loops that exponentially increase gas consumption.

### Vulnerable Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-3)contract NestedLoopExample {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-4)    uint[][] public matrix; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-6)    function processMatrix() public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-7)        for (uint i = 0; i < matrix.length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-8)            for (uint j = 0; j < matrix[i].length; j++) {                [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-9)                matrix[i][j] = matrix[i][j] * 2;            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-10)            }        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-11)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-12)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-2-13)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#why-its-vulnerable_1 "Permanent link")

Nested loops increase the complexity of the operation, leading to higher gas costs as input size increases.
\- Large datasets could render the function unusable within the gas limits, causing DoS conditions.

### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#how-to-check_1 "Permanent link")

-   **Code Review:** Examine nested loops in the code and assess their gas consumption relative to the input size.
-   **Gas Profiling:** Use tools like `eth-gas-reporter` to analyze gas usage during testing.
-   **Dynamic Testing:** Simulate scenarios with large `matrix` sizes to observe the contract’s behavior under stress.

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-3)contract OptimizedNestedLoopExample {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-4)    uint[][] public matrix; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-6)    function processMatrixBatch(uint startRow, uint endRow) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-7)        require(endRow <= matrix.length, "End row exceeds matrix size");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-8)        for (uint i = startRow; i < endRow; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-9)            for (uint j = 0; j < matrix[i].length; j++) {                [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-10)                matrix[i][j] = matrix[i][j] * 2;            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-11)            }        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-12)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-13)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/SCSTG-TEST-0008/#__codelineno-3-14)}`
