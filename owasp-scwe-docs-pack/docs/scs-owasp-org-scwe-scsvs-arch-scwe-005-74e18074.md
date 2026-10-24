---
title: "SCWE-005: Insecure Upgradeable Proxy Design"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:19.473Z"
---
*Last updated: August 19, 2026*


# SCWE-005: Insecure Upgradeable Proxy Design

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#relationships "Permanent link")

-   CWE-668: Exposure of Resource to Wrong Sphere [https://cwe.mitre.org/data/definitions/668.html](https://cwe.mitre.org/data/definitions/668.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#description "Permanent link")

Insecure upgradeable proxy designs occur when a smart contract implements an upgradeable proxy pattern without properly securing or validating upgrades. This may allow unauthorized actors to change the contract’s logic, possibly introducing malicious behavior. It often happens when the upgrade functionality lacks proper access controls or when there is no timelock to delay the upgrade, giving malicious actors an opportunity to exploit the contract.

This vulnerability can lead to critical failures, including the redirection of contract calls to malicious logic or unauthorized updates that compromise the integrity of the contract.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#remediation "Permanent link")

-   **Access Control:** Ensure only trusted parties (e.g., contract owners, multisig wallets) can perform upgrades.
-   **Timelock Mechanism:** Implement a timelock to delay upgrades and provide transparency.
-   **Transparent Proxy Pattern:** Use patterns that prevent unauthorized contract logic changes, such as the Transparent Proxy Pattern.
-   **Audit Proxy Logic Regularly:** Conduct regular audits to ensure that the upgrade mechanism is secure and follows best practices.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#examples "Permanent link")

### Vulnerable Proxy Contract[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#vulnerable-proxy-contract "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-3)contract VulnerableProxy {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-4)    address public implementation;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-7)    function setImplementation(address _implementation) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-8)        require(msg.sender == owner, "Only owner can set implementation");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-9)        implementation = _implementation;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-12)    function () public payable {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-13)        address _impl = implementation;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-14)        require(_impl != address(0), "Implementation address is zero");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-15)        assembly {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-16)            let result := delegatecall(gas, _impl, add(msg.data, 0x20), mload(msg.data), 0, 0)            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-17)            let size := returndatasize            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-18)            let ptr := mload(0x40)            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-19)            return(ptr, size)        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-20)        }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-21)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-0-22)}`

In this example, the `VulnerableProxy` contract allows the owner to update the implementation contract. If the owner is compromised, they can point the proxy to a malicious implementation, allowing the attacker to control the contract's logic.

### Fixed Proxy Contract with Secure Upgrade Mechanism[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#fixed-proxy-contract-with-secure-upgrade-mechanism "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-3)contract SecureProxy {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-4)    address public implementation;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-5)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-6)    uint public lastUpgradeTime;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-7)    uint public upgradeDelay = 1 days;  // 24 hours delay before upgrade [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-9)    modifier onlyOwner() {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-10)        require(msg.sender == owner, "Only owner can perform this action");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-11)        _;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-14)    modifier upgradeable() {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-15)        require(block.timestamp >= lastUpgradeTime + upgradeDelay, "Upgrade not allowed yet");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-16)        _;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-18)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-19)    function setImplementation(address _implementation) public onlyOwner upgradeable {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-20)        implementation = _implementation;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-21)        lastUpgradeTime = block.timestamp; // Update the last upgrade time    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-22)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-23)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-24)    function () public payable {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-25)        address _impl = implementation;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-26)        require(_impl != address(0), "Implementation address is zero");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-27)        assembly {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-28)            let result := delegatecall(gas, _impl, add(msg.data, 0x20), mload(msg.data), 0, 0)            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-29)            let size := returndatasize            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-30)            let ptr := mload(0x40)            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-31)            return(ptr, size)        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-32)        }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-33)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/#__codelineno-1-34)}`

In the fixed `SecureProxy` contract, the following changes have been made:

-   Access Control: The `onlyOwner` modifier ensures that only the contract owner can update the proxy’s implementation.
-   Timelock Mechanism: The `upgradeable` modifier adds a delay (set to 1 day in this example) to prevent rapid contract upgrades. The contract cannot be upgraded until the specified time has passed since the last upgrade.
-   Secure Upgrade Logic: The proxy logic is updated only after passing the necessary access control and timelock checks.
