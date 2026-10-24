---
title: "SCWE-039: Insecure Use of Inline Assembly"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:23.088Z"
---
*Last updated: August 19, 2026*


# SCWE-039: Insecure Use of Inline Assembly

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#relationships "Permanent link")

-   CWE-704: Incorrect Type Conversion or Cast
    [CWE-704 Link](https://cwe.mitre.org/data/definitions/704.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#description "Permanent link")

Insecure use of inline assembly refers to vulnerabilities that arise when low-level assembly code is used improperly. This can lead to: - Incorrect type conversions or casts. - Exploitation of vulnerabilities in low-level operations. - Loss of funds or data.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#remediation "Permanent link")

-   **Avoid inline assembly:** Use high-level Solidity code whenever possible.
-   **Validate inputs:** Ensure all inputs to assembly code are properly validated.
-   **Test thoroughly:** Conduct extensive testing to ensure assembly code is secure.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#examples "Permanent link")

-   **Insecure Inline Assembly- Unsafe Type Casting Leads to Exploitable Overflow**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-3)contract InsecureAssembly {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-4)    function unsafeCast(uint256 value) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-5)        uint8 result;        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-6)        assembly {            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-7)            result := value // Unsafe cast, truncating high bits        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-8)        }        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-9)        return result;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-0-11)}`

    ⚠️ Why is this Vulnerable?
-   Casting a large uint256 into uint8 without bounds checking causes integer truncation.
-   If value = 257, it becomes 1 (256 is lost).
-   Attackers can bypass security checks if truncation affects authentication or balance checks.

-   **Secure Alternative — High-Level Code with Bounds Checking**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-3)contract SecureAssembly {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-4)    function safeCast(uint256 value) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-5)        require(value <= type(uint8).max, "Value too large"); // Prevent truncation        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-6)        return uint8(value);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/#__codelineno-1-8)}`

    Fixes:

-   Bounds checking (require) prevents unintended truncation.
-   Prefer high-level Solidity over assembly when possible; if assembly is required, validate inputs first.

* * *
