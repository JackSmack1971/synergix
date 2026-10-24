---
title: "SCSTG-TEST-0014: Test Gas Usage in Loops"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:18.532Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014.md "Edit this page")

# SCSTG-TEST-0014: Test Gas Usage in Loops

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#description "Permanent link")

Efficient gas usage is critical in smart contract development to ensure transactions are cost-effective and do not exceed block gas limits. Poorly optimized contracts can result in high transaction costs, failed transactions, and potential denial of service (DoS) attacks. Optimizing gas usage helps ensure that smart contracts are scalable, cost-effective, and maintain the overall security of decentralized applications (dApps). This test focuses on ensuring that gas usage is properly optimized, and contracts are designed to operate efficiently within the constraints of Ethereum's gas limits.

* * *

### **Test 1: Validate Gas Usage in Loops**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#test-1-validate-gas-usage-in-loops "Permanent link")

#### **Vulnerable Code**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-3)contract GasInefficient {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-4)    uint256[] public data; [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-6)    function addData(uint256[] memory newData) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-7)        for (uint i = 0; i < newData.length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-8)            data.push(newData[i]);  // Inefficient loop causing high gas costs        [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-9)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-10)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-0-11)}`

#### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#why-its-vulnerable "Permanent link")

-   This contract uses a loop to iterate over an input array and push data into a dynamic array.
-   The gas cost increases linearly with the size of the input array. For large datasets, this can lead to excessive gas usage, potentially causing the transaction to exceed the block gas limit.
-   Smart contracts with inefficient loops that grow dynamically can become unmanageable when interacting with large datasets.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-3)contract OptimizedGas {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-4)    uint256[] public data; [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-6)    function addData(uint256[] memory newData) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-7)        uint256 length = newData.length;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-8)        for (uint i = 0; i < length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-9)            data.push(newData[i]);  // Optimized by storing array length outside the loop        [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-10)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-11)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#__codelineno-1-12)}`

#### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-DEFI/SCSTG-TEST-0014/#how-to-check "Permanent link")

-   **Code Review:** Ensure that loops and functions which deal with dynamic data structures are optimized for gas usage. Look for unnecessary state changes or excessive iterations within a single transaction.
-   **Gas Estimation:** Use tools like eth-gas-reporter or Remix IDE to estimate gas usage before and after optimizations.
-   **Dynamic Testing:** Test the contract with various input sizes and check that it performs within reasonable gas limits, ensuring it doesn't exceed the block gas limit.
