---
title: "SCWE-123: Corrupt Free Memory Pointer in Assembly"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:26.980Z"
---
*Last updated: August 19, 2026*


# SCWE-123: Corrupt Free Memory Pointer in Assembly

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#relationships "Permanent link")

-   CWE-693: Protection Mechanism Failure
    [https://cwe.mitre.org/data/definitions/693.html](https://cwe.mitre.org/data/definitions/693.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#description "Permanent link")

Inline assembly that writes to memory without preserving the Solidity free-memory pointer (at `0x40`) can corrupt ABI encoding for later calls or returns. Downstream decodes may misread buffers, leading to unexpected reverts or data leaks.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#remediation "Permanent link")

-   Save and restore the free-memory pointer when using custom memory writes.
-   Prefer Solidity primitives unless assembly is necessary; encapsulate unsafe sections.
-   Use formalized patterns for encoding/decoding (e.g., `abi.encode`) to avoid manual pointer math.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-0-3)assembly {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-0-4)    mstore(0x40, add(0x40, 0x20)) // advances but later writes may clobber    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-0-5)    mstore(0x00, value) [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-0-6)} [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-0-7)// subsequent abi.encode may read corrupted area`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-1-3)assembly {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-1-4)    let memPtr := mload(0x40)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-1-5)    mstore(memPtr, value)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-1-6)    mstore(0x40, add(memPtr, 0x20)) [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/#__codelineno-1-7)}`
