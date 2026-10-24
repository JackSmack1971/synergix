---
title: "SCSVS-BRIDGE-2¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:58.321Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-BRIDGE-2.md "Edit this page")

# SCSVS-BRIDGE-2[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/#scsvs-bridge-2 "Permanent link")

## S9.2 Data Privacy[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/#s92-data-privacy "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/#control-objective "Permanent link")

Ensure that sensitive data within contracts is secured and that privacy measures are effectively implemented.

### S9.2.A Ensuring Sensitive Data is Secure[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/#s92a-ensuring-sensitive-data-is-secure "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S9.2.A1 | Ensure that private data marked in contracts is protected from unauthorized access through blockchain analysis. |  | ✓ | ✓ |  |

### S9.2.B Zero-Knowledge Proofs[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/#s92b-zero-knowledge-proofs "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S9.2.B1 | Verify that zero-knowledge proofs are implemented to ensure privacy without revealing any underlying data. |  | ✓ | ✓ |  |
| S9.2.B2 | Validate the correctness of proof generation and verification processes to prevent any potential leaks or exploits. |  | ✓ | ✓ |  |
| S9.2.B3 | Ensure that zero-knowledge proofs are integrated seamlessly with the blockchain to maintain performance and security. |  | ✓ | ✓ |  |

### S9.2.C Private Transactions[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/#s92c-private-transactions "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S9.2.C1 | Verify that private transaction mechanisms (e.g., zk-SNARKs, zk-STARKs) are correctly implemented to ensure confidentiality of transaction details. |  | ✓ | ✓ |  |
| S9.2.C2 | Ensure that private transactions maintain the integrity and validity of the blockchain. |  | ✓ | ✓ |  |

### S9.2.D Confidential Contracts[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-2/#s92d-confidential-contracts "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S9.2.D1 | Verify that confidential contracts use cryptographic techniques to hide contract state and execution details from unauthorized parties. |  | ✓ | ✓ |  |
| S9.2.D2 | Ensure that only parties with appropriate permissions can access data within confidential contracts. |  | ✓ | ✓ |  |
