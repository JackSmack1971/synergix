---
title: "OWASP SCS Checklist¶"
source_url: "https://scs.owasp.org/checklists/"
host: "scs.owasp.org"
depth: 2
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:42.852Z"
---
# OWASP SCS Checklist[¶](https://scs.owasp.org/checklists/#owasp-scs-checklist "Permanent link")

![](https://scs.owasp.org/assets/scs_checklist.png)
[Visit SCS Checklist (Google Sheets)](https://docs.google.com/spreadsheets/d/1W3-XeqbCQp7RHRJKVfllcL9VmzrErMad-biL2mwOChM/edit?usp=sharing)

The OWASP Smart Contract Security Checklist helps you verify compliance with SCSVS controls and SCSTG test cases.

-   **Security Assessments / Pentests**: cover the standard attack surface and start exploring.
-   **Standard Compliance**: includes SCSVS and SCSTG.
-   **Learn & practice** smart contract security skills.
-   **Bug Bounties**: step-by-step coverage of the attack surface.

Track your audit progress in-browser: check items off, filter by status, export results.

[Open Interactive Checklist](https://scs.owasp.org/checklists/interactive)

* * *

## Using the Checklist in Security Audits[¶](https://scs.owasp.org/checklists/#using-the-checklist-in-security-audits "Permanent link")

Use the checklist to structure engagements and ensure consistent coverage:

-   **Scoping**: Filter by category (Architecture, Access Control, Oracle, etc.) to align with project scope.
-   **Prioritization**: Focus on Critical and High severity items first; use the priority filter.
-   **Progress tracking**: Mark items complete as you verify; export JSON/CSV for reports.
-   **Gap analysis**: Compare coverage against SCSVS to identify missing or weak controls.

* * *

## What to Check During Audits[¶](https://scs.owasp.org/checklists/#what-to-check-during-audits "Permanent link")

| Area | Key Checks |
| --- | --- |
| **Architecture** | Upgrade mechanisms, proxy initialization, storage layout, privilege transfers |
| **Business Logic** | LTV/liquidation math, slippage, flash loan resistance, rounding, token donation attacks |
| **Access Control** | RBAC, modifiers, init functions, timelocks, arbitrary call prevention |
| **Oracles & Pricing** | TWAP vs spot, staleness, manipulation vectors, cross-chain consistency |
| **Integrations** | ERC20/4626 edge cases, fee-on-transfer, rebasing tokens, external call safety |

* * *

## Code Review Approach[¶](https://scs.owasp.org/checklists/#code-review-approach "Permanent link")

-   **Top-down**: Start with architecture and access control; trace privilege flows.
-   **Entry points**: Map all external/public functions and their authorization paths.
-   **State changes**: Track storage writes and cross-contract calls for reentrancy and ordering.
-   **Math & precision**: Verify integer handling, decimal scaling, unchecked blocks.

* * *

## Protocol Layers to Focus On[¶](https://scs.owasp.org/checklists/#protocol-layers-to-focus-on "Permanent link")

| Layer | Focus |
| --- | --- |
| **Smart contracts** | Core logic, vaults, oracles, governance, upgrade paths |
| **Bridges & cross-chain** | Message validation, replay protection, sequencer assumptions |
| **Off-chain indexers / APIs** | Input validation, rate limits, authentication |
| **Frontends** | Wallet connection, transaction signing UX, error handling |

* * *

## Web2 & Web2.5 Components[¶](https://scs.owasp.org/checklists/#web2-web25-components "Permanent link")

When auditing full-stack dApps, also verify:

-   **Backend APIs**: Auth (JWT/session), input sanitization, rate limiting, CORS.
-   **RPC nodes / subgraphs**: Data integrity, caching, failure handling.
-   **Signing flows**: Key storage, session management, approval flows.
-   **Third-party SDKs**: Wallet connectors, price feeds, analytics—trust boundaries.

* * *

## Related Resources[¶](https://scs.owasp.org/checklists/#related-resources "Permanent link")

-   [SCSVS Controls](https://scs.owasp.org/SCSVS/) – Full verification standard
-   [SCSTG Tests](https://scs.owasp.org/SCSTG/tests/) – Testing guide
-   [SCWE Weaknesses](https://scs.owasp.org/SCWE/) – Weakness enumerations
