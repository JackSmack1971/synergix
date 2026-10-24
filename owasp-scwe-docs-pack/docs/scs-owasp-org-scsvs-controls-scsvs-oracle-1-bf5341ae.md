---
title: "SCSVS-ORACLE-1¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-ORACLE-1/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:57.583Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-ORACLE-1.md "Edit this page")

# SCSVS-ORACLE-1[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ORACLE-1/#scsvs-oracle-1 "Permanent link")

## S7.1 Preventing Overflow/Underflow[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ORACLE-1/#s71-preventing-overflowunderflow "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ORACLE-1/#control-objective "Permanent link")

Implement safe arithmetic practices to prevent overflow and underflow vulnerabilities that can compromise contract functionality and security.

### S7.1.A Use of Safe Math Libraries[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ORACLE-1/#s71a-use-of-safe-math-libraries "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SCWE |
| --- | --- | --- | --- | --- | --- |
| S7.1.A1 | Verify that explicit type casting does not lead to overflow or underflow issues. |  | ✓ | ✓ |  |
| S7.1.A2 | Verify that integer arithmetic operations do not exceed their bounds to prevent integer overflow or underflow vulnerabilities. |  | ✓ | ✓ |  |
| S7.1.A3 | Ensure that operations involving time units and other expressions handle potential overflows correctly. |  | ✓ | ✓ |  |
| S7.1.A4 | Verify that division by zero is correctly handled and causes a transaction revert to prevent unexpected behavior. |  | ✓ | ✓ |  |
| S7.1.A5 | Ensure that variables are managed within their bounds to prevent reverts due to exceeding limits. |  | ✓ | ✓ |  |
| S7.1.A6 | Ensure that arithmetic operations within the unchecked{} block are carefully managed to prevent unintentional overflow or underflow. |  | ✓ | ✓ |  |
| S7.1.A7 | Confirm that inline assembly operations handle division by zero and overflow/underflow according to desired behavior and revert appropriately. |  | ✓ | ✓ |  |
| S7.1.A8 | Implement checks to handle cases where operations might introduce unintended precision issues or rounding errors. |  | ✓ | ✓ |  |

### S7.1.B Fixed-Point Arithmetic[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ORACLE-1/#s71b-fixed-point-arithmetic "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SCWE |
| --- | --- | --- | --- | --- | --- |
| S7.1.B1 | Verify that fixed-point arithmetic operations are performed safely to prevent overflow, underflow, and precision loss. |  | ✓ | ✓ |  |
