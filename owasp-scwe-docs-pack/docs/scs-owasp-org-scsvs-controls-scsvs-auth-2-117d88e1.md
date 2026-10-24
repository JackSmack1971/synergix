---
title: "SCSVS-AUTH-2¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-2/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:56.051Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-AUTH-2.md "Edit this page")

# SCSVS-AUTH-2[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-2/#scsvs-auth-2 "Permanent link")

## S4.2 Authorization Mechanisms[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-2/#s42-authorization-mechanisms "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-2/#control-objective "Permanent link")

Implement secure authorization mechanisms to safeguard critical functions and sensitive operations, ensuring only authorized entities can perform these actions.

### S4.2.A Secure Access to Critical Functions[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-2/#s42a-secure-access-to-critical-functions "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SCWE |
| --- | --- | --- | --- | --- | --- |
| S4.2.A1 | Verify that the contract uses msg.sender for authorization instead of tx.origin to avoid vulnerabilities related to contracts that forward calls from legitimate users. |  | ✓ | ✓ |  |
| S4.2.A2 | Implement and verify appropriate access controls for functions that modify contract state or perform sensitive operations to prevent unauthorized access. |  | ✓ | ✓ |  |

### S4.2.B Timed Permissions[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-2/#s42b-timed-permissions "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SCWE |
| --- | --- | --- | --- | --- | --- |
| S4.2.B1 | Ensure that msg.sender validation is properly implemented when using Merkle trees to maintain security and prevent unauthorized access. |  | ✓ | ✓ |  |
| S4.2.B2 | Use whitelisting to restrict interactions to a specific set of addresses, providing additional security against malicious actors. |  | ✓ | ✓ |  |
| S4.2.B3 | Ensure that functions modifying the contract state or accessing sensitive operations have proper access controls implemented. |  | ✓ | ✓ |  |
