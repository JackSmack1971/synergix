---
title: "SCSVS-ARCH-2¶"
source_url: "https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:28:54.619Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/edit/master/SCSVS/controls/SCSVS-ARCH-2.md "Edit this page")

# SCSVS-ARCH-2[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/#scsvs-arch-2 "Permanent link")

## S1.2 Proxy Patterns[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/#s12-proxy-patterns "Permanent link")

### Control Objective[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/#control-objective "Permanent link")

Ensure that proxy patterns and upgrade mechanisms are implemented securely and managed properly, to mitigate risks during contract upgrades, deprecations, and transitions between contract versions.

### Security Verification Requirements[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/#security-verification-requirements "Permanent link")

### S1.2.A Upgrade Mechanisms[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/#s12a-upgrade-mechanisms "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | R | SWE |
| --- | --- | --- | --- | --- | --- |
| S1.2.A1 | Verify that an upgrade mechanism (e.g., proxy pattern) is implemented for the contract. |  | ✓ | ✓ |  |
| S1.2.A2 | Ensure that the upgrade process includes safeguards against unauthorized upgrades. |  | ✓ | ✓ |  |
| S1.2.A3 | Check that the upgrade mechanism is documented and reviewed for security. |  | ✓ | ✓ |  |
| S1.2.A4 | Verify that immutable variables are consistent across implementations during proxy upgrades to prevent misuse. |  |  | ✓ |  |
| S1.2.A5 | Verify that `selfdestruct` and `delegatecall` in implementation contracts do not introduce vulnerabilities or unexpected behaviors in a proxy setup. |  |  | ✓ |  |
| S1.2.A6 | Verify that UUPSUpgradeable contracts are protected against vulnerabilities that may affect uninitialized implementation contracts, ensuring secure upgrade mechanisms. |  |  | ✓ |  |

### S1.2.B Managing Deprecation[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/#s12b-managing-deprecation "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | R | SWE |
| --- | --- | --- | --- | --- | --- |
| S1.2.B1 | Verify that deprecated contract versions are correctly marked and handled. |  |  | ✓ |  |
| S1.2.B2 | Ensure that access to deprecated versions is restricted or disabled. |  |  | ✓ |  |
| S1.2.B3 | Check that migration paths from deprecated versions to new versions are secure. |  |  | ✓ |  |

### S1.2.C Transparent vs. Opaque Proxies[¶](https://scs.owasp.org/SCSVS/controls/SCSVS-ARCH-2/#s12c-transparent-vs-opaque-proxies "Permanent link")

| **SCSVS VR ID** | Requirement | L1 | L2 | R | SWE |
| --- | --- | --- | --- | --- | --- |
| S1.2.C1 | Verify whether a transparent or opaque proxy pattern is used and its suitability for the contract. |  | ✓ | ✓ |  |
| S1.2.C2 | Ensure that the proxy pattern is correctly implemented and does not introduce vulnerabilities. |  | ✓ | ✓ |  |
| S1.2.C3 | Check that the proxy pattern’s choice is documented and justified. |  | ✓ | ✓ |  |
| S1.2.C4 | Ensure that uninitialized contracts cannot be taken over by attackers and that initialization functions are secured with the correct modifiers. |  |  | ✓ |  |
| S1.2.C5 | Verify that `TransparentUpgradeableProxy` and similar proxy patterns handle selector clashes and non-decodable calldata correctly to maintain transparency. |  |  | ✓ |  |
