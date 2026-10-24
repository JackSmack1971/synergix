---
title: "SCSTG-TEST-0005: Test Timed Permissions"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:16.586Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005.md "Edit this page")

# SCSTG-TEST-0005: Test Timed Permissions

Ensure that access controls are implemented correctly to determine who can use certain functions, and avoid unauthorized changes or withdrawals.

-   Ensure that functions requiring specific roles or permissions are restricted properly using onlyOwner or role-based checks.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-1)    modifier onlyOwner() {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-2)        require(msg.sender == owner, "Caller is not the owner");        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-3)        _;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-4)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-6)    function withdraw() external onlyOwner {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-7)        // Only the owner can withdraw    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0005/#__codelineno-0-8)    }`
