---
title: "SCWE-127: EIP-1559 Basefee Assumptions"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.750Z"
---
*Last updated: August 19, 2026*


# SCWE-127: EIP-1559 Basefee Assumptions

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#relationships "Permanent link")

-   CWE-841: Improper Enforcement of Behavioral Workflow
    [https://cwe.mitre.org/data/definitions/841.html](https://cwe.mitre.org/data/definitions/841.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#description "Permanent link")

Hardcoding gas price/basefee assumptions (e.g., fixed `gasprice` limits or expecting refunds) can break on EIP-1559 chains. Contracts that require exact `block.basefee` ranges or reimburse fixed gas can become stuck or exploitable via gas griefing.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#remediation "Permanent link")

-   Avoid relying on specific basefee values; parameterize and allow updates via governance with delays.
-   Use robust gas estimation and caps on external calls; avoid refund-dependent logic.
-   Simulate on mainnet forks with varying basefee to validate liveness.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#__codelineno-0-1)require(tx.gasprice <= 30 gwei, "gas too high"); // fails as basefee rises`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#__codelineno-1-1)uint256 maxGasPrice = governanceMaxGasPrice; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/#__codelineno-1-2)require(tx.gasprice <= maxGasPrice, "gas too high"); // upgradable with delays`
