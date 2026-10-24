---
title: "OWASP SCS Employee Lifecycle Security Handbook¶"
source_url: "https://scs.owasp.org/handbooks/03-employee-lifecycle-security/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:05.577Z"
---
# OWASP SCS Employee Lifecycle Security Handbook[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#owasp-scs-employee-lifecycle-security-handbook "Permanent link")

![Cover of Employee Lifecycle Security](https://scs.owasp.org/handbooks/covers-final/03-employee-lifecycle-security.png)

[← All handbooks](https://scs.owasp.org/handbooks/)

Handbook 03 · 76 PDF pages

Control identities and privileges from onboarding through role changes, sensitive access, and verified offboarding.

[Open PDF](https://scs.owasp.org/handbooks/pdfs/03-employee-lifecycle-security.pdf) [Download PDF](https://scs.owasp.org/handbooks/pdfs/03-employee-lifecycle-security.pdf)

**OWASP Smart Contract Security Project**

Part of the [OWASP SCS Handbook Series](https://scs.owasp.org/handbooks/). Built to the series [conventions](https://scs.owasp.org/handbooks/#about-the-series).

## Purpose and Scope[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#purpose-and-scope "Permanent link")

This handbook sets guidelines for securing the full employee lifecycle in Web3 and crypto-native organizations: pre-onboarding screening, least-privilege **access provisioning**, and the **offboarding** and revocation work that most teams treat as an afterthought. It is grounded in current practice: access-centric offboarding that coordinates HR, IT, and compliance rather than leaving revocation to a single team; zero-trust rapid revocation backed by identity and device management tooling; and automated identity lifecycle management (identity and access management, IAM, paired with identity governance and administration, IGA) that closes the gap between an employee's actual role and the privileges still attached to their account. The scope runs from background verification through key and credential handling, role-based access design, and the timely revocation that keeps a departure from becoming a breach, set against the compliance backdrop of SOC 2 (System and Organization Controls 2), the Sarbanes-Oxley Act (SOX), and the Payment Card Industry Data Security Standard (PCI DSS) where they apply.

Web3 raises the stakes on lifecycle security in ways a traditional SaaS company does not face. A departing engineer at a Web2 firm loses access to a dashboard; a departing engineer at a Web3 firm may still hold a **multisig** signer key, a deploy credential, or treasury access that no offboarding ticket can claw back once it has left their laptop. The 2022 compromise of Ronin Network's validator keys, reportedly traced to a fraudulent job offer sent to an engineer, and the pattern of Democratic People's Republic of Korea (DPRK) operatives posing as remote contractors, documented in joint advisories from the Federal Bureau of Investigation (FBI) and the Cybersecurity and Infrastructure Security Agency (CISA), both show that the employee lifecycle, not just the smart contract, is where many of the largest Web3 losses actually start. This handbook treats **onboarding** and offboarding as security-critical processes owned jointly by HR, IT, security, and legal, not as paperwork that happens after the security work is done.

## Target Audience[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#target-audience "Permanent link")

HR, operations, security, and team leads in Web3 and crypto-native organizations responsible for the hiring, **access provisioning**, and **offboarding** of employees, contractors, and protocol signers.

## How to Use This Handbook[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#how-to-use-this-handbook "Permanent link")

Read Part I first to fix the vocabulary, the access types unique to Web3 organizations (infrastructure, code, treasury, and communications), and why **offboarding** belongs to security rather than HR alone. Part II is the **onboarding** reference: pre-onboarding checks, least-privilege access provisioning, security training, and the checklist that closes the loop. Part III mirrors it for offboarding: triggers and timing, revocation across every system a departing employee touched, asset and key recovery, and the legal and HR coordination that documentation and audit trails require. Part IV covers the roles that need special handling: contractors, remote and distributed staff, treasury and deploy-key holders, and multisig signers, plus succession planning for roles a single departure could otherwise leave uncovered. The appendices hold a glossary and printable onboarding and offboarding checklists for teams that want a working template today.

## Relationship to SCSVS, SCSTG, and SCWE[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#relationship-to-scsvs-scstg-and-scwe "Permanent link")

This handbook complements the OWASP smart contract standards without duplicating them. The Smart Contract Security Verification Standard (SCSVS) defines the controls a system must satisfy, including the **access control** and key management requirements that pre-onboarding and **offboarding** here exist to enforce day to day. The Smart Contract Security Testing Guide (SCSTG) describes how to test those controls; the audit trail and verification steps in Parts II and III give testers the process evidence the SCSTG asks them to check for. The Smart Contract Weakness Enumeration (SCWE) catalogs weaknesses in contract code; an orphaned deploy key or a multisig signer who never handed back their role sits upstream of many of those weaknesses, an organizational gap the enumeration does not itself track. Two companion handbooks share this ground directly: the Hiring, Remote Work, and Insider Threat Handbook (05) covers the vetting and insider-risk detection that pre-onboarding here depends on, and the Web3 Operational Security Handbook (11) owns the day-to-day key hygiene and communications discipline that this handbook's provisioning and revocation controls are designed to protect.

## Contents[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#contents "Permanent link")

### Part I: Foundations[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#part-i-foundations "Permanent link")

-   [1\. Introduction to Lifecycle Security](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part1-foundations/#1-introduction-to-lifecycle-security)

### Part II: Onboarding[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#part-ii-onboarding "Permanent link")

-   [2\. Pre-Onboarding](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part2-onboarding/#2-pre-onboarding)
-   [3\. Access Provisioning](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part2-onboarding/#3-access-provisioning)
-   [4\. Training and Awareness](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part2-onboarding/#4-training-and-awareness)
-   [5\. Checklist and Documentation](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part2-onboarding/#5-checklist-and-documentation)

### Part III: Offboarding[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#part-iii-offboarding "Permanent link")

-   [6\. Offboarding Triggers and Timing](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part3-offboarding/#6-offboarding-triggers-and-timing)
-   [7\. Access Revocation](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part3-offboarding/#7-access-revocation)
-   [8\. Asset and Key Recovery](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part3-offboarding/#8-asset-and-key-recovery)
-   [9\. Checklist and Documentation](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part3-offboarding/#9-checklist-and-documentation)
-   [10\. Legal and HR Coordination](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part3-offboarding/#10-legal-and-hr-coordination)

### Part IV: Special Considerations[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#part-iv-special-considerations "Permanent link")

-   [11\. Contractors and Short-Term Roles](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part4-special-considerations/#11-contractors-and-short-term-roles)
-   [12\. Remote and Distributed Teams](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part4-special-considerations/#12-remote-and-distributed-teams)
-   [13\. High-Risk Roles (Treasury, Deploy Keys, Admin)](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part4-special-considerations/#13-high-risk-roles-treasury-deploy-keys-admin)
-   [14\. Multisig and Protocol Signer Lifecycle](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part4-special-considerations/#14-multisig-and-protocol-signer-lifecycle)
-   [15\. Succession and Backup for Key Roles](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part4-special-considerations/#15-succession-and-backup-for-key-roles)

### Part V: Appendices[¶](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/#part-v-appendices "Permanent link")

-   [16\. Appendix A: Glossary](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part5-appendices/#16-appendix-a-glossary)
-   [17\. Appendix B: Onboarding Checklist (Printable)](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part5-appendices/#17-appendix-b-onboarding-checklist-printable)
-   [18\. Appendix C: Offboarding Checklist (Printable)](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/part5-appendices/#18-appendix-c-offboarding-checklist-printable)
-   [19\. Appendix D: References and Further Reading](https://scs.owasp.org/handbooks/03-employee-lifecycle-security/references/)
