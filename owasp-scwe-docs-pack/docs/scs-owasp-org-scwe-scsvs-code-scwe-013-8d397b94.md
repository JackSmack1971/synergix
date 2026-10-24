---
title: "SCWE-013: Unauthorized Parameter Changes"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:22.822Z"
---
*Last updated: August 19, 2026*


# SCWE-013: Unauthorized Parameter Changes

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#relationships "Permanent link")

-   CWE-233: Improper Handling of Parameters [https://cwe.mitre.org/data/definitions/233.html](https://cwe.mitre.org/data/definitions/233.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#description "Permanent link")

Unauthorized parameter changes occur when privileged smart contract parameters—such as fees, governance rules, withdrawal limits, or security configurations—can be modified by a single entity or an unauthorized user. This can lead to **unexpected behavior, security risks, or financial loss** if an attacker gains access to the privileged account.

Key risks associated with unauthorized parameter changes: - **Single Point of Control**: A centralized owner can unilaterally alter critical parameters, leading to governance concerns. - **Malicious Modifications**: Attackers who exploit an access control flaw may change key parameters, resulting in stolen funds or manipulated contract logic. - **Lack of Transparency**: Hidden or undocumented parameter changes can mislead users and investors, reducing trust. - **Impact on DeFi Protocols**: Unauthorized changes to liquidity pool fees, interest rates, or reward mechanisms can disrupt incentives and harm protocol users.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#remediation "Permanent link")

-   **Use Role-Based Access Control (RBAC)**: Assign granular roles and restrict who can modify key parameters.
-   **Multisig Approval for Parameter Changes**: Require governance approval (e.g., Gnosis Safe) before making critical updates.
-   **Timelocks for Parameter Changes**: Introduce time delays on modifications to allow community review and prevent instant malicious changes.
-   **On-Chain Governance for DAOs**: Utilize decentralized governance mechanisms where stakeholders vote on parameter updates.
-   **Emit Events for Transparency**: Log all parameter changes on-chain to ensure visibility and auditability.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#examples "Permanent link")

### Example of a Contract With Unauthorized Parameter Changes (Centralized Control)[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#example-of-a-contract-with-unauthorized-parameter-changes-centralized-control "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-3)contract RiskyContract {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-5)    uint256 public feeRate; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-7)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-8)        owner = msg.sender;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-9)        feeRate = 5; // Default fee rate    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-12)    function updateFeeRate(uint256 newRate) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-13)        require(msg.sender == owner, "Only owner can update fee rate");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-14)        feeRate = newRate; // ❌ Single entity can modify a critical parameter at any time    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-15)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-0-16)}`

-   In this example, the owner can unilaterally change the fee rate, which poses a security risk.

### Refactored to Require Multisig and Timelocks[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#refactored-to-require-multisig-and-timelocks "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-3)interface ITimelock {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-4)    function queueTransaction(address target, uint256 value, bytes calldata data, uint256 eta) external;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-5)    function executeTransaction(address target, uint256 value, bytes calldata data, uint256 eta) external; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-6)} [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-7)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-8)contract SecureGovernance {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-9)    ITimelock public timelock;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-10)    uint256 public feeRate; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-12)    constructor(address _timelock) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-13)        timelock = ITimelock(_timelock);        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-14)        feeRate = 5; // Default fee rate    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-15)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-16)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-17)    function updateFeeRate(uint256 newRate) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-18)        bytes memory data = abi.encodeWithSignature("setFeeRate(uint256)", newRate);        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-19)        timelock.queueTransaction(address(this), 0, data, block.timestamp + 2 days); // ✅ Adds delay before execution    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-20)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-21)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-22)    function setFeeRate(uint256 newRate) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-23)        require(msg.sender == address(timelock), "Only timelock can execute");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-24)        feeRate = newRate;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-25)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/#__codelineno-1-26)}`

This improved version: - Uses a Timelock contract to delay parameter changes, preventing instant unauthorized updates. - Restricts execution to an approved governance mechanism, preventing a single actor from making direct changes.
