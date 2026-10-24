---
title: "SCSVS-COMP-6¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-6/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:59.765Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-COMP-6.md "Edit this page")

# SCSVS-COMP-6[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-6/#scsvs-comp-6 "Permanent link")

## S11.6 Uniswap V4 Hook[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-6/#s116-uniswap-v4-hook "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-6/#control-objective "Permanent link")

Ensure secure integration and customization of Uniswap components.

### S11.6.A Secure Integration and Customization[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-6/#s116a-secure-integration-and-customization "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S11.6.A1 | Verify the correct usage of Uniswap’s TickMath and FullMath libraries to ensure proper handling of unchecked arithmetic operations, adhering to version-specific Solidity considerations. |  | ✓ | ✓ |  |
