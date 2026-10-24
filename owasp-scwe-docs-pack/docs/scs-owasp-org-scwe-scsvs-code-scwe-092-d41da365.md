---
title: "SCWE-092: Missing Disable Initializer in Constructor for Proxy Contracts"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.917Z"
---
*Last updated: August 19, 2026*


# SCWE-092: Missing Disable Initializer in Constructor for Proxy Contracts

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#relationships "Permanent link")

-   **CWE-665**: [Improper Initialization](https://cwe.mitre.org/data/definitions/665.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#description "Permanent link")

This weakness occurs when upgradeable proxy contracts (e.g., UUPS or Transparent Proxy patterns) do not include a call to `_disableInitializers()` inside their constructor. Without this safeguard, malicious actors may invoke the `initialize()` function directly on the implementation contract. This can lead to takeover of admin roles, unauthorized ownership assignment, or malicious configuration of protocol-critical parameters.

This mistake is frequently observed in contracts built with OpenZeppelin Upgradeable libraries where developers forget to disable initializers in the implementation contract’s constructor.

## Impact[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#impact "Permanent link")

Failure to disable initializers in proxy contracts is a recurring and high-severity weakness. It enables attackers to:
\- Become the owner/admin of an uninitialized logic contract.
\- Hijack upgradeability or governance control.
\- Set malicious parameters (fees, treasury addresses, token supply logic, etc.).

This weakness has caused multiple security incidents in production DeFi and NFT projects where attackers initialized orphaned implementation contracts and drained funds.

Its importance stems from:
\- Widespread use of upgradeable contracts in DeFi and DAOs.
\- Frequent developer oversight when using proxy patterns.
\- High impact — loss of protocol ownership, funds, and governance control.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#remediation "Permanent link")

-   Always call `_disableInitializers()` in the constructor of implementation contracts.
-   Review all upgradeable contracts to ensure the implementation cannot be directly initialized.
-   Use OpenZeppelin’s recommended pattern and annotations (e.g., `@custom:oz-upgrades-unsafe-allow constructor`) when disabling initializers.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#examples "Permanent link")

-   **❌ Vulnerable Code**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-1)// Implementation contract for a UUPS Proxy [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-4)import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-5)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-6)contract Vault is Initializable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-7)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-8)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-9)    function initialize(address _owner) public initializer {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-10)        owner = _owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-0-12)}`


⚠️ Issue:
\- The constructor does not call `_disableInitializers()`.
\- Attackers can directly call `initialize()` on the implementation contract (not through the proxy) and take over ownership.

-   **✅ Safe Code**

    `[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-1)// Secure implementation contract for a UUPS Proxy [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-4)import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-5)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-6)contract Vault is Initializable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-7)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-9)    /// @custom:oz-upgrades-unsafe-allow constructor    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-10)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-11)        _disableInitializers(); // Prevents initialize() from being called on implementation    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-14)    function initialize(address _owner) public initializer {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-15)        owner = _owner;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-092/#__codelineno-1-17)}`


✅ Fix:
\- Adding `_disableInitializers()` in the constructor ensures the logic (implementation) contract cannot be initialized directly.
\- Only the proxy can call `initialize()` safely during deployment.
