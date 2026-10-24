---
title: "SCWE-086: Missing Validation of Oracle Response Fields (Stale or Incomplete Data)"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.640Z"
---
*Last updated: August 19, 2026*


# SCWE-086: Missing Validation of Oracle Response Fields (Stale or Incomplete Data)

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#relationships "Permanent link")

-   **CWE-345**: [Insufficient Verification of Data Authenticity](https://cwe.mitre.org/data/definitions/345.html)
-   **CWE-20**: [Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#description "Permanent link")

This weakness occurs when smart contracts consume data from oracles (e.g., Chainlink) without validating critical fields in the response such as `answeredInRound`, `timestamp`, or even the `answer` itself. Failing to validate these fields can lead to:

-   Use of stale price data from old oracle rounds.
-   Acceptance of incomplete oracle responses (e.g., `timestamp == 0`).
-   Execution based on invalid or zero-priced data.

This can severely affect the security of DeFi protocols or any smart contract relying on accurate, fresh data feeds.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#remediation "Permanent link")

-   **Validate `answer` field:** Ensure the value returned is greater than zero and not malformed.
-   **Check `answeredInRound >= roundId`:** Confirms that the data is not from a stale round.
-   **Verify `timestamp != 0`:** Ensures that the oracle actually returned a complete result.

Additional best practices include: - Using fallback mechanisms or thresholds for deviation checks. - Halting sensitive functions if oracle data is suspect or missing.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#examples "Permanent link")

-   **❌ Vulnerable Code (No Response Validation)**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-0-1)(, int256 answer,,,) = AggregatorV3Interface(oracle).latestRoundData(); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-0-2)require(uint256(answer) > 0, "Zero price"); // Minimal check only`

-   **✅ Secure Code (With Full Oracle Validation)**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-1-1)(uint80 roundID, int256 answer,, uint256 timestamp, uint80 answeredInRound) =      [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-1-2)    AggregatorV3Interface(oracle).latestRoundData(); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-1-4)require(answer > 0, "Invalid price: <= 0"); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-1-5)require(answeredInRound >= roundID, "Stale round data"); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#__codelineno-1-6)require(timestamp != 0, "Incomplete oracle response");`


## References[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/#references "Permanent link")

-   [Chainlink Oracle Security Best Practices](https://docs.chain.link/data-feeds/security/)
