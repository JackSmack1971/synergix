---
title: "SCSVS-AUTH-1¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-1/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:55.934Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-AUTH-1.md "Edit this page")

# SCSVS-AUTH-1[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-1/#scsvs-auth-1 "Permanent link")

## S4.1 Role-Based Access Control (RBAC)[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-1/#s41-role-based-access-control-rbac "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-1/#control-objective "Permanent link")

Implement role-based access control to manage permissions and ensure that only authorized users can access specific functions. This includes validating identities, applying the least privilege principle, and ensuring appropriate access controls are in place.

### S4.1.A Multi-Signature Schemes[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-1/#s41a-multi-signature-schemes "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SCWE |
| --- | --- | --- | --- | --- | --- |
| S4.1.A1 | Ensure that the visibility modifier for all functions is appropriate, preventing unnecessary exposure of internal functions. |  | ✓ | ✓ |  |

### S4.1.B Identity Verification[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-1/#s41b-identity-verification "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SCWE |
| --- | --- | --- | --- | --- | --- |
| S4.1.B1 | Validate that unexpected addresses do not result in unintended behaviors, particularly when these addresses refer to contracts within the same protocol. |  | ✓ | ✓ |  |
| S4.1.B2 | Verify that functions like ecrecover handle all potential null addresses properly to avoid vulnerabilities arising from unexpected ecrecover outputs. |  | ✓ | ✓ |  |

### S4.1.C Least Privilege Principle[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-AUTH-1/#s41c-least-privilege-principle "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SCWE |
| --- | --- | --- | --- | --- | --- |
| S4.1.C1 | Use msg.sender (not tx.origin) for authorization to avoid phishing via malicious intermediary contracts. Optionally, require(tx.origin == msg.sender) restricts callers to EOAs only — use only when EOA-only access is explicitly required. |  | ✓ | ✓ |  |
| S4.1.C2 | Certain addresses might be blocked or restricted from receiving tokens (e.g., LUSD). Ensure that address restrictions are properly managed and verified. |  | ✓ | ✓ |  |
| S4.1.C3 | Ensure that Guard’s hooks (e.g., checkTransaction(), checkAfterExecution()) are executed to enforce critical security checks. |  | ✓ | ✓ |  |
| S4.1.C4 | Ensure that access controls are implemented correctly to determine who can use certain functions, and avoid unauthorized changes or withdrawals. |  | ✓ | ✓ |  |
