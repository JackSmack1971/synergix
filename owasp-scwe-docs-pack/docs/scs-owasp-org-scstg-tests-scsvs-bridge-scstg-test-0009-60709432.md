---
title: "SCSTG-TEST-0009: Blockchain Data and State Management"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:18.288Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009.md "Edit this page")

# SCSTG-TEST-0009: Blockchain Data and State Management

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#description "Permanent link")

Effective management of blockchain data and state is crucial for ensuring the consistency and security of decentralized applications. Poor state management can lead to data corruption, inconsistencies between contracts, and vulnerabilities that attackers can exploit. Ensuring that data changes are properly tracked, validated, and secure is key to maintaining the integrity of the system. This includes ensuring that sensitive data is not exposed, and that critical functions such as state transitions are properly handled. This test focuses on validating that smart contracts effectively manage their state and data in a secure and robust manner.

* * *

### **Test 1: Validate Proper Use of Storage Variables**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#test-1-validate-proper-use-of-storage-variables "Permanent link")

#### Vulnerable Code[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-0-1)contract DataStorage {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-0-2)    uint256 public value; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-0-3)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-0-4)    function updateValue(uint256 newValue) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-0-5)        value = newValue;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-0-6)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-0-7)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#why-its-vulnerable "Permanent link")

-   The contract directly updates the state variable `value` without validating or securing the transaction, exposing the contract to potential manipulation.
-   If `newValue` is provided by an untrusted user, it could lead to data corruption or loss of value.

#### Fixed:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#fixed "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-1)contract SecureDataStorage {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-2)    uint256 public value;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-3)    address public owner; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-4)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-5)    modifier onlyOwner() {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-6)        require(msg.sender == owner, "Unauthorized");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-7)        _;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-9)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-10)    constructor() {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-11)        owner = msg.sender;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-12)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-13)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-14)    function updateValue(uint256 newValue) public onlyOwner {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-15)        value = newValue;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-16)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-1-17)}`

#### How to Check[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#how-to-check "Permanent link")

-   **Code Review:** Ensure that state variables are updated only through validated functions, and that access to sensitive operations is restricted through appropriate access controls.
-   **Testing:** Test the contract by submitting values from different sources and verify that the state is only updated when appropriate conditions are met.

* * *

### **Test 2: Ensure Proper Validation of External Data Inputs**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#test-2-ensure-proper-validation-of-external-data-inputs "Permanent link")

#### Vulnerable Code[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#vulnerable-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-1)contract ExternalData {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-2)    uint256 public externalValue; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-3)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-4)    function updateExternalData(address oracle) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-5)        // Vulnerable: call returns (bool, bytes); no success check; invalid assignment        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-6)        (bool success, bytes memory data) = oracle.call(abi.encodeWithSignature("getData()"));        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-7)        if (data.length >= 32) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-8)            externalValue = abi.decode(data, (uint256));  // Proceeds without checking success        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-9)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-10)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-2-11)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#why-its-vulnerable_1 "Permanent link")

#### Example 2: Unsecured External Data Sources[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#example-2-unsecured-external-data-sources "Permanent link")

-   The contract calls external data sources without validating the data properly, allowing attackers to feed false or malicious data.
-   The `oracle.call()` method exposes the contract to arbitrary external calls, which could result in unintended consequences.

#### Fixed:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#fixed_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-1)interface IOracle {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-2)    function getData() external view returns (uint256); [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-3)} [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-4)[](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-5)contract SecureExternalData {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-6)    uint256 public externalValue;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-7)    address public oracle; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-8)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-9)    modifier onlyOracle() {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-10)        require(msg.sender == oracle, "Unauthorized");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-11)        _;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-12)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-13)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-14)    constructor(address _oracle) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-15)        oracle = _oracle;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-16)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-17)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-18)    function updateExternalData() public onlyOracle {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-19)        externalValue = IOracle(oracle).getData();  // Safe interaction with oracle interface    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-20)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-3-21)}`

#### How to Check[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#how-to-check_1 "Permanent link")

-   **Code Review:** Look for external contract calls and ensure that proper validation mechanisms (e.g., access control and data validation) are in place.
-   **Dynamic Testing:** Attempt to feed invalid or malicious data to the contract and verify that it rejects the input or fails gracefully.

* * *

### **Test 3: Prevent Data Inconsistencies Through Proper Event Logging**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#test-3-prevent-data-inconsistencies-through-proper-event-logging "Permanent link")

#### Vulnerable Code[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#vulnerable-code_2 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-1)contract InconsistentState {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-2)    uint256 public data; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-3)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-4)    function setData(uint256 newData) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-5)        data = newData;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-6)        // No event emitted    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-7)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-4-8)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#why-its-vulnerable_2 "Permanent link")

-   The contract does not emit events after updating the state, leading to a lack of transparency and difficulty tracking state changes.
-   The absence of events makes it harder to detect inconsistencies or malicious changes to the data.

#### Fixed:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#fixed_2 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-1)contract ConsistentState {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-2)    uint256 public data; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-3)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-4)    event DataUpdated(uint256 newData); [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-6)    function setData(uint256 newData) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-7)        data = newData;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-8)        emit DataUpdated(newData);  // Emits event on state change    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-9)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#__codelineno-5-10)}`

#### How to Check[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BRIDGE/SCSTG-TEST-0009/#how-to-check_2 "Permanent link")

-   **Code Review:** Ensure that important state changes and data updates are accompanied by event emissions to track changes and ensure consistency.
-   **Testing:** Monitor the contract’s events and check that critical operations such as state changes are logged correctly.
