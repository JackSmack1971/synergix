---
title: "SCWE-089: Vulnerable & Outdated Libraries"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.539Z"
---
*Last updated: August 19, 2026*


# SCWE-089: Vulnerable & Outdated Libraries

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#relationships "Permanent link")

-   CWE-1104: Use of Unmaintained Third Party Components
    [CWE-1104 Link](https://cwe.mitre.org/data/definitions/1104.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#description "Permanent link")

Smart contracts that depend on outdated or vulnerable third‑party libraries inherit their security flaws. Attackers can exploit known issues in widely used libraries (e.g., reentrancy, integer overflow, or access control bypasses), especially if the library is no longer maintained or patched.
Common risks include:
\- Exploitation of known vulnerabilities in older OpenZeppelin versions or other dependencies.
\- Inheriting insecure logic or deprecated patterns from unmaintained libraries.
\- Increased attack surface due to indirect dependencies.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#remediation "Permanent link")

-   **Version pinning:** Always specify exact, up‑to‑date versions of dependencies in `package.json`, `foundry.toml`, or `hardhat.config.js`.
-   **Regular audits:** Periodically review library versions for known vulnerabilities and upgrade accordingly.
-   **Vendor management:** Rely on reputable, actively maintained libraries (e.g., OpenZeppelin). Avoid custom forks unless fully audited.
-   **Automated scanning:** Use dependency scanners (e.g., `npm audit`, `snyk`, `slither-check-oz`) to detect outdated or vulnerable libraries.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#examples "Permanent link")

-   **Outdated Dependency Example (`package.json`)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-0-1){   [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-0-2)  "dependencies": {    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-0-3)    "@openzeppelin/contracts": "^2.3.0",    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-0-4)    "truffle": "^5.0.0"  [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-0-5)  },  [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-0-6)  "notes": "Insecure: OpenZeppelin v2.3.0 contains outdated ERC777 and SafeMath implementations." [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-0-7)}`

-   **Updated Dependency Example (`package.json`)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-1-1){   [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-1-2)  "dependencies": {    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-1-3)    "@openzeppelin/contracts": "^5.0.0",    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-1-4)    "hardhat": "^2.22.0"  [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-1-5)  },  [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-1-6)  "notes": "Secure: Latest OpenZeppelin release with modern ERC20, patched ERC777, and Solidity 0.8+ overflow checks." [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/#__codelineno-1-7)}`
