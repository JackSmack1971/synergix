---
title: "Smart Contract Security Weakness Enumeration (SCWE)"
source_url: "https://scs.owasp.org/SCWE/"
host: "scs.owasp.org"
depth: 2
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:42.344Z"
---
# Smart Contract Security Weakness Enumeration (SCWE)

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

[GitHub Repo](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/)

[OWASP Project Page](https://owasp.org/www-project-smart-contract-security-testing-guide)

About the SCWE

The Smart Contract Security Weakness Enumeration (SCWE) is a list of common security and privacy weaknesses in smart contracts. It is intended to be used as a reference for developers, security researchers, and security professionals. It acts as the bridge between the [SCSVS](https://scs.owasp.org/SCSVS) and the [SCSTG](https://scs.owasp.org/SCSTG).

![](https://scs.owasp.org/assets/scwe-overview.png)

For its definition we draw inspiration from the [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/), which is a community-developed list of common software security weaknesses. The SCWE is intended to be a **complementary list to the CWE**, focusing specifically on security weaknesses in smart contracts.

A **weakness** is a security or privacy issue that can be introduced into a smart contracts. Weaknesses are categorized by the SCSVS categories and controls. For example, a weakness related to the use of insecure random number generators is categorized under the `SCSVS-CODE-1` control.

Each weakness contains the following information:

-   **Overview**: A brief description of the weakness.
-   **Impact**: The potential impact of the weakness on the security or privacy of the application.
-   **Modes of Introduction**: The ways in which the weakness can be introduced into an application.
-   **Mitigations**: Recommendations for mitigating the weakness.

> **"Weakness vs Vulnerability"**: It is important to note that **a weakness is not a vulnerability**, but it can lead to the introduction of vulnerabilities. According to the [CWE](https://cwe.mitre.org/documents/glossary/#Weakness), a weakness is a condition in a software, firmware, hardware, or service component that, under certain circumstances, could contribute to the introduction of vulnerabilities. Whereas a vulnerability is a flaw in a software, firmware, hardware, or service component resulting from a weakness that can be exploited, causing a negative impact to the confidentiality, integrity, or availability of an impacted component or components.

Open Call for New SCWE Submissions

**Want to contribute a new SCWE entry?**

-   Open an issue in our [GitHub repository](https://github.com/OWASP/owasp-scs/issues) with your proposed SCWE-XXX identifier and a brief description.
-   After approval and metadata assignment, submit a Pull Request with your new SCWE entry.
-   See the full [contribution process here](https://pad.riseup.net/p/r.f55dffbdfba1847645dbda2f2f7f084c).
-   See [this sample issue](https://github.com/OWASP/owasp-scs/issues/12) and [this sample PR](https://github.com/OWASP/owasp-scs/pull/14) for examples of a valid submission.

> Thank you for helping us improve the security of smart contracts!

| SCWE ID | Title | SCSVS CG ID | SCSVS SCG IDs | Status |
| --- | --- | --- | --- | --- |
| SCWE-082 | *[Lack of Proper Gas Management](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/)* | SCSVS-DEFI | SCSVS-DEFI-1 | newstatus:new |
| SCWE-058 | *[DoS with Block Gas Limit](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/)* | SCSVS-DEFI | SCSVS-DEFI-1 | newstatus:new |
| SCWE-151 | *[Add/Remove Liquidity Without Minimum Output Validation](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-151/)* | SCSVS-DEFI | SCSVS-DEFI-2 | newstatus:new |
| SCWE-109 | *[Unbounded Loops on Untrusted Input](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-109/)* | SCSVS-DEFI | SCSVS-DEFI-1 | newstatus:new |
| SCWE-059 | *[Insufficient Gas Griefing](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-059/)* | SCSVS-DEFI | SCSVS-DEFI-2 | newstatus:new |
| SCWE-077 | *[Lack of Rate Limiting](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/)* | SCSVS-DEFI | SCSVS-DEFI-2 | newstatus:new |
| SCWE-148 | *[Gas Exhaustion via Unbounded Loops with External Calls](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-148/)* | SCSVS-DEFI | SCSVS-DEFI-1 | newstatus:new |
| SCWE-125 | *[Missing Post-Operation Health Check](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-125/)* | SCSVS-DEFI | SCSVS-DEFI-1 | newstatus:new |
| SCWE-116 | *[Missing Supply Cap Enforcement](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-116/)* | SCSVS-DEFI | SCSVS-DEFI-2 | newstatus:new |
| SCWE-126 | *[Unbounded Withdrawal Queue Growth](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-126/)* | SCSVS-DEFI | SCSVS-DEFI-2 | newstatus:new |
| SCWE-036 | *[Inadequate Gas Limit Handling](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-036/)* | SCSVS-DEFI | SCSVS-DEFI-1 | newstatus:new |
| SCWE-054 | *[Signature Malleability](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-054/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-2 | newstatus:new |
| SCWE-074 | *[Hash Collisions with Multiple Variable Length Arguments](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-074/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-2 | newstatus:new |
| SCWE-056 | *[Lack of Proper Signature Verification](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-056/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-1 | newstatus:new |
| SCWE-025 | *[Improper Cryptographic Key Management](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-025/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-1 | newstatus:new |
| SCWE-084 | *[Insecure Use of blockhash](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-2 | newstatus:new |
| SCWE-115 | *[Weak VRF Parameterization or Callback Validation](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-1 | newstatus:new |
| SCWE-131 | *[Missing Domain Separation in Aggregate Signatures](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-131/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-2 | newstatus:new |
| SCWE-026 | *[Insufficient Hash Verification](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-026/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-2 | newstatus:new |
| SCWE-027 | *[Vulnerable Cryptographic Algorithms](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-027/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-2 | newstatus:new |
| SCWE-114 | *[ECDSA Nonce Reuse](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-114/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-1 | newstatus:new |
| SCWE-055 | *[Missing Protection against Signature Replay Attacks](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-055/)* | SCSVS-CRYPTO | SCSVS-CRYPTO-1 | newstatus:new |
| SCWE-083 | *[Failure to Handle Edge Cases](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-083/)* | SCSVS-COMP | SCSVS-COMP-2 | newstatus:new |
| SCWE-057 | *[Write to Arbitrary Storage Location](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/)* | SCSVS-COMP | SCSVS-COMP-2 | newstatus:new |
| SCWE-135 | *[ERC4626 Share Inflation via Donations](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-135/)* | SCSVS-COMP | SCSVS-COMP-1 | newstatus:new |
| SCWE-110 | *[Fee-On-Transfer Token Misaccounting](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-110/)* | SCSVS-COMP | SCSVS-COMP-1 | newstatus:new |
| SCWE-111 | *[Rebase Token Balance Drift](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-111/)* | SCSVS-COMP | SCSVS-COMP-1 | newstatus:new |
| SCWE-127 | *[EIP-1559 Basefee Assumptions](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-127/)* | SCSVS-BLOCK | SCSVS-BLOCK-2 | newstatus:new |
| SCWE-073 | *[Message Call with Hardcoded Gas Amount](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/)* | SCSVS-BLOCK | SCSVS-BLOCK-1 | newstatus:new |
| SCWE-031 | *[Insecure use of Block Variables](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-031/)* | SCSVS-BLOCK | SCSVS-BLOCK-2 | newstatus:new |
| SCWE-024 | *[Weak Randomness Sources](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/)* | SCSVS-BLOCK | SCSVS-BLOCK-1 | newstatus:new |
| SCWE-153 | *[Reliance on block.prevrandao for High-Value Randomness](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-153/)* | SCSVS-BLOCK | SCSVS-BLOCK-1 | newstatus:new |
| SCWE-065 | *[Block Values as a Proxy for Time](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-065/)* | SCSVS-BLOCK | SCSVS-BLOCK-2 | newstatus:new |
| SCWE-001 | *[Improper Contract Architecture](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-003 | *[Lack of Modularity](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-003/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-002 | *[Excessive Contract Complexity](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-002/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-005 | *[Insecure Upgradeable Proxy Design](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-005/)* | SCSVS-ARCH | SCSVS-ARCH-2 | newstatus:new |
| SCWE-119 | *[Shared Proxy Admin and Logic Owner Key](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-119/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-051 | *[Improper Use of CREATE2 for Contract Deployment](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/)* | SCSVS-ARCH | SCSVS-ARCH-2 | newstatus:new |
| SCWE-070 | *[Incorrect Constructor Name](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-070/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-150 | *[Storage Slot Collision When Upgrading Implementation](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-150/)* | SCSVS-ARCH | SCSVS-ARCH-2 | newstatus:new |
| SCWE-118 | *[Unauthenticated Beacon Upgrade](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-118/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-080 | *[Incorrect Type Conversion](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-080/)* | SCSVS-ARCH | SCSVS-ARCH-2 | newstatus:new |
| SCWE-099 | *[Storage Layout Collision on Upgrade](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-099/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-052 | *[Transaction Order Dependence](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-052/)* | SCSVS-ARCH | SCSVS-ARCH-3 | newstatus:new |
| SCWE-071 | *[Uninitialized Storage Pointer](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-071/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-098 | *[Initialization Front-Running in Upgradeable Contracts](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-098/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-064 | *[Incorrect Inheritance Order](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-064/)* | SCSVS-ARCH | SCSVS-ARCH-2 | newstatus:new |
| SCWE-004 | *[Uncaught Exceptions](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-004/)* | SCSVS-ARCH | SCSVS-ARCH-2 | newstatus:new |
| SCWE-006 | *[Inconsistent Inheritance Hierarchy](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-006/)* | SCSVS-ARCH | SCSVS-ARCH-3 | newstatus:new |
| SCWE-117 | *[Proxy Implementation Selfdestruct Exposure](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-117/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-145 | *[Unvalidated Constructor Parameters](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-145/)* | SCSVS-ARCH | SCSVS-ARCH-1 | newstatus:new |
| SCWE-030 | *[Insecure Oracle Data Updates](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-030/)* | SCSVS-ORACLE | SCSVS-ORACLE-1 | newstatus:new |
| SCWE-086 | *[Missing Validation of Oracle Response Fields (Stale or Incomplete Data)](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-086/)* | SCSVS-ORACLE | SCSVS-ORACLE-1 | newstatus:new |
| SCWE-130 | *[Admin-Write Oracle Without Delay](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-130/)* | SCSVS-ORACLE | SCSVS-ORACLE-1 | newstatus:new |
| SCWE-028 | *[Price Oracle Manipulation](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/)* | SCSVS-ORACLE | SCSVS-ORACLE-1 | newstatus:new |
| SCWE-113 | *[Insufficient TWAP Window or Single Observation](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-113/)* | SCSVS-ORACLE | SCSVS-ORACLE-2 | newstatus:new |
| SCWE-112 | *[Reliance on Low-Liquidity Spot Prices](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-112/)* | SCSVS-ORACLE | SCSVS-ORACLE-2 | newstatus:new |
| SCWE-029 | *[Lack of Decentralized Oracle Sources](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/)* | SCSVS-ORACLE | SCSVS-ORACLE-1 | newstatus:new |
| SCWE-085 | *[Misuse of Oracle Min/Max Price Band Without Validation](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-085/)* | SCSVS-ORACLE | SCSVS-ORACLE-1 | newstatus:new |
| SCWE-088 | *[Improper Decimal Normalization in Price-Based Calculations](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-088/)* | SCSVS-ORACLE | SCSVS-ORACLE-1 | newstatus:new |
| SCWE-100 | *[Missing Quorum Validation in Governance Execution](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-075 | *[Incorrect Ether Balance Tracking](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-140 | *[Ether Locked Due to Missing Withdrawal Path](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-140/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-012 | *[Lack of Multisig Governance](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-012/)* | SCSVS-GOV | SCSVS-GOV-1 | newstatus:new |
| SCWE-078 | *[Improper Handling of Ether Transfers](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-037 | *[Insufficient Protection Against Front-Running](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-081 | *[Improper Handling of Nonce](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/)* | SCSVS-GOV | SCSVS-GOV-2 | newstatus:new |
| SCWE-015 | *[Poor Governance Documentation](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-015/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-102 | *[Missing Checks-Effects-Interactions Pattern](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-102/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-136 | *[Unbounded Proposal Execution Gas](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-136/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-142 | *[Extractable Value from Predictable Transaction Ordering](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-142/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-043 | *[Insecure Use of Fallback Functions](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-043/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-101 | *[Flash-Loan-Fueled Governance Manipulation](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-101/)* | SCSVS-GOV | SCSVS-GOV-1 | newstatus:new |
| SCWE-044 | *[Insecure Use of Storage](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-044/)* | SCSVS-GOV | SCSVS-GOV-1 | newstatus:new |
| SCWE-079 | *[Insecure Use of Transfer and Send](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-079/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-156 | *[Missing Emergency Circuit Breaker for Critical Operations](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-156/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-020 | *[Absence of Time-Locked Functions](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-020/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-050 | *[Unprotected SELFDESTRUCT Instruction](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-050/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-129 | *[Single EOA Admin Without Rotation](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-129/)* | SCSVS-AUTH | SCSVS-AUTH-1 | newstatus:new |
| SCWE-019 | *[Insecure Signature Verification](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-019/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-017 | *[Privileged Role Mismanagement](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-017/)* | SCSVS-AUTH | SCSVS-AUTH-1 | newstatus:new |
| SCWE-139 | *[Single-Step Ownership Transfer Without Confirmation](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-139/)* | SCSVS-AUTH | SCSVS-AUTH-1 | newstatus:new |
| SCWE-049 | *[Unprotected Ether Withdrawal](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-049/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-147 | *[Permit or Meta-Transaction Signatures Without Expiration](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-147/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-038 | *[Insecure Use of Selfdestruct](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-038/)* | SCSVS-AUTH | SCSVS-AUTH-1 | newstatus:new |
| SCWE-045 | *[Insecure Use of Modifiers](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-045/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-016 | *[Insufficient Authorization Checks](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-016/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-105 | *[Permit Signature Replay via Missing Domain Separator or Nonce](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-105/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-106 | *[Unauthenticated Meta-Transactions](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-106/)* | SCSVS-AUTH | SCSVS-AUTH-2 | newstatus:new |
| SCWE-155 | *[Single Point of Failure in Administrative Key Management](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-155/)* | SCSVS-AUTH | SCSVS-AUTH-1 | newstatus:new |
| SCWE-018 | *[Use of tx.origin for Authorization](https://scs.owasp.org/SCWE/SCSVS-AUTH/SCWE-018/)* | SCSVS-AUTH | SCSVS-AUTH-1 | newstatus:new |
| SCWE-096 | *[Missing Token Burn During Cross-Chain NFT Withdrawal](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-096/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-1 | newstatus:new |
| SCWE-094 | *[Insufficient Gas Limit Validation in LayerZero Message Sending](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-2 | newstatus:new |
| SCWE-087 | *[Missing Payload Size Validation in Cross-Chain Messaging (Denial of Service/Stuck Funds)](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-2 | newstatus:new |
| SCWE-033 | *[Chain Split Risks](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-033/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-1 | newstatus:new |
| SCWE-133 | *[Missing Replay Nonce per Bridge Lane](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-133/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-1 | newstatus:new |
| SCWE-132 | *[Mismatched Token Decimals in Bridge Mint/Burn](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-132/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-1 | newstatus:new |
| SCWE-034 | *[Insecure Cross-Chain Messaging](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-034/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-2 | newstatus:new |
| SCWE-032 | *[Dependency on Block Gas Limit](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-032/)* | SCSVS-BRIDGE | SCSVS-BRIDGE-2 | newstatus:new |
| SCWE-103 | *[ERC20 Approval Double-Spend (Allowance Race)](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-103/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-107 | *[Missing Chain ID Validation in Cross-Chain Messages](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-107/)* | SCSVS-COMM | SCSVS-COMM-3 | newstatus:new |
| SCWE-128 | *[Insecure Multicall Context Forwarding](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-128/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-022 | *[Message Replay Vulnerabilities](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-022/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-149 | *[Transfers to Addresses That Cannot Receive Funds](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-149/)* | SCSVS-COMM | SCSVS-COMM-2 | newstatus:new |
| SCWE-108 | *[Unverified Cross-Chain Message Proofs](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/)* | SCSVS-COMM | SCSVS-COMM-3 | newstatus:new |
| SCWE-104 | *[Unprotected ERC777 Token Hooks](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-104/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-023 | *[Lack of Communication Authenticity](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-023/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-134 | *[Low-Level Call to Non-Contract Address](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-042 | *[Insecure Use of External Calls](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/)* | SCSVS-COMM | SCSVS-COMM-2 | newstatus:new |
| SCWE-035 | *[Insecure Delegatecall Usage](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-063 | *[Insecure Event Emission](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/)* | SCSVS-COMM | SCSVS-COMM-2 | newstatus:new |
| SCWE-138 | *[Reentrancy via ERC721/ERC1155 Safe Transfer Callbacks](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-138/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-021 | *[Unsecured Data Transmission](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-021/)* | SCSVS-COMM | SCSVS-COMM-1 | newstatus:new |
| SCWE-007 | *[Presence of Unused Variables](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-007/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-123 | *[Corrupt Free Memory Pointer in Assembly](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-123/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-121 | *[Swallowed Revert Reasons](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-121/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-009 | *[Deprecated Variable and Function Usage](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-009/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-093 | *[Unnamed Function Parameters](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-093/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-039 | *[Insecure Use of Inline Assembly](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-039/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-010 | *[Shadowing Variables and Functions](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-010/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-040 | *[Incorrect Storage Packing](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-040/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-072 | *[Use of Deprecated Solidity Functions](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-072/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-047 | *[Integer Overflows and Underflows](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-047/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-137 | *[Read-Only Reentrancy via View Function State Staleness](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-069 | *[Shadowing State Variables](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-069/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-144 | *[Bypassable Contract Existence Check via extcodesize](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-144/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-091 | *[Lack of Zero Value Check in Token Transfers](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-091/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-143 | *[Critical Address Parameters Not Validated for Zero Address](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-143/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-092 | *[Missing Disable Initializer in Constructor for Proxy Contracts](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-013 | *[Unauthorized Parameter Changes](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-013/)* | SCSVS-GOV | SCSVS-GOV-2 | newstatus:new |
| SCWE-097 | *[Missing Explicit Function Visibility](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-097/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-120 | *[Missing Return Data Length Validation](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-120/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-014 | *[Lack of Emergency Stop Mechanism](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-014/)* | SCSVS-GOV | SCSVS-GOV-3 | newstatus:new |
| SCWE-089 | *[Vulnerable & Outdated Libraries](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-089/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-048 | *[Unchecked Call Return Value](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-048/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-062 | *[Dead Code](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-062/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-146 | *[Improper Use of try/catch Leading to Silent Failures](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-076 | *[Right-To-Left-Override Control Character (U+202E)](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-076/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-122 | *[Calldata Length Not Validated Before Decode](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-122/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-141 | *[Lack of Deadline Validation in Time-Sensitive External Calls](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-141/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-041 | *[Unsafe Downcasting](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-041/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-046 | *[Reentrancy Attacks](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-046/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-008 | *[Hardcoded Constants](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-008/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-095 | *[Missing Destination Address Size Check](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-095/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-154 | *[Calldata Decode Without Length Check](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-154/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-060 | *[Floating Pragma](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-060/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-152 | *[Misuse of Custom Errors Leading to Information Leakage or Wrong Revert Behavior](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-152/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-066 | *[Incorrect Handling of Bitwise Operations](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-066/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-053 | *[Improper Deletion of Mappings](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-090 | *[Missing Slippage Protection in Automated Token Swaps](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-090/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
| SCWE-067 | *[Assert Violation](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-067/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-061 | *[Outdated Compiler Version](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-061/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-124 | *[Inconsistent Rounding Direction in Financial Math](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-124/)* | SCSVS-CODE | SCSVS-CODE-2 | newstatus:new |
| SCWE-011 | *[Insecure ABI Encoding and Decoding](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/)* | SCSVS-ARCH | SCSVS-ARCH-3 | newstatus:new |
| SCWE-068 | *[State Variable Default Visibility](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/)* | SCSVS-CODE | SCSVS-CODE-1 | newstatus:new |
