---
title: "SCWE-080: Incorrect Type Conversion"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:21.046Z"
---
*Last updated: August 19, 2026*


# SCWE-080: Incorrect Type Conversion

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#relationships "Permanent link")

-   **CWE-704: Incorrect Type Conversion or Cast**
    [https://cwe.mitre.org/data/definitions/704.html](https://cwe.mitre.org/data/definitions/704.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#description "Permanent link")

Incorrect type conversion occurs when a value is cast or implicitly converted between incompatible types, potentially leading to precision loss, unexpected behavior, or security vulnerabilities. Solidity allows certain implicit conversions (e.g., from `uint256` to `uint8`), which can lead to silent truncation of data. Additionally, casting between types like `address` and `uint` can lead to unexpected security risks.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#remediation "Permanent link")

-   Avoid unsafe downcasts from larger to smaller types unless explicitly required.
-   Always validate the range before converting between numerical types.
-   Use explicit conversion functions where applicable, ensuring proper handling of edge cases.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-4)    function unsafeDowncast(uint256 value) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-5)        return uint8(value);  // ❌ Truncates value if > 255    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-8)    function unsafeAddressToUint(address addr) public pure returns (uint256) {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-9)        return uint256(uint160(addr));  // ❌ May lead to unexpected behaviors    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-0-11)}`

**Why is this vulnerable?**

-   `uint8(value)` will silently truncate values above 255, leading to unintended loss of data.
-   `uint256(uint160(addr))` might be used incorrectly in arithmetic operations, potentially allowing address manipulation.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-3)contract SecureExample {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-4)    function safeDowncast(uint256 value) public pure returns (uint8) {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-5)        require(value <= type(uint8).max, "Value exceeds uint8 range");  // ✅ Ensure valid range        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-6)        return uint8(value);    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-9)    function safeAddressToUint(address addr) public pure returns (uint160) {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-10)        return uint160(addr);  // ✅ Restrict conversion to valid 160-bit range    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-11)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/#__codelineno-1-12)}`

**Why is this safe?**

-   Ensures that values do not exceed the allowed range before downcasting.
-   Restricts type conversion to avoid security risks from improper arithmetic operations.
-   Prevents silent data loss that could lead to unintended contract behavior.

**By enforcing safe type conversions, developers can ensure contract logic remains reliable and free from unexpected truncation issues.**
