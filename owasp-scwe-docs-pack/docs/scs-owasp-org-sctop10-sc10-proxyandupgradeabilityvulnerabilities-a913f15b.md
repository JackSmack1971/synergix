---
title: "SC10:2026 Proxy & Upgradeability Vulnerabilities"
source_url: "https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:01.529Z"
---
# SC10:2026 Proxy & Upgradeability Vulnerabilities

## Vulnerability: Proxy & Upgradeability Vulnerabilities[¶](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#vulnerability-proxy-upgradeability-vulnerabilities "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#description "Permanent link")

Proxy and upgradeability vulnerabilities describe any situation where a smart contract uses an upgradeable architecture (proxy, beacon, or implementation-swapping pattern) and the upgrade path, initialization, or admin controls are misdesigned or misconfigured. Upgradeable contracts separate a **proxy** (which holds state and delegates calls) from an **implementation** (which contains logic). When upgradeability is improperly secured, attackers can hijack the proxy admin or upgrade role to deploy malicious implementations, re-initialize contracts to seize ownership, or bypass critical checks in initialization or migration steps.

This affects all contract types that use upgradeability: DeFi (lending, vaults, DEXes), NFTs (collections, marketplaces), DAOs (governance, treasuries), bridges (messengers, asset contracts), and L2/cross-chain systems. Common patterns include Transparent Proxy, UUPS (EIP-1822), Beacon Proxy, and custom router-implementation designs. On non-EVM chains, analogous upgrade mechanisms exist (e.g., Move modules, Solana program upgrades) with similar trust and initialization risks.

Few areas to focus on:

-   **Upgrade and admin roles** (who can change the implementation, storage layout compatibility)
-   **Initialization and re-initialization** (unprotected `initialize`, missing `initializer` guards, storage collisions)
-   **Proxy delegation** (`delegatecall` context, `msg.sender`/`msg.value` propagation)
-   **Storage layout** (slot collisions between proxy and implementation, append-only storage)
-   **Timelocks and governance** (upgrade process, rollback capability)

Attackers exploit:

-   **Unprotected upgrade functions** that allow any caller to point the proxy to a malicious implementation
-   **Re-initialization** to reset ownership, configuration, or access controls
-   **Initialization through delegatecall** where implementation can be initialized with attacker-controlled parameters
-   **Storage collision** between proxy and implementation leading to overwrites

These issues often overlap with access control (SC01) but warrant separate attention due to the systemic impact of proxy and upgrade mechanisms.

### Example (Vulnerable Upgradeable Proxy Admin)[¶](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#example-vulnerable-upgradeable-proxy-admin "Permanent link")

`[](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-4)contract VulnerableProxyAdmin {     [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-5)    address public admin;    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-6)    address public implementation; [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-7)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-8)    constructor(address _implementation) {        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-9)        // Critical: no way to set custom admin; implicitly trusts deployer logic        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-10)        admin = msg.sender;        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-11)        implementation = _implementation;    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-12)    } [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-13)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-14)    function upgrade(address newImplementation) external {        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-15)        // Missing: access control (only admin) and sanity checks        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-16)        implementation = newImplementation;    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-17)    } [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-0-18)}`

**Issues:**

-   No access control on `upgrade`; any caller can change `implementation`.
-   No checks on `newImplementation` (e.g., interface compatibility, non-zero address).

### Example (Safer Upgradeability Pattern)[¶](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#example-safer-upgradeability-pattern "Permanent link")

`[](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-4)import "@openzeppelin/contracts/access/Ownable.sol"; [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-5)[](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-6)contract SafeProxyAdmin is Ownable {     [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-7)    address public implementation; [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-8)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-9)    event Upgraded(address indexed newImplementation); [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-10)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-11)    error InvalidImplementation(); [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-12)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-13)    constructor(address _implementation) {        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-14)        _setImplementation(_implementation);        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-15)        _transferOwnership(msg.sender);    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-16)    } [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-17)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-18)    function _setImplementation(address _implementation) internal {        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-19)        if (_implementation == address(0)) revert InvalidImplementation();        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-20)        implementation = _implementation;    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-21)    } [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-22)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-23)    function upgrade(address newImplementation) external onlyOwner {        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-24)        _setImplementation(newImplementation);        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-25)        emit Upgraded(newImplementation);    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-26)    } [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-1-27)}`

**Security Improvements:**

-   `upgrade` is restricted to the contract owner (which should itself be a robust governance or multisig).
-   Implementation addresses are validated and upgrades are logged via events.

### Initialization & Re-Initialization Risks[¶](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#initialization-re-initialization-risks "Permanent link")

Initialization functions (e.g., `initialize()`, `initializer` modifiers in OpenZeppelin) are critical in upgradeable patterns. Common pitfalls:

-   **Unprotected initializers** that anyone can call.
-   **Re-initialization** that can reset ownership, configuration, or state.
-   Initialization logic that can be reached **through delegatecalls** from proxies in unintended ways.

Basic example:

`[](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-3)[](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-4)contract VulnerableLogic {     [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-5)    address public owner; [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-6)    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-7)    // Missing initializer guard    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-8)    function initialize(address _owner) external {        [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-9)        owner = _owner;    [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-10)    } [](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#__codelineno-2-11)}`

If used behind a proxy without proper initialization control, attackers can call `initialize` via the proxy and set themselves as owner, taking over the protocol.

### 2025 Case Studies[¶](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#2025-case-studies "Permanent link")

-   **Kinto Protocol (July 2025, $1.55M loss)**
    Attackers exploited **uninitialized ERC1967 proxy contracts**. They detected freshly deployed proxy contracts that had not been properly initialized, then initialized them with malicious implementations containing dormant backdoors. Months later, the attacker activated the backdoor, upgraded the proxy to malicious code, and minted K tokens directly to drain $1.55M. The vulnerability: **unprotected initialization** allowing anyone to become the proxy admin.

-   **Uninitialized Proxy Campaign (2025, $10M+ across protocols)**
    A broader campaign targeted uninitialized ERC1967 proxies across multiple EVM chains. Attackers used automated scanning to detect newly deployed proxies before legitimate developers could initialize them, then initialized with malicious implementations. The backdoors lay dormant for months, evading audits. When activated, attackers could upgrade proxies and drain funds.

-   [https://audita.io/blog-articles/the-proxy-hack-uninitialized-contracts-costing-defi-10m-in-losses](https://audita.io/blog-articles/the-proxy-hack-uninitialized-contracts-costing-defi-10m-in-losses)
-   [https://medium.com/mamori-finance/post-mortem-k-proxy-hack-our-path-forward-c2c3809882c6](https://medium.com/mamori-finance/post-mortem-k-proxy-hack-our-path-forward-c2c3809882c6)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC10-ProxyAndUpgradeabilityVulnerabilities/#best-practices-mitigations "Permanent link")

-   **Use well-established proxy patterns and libraries** (e.g., OpenZeppelin UUPS/transparent proxies) instead of bespoke designs.
-   Protect upgrade and admin roles with **robust governance / multisigs**; never leave them on EOAs without strong operational controls.
-   Apply **initializer guards**:
-   Use `initializer` and `reinitializer` modifiers correctly.
-   Lock implementation contracts once deployed to prevent direct initialization.
-   Require **timelocks and multi-step processes** for upgrades:
-   Announce upgrade proposals.
-   Allow time for review/monitoring before execution.
-   Maintain comprehensive **upgrade runbooks** and checklists, including:
-   Testing of migrations.
-   Verification of new implementation code and storage layout.
-   On-chain simulation of upgrade steps where possible.
