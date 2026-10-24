---
title: "SCSVS-CODE-2¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-2/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:55.125Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-CODE-2.md "Edit this page")

# SCSVS-CODE-2[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-2/#scsvs-code-2 "Permanent link")

## S2.2 Code Clarity[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-2/#s22-code-clarity "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-2/#control-objective "Permanent link")

Promote code clarity and maintainability through thorough documentation, logical structure, and adherence to consistent coding standards, enabling easier understanding and modification by developers.

### S2.2.A Readability and Documentation[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-2/#s22a-readability-and-documentation "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S2.2.A1 | Ensure that all smart contract functions and critical code blocks are documented with clear comments that explain their purpose and logic. |  | ✓ | ✓ |  |
| S2.2.A2 | Verify that the structure of the smart contract is logical and organized to facilitate understanding and modification by other developers. |  | ✓ | ✓ |  |
| S2.2.A3 | Check that the smart contract documentation includes a high-level overview of its functionality, usage instructions, and any dependencies on other contracts or systems. |  | ✓ | ✓ |  |
| S2.2.A4 | Ensure that smart contract code follows consistent naming conventions for variables, functions, and contract names to improve readability and maintainability. |  | ✓ | ✓ |  |

### S2.2.B Code Linting and Formatting Tools[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CODE-2/#s22b-code-linting-and-formatting-tools "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S2.2.B1 | Ensure that a code linting tool specific to smart contracts is integrated into the development workflow to enforce coding standards and style guidelines. |  | ✓ | ✓ |  |
| S2.2.B2 | Verify that all smart contract code passes linting checks without errors or warnings before being committed to the repository. |  | ✓ | ✓ |  |
| S2.2.B3 | Check that code formatting tools are applied to maintain consistent indentation, spacing, and line breaks in smart contract code. |  | ✓ | ✓ |  |
| S2.2.B4 | Ensure that the linting and formatting configurations are reviewed and updated regularly to reflect new best practices and emerging issues in smart contract development. |  | ✓ | ✓ |  |
| S2.2.B5 | Verify that the linting and formatting tools are compatible with the development environment and do not introduce unintended changes to the smart contract code. |  | ✓ | ✓ |  |
