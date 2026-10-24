---
title: "SCWE-108: Unverified Cross-Chain Message Proofs"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.198Z"
---
*Last updated: August 19, 2026*


# SCWE-108: Unverified Cross-Chain Message Proofs

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#relationships "Permanent link")

-   CWE-345: Insufficient Verification of Data Authenticity
    [https://cwe.mitre.org/data/definitions/345.html](https://cwe.mitre.org/data/definitions/345.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#description "Permanent link")

Relayers may deliver fabricated payloads if the destination contract does not validate Merkle proofs, light-client headers, or signatures that attest to the message on the source chain. Forged messages can mint wrapped assets or execute arbitrary calls.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#remediation "Permanent link")

-   Verify message inclusion against a trusted root (Merkle/Patricia proof) or light-client header.
-   Validate signatures from authorized validators and enforce quorum thresholds.
-   Reject messages that fail proof verification or originate from unrecognized relayers.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-0-3)contract Inbox {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-0-4)    function deliver(bytes calldata payload) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-0-5)        _process(payload); // assumes relayer is honest    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-0-7)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-3)contract Inbox {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-4)    address[] public validators;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-5)    uint256 public constant QUORUM = 2; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-7)    function deliver(bytes calldata payload, bytes[] calldata sigs) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-8)        require(_verifyQuorum(payload, sigs) >= QUORUM, "invalid proof");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-9)        _process(payload);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-108/#__codelineno-1-11)}`
