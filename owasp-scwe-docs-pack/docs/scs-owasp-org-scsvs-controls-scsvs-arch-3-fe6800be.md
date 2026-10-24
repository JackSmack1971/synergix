---
title: "SCSVS-ARCH-3¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:54.732Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-ARCH-3.md "Edit this page")

# SCSVS-ARCH-3[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/#scsvs-arch-3 "Permanent link")

## S1.3 Threat Modeling[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/#s13-threat-modeling "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/#control-objective "Permanent link")

Identify, assess, and mitigate security threats for smart contract systems by implementing a thorough threat modeling process, ensuring that risks are minimized and protections are in place for critical contract features.

### Security Verification Requirements[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/#security-verification-requirements "Permanent link")

### S1.3.A Identifying Threats[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/#s13a-identifying-threats "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S1.3.A1 | Verify that potential threats are identified and documented. | ✓ | ✓ | ✓ |  |
| S1.3.A2 | Ensure that the threat identification process includes input from security experts. |  | ✓ | ✓ |  |
| S1.3.A3 | Check that threats are categorized based on their impact and likelihood. |  | ✓ | ✓ |  |
| S1.3.A4 | Implement protections against front-running in governor proposal creation to prevent attackers from blocking proposals or gaining undue advantages. |  |  | ✓ |  |

### S1.3.B Assessing Risks[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/#s13b-assessing-risks "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S1.3.B1 | Verify that risk assessments are performed for identified threats. |  | ✓ | ✓ |  |
| S1.3.B2 | Ensure that risks are prioritized based on their potential impact and likelihood. |  | ✓ | ✓ |  |
| S1.3.B3 | Check that risk assessment results are documented and reviewed. |  | ✓ | ✓ |  |

### S1.3.C Implementing Mitigations[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-3/#s13c-implementing-mitigations "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S1.3.C1 | Verify that mitigations are implemented for high-priority risks. |  | ✓ | ✓ |  |
| S1.3.C2 | Ensure that mitigation strategies are documented and tested. |  | ✓ | ✓ |  |
| S1.3.C3 | Check that the effectiveness of implemented mitigations is reviewed and validated. |  | ✓ | ✓ |  |
