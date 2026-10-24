---
title: "SCWE-100: Missing Quorum Validation in Governance Execution"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.336Z"
---
*Last updated: August 19, 2026*


# SCWE-100: Missing Quorum Validation in Governance Execution

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#relationships "Permanent link")

-   CWE-754: Improper Check for Unusual or Exceptional Conditions
    [https://cwe.mitre.org/data/definitions/754.html](https://cwe.mitre.org/data/definitions/754.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#description "Permanent link")

Governance systems that allow proposal execution based solely on vote counts (e.g., "for" > "against") without enforcing a minimum participation threshold (quorum) can execute proposals with negligible community participation. A proposal may "pass" with only a handful of votes if quorum is not checked, allowing a small group or attacker with accumulated tokens to push through changes that lack legitimate community mandate.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#remediation "Permanent link")

-   Enforce a minimum quorum (e.g., percentage of total supply or voting power) before allowing execution.
-   Require both vote majority and quorum to be satisfied; revert execution if quorum is not met.
-   Consider time-weighted or participation-based quorum to prevent last-block manipulation.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-3)contract VulnerableGov {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-4)    mapping(uint256 => uint256) public forVotes;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-5)    mapping(uint256 => uint256) public againstVotes;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-6)    uint256 public totalSupply; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-8)    function execute(uint256 proposalId) external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-9)        require(forVotes[proposalId] > againstVotes[proposalId], "proposal failed");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-10)        // No quorum check — can execute with 2 for, 1 against even if totalSupply is 1M        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-11)        _executeProposal(proposalId);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-12)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-0-13)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-3)contract SecureGov {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-4)    mapping(uint256 => uint256) public forVotes;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-5)    mapping(uint256 => uint256) public againstVotes;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-6)    uint256 public totalSupply;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-7)    uint256 public constant QUORUM_BPS = 400; // 4% [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-9)    function execute(uint256 proposalId) external {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-10)        uint256 totalVotes = forVotes[proposalId] + againstVotes[proposalId];        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-11)        require(forVotes[proposalId] > againstVotes[proposalId], "proposal failed");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-12)        require(totalVotes * 10000 >= totalSupply * QUORUM_BPS, "quorum not met");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-13)        _executeProposal(proposalId);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-100/#__codelineno-1-15)}`
