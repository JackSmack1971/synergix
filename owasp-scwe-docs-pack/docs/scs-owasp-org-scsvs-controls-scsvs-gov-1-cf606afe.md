---
title: "SCSVS-GOV-1¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-1/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:55.493Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-GOV-1.md "Edit this page")

# SCSVS-GOV-1[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-1/#scsvs-gov-1 "Permanent link")

## S3.1 Economic Models[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-1/#s31-economic-models "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-1/#control-objective "Permanent link")

Ensure that economic models, including incentive structures and tokenomics, are designed and implemented in a way that secures value and incentivizes proper behavior within the ecosystem. Contracts should handle fluctuating token values and avoid creating opportunities for exploitation.

### S3.1.A Incentive Structures[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-1/#s31a-incentive-structures "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S3.1.A1 | Ensure that the withdrawal process implements a pull-based approach rather than a push-based one to track accounting and allow users to pull payments. | ✓ | ✓ | ✓ |  |
| S3.1.A2 | The rate of cbETH to ETH can decrease, impacting users who hold or interact with cbETH. Ensure mechanisms are in place to handle fluctuations in conversion rates. |  | ✓ | ✓ |  |
| S3.1.A3 | Validators on the Ethereum 2.0 Beacon Chain can be penalized or slashed for misbehavior, which can affect the value of rETH. Ensure that these dynamics are considered in value assessments and interactions. |  | ✓ | ✓ |  |
| S3.1.A4 | The conversion rate between ETH and rETH might change over time based on the rewards accrued from staking. Ensure that these fluctuations are properly managed and captured. |  | ✓ | ✓ |  |
