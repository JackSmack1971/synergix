---
title: "SCSVS-GOV-3¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-3/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:55.740Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-GOV-3.md "Edit this page")

# SCSVS-GOV-3[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-3/#scsvs-gov-3 "Permanent link")

## S3.3 Preventing Reentrancy and Logic Flaws[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-3/#s33-preventing-reentrancy-and-logic-flaws "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-3/#control-objective "Permanent link")

Ensure the smart contract's transaction flow and logic integrity are protected from reentrancy attacks and logic flaws. Contracts should implement robust control structures and security patterns to prevent reentrancy, handle complex flows, and ensure that state transitions are secure and symmetrical.

### S3.3.A Transaction Flow Security[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-3/#s33a-transaction-flow-security "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S3.3.A1 | Check for edge cases in loop control structures to prevent unexpected behaviors due to break or continue statements. |  | ✓ | ✓ |  |
| S3.3.A2 | Ensure that scenarios where sender and recipient are the same are considered to prevent unintended issues in smart contracts. |  | ✓ | ✓ |  |
| S3.3.A3 | Ensure that the `NonReentrant` modifier is applied before other modifiers in functions to prevent reentrancy attacks. |  | ✓ | ✓ |  |
| S3.3.A4 | Verify that the check-effect-interaction pattern is implemented to prevent reentrancy attacks. |  | ✓ | ✓ |  |
| S3.3.A5 | Ensure that function calls with arbitrary user input and low-level calls are handled securely to avoid introducing risks. |  | ✓ | ✓ |  |

### S3.3.B Function Integrity[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-3/#s33b-function-integrity "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S3.3.B1 | Ensure that functions intended to be unique per parameter set are not callable multiple times to prevent potential issues. |  | ✓ | ✓ |  |
| S3.3.B2 | Verify that state changes in functions, such as withdraw and deposit, are symmetrically handled to avoid undesired behavior due to inconsistencies. |  | ✓ | ✓ |  |
