---
title: "SCWE-048: Unchecked Call Return Value"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:23.914Z"
---
*Last updated: August 19, 2026*


# SCWE-048: Unchecked Call Return Value

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#relationships "Permanent link")

-   CWE-252: Unchecked Return Value [https://cwe.mitre.org/data/definitions/252.html](https://cwe.mitre.org/data/definitions/252.html)
-   CWE-390: Detection of Error Condition Without Action [https://cwe.mitre.org/data/definitions/390.html](https://cwe.mitre.org/data/definitions/390.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#description "Permanent link")

Unchecked call return value vulnerabilities occur when a contract fails to validate the success or failure of low-level calls, such as `call`, `delegatecall`, and `staticcall`. Ignoring the return values of these calls can result in undetected errors, allowing malicious or unintended actions to succeed silently.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#remediation "Permanent link")

-   **Check return values:** Always verify the success of low-level calls.
-   **Use higher-level abstractions:** Prefer method calls or, if you are confident that 2300 gas are sufficient for the recipient to handle the transfer, `transfer` over `call`, as they revert on failure.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#examples "Permanent link")

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-0-3)contract UncheckedCall {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-0-4)    function sendEther(address _recipient) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-0-5)        _recipient.call{value: msg.value}(""); // Unchecked call, no error handling    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-0-7)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-3)contract CheckedCall {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-4)    function sendEther(address payable _recipient) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-5)        (bool success, ) = _recipient.call{value: msg.value}("");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-6)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/#__codelineno-1-8)}`
