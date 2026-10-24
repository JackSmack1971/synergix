---
title: "SCSTG-TEST-0012: Test Token Implementations (ERC20, ERC721, ERC1155)"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:18.770Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012.md "Edit this page")

# SCSTG-TEST-0012: Test Token Implementations (ERC20, ERC721, ERC1155)

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#description "Permanent link")

Component-Specific Security focuses on ensuring that each specific component of a decentralized application (dApp) or smart contract ecosystem is securely implemented. This includes a wide range of areas such as token standards (ERC20, ERC721, ERC1155), NFTs, vaults, liquidity pools, and other components. Properly securing these components is essential to avoid vulnerabilities that can lead to funds being stolen, lost, or misused. This test will focus on validating the security considerations for the components listed in the controls, ensuring that each one is implemented securely and with the appropriate mechanisms to protect users and assets.

* * *

### **Test: Ensure Proper Token Implementation (ERC20, ERC721, ERC1155)**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#test-ensure-proper-token-implementation-erc20-erc721-erc1155 "Permanent link")

#### \*\*Vulnerable Code: \*\*[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-1)pragma solidity ^0.5.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-3)contract SimpleERC20 {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-4)    mapping(address => uint256) public balanceOf;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-5)    mapping(address => mapping(address => uint256)) public allowance; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-6)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-7)    string public name = "Simple Token";    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-8)    string public symbol = "STK";    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-9)    uint8 public decimals = 18;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-10)    uint256 public totalSupply; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-11)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-12)    // Unchecked approve function (vulnerable to approval race condition)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-13)    function approve(address spender, uint256 amount) public returns (bool) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-14)        allowance[msg.sender][spender] = amount;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-15)        return true;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-16)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-0-17)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#why-its-vulnerable "Permanent link")

-   The `approve` function does not include a check for the current allowance before setting a new one, which could allow for the "approval race condition." This can result in a vulnerability where an attacker could bypass the allowance mechanism and transfer more tokens than intended.
-   This issue is a well-known vulnerability in ERC20 token implementations.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-3)contract SafeERC20 {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-4)    mapping(address => uint256) public balanceOf;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-5)    mapping(address => mapping(address => uint256)) public allowance; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-6)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-7)    string public name = "Safe Token";    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-8)    string public symbol = "STK";    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-9)    uint8 public decimals = 18;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-10)    uint256 public totalSupply; [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-11)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-12)    // Secure approve function to prevent race condition    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-13)    function approve(address spender, uint256 amount) public returns (bool) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-14)        require(amount == 0 || allowance[msg.sender][spender] == 0, "Approve: non-zero allowance");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-15)        allowance[msg.sender][spender] = amount;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-16)        return true;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-17)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#__codelineno-1-18)}`

### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-COMP/SCSTG-TEST-0012/#how-to-check "Permanent link")

-   **Code Review:** Look for the `approve` function in token contracts and ensure that it includes the necessary checks to prevent the race condition. The secure approach is to first set the allowance to zero before updating it to a new value, or to require that it is zero if being reset.
-   **Static Analysis:** Use tools such as SolidityScan, MythX or Slither to check for the "approval race condition" and ensure the contract doesn't allow for this vulnerability.
-   **Dynamic Testing:** Test token transfer functionality with edge cases where the allowance is set to non-zero values before calling `approve`. Verify that it works correctly and no unauthorized transfers are possible.
