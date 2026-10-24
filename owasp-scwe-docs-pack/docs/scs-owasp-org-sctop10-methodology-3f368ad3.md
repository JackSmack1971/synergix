---
title: "Ranking Methodology¶"
source_url: "https://scs.owasp.org/sctop10/methodology/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:01.638Z"
---
# Ranking Methodology[¶](https://scs.owasp.org/sctop10/methodology/#ranking-methodology "Permanent link")

This methodology explains the conceptual framework and underlying calculations used to form the OWASP Smart Contract Top 10 2026. The process combines **survey responses** from practitioners with **2025 incident data** and **qualitative feedback** to produce a transparent, reproducible ranking.

## Overview[¶](https://scs.owasp.org/sctop10/methodology/#overview "Permanent link")

The aim is to make the ranking process **transparent and reproducible**:

-   Individual survey responses are aggregated into per-category statistics (mean, median, standard deviation, etc.).
-   The primary ordering is driven by **mean rank**, with supporting metrics used when categories are close.
-   Qualitative input and 2025 breach data inform category definitions and refinements.

## Elicitation Model[¶](https://scs.owasp.org/sctop10/methodology/#elicitation-model "Permanent link")

### Risk Categories[¶](https://scs.owasp.org/sctop10/methodology/#risk-categories "Permanent link")

The framework uses a fixed set of distinct risk categories. For the 2026 process, the survey and analysis covered categories including:

-   Access Control Vulnerabilities
-   Business Logic Vulnerabilities (Logic Errors)
-   Price Oracle Manipulation
-   Flash Loan–Facilitated Attacks
-   Lack of Input Validation
-   Unchecked External Calls
-   Reentrancy Attacks
-   Arithmetic Errors / Integer Overflow and Underflow
-   Proxy & Upgradeability Vulnerabilities
-   Insecure Randomness (later removed)
-   Denial of Service (DoS) Attacks (later removed)
-   Arithmetic Errors (added)
-   Proxy & Upgradeability Vulnerabilities (added)

Respondents assign a rank from 1 to *K* to each category, where *K* is the total number of categories (for the Top 10, *K* = 10).

### Direction of the Scale[¶](https://scs.owasp.org/sctop10/methodology/#direction-of-the-scale "Permanent link")

Ranks are interpreted in the conventional way:

-   **1** = highest risk / highest priority
-   **K** = lowest risk / lowest priority

No inversion, rescaling, or transformation of the raw ranks is performed. Lower numbers indicate greater perceived importance.

## Data Preparation[¶](https://scs.owasp.org/sctop10/methodology/#data-preparation "Permanent link")

### Structure of the Data[¶](https://scs.owasp.org/sctop10/methodology/#structure-of-the-data "Permanent link")

Conceptually, the data is represented as a matrix *R* where:

-   Each **row** corresponds to a single respondent
-   Each **column** corresponds to a risk category
-   *ri,j* is the rank assigned by respondent *i* to category *j*

### Cleaning and Validation[¶](https://scs.owasp.org/sctop10/methodology/#cleaning-and-validation "Permanent link")

Before aggregation, the following steps are applied:

1.  **Header detection:** Identify the row containing column names (e.g., timestamp label).
2.  **Row selection:** Treat all subsequent non-empty rows as responses; ignore introductory text or metadata.
3.  **Type checks:** For each rank cell, strip whitespace and validate that it is an integer in the range {1, 2, …, K}.
4.  **Filtering:** Treat non-numeric or out-of-range values as missing; exclude them from numerical calculations.

These steps ensure that only well-formed ranking data is used in the analysis.

## Aggregation of Rankings[¶](https://scs.owasp.org/sctop10/methodology/#aggregation-of-rankings "Permanent link")

### Per-Category Summary Statistics[¶](https://scs.owasp.org/sctop10/methodology/#per-category-summary-statistics "Permanent link")

For each category *j*, we consider the set of valid ranks *Sj*. On this set we compute:

| Statistic | Description |
| --- | --- |
| **Mean rank** | Arithmetic mean; lower values indicate higher perceived risk on average. |
| **Median rank** | Middle value of the sorted sample; robust to outliers. |
| **Standard deviation** | Captures disagreement among respondents; larger values indicate more polarised views. |
| **Min / Max** | Range of observed ranks (e.g., whether a category was ever ranked 1 or 10). |
| **#rank1** | Count of respondents who placed the category at rank 1. |
| **#top3** | Count of respondents who placed the category in the top 3. |

