---
title: "SCWE-126: Unbounded Withdrawal Queue Growth"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.834Z"
---
*Last updated: August 19, 2026*


# SCWE-126: Unbounded Withdrawal Queue Growth

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#description "Permanent link")

Protocols that queue withdrawals without bounding length or processing batches can face gas exhaustion when executing large queues. Attackers can spam small requests to DoS withdrawal execution or force users to accept delays.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#remediation "Permanent link")

-   Cap queue size or use batched/paged processing with upper gas limits.
-   Charge fees or require minimum amounts to discourage spam.
-   Allow users to cancel/claim in smaller chunks rather than processing the entire queue at once.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-0-1)function processAll() external {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-0-2)    for (uint256 i = 0; i < queue.length; i++) {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-0-3)        _pay(queue[i]);    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-0-4)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-0-5)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-1-1)function processBatch(uint256 start, uint256 max) external {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-1-2)    uint256 end = start + max;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-1-3)    if (end > queue.length) end = queue.length;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-1-4)    for (uint256 i = start; i < end; i++) {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-1-5)        _pay(queue[i]);    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-1-6)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/#__codelineno-1-7)}`
