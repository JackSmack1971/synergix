---
title: "SC01:2025 Access Control Vulnerabilities"
source_url: "https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:02.041Z"
---
# SC01:2025 Access Control Vulnerabilities

## Vulnerability: Improper Access Control[¶](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#vulnerability-improper-access-control "Permanent link")

### Description:[¶](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#description "Permanent link")

An access control vulnerability is a security flaw that allows unauthorized users to access or modify the contract's data or functions. These vulnerabilities arise when the contract's code fails to adequately restrict access based on user permission levels. Access control in smart contracts can relate to governance and critical logic, such as minting tokens, voting on proposals, withdrawing funds, pausing and upgrading the contracts, and changing ownership.

### Example (Vulnerable contract):[¶](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#example-vulnerable-contract "Permanent link")

`[](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-4)contract Solidity_AccessControl {     [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-5)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-6)    [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-7)    // Burn function with no access control    [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-8)    function burn(address account, uint256 amount) public {        [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-9)        require(balances[account] >= amount, "Insufficient balance");        [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-10)        balances[account] -= amount;    [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-11)    } [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-0-12)}`

### Impact:[¶](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#impact "Permanent link")

-   Attackers can gain unauthorized access to critical functions and data within the contract, compromising its integrity and security.
-   Vulnerabilities can lead to the theft of funds or assets controlled by the contract, causing significant financial damage to users and stakeholders.

### Remediation:[¶](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#remediation "Permanent link")

-   Ensure initialization functions can only be called once and exclusively by authorized entities.
-   Use established access control patterns like Ownable or RBAC (Role-Based Access Control) in your contracts to manage permissions and ensure that only authorized users can access certain functions. This can be done by adding appropriate access control modifiers, such as `onlyOwner` or custom roles to sensitive functions.

### Example (Fixed version):[¶](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#example-fixed-version "Permanent link")

`[](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-4)// Import the Ownable contract from OpenZeppelin to manage ownership [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-5)import "@openzeppelin/contracts/access/Ownable.sol"; [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-6)[](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-7)contract Solidity_AccessControl is Ownable {     [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-8)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-9)    [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-10)    // Burn function with proper access control, only accessible by the contract owner    [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-11)    function burn(address account, uint256 amount) public onlyOwner {        [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-12)        require(balances[account] >= amount, "Insufficient balance");        [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-13)        balances[account] -= amount;    [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-14)    } [](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#__codelineno-1-15)}`

### Examples of Smart Contracts That Fell Victim to Improper Access Control Attacks:[¶](https://scs.owasp.org/sctop10/archive/2025/SC01-AccessControlVulnerabilities/#examples-of-smart-contracts-that-fell-victim-to-improper-access-control-attacks "Permanent link")

1.  [HospoWise Hack](https://etherscan.io/address/0x952aa09109e3ce1a66d41dc806d9024a91dd5684#code) : A Comprehensive [Hack Analysis](https://blog.solidityscan.com/access-control-vulnerabilities-in-smart-contracts-a31757f5d707)
2.  [LAND NFT Hack](https://bscscan.com/address/0x1a62fe088F46561bE92BB5F6e83266289b94C154#code) : A Comprehensive [Hack Analysis](https://blog.solidityscan.com/land-hack-analysis-missing-access-control-66fb9555a3e3)
