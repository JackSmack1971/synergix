---
title: "SCSVS-BLOCK-1¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-1/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:57.884Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-BLOCK-1.md "Edit this page")

# SCSVS-BLOCK-1[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-1/#scsvs-block-1 "Permanent link")

## S8.1 Gas Limits[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-1/#s81-gas-limits "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-1/#control-objective "Permanent link")

Ensure that contract design and function implementations are efficient in gas usage to mitigate risks associated with out-of-gas errors and related vulnerabilities.

### S8.1.A Efficient Loop and Function Design[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-1/#s81a-efficient-loop-and-function-design "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S8.1.A1 | Ensure that contracts are protected against insufficient gas griefing attacks by carefully managing gas consumption in critical functions. |  | ✓ | ✓ |  |
| S8.1.A2 | Ensure that systems like the RocketDepositPool contract handle failures in functions like burn() gracefully. |  | ✓ | ✓ |  |
| S8.1.A3 | Verify that gas usage in functions and loops is efficient to avoid out-of-gas errors. |  | ✓ | ✓ |  |
| S8.1.A4 | Implement mechanisms to prevent denial of service attacks due to block gas limits, ensuring that transactions or operations do not exceed the gas limit constraints. |  | ✓ | ✓ |  |

### S8.1.B Fallback Mechanisms[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-1/#s81b-fallback-mechanisms "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S8.1.B1 | Ensure that try/catch blocks are provided with adequate gas to avoid failures and unexpected behavior in case of errors. |  | ✓ | ✓ |  |
