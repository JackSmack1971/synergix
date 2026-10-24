---
title: "SCSTG-TEST-0011: Test Contract Interactions"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:16.989Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011.md "Edit this page")

# SCSTG-TEST-0011: Test Contract Interactions

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#description "Permanent link")

Ensuring secure interactions and communications in smart contracts is crucial for protecting against unauthorized access, manipulation, and attacks. This includes ensuring that contracts interact securely with external contracts, manage oracle integrations safely, and use secure methods for cross-chain and bridge operations. A failure to adhere to best practices for these interactions can expose the contract to vulnerabilities such as reentrancy, front-running, or incorrect data feeds. This test focuses on validating that smart contracts perform secure interactions and communications, safeguarding the system from common attack vectors.

* * *

### **Test 1: Ensure Secure Contract Interactions**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#test-1-ensure-secure-contract-interactions "Permanent link")

#### **Vulnerable Code:**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-1)pragma solidity ^0.5.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-3)contract VulnerableContract {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-4)    address public trustedAddress; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-6)    constructor(address _trustedAddress) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-7)        trustedAddress = _trustedAddress;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-9)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-10)    function callExternalContract(address _to, uint256 _value) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-11)        _to.call{value: _value}(""); // Vulnerable to reentrancy or other attacks    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-12)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-0-13)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#why-its-vulnerable "Permanent link")

-   The contract uses `.call` to make external calls, which is generally unsafe and susceptible to reentrancy attacks.
-   The function allows anyone to trigger the call and transfer funds, exposing the contract to potential attacks.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-3)contract SecureContract {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-4)    address public trustedAddress; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-6)    constructor(address _trustedAddress) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-7)        trustedAddress = _trustedAddress;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-9)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-10)    function callExternalContract(address _to, uint256 _value) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-11)        require(_to != address(0), "Invalid address");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-12)        (bool success, ) = _to.call{value: _value}("");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-13)        require(success, "External call failed");    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-14)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#__codelineno-1-15)}`

### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMM/SCSTG-TEST-0011/#how-to-check "Permanent link")

-   **Code Review:** Look for external calls in the contract and ensure that they are using safe methods such as `transfer` or `send` where appropriate, or implementing reentrancy protection.
-   **Static Analysis:** Use static analysis tools like SolidityScan, MythX or Slither to detect unsafe calls in the code.
-   **Dynamic Testing:** Simulate a reentrancy attack by deploying a contract that calls the vulnerable contract and tries to drain funds.
