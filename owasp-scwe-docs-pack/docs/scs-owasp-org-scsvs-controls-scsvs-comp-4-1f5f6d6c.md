---
title: "SCSVS-COMP-4¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-4/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:59.557Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-COMP-4.md "Edit this page")

# SCSVS-COMP-4[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-4/#scsvs-comp-4 "Permanent link")

## S11.4 Liquid Staking[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-4/#s114-liquid-staking "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-4/#control-objective "Permanent link")

Ensure secure staking mechanisms to protect users' assets.

### S11.4.A Secure Staking Mechanisms[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-COMP-4/#s114a-secure-staking-mechanisms "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | L3 | SWE |
| --- | --- | --- | --- | --- | --- |
| S11.4.A1 | Verify that mechanisms for detaching sfrxETH from frxETH are robust to prevent discrepancies and ensure accurate reward transfers, particularly when controlled by centralized entities. |  | ✓ | ✓ |  |
| S11.4.A2 | Monitor potential future changes in the sfrxETH/ETH rate and ensure users are adequately forewarned to mitigate risks associated with rate fluctuations. |  | ✓ | ✓ |  |
