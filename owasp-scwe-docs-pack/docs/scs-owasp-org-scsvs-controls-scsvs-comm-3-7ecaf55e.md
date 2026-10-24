---
title: "SCSVS-COMM-3¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-3/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:56.817Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-COMM-3.md "Edit this page")

# SCSVS-COMM-3[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-3/#scsvs-comm-3 "Permanent link")

## S5.3 Cross-Chain Interactions[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-3/#s53-cross-chain-interactions "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-3/#control-objective "Permanent link")

Ensure secure handling of external calls and atomic swaps during cross-chain interactions to maintain operational reliability and prevent fraud.

### S5.3.A Handling External Calls Securely[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-3/#s53a-handling-external-calls-securely "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S5.3.A1 | Ensure that parameters for Chainlink VRF (Verifiable Random Function) are thoroughly validated to prevent the fulfillRandomWord function from returning incorrect values instead of reverting. |  | ✓ | ✓ |  |
| S5.3.A2 | Implement robust security checks for cross-chain messaging to ensure correct permissions and intended functionality. |  | ✓ | ✓ |  |
| S5.3.A3 | Verify that contracts created using the CREATE opcode handle block reorganizations securely to prevent unexpected eliminations. |  | ✓ | ✓ |  |
| S5.3.A4 | Ensure robust cross-chain messaging security checks to prevent replay attacks where signatures valid on one chain might be exploited on another. |  | ✓ | ✓ |  |

### S5.3.B Atomic Swaps[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-3/#s53b-atomic-swaps "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S5.3.B1 | Verify that the smart contract supports atomic swaps with robust mechanisms to ensure that swaps are completed successfully or not executed at all. |  | ✓ | ✓ |  |
| S5.3.B2 | Ensure that the smart contract includes checks to validate the atomic swap conditions and prevent partial or fraudulent swaps. |  | ✓ | ✓ |  |
| S5.3.B3 | Check that the smart contract handles potential failures or disputes in atomic swaps securely and fairly. |  | ✓ | ✓ |  |
| S5.3.B4 | Verify that the atomic swap functionality is tested thoroughly to cover various scenarios and edge cases. |  | ✓ | ✓ |  |
