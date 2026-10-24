---
title: "SCWE-041: Unsafe Downcasting"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:23.428Z"
---
*Last updated: August 19, 2026*


# SCWE-041: Unsafe Downcasting

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#relationships "Permanent link")

-   **CWE-681: Incorrect Conversion between Numeric Types**
    [https://cwe.mitre.org/data/definitions/681.html](https://cwe.mitre.org/data/definitions/681.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#description "Permanent link")

Unsafe downcasting occurs when a larger integer type is implicitly or explicitly converted to a smaller type, leading to precision loss, unintended value changes, or integer overflows. Solidity does not automatically check for overflow when performing explicit type conversions, making it possible to unintentionally truncate values.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#remediation "Permanent link")

To prevent unsafe downcasting:
\- Always validate that the value fits within the target data type before casting.
\- Use safe mathematical libraries like OpenZeppelin's `SafeCast` to ensure proper conversions.
\- Avoid unnecessary downcasting unless explicitly needed for gas optimization.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-0-3)contract UnsafeDowncasting {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-0-4)    function truncateValue(uint256 largeNumber) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-0-5)        return uint8(largeNumber);  // ⚠️ Potential data loss if largeNumber > 255    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-0-7)}`

**Why is this vulnerable?** - If `largeNumber > 255`, the higher bits will be truncated, resulting in unexpected values. - No validation ensures that `largeNumber` fits within `uint8`, leading to silent failures.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-3)import "@openzeppelin/contracts/utils/math/SafeCast.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-5)contract SafeDowncasting {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-6)    using SafeCast for uint256; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-8)    function safeTruncateValue(uint256 largeNumber) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-9)        return largeNumber.toUint8();  // ✅ Ensures safe conversion    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/#__codelineno-1-11)}`

**Why is this safe?**

-   Uses OpenZeppelin’s `SafeCast` library to enforce safe downcasting.
-   If `largeNumber` exceeds `uint8` limits, the transaction will revert instead of silently truncating.
-   Prevents unexpected behavior and potential security vulnerabilities.

**By properly handling type conversions, developers can avoid integer truncation issues and maintain data integrity in smart contracts.**
