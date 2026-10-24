---
title: "SCSTG-TEST-0002: Identity Verification Test"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0002/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:16.111Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0002.md "Edit this page")

# SCSTG-TEST-0002: Identity Verification Test

Validate that unexpected addresses do not result in unintended behaviors, particularly when these addresses refer to contracts within the same protocol.

-   Ensure that when interacting with contracts, unexpected addresses are properly validated before performing sensitive operations.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0002/#__codelineno-0-1)require(address(contract) != address(0), "Invalid address");`


Verify that functions like ecrecover handle all potential null addresses properly to avoid vulnerabilities arising from unexpected ecrecover outputs.

-   Ensure that ecrecover does not process empty or null addresses.

    `[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0002/#__codelineno-1-1)address recovered = ecrecover(messageHash, v, r, s); [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/SCSTG-TEST-0002/#__codelineno-1-2)require(recovered != address(0), "Invalid signature");`
