---
title: "SCWE-040: Incorrect Storage Packing"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:23.247Z"
---
*Last updated: August 19, 2026*


# SCWE-040: Incorrect Storage Packing

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#relationships "Permanent link")

-   **CWE-805: Buffer Access with Incorrect Length Value**
    [https://cwe.mitre.org/data/definitions/805.html](https://cwe.mitre.org/data/definitions/805.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#description "Permanent link")

Incorrect storage packing in Solidity occurs when storage variables are not efficiently packed within a single storage slot, leading to unnecessary gas consumption. Solidity automatically stores variables in 32-byte (256-bit) slots, and inefficient ordering of data types can lead to wasted space. Contracts that fail to optimize storage packing may incur higher gas costs during deployments and transactions.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#remediation "Permanent link")

To optimize storage packing:
\- Group smaller data types together (e.g., `uint8`, `bool`) to fit within a single 32-byte slot.
\- Avoid leaving gaps between variables of different sizes.
\- Order state variables efficiently to minimize wasted storage slots.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-3)contract InefficientStorage {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-4)    uint256 a;  // Occupies full 32-byte slot    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-5)    bool b;     // Occupies another 32-byte slot (wasteful)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-6)    uint8 c;    // Uses a new 32-byte slot instead of sharing    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-7)    uint256 d;  // Uses its own slot, leading to extra gas costs [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-0-8)}`

**Why is this vulnerable?** - Each variable unnecessarily occupies a separate storage slot, increasing gas costs. - The `bool` and `uint8` could be packed into the same 32-byte slot, reducing wasted storage space.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-3)contract OptimizedStorage {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-4)    uint256 a;   // Occupies one full 32-byte slot    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-5)    uint256 d;   // Placed next to 'a' to use another full slot    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-6)    bool b;      // Packed within the same slot as 'c'    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-7)    uint8 c;     // Fits within the same slot as 'b' [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/#__codelineno-1-8)}`

**Why is this safe?** - `bool` and `uint8` share the same storage slot, reducing unnecessary storage use. - `uint256` variables are placed together to minimize fragmentation. - Optimized storage layout leads to lower gas costs for contract execution.

**By correctly ordering state variables and utilizing Solidity’s storage packing rules, developers can significantly reduce gas fees and improve contract efficiency.**
