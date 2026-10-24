---
title: "SCWE-093: Unnamed Function Parameters"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:26.049Z"
---
*Last updated: August 19, 2026*


# SCWE-093: Unnamed Function Parameters

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#relationships "Permanent link")

-   **CWE-710**: [Improper Adherence to Coding Standards](https://cwe.mitre.org/data/definitions/710.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#description "Permanent link")

This weakness occurs when functions declare parameters without names (only types). Unnamed parameters reduce code clarity and hinder maintainability, making it difficult for reviewers and future maintainers to understand the purpose and expected usage of each argument. In smart contracts, where correctness is critical, this ambiguity can result in misinterpretation, incorrect argument ordering in calls or refactors, and subtle logic errors.

## Impact[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#impact "Permanent link")

Lack of clear parameter names can lead to: - Misuse of function arguments due to misunderstanding of their meaning.
\- Increased likelihood of logic bugs during refactoring and maintenance.
\- Higher audit and review overhead; reduced readability and self-documentation.
\- Potential security issues if parameters are confused (e.g., recipient vs. sender, amount vs. fee).

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#remediation "Permanent link")

-   Always provide descriptive names for all function parameters.
-   Choose meaningful, self-explanatory names consistent with a coding standard.
-   Supplement with NatSpec where helpful to document parameter intent and units.
-   Enforce naming conventions with linters and code review checklists.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#examples "Permanent link")

-   **Vulnerable Code (Unnamed parameters reduce clarity)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-2)pragma solidity 0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-4)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-5)    function transfer(address, uint256, bytes memory) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-6)        // Function logic    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-0-8)}`

-   **✅ Safe Code (Named parameters improve readability)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-2)pragma solidity 0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-4)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-5)    function transfer(address recipient, uint256 amount, bytes memory data) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-6)        // Function logic    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/#__codelineno-1-8)}`
