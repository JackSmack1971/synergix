---
title: "SCSVS-CRYPTO-1¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-1/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:57.132Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-CRYPTO-1.md "Edit this page")

# SCSVS-CRYPTO-1[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-1/#scsvs-crypto-1 "Permanent link")

## S6.1 Key Management[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-1/#s61-key-management "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-1/#control-objective "Permanent link")

Ensure secure handling and storage of private keys and implement robust signature verification processes to prevent unauthorized access and actions.

### S6.1.A Secure Handling and Storage of Private Keys[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-1/#s61a-secure-handling-and-storage-of-private-keys "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S6.1.A1 | Verify that the ecrecover() function handles malformed inputs correctly and does not return invalid data. |  | ✓ | ✓ |  |
| S6.1.A2 | Ensure that signature verification mechanisms are robust against signature malleability and replay attacks, particularly by using nonces or hashed messages rather than relying solely on the signature itself. |  | ✓ | ✓ |  |
| S6.1.A3 | Verify that SignatureChecker.isValidSignatureNow handles edge cases properly and does not revert unexpectedly, considering the ABI decoding issues introduced in Solidity 0.8. |  | ✓ | ✓ |  |
| S6.1.A4 | Ensure that all signatures are checked thoroughly to prevent unauthorized transactions or actions due to weak or improperly managed signature validation. |  | ✓ | ✓ |  |
| S6.1.A5 | Validate that signature protection mechanisms are up-to-date and resistant to signature malleability attacks by avoiding outdated libraries and practices. |  | ✓ | ✓ |  |

### S6.1.B Multi-Signature Wallets[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-CRYPTO-1/#s61b-multi-signature-wallets "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S6.1.B1 | Verify that multi-signature wallets require a predefined number of signatures before executing any transaction. |  | ✓ | ✓ |  |
| S6.1.B2 | Ensure that the multi-signature wallet logic is resistant to replay attacks. |  | ✓ | ✓ |  |
| S6.1.B3 | Verify that the process of adding or removing signatories from the multi-signature wallet is secure and controlled. |  | ✓ | ✓ |  |
