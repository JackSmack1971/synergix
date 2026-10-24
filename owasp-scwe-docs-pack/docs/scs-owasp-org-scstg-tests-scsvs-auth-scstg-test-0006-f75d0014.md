---
title: "SCSTG-TEST-0006: Test Access Control Using Merkle Trees"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:16.732Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006.md "Edit this page")

# SCSTG-TEST-0006: Test Access Control Using Merkle Trees

Ensure that `msg.sender` validation is properly implemented when using Merkle trees to maintain security and prevent unauthorized access.

-   When using Merkle trees to authenticate users or grant permissions, ensure that the contract verifies that `msg.sender` matches the expected address and Merkle proof. This prevents unauthorized actors from bypassing security by submitting incorrect proofs.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-0-1)    require(verifyMerkleProof(msg.sender, merkleProof), "Invalid Merkle proof");`

-   Use whitelisting to restrict interactions to a specific set of addresses, providing additional security against malicious actors.

-   Implement a whitelisting mechanism that allows only approved addresses to interact with specific functions. Ensure that only addresses explicitly added to the whitelist are able to execute sensitive operations.


    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-1)    address[] public whitelist; [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-2)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-3)    modifier onlyWhitelisted() {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-4)        bool isWhitelisted = false;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-5)        for (uint i = 0; i < whitelist.length; i++) {            [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-6)            if (msg.sender == whitelist[i]) {                [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-7)                isWhitelisted = true;                [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-8)                break;            [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-9)            }        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-10)        }        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-11)        require(isWhitelisted, "Address not whitelisted");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-12)        _;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-13)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-14)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-15)    function addToWhitelist(address _address) external onlyOwner {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-16)        whitelist.push(_address);    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-1-17)    }`

\- Ensure that functions modifying the contract state or accessing sensitive operations have proper access controls implemented.

-   Critical functions, such as those that modify contract state or handle sensitive information, should only be callable by authorized addresses (e.g., the owner or an admin). Use modifiers to enforce access controls for these functions.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-1)    modifier onlyOwner() {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-2)        require(msg.sender == owner, "Not the contract owner");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-3)        _;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-4)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-6)    function modifyContractState() external onlyOwner {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-7)        // Logic to modify contract state    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0006/#__codelineno-2-8)    }`
