---
title: "SCSVS-BLOCK-2¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-2/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:57.985Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-BLOCK-2.md "Edit this page")

# SCSVS-BLOCK-2[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-2/#scsvs-block-2 "Permanent link")

## S8.2 Resilience Against Resource Exhaustion[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-2/#s82-resilience-against-resource-exhaustion "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-2/#control-objective "Permanent link")

Implement strategies to protect contracts from resource exhaustion attacks that can lead to DoS scenarios.

### S8.2.A Rate Limiting[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BLOCK-2/#s82a-rate-limiting "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S8.2.A1 | Avoid using blocking mechanisms that could lead to a Denial-of-Service (DoS) attack. |  | ✓ | ✓ |  |
| S8.2.A2 | Protect against potential DoS in functions like supportsERC165InterfaceUnchecked() by handling excessive data queries efficiently. |  | ✓ | ✓ |  |
| S8.2.A3 | Ensure that assertions do not lead to denial of service or unexpected contract reverts, especially in scenarios where conditions are not met. |  | ✓ | ✓ |  |
| S8.2.A4 | Verify that return values from external function calls are checked to prevent issues related to unchecked return values, which could lead to unexpected behavior. |  | ✓ | ✓ |  |
| S8.2.A5 | Ensure that contract functions are protected against denial of service due to unexpected reverts by handling all possible error conditions appropriately. |  | ✓ | ✓ |  |
| S8.2.A6 | Ensure that functions such as supportsERC165InterfaceUnchecked() in ERC165Checker.sol handle large data queries efficiently to avoid excessive resource consumption. |  | ✓ | ✓ |  |
