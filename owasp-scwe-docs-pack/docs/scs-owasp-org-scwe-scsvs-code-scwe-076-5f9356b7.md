---
title: "SCWE-076: Right-To-Left-Override Control Character (U+202E)"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.426Z"
---
*Last updated: August 19, 2026*


# SCWE-076: Right-To-Left-Override Control Character (U+202E)

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#relationships "Permanent link")

-   CWE-451: User Interface (UI) Misrepresentation of Critical Information
    [CWE-451 Link](https://cwe.mitre.org/data/definitions/451.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#description "Permanent link")

The Right-To-Left-Override (RTLO) control character (U+202E) can be used to manipulate the display order of text, creating misleading or deceptive visual representations in source code. Malicious actors can exploit this to: - Mask malicious logic or misrepresent code intent. - Introduce security-critical bugs that are difficult to detect visually. - Deceive auditors, developers, or end-users by obscuring real functionality.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#remediation "Permanent link")

-   **Disallow U+202E in source code:** Ensure RTLO and similar Unicode direction control characters are explicitly banned in smart contracts.
-   **Static analysis tools:** Use static analysis to detect and prevent Unicode control characters in contract source code.
-   **Education and awareness:** Educate developers about the risks associated with Unicode control characters in smart contract development.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#examples "Permanent link")

-   **Code with RTLO Character**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-3)contract MaliciousExample {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-4)    function performAction() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-5)        // The following line contains an RTLO character to misrepresent the logic visually        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-6)        executeLogic(/* attacker logic‮/*desrever ro*/victim logic */);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-8)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-9)    function executeLogic(bytes memory logic) internal {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-10)        // Process logic here    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-0-12)}`

-   **Code Without RTLO Character**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-3)contract SecureExample {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-4)    function performAction(bytes memory logic) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-5)        // Properly documented and clear function calls        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-6)        executeLogic(logic);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-9)    function executeLogic(bytes memory logic) internal {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-10)        // Process logic here    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/#__codelineno-1-12)}`
