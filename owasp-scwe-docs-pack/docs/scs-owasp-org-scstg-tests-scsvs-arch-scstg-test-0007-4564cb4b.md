---
title: "SCSTG-TEST-0007: Modularity and Upgradability"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:15.008Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007.md "Edit this page")

# SCSTG-TEST-0007: Modularity and Upgradability

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#description "Permanent link")

Modularity and upgradability are essential principles for the long-term security and maintainability of smart contracts. Poor modularity often leads to monolithic designs that combine critical logic and storage, making it difficult to upgrade, audit, or scale the system. Without controlled upgrade mechanisms, an attacker could exploit weaknesses in the upgrade process, leading to unauthorized contract changes or the introduction of security flaws. Ensuring a well-structured contract with clear modular separation, as well as a secure upgrade process, is crucial to avoiding such vulnerabilities.

* * *

### **Test 1: Ensure Proper Separation of Logic and State**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#test-1-ensure-proper-separation-of-logic-and-state "Permanent link")

#### Vulnerable Code[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-1)contract Monolithic {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-2)    uint256 public data;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-3)    address public admin; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-4)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-5)    function updateData(uint256 _data) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-6)        require(msg.sender == admin, "Unauthorized");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-7)        data = _data;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-9)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-10)    function upgrade(address newAdmin) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-11)        require(msg.sender == admin, "Unauthorized");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-12)        admin = newAdmin;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-13)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-0-14)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#why-its-vulnerable "Permanent link")

-   The monolithic design combines logic and state in a single contract, making upgrades risky.
-   Changes to storage or logic could inadvertently corrupt existing data.
-   The lack of separation makes it more difficult to isolate bugs or vulnerabilities in logic.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-1)contract Logic {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-2)    address public admin;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-3)    Storage public storageContract; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-4)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-5)    constructor(address _storageContract) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-6)        admin = msg.sender;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-7)        storageContract = Storage(_storageContract);    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-9)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-10)    function updateData(uint256 _data) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-11)        require(msg.sender == admin, "Unauthorized");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-12)        storageContract.setData(_data);    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-13)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-14)} [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-15)[](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-16)contract Storage {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-17)    uint256 public data; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-18)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-19)    function setData(uint256 _data) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-20)        data = _data;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-21)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-1-22)}`

#### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#how-to-check "Permanent link")

-   Code Review: Verify the separation of logic and storage into separate contracts.
-   Storage Analysis: Ensure that the storage layout remains intact when upgrading the contract logic, and that no data corruption occurs.

### **Test 2: Verify Secure and Controlled Upgrade Mechanism**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#test-2-verify-secure-and-controlled-upgrade-mechanism "Permanent link")

#### Vulnerable Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#vulnerable-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-2-1)contract Proxy {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-2-2)    address public implementation; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-2-3)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-2-4)    function upgrade(address newImplementation) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-2-5)        implementation = newImplementation;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-2-6)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-2-7)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#why-its-vulnerable_1 "Permanent link")

-   The upgrade function is not protected with any access control, allowing any user to replace the implementation contract. This opens the door for malicious actors to hijack the contract functionality.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#fixed-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-1)contract SecureProxy {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-2)    address public implementation;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-3)    address public admin; [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-4)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-5)    modifier onlyAdmin() {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-6)        require(msg.sender == admin, "Unauthorized");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-7)        _;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-9)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-10)    function upgrade(address newImplementation) public onlyAdmin {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-11)        implementation = newImplementation;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-12)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#__codelineno-3-13)}`

#### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-ARCH/SCSTG-TEST-0007/#how-to-check_1 "Permanent link")

-   Code Review: Ensure that upgrade functions are protected by access control mechanisms (e.g., only the admin can upgrade).
-   Dynamic Testing: Attempt to perform an unauthorized upgrade to verify that the access control works as intended.
