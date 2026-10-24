---
title: "SCWE-012: Lack of Multisig Governance"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:28.225Z"
---
*Last updated: August 19, 2026*


# SCWE-012: Lack of Multisig Governance

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#relationships "Permanent link")

-   CWE-285: Improper Authorization
    [https://cwe.mitre.org/data/definitions/285.html](https://cwe.mitre.org/data/definitions/285.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#description "Permanent link")

Lack of multisig governance occurs when critical smart contract functions, such as upgrades, fund withdrawals, or parameter changes, are controlled by a single entity. This creates a **single point of failure**, increasing the risk of **compromise, insider abuse, or unauthorized access**. Without multisig governance, attackers or malicious actors can easily exploit privileged functions if the private key of a single administrator is compromised.

Key risks associated with missing multisig governance: - **Centralization Risk**: A single entity can control and modify key contract parameters. - **Single Point of Failure**: Loss or compromise of the owner's private key can result in catastrophic consequences. - **Unauthorized Access**: An attacker gaining control of the private key can execute privileged functions without approval. - **Lack of Accountability**: Decisions are made unilaterally, reducing transparency and security.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#remediation "Permanent link")

-   **Implement a Multisig Wallet**: Use multisignature schemes (e.g., Gnosis Safe) to require multiple signers for critical transactions.
-   **Role-Based Access Control (RBAC)**: Assign multiple roles with different privileges to prevent centralized control.
-   **Timelocks for Critical Functions**: Introduce a delay for privileged actions, allowing time for community intervention if needed.
-   **On-Chain Governance Mechanisms**: Decentralize decision-making using **DAO-based governance** where applicable.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#examples "Permanent link")

### Example of a Contract Without Multisig Governance (Centralized Owner)[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#example-of-a-contract-without-multisig-governance-centralized-owner "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-3)contract CentralizedGovernance {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-4)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-6)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-7)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-10)    function upgradeContract(address newContract) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-11)        require(msg.sender == owner, "Only owner can upgrade");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-12)        // Only a single owner can perform critical actions    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-14)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-15)    function withdrawFunds(address payable recipient, uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-16)        require(msg.sender == owner, "Only owner can withdraw funds");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-17)        (bool ok, ) = recipient.call{value: amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-18)        require(ok, "Transfer failed"); // ❌ No multisig verification    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-19)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-0-20)}`

-   In this example, all governance actions depend on a single owner, making it a high-risk design.

### Refactored to Use Multisig Governance[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#refactored-to-use-multisig-governance "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-3)interface IMultiSig {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-4)    function submitTransaction(address destination, uint256 value, bytes calldata data) external; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-5)} [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-6)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-7)contract SecureGovernance {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-8)    IMultiSig public multisigWallet; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-10)    constructor(address _multisigWallet) {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-11)        multisigWallet = IMultiSig(_multisigWallet);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-14)    function upgradeContract(address newContract) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-15)        bytes memory data = abi.encodeWithSignature("upgradeTo(address)", newContract);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-16)        multisigWallet.submitTransaction(address(this), 0, data); // ✅ Requires multisig approval    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-18)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-19)    function withdrawFunds(address payable recipient, uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-20)        bytes memory data = abi.encodeWithSignature("transfer(address,uint256)", recipient, amount);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-21)        multisigWallet.submitTransaction(address(this), 0, data); // ✅ Multisig verification for withdrawals    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-22)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/#__codelineno-1-23)}`

-   This improved version delegates authority to a multisig wallet, requiring multiple approvals before executing critical actions.
