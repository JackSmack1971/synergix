---
title: "Denial of Service (DoS)"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:17.740Z"
---
# Denial of Service (DoS)

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#description "Permanent link")

Denial of Service (DoS) vulnerabilities occur when a smart contract or system is made unavailable to its users by exhausting computational resources or blocking critical operations. This type of vulnerability can result from inefficient function design, excessive gas usage, or unhandled failure conditions. DoS attacks can lead to degraded performance, halted operations, and a poor user experience. To prevent DoS vulnerabilities, developers must carefully design gas-efficient operations, handle errors gracefully, and mitigate the risk of resource exhaustion.

### **Example: Unbounded Loop with User Input**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#example-unbounded-loop-with-user-input "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-3)contract GasDoSVulnerable {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-4)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-6)    // Allows a user to send tokens to many recipients in one transaction.    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-7)    function bulkTransfer(address[] memory recipients, uint256[] memory amounts) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-8)        require(recipients.length == amounts.length, "Invalid input"); [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-9)        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-10)        for (uint256 i = 0; i < recipients.length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-11)            require(amounts[i] > 0, "Amount must be greater than zero");            [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-12)            balances[recipients[i]] += amounts[i];        [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-13)        }    [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-14)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#__codelineno-0-15)}`

### **Impact**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#impact "Permanent link")

-   **Gas Limit Exhaustion**: Functions that rely on loops with dynamic input sizes or unoptimized logic can lead to excessive gas consumption. This can result in transactions exceeding the block gas limit, causing out-of-gas errors or failing to complete.
-   **Transaction Failures**: Without adequate handling of gas usage or error conditions, contracts can fail unexpectedly, preventing legitimate operations and denying service to users.
-   **Resource Exhaustion**: Improperly managed resource consumption, such as large data queries or excessive loop iterations, can overwhelm the system, causing DoS by exhausting computational resources or making the contract unavailable for further interactions.
-   **Increased Transaction Costs**: Inefficient gas usage may lead to higher transaction fees, discouraging users from interacting with the contract or causing network congestion.

### **Remediation**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#remediation "Permanent link")

#### Efficient Loop and Function Design:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#efficient-loop-and-function-design "Permanent link")

-   Optimize functions with loops to reduce gas consumption and prevent DoS attacks by ensuring that loops operate with fixed or minimal input sizes. Avoid using large dynamic data arrays in loops.
-   Ensure critical functions, like `burn()`, handle failures gracefully, so that the contract does not enter an unrecoverable state.
-   Protect against griefing attacks by managing gas consumption carefully, ensuring that operations are efficient and do not hit gas limits.

#### Fallback Mechanisms:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#fallback-mechanisms "Permanent link")

-   Implement try/catch blocks with sufficient gas to prevent unexpected failures from leaving the contract in an inconsistent or unresponsive state.
-   Design fallback mechanisms that ensure errors are caught and handled without causing DoS vulnerabilities, such as failing silently or leaving contracts in a halted state.

#### Rate Limiting and Resource Management:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#rate-limiting-and-resource-management "Permanent link")

-   Avoid blocking mechanisms that could lead to DoS attacks. For example, ensure that excessive queries or operations are handled efficiently, especially when dealing with external systems or large datasets.
-   Use rate limiting or batching for high-volume transactions to prevent overwhelming the system or consuming excessive resources.
-   Implement efficient error handling for external function calls to ensure that the contract doesn't fail or become unresponsive due to unchecked return values or failed external interactions.

#### Error Handling:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-BLOCK/overview/#error-handling "Permanent link")

-   Ensure that assertions do not lead to DoS by carefully checking conditions and ensuring that failures are handled appropriately, rather than causing reverts that impact overall system availability.
-   Protect against DoS due to unexpected reverts by considering all possible failure scenarios in the contract's logic and providing proper fallback solutions.
-   Ensure functions like `supportsERC165InterfaceUnchecked()` in the ERC165Checker.sol handle large data queries efficiently, minimizing the risk of resource exhaustion.
