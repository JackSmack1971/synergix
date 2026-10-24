---
title: "SCSTG-TEST-0010: Test Compiler Version and Deprecated Functions"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:15.261Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010.md "Edit this page")

# SCSTG-TEST-0010: Test Compiler Version and Deprecated Functions

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#description "Permanent link")

Proper management of development policies, secure coding standards, code clarity, and test coverage ensures that smart contracts are secure, maintainable, and resilient to vulnerabilities. This test focuses on ensuring adherence to best practices and guidelines for developing and reviewing smart contracts. This includes the use of current compilers, avoiding deprecated functions, thorough code reviews, and ensuring proper test coverage. Code clarity is also critical for maintaining contracts over time and ensuring they remain understandable and auditable.

* * *

### **Test 1: Verify Compiler Version and Avoid Deprecated Functions**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#test-1-verify-compiler-version-and-avoid-deprecated-functions "Permanent link")

#### Vulnerable Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-1)pragma solidity ^0.4.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-4)    uint256 public value; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-6)    function setValue(uint256 _value) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-7)        value = _value;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-0-9)}`

#### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#why-its-vulnerable "Permanent link")

-   The contract uses an outdated compiler version (^0.4.0). Using old versions of Solidity may lead to known security vulnerabilities and lack of support for modern features.
-   Older compiler versions also lack optimizations and security fixes that are available in newer versions.

#### Fixed:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#fixed "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-1)pragma solidity ^0.8.0;  // Update to the latest stable version [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-3)contract Example {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-4)    uint256 public value; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-6)    function setValue(uint256 _value) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-7)        value = _value;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-1-9)}`

#### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#how-to-check "Permanent link")

-   Code Review: Ensure that the pragma directive specifies an up-to-date version of Solidity (e.g., ^0.8.x) and not outdated ones such as ^0.4.x.
-   Automated Check: Use Solidity linting tools or automated CI/CD pipelines to flag usage of outdated compiler versions.

* * *

### **Test 2: Ensure Code Review Processes and Avoid Deprecated Functions**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#test-2-ensure-code-review-processes-and-avoid-deprecated-functions "Permanent link")

#### **Vulnerable Code:**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#vulnerable-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-1)pragma solidity ^0.4.24; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-3)// Example: ETH vault (sends Ether, not ERC20 tokens). Variable names simplified for clarity. [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-4)contract Token {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-5)    string public name = "Token";    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-6)    uint public totalSupply = 1000000;  // Tracks remaining withdrawable ETH [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-7)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-8)    // Deprecated: uses transfer() for Ether; deprecated in Solidity 0.5+    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-9)    function transfer(address recipient, uint amount) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-10)        require(msg.sender != recipient, "Cannot transfer to yourself");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-11)        require(amount <= totalSupply, "Amount exceeds total supply"); [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-12)        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-13)        totalSupply -= amount;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-14)        // Deprecated: The transfer method below is obsolete        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-15)        recipient.transfer(amount);    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-16)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-2-17)}`

#### Why It’s Vulnerable[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#why-its-vulnerable_1 "Permanent link")

-   The function transfer in the above example uses a deprecated `transfer()` method to send Ether to the recipient.
-   The `transfer()` method was removed in Solidity 0.5.x, and it’s recommended to use `call()` instead to prevent errors due to changes in gas limits and transfer behavior in newer Solidity versions.
-   Using deprecated functions can make your contract incompatible with future versions of Solidity and leave it vulnerable to unexpected behavior.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-3)// ETH vault example: sends Ether via call{value} (see SCWE-079) [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-4)contract Token {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-5)    string public name = "Token";    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-6)    uint public totalSupply = 1000000; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-7)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-8)    function transfer(address payable recipient, uint amount) public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-9)        require(msg.sender != recipient, "Cannot transfer to yourself");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-10)        require(amount <= totalSupply, "Amount exceeds total supply"); [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-11)        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-12)        totalSupply -= amount;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-13)        // Replaced deprecated transfer method with call to ensure proper handling        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-14)        (bool success, ) = recipient.call{value: amount}("");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-15)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-16)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#__codelineno-3-17)}`

#### Why the Fix Works[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#why-the-fix-works "Permanent link")

-   The updated code uses the `call()` method instead of the deprecated `transfer()` method to send Ether.
-   The `call()` method is more flexible and is recommended in Solidity 0.5.x and later, as it allows specifying gas and properly handling errors.
-   This change ensures that the contract is compatible with newer Solidity versions (>=0.5.x) and avoids potential issues with future upgrades.

#### How to Check[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CODE/SCSTG-TEST-0010/#how-to-check_1 "Permanent link")

-   Code Review: Ensure the contract is not using any deprecated or obsolete functions. Look for any `transfer()`, `send()`, or other outdated methods, and replace them with the more secure `call()` method when sending Ether.
-   Static Analysis Tools: Use tools like SolidityScan, MythX, Slither, or linters to detect deprecated features and provide suggestions for updating the code.
-   Testing: Test the contract using the latest Solidity version and verify that no deprecated functions are used, ensuring compatibility with newer compilers.
