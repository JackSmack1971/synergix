---
title: "SCSVS-BRIDGE-3¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-3/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:58.462Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-BRIDGE-3.md "Edit this page")

# SCSVS-BRIDGE-3[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-3/#scsvs-bridge-3 "Permanent link")

## S9.3 Event Logging[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-3/#s93-event-logging "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-3/#control-objective "Permanent link")

Implement transparent and secure logging practices to ensure traceability and detect unauthorized changes.

### S9.3.A Transparent and Secure Logging Practices[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-3/#s93a-transparent-and-secure-logging-practices "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S9.3.A1 | Verify that events are emitted properly, especially for critical changes to ensure traceability and transparency. |  | ✓ | ✓ |  |
| S9.3.A2 | Verify that the contract’s event logging correctly reflects critical changes to ensure transparency and traceability. |  | ✓ | ✓ |  |

### S9.3.B Log Analysis[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-BRIDGE-3/#s93b-log-analysis "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S9.3.B1 | Implement tools and processes for analyzing event logs to detect anomalies or unauthorized changes. |  | ✓ | ✓ |  |
| S9.3.B2 | Set up alerts for unusual patterns or discrepancies in logged events. |  | ✓ | ✓ |  |