### Primary Aggregation Metric[¶](https://scs.owasp.org/sctop10/methodology/#primary-aggregation-metric "Permanent link")

The primary metric used to order categories is the **mean rank**:

> **Lower mean rank ⇒ higher place in the final Top 10.**

This choice:

-   Respects the ordinal structure of the scale
-   Incorporates the full distribution of responses
-   Yields a simple, explainable ordering

### Supporting Metrics[¶](https://scs.owasp.org/sctop10/methodology/#supporting-metrics "Permanent link")

When two categories have similar mean ranks, the following are used to refine the ordering:

-   **Median ranks** — reveal skew and broad agreement
-   **Standard deviations** — highlight polarised opinions
-   **#rank1 and #top3** — indicate intensity of concern (e.g., a category may be a frequent first choice even without the lowest mean)

## How the Statistics Are Computed[¶](https://scs.owasp.org/sctop10/methodology/#how-the-statistics-are-computed "Permanent link")

For each category *j*, the following quantities are computed from the valid ranks *Sj*:

| Statistic | Formula / Definition |
| --- | --- |
| **Mean rank** | *r̄j* = (1 / *nj*) × Σ *r* over *r* ∈ *Sj* |
| **Median** | Middle value of the sorted sample (or average of the two central values if *nj* is even) |
| **Standard deviation** | *σj* = √\[(1 / *nj*) × Σ (*r* − *r̄j*)²\] |
| **Min / Max** | Minimum and maximum observed ranks in *Sj* |
| **#rank1** | Count of respondents who placed category *j* at rank 1 |
| **#top3** | Count of respondents who placed category *j* at rank 1, 2, or 3 |

Categories are ordered by **ascending mean rank** (lower mean ⇒ higher place in the Top 10). The actual computed statistics depend on the survey data at the time of analysis; the formulas above define how they are derived.

## From Statistics to the Final Ranked List[¶](https://scs.owasp.org/sctop10/methodology/#from-statistics-to-the-final-ranked-list "Permanent link")

### Construction Procedure[¶](https://scs.owasp.org/sctop10/methodology/#construction-procedure "Permanent link")

1.  For each category, compute mean, median, standard deviation, and auxiliary counts.
2.  Sort categories by increasing mean rank to obtain a preliminary ordering.
3.  For categories with very similar mean ranks, use medians, dispersion, and #rank1/#top3 to decide on any refinements.
4.  Cross-check the statistical ordering against 2025 incident data and qualitative feedback to align with practitioner narratives and emerging themes.

This approach is both **data-driven** and **context-aware**: numerical outputs guide the ordering, while qualitative and incident-based input prevents over-interpretation of small numerical differences.

### Risk Tiers[¶](https://scs.owasp.org/sctop10/methodology/#risk-tiers "Permanent link")

Rather than treating the list as a strictly linear order, it is useful to think in terms of *tiers*:

-   **Top tier** — Categories with the lowest mean ranks and high concentrations of rank-1 and top-3 placements (e.g., Access Control, Business Logic, Price Oracle Manipulation).
-   **Middle tier** — Moderate mean ranks with less consensus (e.g., Flash Loan–Facilitated Attacks, Lack of Input Validation).
-   **Tail** — Consistently ranked lower but still important (e.g., Insecure Randomness, DoS).

These tiers inform how much narrative emphasis and documentation each category receives.

## Qualitative Dimensions[¶](https://scs.owasp.org/sctop10/methodology/#qualitative-dimensions "Permanent link")

The survey design includes free-text questions about:

-   Factors influencing rankings (e.g., frequency in production, ease of exploitation, size of losses, difficulty of prevention, systemic impact).
-   Additional or emerging risk categories not captured by the current list.

Qualitative responses are tokenised, normalised, and clustered into themes such as:

-   Upgradeability and proxy risk
-   Economic and incentive design
-   Cross-chain and bridge failures
-   Supply-chain attacks
-   Operational or governance failures

These themes shape how categories are defined, described, and grouped in the final Top 10—for example, informing the promotion of **Proxy & Upgradeability Vulnerabilities** and **Arithmetic Errors** based on 2025 incident data, even when survey categories differed slightly.

## Related Pages[¶](https://scs.owasp.org/sctop10/methodology/#related-pages "Permanent link")

-   [Data Sources](https://scs.owasp.org/sctop10/data-sources/) — Survey, incident databases, and external references used for the 2026 ranking.
