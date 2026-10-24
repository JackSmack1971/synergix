---
title: "SCWE-113: Insufficient TWAP Window or Single Observation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.008Z"
---
*Last updated: August 19, 2026*


# SCWE-113: Insufficient TWAP Window or Single Observation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#relationships "Permanent link")

-   CWE-346: Origin Validation Error
    [https://cwe.mitre.org/data/definitions/346.html](https://cwe.mitre.org/data/definitions/346.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#description "Permanent link")

TWAP oracles that use very short windows or a single cumulative observation can be manipulated within a block or a few trades. Attackers can swing the average price temporarily to borrow, liquidate, or mint at a favorable rate.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#remediation "Permanent link")

-   Use sufficiently long averaging windows and multiple observations with minimum elapsed time.
-   Enforce maximum per-block updates to prevent same-block manipulation.
-   Cross-check TWAP output against external reference feeds or deviation thresholds.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-3)interface IUniswapV3Pool {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-4)    function observe(uint32[] calldata secondsAgos)        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-5)        external view returns (int56[] memory tickCumulatives, uint160[] memory); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-6)} [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-7)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-8)contract PriceFeed {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-9)    IUniswapV3Pool public pool; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-11)    function twap() external view returns (int56) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-12)        uint32[] memory secondsAgos = new uint32[](1);        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-13)        secondsAgos[0] = 0; // single observation at current block — manipulatable in same block        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-14)        (int56[] memory tickCumulatives,) = pool.observe(secondsAgos);        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-15)        return tickCumulatives[0];    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-0-17)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-3)interface IUniswapV3Pool {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-4)    function observe(uint32[] calldata secondsAgos)        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-5)        external view returns (int56[] memory tickCumulatives, uint160[] memory); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-6)} [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-7)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-8)contract PriceFeed {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-9)    IUniswapV3Pool public pool;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-10)    uint32 public constant TWAP_WINDOW = 1 hours; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-12)    function twap() external view returns (int24) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-13)        uint32[] memory secondsAgos = new uint32[](2);        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-14)        secondsAgos[0] = TWAP_WINDOW; // start of window        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-15)        secondsAgos[1] = 0;           // current block        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-16)        (int56[] memory tickCumulatives,) = pool.observe(secondsAgos);        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-17)        int56 tickDelta = tickCumulatives[1] - tickCumulatives[0];        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-18)        return int24(tickDelta / int56(uint56(TWAP_WINDOW)));    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-19)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/#__codelineno-1-20)}`
