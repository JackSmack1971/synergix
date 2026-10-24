---
title: "SCSVS-COMP-3¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-3/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:59.446Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-COMP-3.md "Edit this page")

# SCSVS-COMP-3[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-3/#scsvs-comp-3 "Permanent link")

## S11.3 Vaults[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-3/#s113-vaults "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-3/#control-objective "Permanent link")

Ensure secure asset storage and management within vault systems.

### S11.3.A Secure Asset Storage and Management[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-3/#s113a-secure-asset-storage-and-management "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S11.3.A1 | Address potential overhead issues associated with withdrawing stETH or wstETH, including queue times and withdrawal limits, to ensure smooth operations. |  | ✓ | ✓ |  |
| S11.3.A2 | Handle conversions between stETH and wstETH carefully to avoid potential issues due to the rebasing nature of stETH. |  | ✓ | ✓ |  |
