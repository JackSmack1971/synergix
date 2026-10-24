---
title: "SCWE-085: Misuse of Oracle Min/Max Price Band Without Validation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.532Z"
---
*Last updated: August 19, 2026*


# SCWE-085: Misuse of Oracle Min/Max Price Band Without Validation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#relationships "Permanent link")

-   **CWE-345**: [Insufficient Verification of Data Authenticity](https://cwe.mitre.org/data/definitions/345.html)
-   **CWE-20**: [Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)

* * *

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#description "Permanent link")

This weakness occurs when smart contracts consume price oracle data (e.g., from Chainlink) without verifying whether the returned price falls within an expected or trusted range (e.g., `minPrice`/`maxPrice`). Oracles may return fallback floor or ceiling values when actual prices exceed internal limits or when the feed encounters data instability.

Failing to detect and reject such edge-case values can result in incorrect or exploitable logic paths in smart contracts. This weakness may allow attackers to:

-   Trigger mispriced swaps or asset conversions.
-   Exploit collateralization thresholds.
-   Manipulate auction pricing or tiered reward structures.
-   Influence governance systems based on price weightings.

These issues are especially dangerous during periods of high volatility or partial oracle outages, where fallback values may be automatically returned.

* * *

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#remediation "Permanent link")

To mitigate this risk:

-   Always verify that the oracle-provided price lies within an expected range.
-   Check whether the returned value is a fallback boundary by comparing it against known `minPrice`/`maxPrice` values.
-   Monitor and log unusual oracle values for off-chain alerts and incident response.

* * *

## Example[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#example "Permanent link")

-   Vulnerable contract

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-0-1)(int256 price,,,) = AggregatorV3Interface(oracle).latestRoundData(); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-0-3)// Uses price directly without checking for boundary values [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-0-4)uint256 tokenAmount = uint256(price) * userInput;`

\- Fixed Contract

`[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-1-1)(int256 price,,,) = AggregatorV3Interface(oracle).latestRoundData(); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-1-3)// Validate that the price is within trusted bounds [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-1-4)require(price > minPrice && price < maxPrice, "Price out of expected bounds"); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-1-5)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#__codelineno-1-6)uint256 tokenAmount = uint256(price) * userInput;`

This ensures that the contract rejects unexpected oracle values that might be returned during errors or manipulation attempts.

## References[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/#references "Permanent link")

-   **Chainlink Docs**: [Chainlink Price Feeds Documentation](https://docs.chain.link/data-feeds)
-   **CWE-345**: [Insufficient Verification of Data Authenticity](https://cwe.mitre.org/data/definitions/345.html)
-   **CWE-20**: [Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)
