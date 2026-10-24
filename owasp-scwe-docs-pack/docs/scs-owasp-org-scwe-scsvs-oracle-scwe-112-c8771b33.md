---
title: "SCWE-112: Reliance on Low-Liquidity Spot Prices"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.889Z"
---
*Last updated: August 19, 2026*


# SCWE-112: Reliance on Low-Liquidity Spot Prices

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#relationships "Permanent link")

-   CWE-346: Origin Validation Error
    [https://cwe.mitre.org/data/definitions/346.html](https://cwe.mitre.org/data/definitions/346.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#description "Permanent link")

Using a single on-chain DEX spot price from an illiquid pool lets attackers move the price with small trades or flash loans, then exploit inflated/deflated valuations for lending, liquidations, or swaps.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#remediation "Permanent link")

-   Require minimum liquidity thresholds and sanity bounds before trusting a pool.
-   Use robust oracles (Chainlink, TWAP, median of multiple feeds) instead of raw spot prices.
-   Apply deviation checks against reference feeds and revert when deviation exceeds limits.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-3)contract Lending {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-4)    IUniswapV2Pair public pair; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-6)    function getPrice() public view returns (uint256) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-7)        (uint112 r0, uint112 r1,) = pair.getReserves();        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-8)        return uint256(r1) * 1e18 / r0; // trusts small pool    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-0-10)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-3)contract Lending {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-4)    IAggregatorV3 public chainlink; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-5)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-6)    function getPrice() public view returns (uint256) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-7)        (, int256 price,,,) = chainlink.latestRoundData();        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-8)        require(price > 0, "stale");        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-9)        return uint256(price);    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/#__codelineno-1-11)}`
