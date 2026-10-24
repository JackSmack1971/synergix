---
title: "SCSTG-TEST-0003: Least Privilege Principle Test"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:16.226Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003.md "Edit this page")

# SCSTG-TEST-0003: Least Privilege Principle Test

Use msg.sender instead of tx.origin for authorization to avoid potential abuse from malicious contracts; include checks like require(tx.origin == msg.sender) to ensure the sender is an EOA.

-   tx.origin can be abused by malicious contracts to trick the system into performing actions on behalf of an unsuspecting user. msg.sender is preferred since it refers to the direct sender of the message.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-0-1)require(msg.sender == owner, "Not the owner"); [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-0-2)require(tx.origin == msg.sender, "Only EOA can execute");`


Certain addresses might be blocked or restricted from receiving tokens (e.g., LUSD). Ensure that address restrictions are properly managed and verified.

-   If certain addresses (like LUSD) should be blocked from receiving tokens, ensure that there’s a check in place to restrict these addresses.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-1-1)address restrictedAddress = 0x123...;  // Example of a restricted address [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-1-2)require(msg.sender != restrictedAddress, "Restricted address cannot perform this operation");`


Ensure that Guard’s hooks (e.g., checkTransaction(), checkAfterExecution()) are executed to enforce critical security checks.

-   If using a Guard contract, ensure that hooks like checkTransaction() or checkAfterExecution() are properly implemented to enforce security conditions.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-2-1)function checkTransaction() internal {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-2-2)    // Add conditions to verify transaction before execution [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-2-3)} [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-2-4)[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-2-5)function checkAfterExecution() internal {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-2-6)    // Add conditions to verify transaction after execution [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0003/#__codelineno-2-7)}`
