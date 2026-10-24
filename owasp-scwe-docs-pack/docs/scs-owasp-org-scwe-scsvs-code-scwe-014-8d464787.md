---
title: "SCWE-014: Lack of Emergency Stop Mechanism"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:22.941Z"
---
*Last updated: August 19, 2026*


# SCWE-014: Lack of Emergency Stop Mechanism

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#relationships "Permanent link")

-   **CWE-693**: Protection Mechanism Failure
    [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#description "Permanent link")

A Lack of Emergency Stop Mechanism refers to the absence of a built-in feature in a smart contract that allows for halting or pausing critical operations during emergencies. This mechanism is essential for mitigating risks like a discovered vulnerability, unexpected behavior, or a malicious attack. Without this safeguard, the contract may continue executing malicious actions or suffer irreversible damage. The ability to stop critical functions provides an important recovery measure in scenarios where an exploit is detected or control needs to be regained.

Key risks: - Continuous execution of harmful or malicious actions without control. - Difficulty in recovering from unexpected failures. - Increased vulnerability to hacks or exploitation.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#remediation "Permanent link")

-   **Implement a pausable contract pattern**: Use the `Pausable` contract from the OpenZeppelin library to implement a mechanism that allows authorized users (e.g., the owner or a governance entity) to pause and unpause certain critical contract functions.
-   **Limit emergency stop to critical functions**: Ensure that only critical functions can be paused to minimize the impact on the rest of the system's operation.
-   **Implement role-based access control**: Use a role-based mechanism to control who has the ability to pause or unpause functions, reducing the risk of unauthorized access.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#examples "Permanent link")

### Lack of Emergency Stop Mechanism Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#lack-of-emergency-stop-mechanism-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-3)contract NoEmergencyStop {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-5)    uint public criticalValue; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-7)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-8)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-11)    // This function is critical and lacks an emergency stop mechanism    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-12)    function updateCriticalValue(uint newValue) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-13)        require(msg.sender == owner, "Only the owner can update this value");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-14)        criticalValue = newValue;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-15)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-0-16)}`

In the `NoEmergencyStop` contract, there is no way to stop or pause critical operations, which makes it vulnerable to continued exploitation if an issue arises.

### Fixed: Emergency Stop Mechanism Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#fixed-emergency-stop-mechanism-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-3)import "@openzeppelin/contracts/security/Pausable.sol"; // OZ 5.x: utils/Pausable.sol [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-5)contract EmergencyStopExample is Pausable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-6)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-7)    uint public criticalValue; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-9)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-10)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-12)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-13)    // Critical function that can be paused in case of emergency    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-14)    function updateCriticalValue(uint newValue) public whenNotPaused {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-15)        require(msg.sender == owner, "Only the owner can update this value");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-16)        criticalValue = newValue;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-18)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-19)    // Emergency stop function to pause the contract    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-20)    function emergencyStop() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-21)        require(msg.sender == owner, "Only the owner can stop the contract");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-22)        _pause();  // Pauses the contract    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-23)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-24)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-25)    // Emergency restart function to unpause the contract    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-26)    function resumeOperations() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-27)        require(msg.sender == owner, "Only the owner can resume the contract");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-28)        _unpause();  // Resumes the contract    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-29)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/#__codelineno-1-30)}`

The `EmergencyStopExample` contract implements the `Pausable` pattern, which allows the contract owner to pause and unpause critical functions using the `emergencyStop` and `resumeOperations` functions. This ensures that if a vulnerability is discovered or a critical issue occurs, the contract can be halted temporarily to prevent further damage.
