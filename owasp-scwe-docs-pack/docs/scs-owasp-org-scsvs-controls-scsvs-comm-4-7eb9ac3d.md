---
title: "SCSVS-COMM-4¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-4/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:56.913Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-COMM-4.md "Edit this page")

# SCSVS-COMM-4[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-4/#scsvs-comm-4 "Permanent link")

## S5.4 Bridges[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-4/#s54-bridges "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-4/#control-objective "Permanent link")

Ensure the security of cross-chain transactions by implementing robust validation and verification mechanisms to prevent fraud and maintain data integrity.

### S5.4.A Cross-Chain Transaction Security[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMM-4/#s54a-cross-chain-transaction-security "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S5.4.A1 | Verify that the smart contract for cross-chain transactions includes robust mechanisms for verifying and validating transactions across different chains. |  | ✓ | ✓ |  |
| S5.4.A2 | Ensure that the smart contract prevents double-spending and replay attacks in cross-chain transactions by implementing appropriate security checks. |  | ✓ | ✓ |  |
| S5.4.A3 | Check that the cross-chain transaction contract handles communication and data integrity securely between different blockchain networks. |  | ✓ | ✓ |  |
| S5.4.A4 | Verify that the smart contract includes fallback and recovery mechanisms for handling failures or inconsistencies in cross-chain transactions. |  | ✓ | ✓ |  |
