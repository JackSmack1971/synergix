---
title: "SC04:2025 Lack of Input Validation"
source_url: "https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:02.439Z"
---
# SC04:2025 Lack of Input Validation

## Vulnerability: Lack of Input Validation[¶](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#vulnerability-lack-of-input-validation "Permanent link")

### Description:[¶](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#description "Permanent link")

Input validation ensures that a smart contract processes only valid and expected data. When contracts fail to validate incoming inputs, they inadvertently expose themselves to security risks such as logic manipulation, unauthorized access, and unexpected behavior.For example, if a contract assumes user inputs are always valid without verification, attackers can exploit this trust to introduce malicious data. This lack of input validation compromises the security and reliability of the smart contract.

### Example (Vulnerable Contract):[¶](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#example-vulnerable-contract "Permanent link")

`[](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-4)contract Solidity_LackOfInputValidation {     [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-5)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-6)    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-7)    function setBalance(address user, uint256 amount) public {        [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-8)        // The function allows anyone to set arbitrary balances for any user without validation.        [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-9)        balances[user] = amount;    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-10)    } [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-0-11)}`

### Impact:[¶](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#impact "Permanent link")

-   Attackers can manipulate inputs to drain funds, steal tokens, or cause other financial harm.
-   Improper inputs can corrupt state variables, leading to unreliable and insecure contract behavior.
-   Attackers may exploit the contract to perform unauthorized transactions or operations, impacting both the user and the broader system.

### Remediation:[¶](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#remediation "Permanent link")

-   Ensure that inputs conform to the expected type.
-   Validate that inputs fall within acceptable boundaries.
-   Ensure that only authorized entities can invoke specific functions.
-   Validate the structure of inputs, such as address formats or string lengths.
-   Always halt execution and provide clear error messages when inputs fail validation.

### Example (Fixed version):[¶](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#example-fixed-version "Permanent link")

`[](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-4)contract LackOfInputValidation {     [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-5)    mapping(address => uint256) public balances;    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-6)    address public owner; [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-7)    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-8)    constructor() {        [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-9)        owner = msg.sender;    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-10)    } [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-11)    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-12)    modifier onlyOwner() {        [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-13)        require(msg.sender == owner, "Caller is not authorized");        [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-14)        _;    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-15)    } [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-16)    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-17)    function setBalance(address user, uint256 amount) public onlyOwner {        [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-18)        require(user != address(0), "Invalid address");        [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-19)        balances[user] = amount;    [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-20)    } [](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#__codelineno-1-21)}`

### Examples of Smart Contracts that fell victim to attacks due to Lack of Input Validation:[¶](https://scs.owasp.org/sctop10/archive/2025/SC04-LackOfInputValidation/#examples-of-smart-contracts-that-fell-victim-to-attacks-due-to-lack-of-input-validation "Permanent link")

1.  [Convergence Finance](https://etherscan.io/address/0x2b083beaaC310CC5E190B1d2507038CcB03E7606#code) : A Comprehensive [Hack Analysis](https://blog.solidityscan.com/convergence-finance-hack-analysis-12e6acd9ea08)
2.  [Socket Gateway](https://etherscan.io/address/0x3a23F943181408EAC424116Af7b7790c94Cb97a5#code) : A Comprehensive [Hack Analysis](https://blog.solidityscan.com/socket-gateway-hack-analysis-b0e9567f7d3e)
