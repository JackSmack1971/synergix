---
title: "SCWE-091: Lack of Zero Value Check in Token Transfers"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.784Z"
---
*Last updated: August 19, 2026*


# SCWE-091: Lack of Zero Value Check in Token Transfers

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#relationships "Permanent link")

-   CWE-754: Improper Check for Unusual or Exceptional Conditions
    [CWE-754 Link](https://cwe.mitre.org/data/definitions/754.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#description "Permanent link")

This weakness occurs when smart contracts perform ERC20 token transfers without first validating that the transfer amount is greater than zero. While most ERC20 tokens allow zero‑value transfers, some implementations (e.g., LEND and others) revert when the amount is zero. This inconsistency can cause unexpected reverts in production, disrupt execution flow, and prevent critical contract logic from completing successfully.
Common risks include:
\- Unexpected revert when interacting with non‑standard ERC20 tokens that disallow zero‑value operations.
\- Potential denial‑of‑service conditions if an attacker or integration repeatedly triggers zero‑value transfers.
\- Broken integrations when protocols assume uniform ERC20 behavior across diverse tokens.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#remediation "Permanent link")

-   **Validate transfer amounts:** Ensure `amount > 0` before calling `transfer`/`transferFrom`.
-   **Treat zero as a no‑op if acceptable:** Early‑return when `amount == 0` rather than calling token methods.
-   **Use robust token wrappers:** Centralize token operations (e.g., via OpenZeppelin `SafeERC20`) and standardize zero‑value handling.
-   **Integration testing:** Include zero‑value cases for all integrated tokens (especially known non‑standard tokens like LEND).
-   **Input sanitization:** Validate and sanitize externally supplied amounts prior to token interactions.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#examples "Permanent link")

-   **Vulnerable Code (No Zero Value Check)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-4)import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol"; // OZ 5.x: token/ERC20/utils/SafeERC20.sol [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-5)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-6)contract ExampleContract {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-7)    using SafeERC20 for IERC20;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-8)    IERC20 public inToken;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-9)    address public vault; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-11)    function transferTokens(uint256 feeTokenAmount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-12)        // No validation → may revert with some ERC20 tokens        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-13)        inToken.safeTransfer(vault, feeTokenAmount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-14)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-0-15)}`

-   **Safe Code (With Zero Value Check)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-4)import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol"; // OZ 5.x: token/ERC20/utils/SafeERC20.sol [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-5)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-6)contract ExampleContract {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-7)    using SafeERC20 for IERC20;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-8)    IERC20 public inToken;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-9)    address public vault; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-11)    function transferTokens(uint256 feeTokenAmount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-12)        require(feeTokenAmount > 0, "Amount must be greater than zero");        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-13)        inToken.safeTransfer(vault, feeTokenAmount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-1-15)}`

-   **Alternative Safe Pattern (No‑op on Zero)**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-4)import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol"; // OZ 5.x: token/ERC20/utils/SafeERC20.sol [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-5)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-6)contract ExampleContract {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-7)    using SafeERC20 for IERC20;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-8)    IERC20 public inToken;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-9)    address public vault; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-10)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-11)    function transferTokens(uint256 feeTokenAmount) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-12)        if (feeTokenAmount == 0) {            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-13)            return; // Skip calling token methods to avoid non-standard reverts        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-14)        }        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-15)        inToken.safeTransfer(vault, feeTokenAmount);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/#__codelineno-2-17)}`
