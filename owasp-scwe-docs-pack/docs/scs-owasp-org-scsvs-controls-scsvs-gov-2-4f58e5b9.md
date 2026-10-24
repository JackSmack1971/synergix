---
title: "SCSVS-GOV-2¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-2/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:55.604Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-GOV-2.md "Edit this page")

# SCSVS-GOV-2[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-2/#scsvs-gov-2 "Permanent link")

## S3.2 Tokenomics[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-2/#s32-tokenomics "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-2/#control-objective "Permanent link")

Ensure that tokens used within the smart contract ecosystem are securely implemented, including aspects such as value management, rebasing mechanisms, and reward systems. Contracts should prevent token vulnerabilities like double-spending, incorrect rewards, and improper fee handling.

### S3.2.A Economic Security of Tokens and Their Use Cases[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-GOV-2/#s32a-economic-security-of-tokens-and-their-use-cases "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S3.2.A1 | Ensure that Merkle trees do not contain duplicate proofs, as this can lead to vulnerabilities like double-spending. |  | ✓ | ✓ |  |
| S3.2.A2 | Verify that DeFi protocols account for tokens with negative rebase mechanisms, ensuring that value changes and potential miscalculations are properly handled and mitigated. |  | ✓ | ✓ |  |
| S3.2.A3 | Verify that reward claims are correctly implemented to ensure users receive their correct rewards. |  | ✓ | ✓ |  |
| S3.2.A4 | Verify that tokens do not have vulnerabilities such as incorrect fee application or unexpected behavior due to token transfer issues. |  | ✓ | ✓ |  |
| S3.2.A5 | Verify that all claimable addresses are included in the hashing process for Merkle tree leaves to prevent attackers from claiming funds they should not. |  | ✓ | ✓ |  |
