---
title: "SCSTG-TEST-0015: Testing Business Logic and Economic Security"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:15.613Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015.md "Edit this page")

# SCSTG-TEST-0015: Testing Business Logic and Economic Security

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#description "Permanent link")

Business logic and economic security are crucial for ensuring that smart contracts function as intended and that the economic incentives align with the intended use cases. If vulnerabilities in the logic or economic models are present, attackers may exploit them for financial gain. This test focuses on reviewing economic models, incentive structures, and tokenomics to ensure that smart contracts are designed to prevent logic flaws, reentrancy attacks, and malicious economic manipulation.

* * *

### **Test 1: Ensure Economic Model Integrity and Prevent Logic Flaws**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#test-1-ensure-economic-model-integrity-and-prevent-logic-flaws "Permanent link")

#### Vulnerable Code[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-3)contract IncentiveModel {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-4)    uint256 public rewardPool; [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-6)    function distributeRewards(address[] memory users) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-7)        uint256 reward = rewardPool / users.length;  // Dividing the total reward pool among users        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-8)        for (uint256 i = 0; i < users.length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-9)            (bool ok, ) = payable(users[i]).call{value: reward}("");            [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-10)            require(ok, "Transfer failed");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-11)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-12)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-0-13)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#why-its-vulnerable "Permanent link")

-   If the `users` array is empty, the division by zero will occur, leading to a runtime exception.
-   Additionally, if the reward pool is too small or the number of users is too large, it could cause unexpected behavior, leading to attackers exploiting the system by flooding the contract with too many addresses.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-3)contract SecureIncentiveModel {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-4)    uint256 public rewardPool; [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-6)    modifier nonZeroUsers(address[] memory users) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-7)        require(users.length > 0, "No users provided");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-8)        _;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-9)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-10)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-11)    function distributeRewards(address[] memory users) public nonZeroUsers(users) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-12)        uint256 reward = rewardPool / users.length;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-13)        require(reward > 0, "Reward amount is too low");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-14)        for (uint256 i = 0; i < users.length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-15)            (bool ok, ) = payable(users[i]).call{value: reward}("");            [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-16)            require(ok, "Transfer failed");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-17)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-18)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#__codelineno-1-19)}`

### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-GOV/SCSTG-TEST-0015/#how-to-check "Permanent link")

-   **Code Review:** Look for scenarios where division or mathematical operations could result in errors like division by zero or unintended behavior due to extreme input values.
-   **Dynamic Testing:** Test the function with edge cases such as empty user lists, very large user arrays, and reward pool sizes. Ensure that the system handles these cases gracefully and does not allow unexpected errors or exploits.
