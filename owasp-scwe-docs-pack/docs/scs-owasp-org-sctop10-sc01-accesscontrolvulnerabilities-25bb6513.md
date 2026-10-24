---
title: "SC01:2026 Access Control Vulnerabilities"
source_url: "https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:00.247Z"
---
# SC01:2026 Access Control Vulnerabilities

## Vulnerability: Improper Access Control[¶](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#vulnerability-improper-access-control "Permanent link")

### Description[¶](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#description "Permanent link")

Improper access control describes any situation where a smart contract does not rigorously enforce *who* may invoke privileged behavior, *under which* conditions, and *with which* parameters. In modern DeFi systems this goes far beyond a single `onlyOwner` modifier. Governance contracts, multisigs, guardians, proxy admins, and cross‑chain routers all participate in enforcing who can mint or burn tokens, move reserves, reconfigure pools, pause or unpause core logic, or upgrade implementations. If any of these trust boundaries are weak or inconsistently applied, an attacker may be able to impersonate a privileged actor or cause the system to treat an untrusted address as if it were authorized.

Few areas to focus on: - **Ownership / admin controls** (e.g., `onlyOwner`, governor, multisig) - **Upgrade and pause mechanisms** (proxy admins, guardians) - **Fund movement and accounting** (mint/burn, pool reconfiguration, fee routing) - **Cross-chain or cross-module trust boundaries** (bridges, vault routers, L2 messengers)

Attackers exploit:

-   **Missing modifiers or role checks** on sensitive functions
-   **Incorrect assumption of `msg.sender`** (e.g., via delegate calls or meta-transactions)
-   **Unprotected initialization / re-initialization** of contracts or proxies
-   **Privilege confusion** across modules (e.g., off-by-one checks, mistaken trusted addresses)

When combined with other issues (e.g., logic bugs, upgradeability flaws), access control failures can lead to full protocol compromise.

### Example (Vulnerable Contract)[¶](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#example-vulnerable-contract "Permanent link")

`[](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-3)[](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-4)contract LiquidityPoolVulnerable {     [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-5)    address public owner;    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-6)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-7)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-8)    constructor() {        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-9)        owner = msg.sender;    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-10)    } [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-11)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-12)    // Anyone can set a new owner – critical access control bug    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-13)    function transferOwnership(address newOwner) external {        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-14)        owner = newOwner; // No access control    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-15)    } [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-16)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-17)    // Intended to be called only by the owner to rescue tokens    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-18)    function emergencyWithdraw(address to, uint256 amount) external {        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-19)        // Missing: require(msg.sender == owner)        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-20)        require(balances[address(this)] >= amount, "insufficient");        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-21)        balances[address(this)] -= amount;        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-22)        balances[to] += amount;    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-23)    } [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-0-24)}`

**Issues:**

-   `transferOwnership` is callable by anyone, allowing arbitrary takeover.
-   `emergencyWithdraw` lacks any access control, effectively granting any caller the ability to drain the contract’s balance.

### Example (Fixed Version with Role-Based Access Control)[¶](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#example-fixed-version-with-role-based-access-control "Permanent link")

`[](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-2)pragma solidity ^0.8.20; [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-3)[](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-4)import "@openzeppelin/contracts/access/AccessControl.sol"; [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-5)[](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-6)contract LiquidityPoolSecure is AccessControl {     [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-7)    bytes32 public constant GOVERNANCE_ROLE = keccak256("GOVERNANCE_ROLE");    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-8)    bytes32 public constant GUARDIAN_ROLE = keccak256("GUARDIAN_ROLE"); [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-9)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-10)    mapping(address => uint256) public balances; [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-11)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-12)    event EmergencyWithdraw(address indexed to, uint256 amount, address indexed triggeredBy); [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-13)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-14)    constructor(address governance, address guardian) {        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-15)        _grantRole(DEFAULT_ADMIN_ROLE, governance);        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-16)        _grantRole(GOVERNANCE_ROLE, governance);        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-17)        _grantRole(GUARDIAN_ROLE, guardian);    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-18)    } [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-19)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-20)    function grantGovernance(address newGov) external onlyRole(DEFAULT_ADMIN_ROLE) {        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-21)        _grantRole(GOVERNANCE_ROLE, newGov);    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-22)    } [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-23)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-24)    function setGuardian(address newGuardian) external onlyRole(GOVERNANCE_ROLE) {        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-25)        _grantRole(GUARDIAN_ROLE, newGuardian);    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-26)    } [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-27)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-28)    // Only governance or designated guardians can trigger emergency withdrawals    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-29)    function emergencyWithdraw(address to, uint256 amount)        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-30)        external        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-31)        onlyRole(GUARDIAN_ROLE)    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-32)    {        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-33)        require(to != address(0), "invalid to");        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-34)        require(balances[address(this)] >= amount, "insufficient");        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-35)        balances[address(this)] -= amount;        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-36)        balances[to] += amount; [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-37)        [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-38)        emit EmergencyWithdraw(to, amount, msg.sender);    [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-39)    } [](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#__codelineno-1-40)}`

**Security Improvements:**

-   Explicit **RBAC**: `DEFAULT_ADMIN_ROLE`, `GOVERNANCE_ROLE`, and `GUARDIAN_ROLE`.
-   Only trusted roles can reconfigure privileges or perform emergency withdrawals.
-   Clear separation between configuration (governance) and emergency response (guardian).

### 2025 Case Studies[¶](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#2025-case-studies "Permanent link")

-   **Balancer V2 (November 2025, ~$128M loss)**
    A complex multi-chain pool ecosystem suffered from flawed access control in pool configuration and ownership assumptions. The `manageUserBalance` function had improper access controls—it checked `msg.sender` against a user-provided `op.sender` value, which attackers could set to match `msg.sender` and bypass protections, allowing them to masquerade as pool controllers and execute unauthorized WITHDRAW\_INTERNAL operations. This was chained with a rounding error in `_upscaleArray` to drain liquidity.
    Key lessons:
-   Critical pool operations must be **guarded by explicit role checks** and on-chain governance.
-   Any cross-chain or cross-module "owner" concept must be **verified on-chain**, not assumed from message origin.
-   [https://www.openzeppelin.com/news/understanding-the-balancer-v2-exploit](https://www.openzeppelin.com/news/understanding-the-balancer-v2-exploit)
-   [https://research.checkpoint.com/2025/how-an-attacker-drained-128m-from-balancer-through-rounding-error-exploitation/](https://research.checkpoint.com/2025/how-an-attacker-drained-128m-from-balancer-through-rounding-error-exploitation/)
-   [https://www.halborn.com/blog/post/explained-the-balancer-hack-november-2025](https://www.halborn.com/blog/post/explained-the-balancer-hack-november-2025)

-   **Zoth (March 2025, $8.4M loss)**
    Improper privilege checks around core accounting and administrative functions allowed attackers to perform unauthorized fund movements. The attacker compromised Zoth's deployer wallet (single EOA controlling admin) and performed a malicious upgrade to the USD0PPSubVaultUpgradeable proxy, deploying a malicious implementation to withdraw $8.4M. The protocol relied on brittle assumptions—a single private key controlling critical admin functions.
    Key lessons:

-   Avoid **implicit trust** in addresses (e.g., "deployer is trusted forever").
-   Use **role-based access control (RBAC)** with clear separation between operational, emergency, and upgrade roles.
-   [https://blog.solidityscan.com/zoth-hack-analysis-80ba3ac5076b](https://blog.solidityscan.com/zoth-hack-analysis-80ba3ac5076b)
-   [https://www.halborn.com/blog/post/explained-the-zoth-hack-march-2025](https://www.halborn.com/blog/post/explained-the-zoth-hack-march-2025)

-   **Cork Protocol (May 2025, $11–12M loss)**
    The Uniswap V4 hook callbacks (e.g., `beforeSwap`) lacked proper access control—they did not validate that the caller was the trusted PoolManager. The `beforeSwap` function had no `onlyPoolManager` modifier. Attackers called the hook directly with arbitrary parameters, fooling the protocol into crediting them with derivative tokens. The root cause was **missing caller validation** on hook entry points.
    Key lessons:

-   Hook and callback entry points must **validate the caller** (e.g., onlyPoolManager) explicitly on-chain.
-   [https://dedaub.com/blog/the-11m-cork-protocol-hack-a-critical-lesson-in-uniswap-v4-hook-security/](https://dedaub.com/blog/the-11m-cork-protocol-hack-a-critical-lesson-in-uniswap-v4-hook-security/)
-   [https://www.coindesk.com/business/2025/05/28/a16z-backed-cork-protocol-suffers-usd12m-smart-contract-exploit](https://www.coindesk.com/business/2025/05/28/a16z-backed-cork-protocol-suffers-usd12m-smart-contract-exploit)

### Best Practices & Mitigations[¶](https://scs.owasp.org/sctop10/SC01-AccessControlVulnerabilities/#best-practices-mitigations "Permanent link")

Robust access control starts with using battle‑tested primitives such as OpenZeppelin’s `Ownable` and `AccessControl` rather than bespoke role systems. Privileged roles should be few, clearly documented, and ideally held by well‑secured multisigs or governance modules instead of EOAs. Initialization routines for upgradeable contracts must be locked after first use, with `initializer`/`reinitializer` guards and explicit versioning to prevent re‑initialization attacks. Upgrade paths for proxies and core components should be tightly controlled and observable, with events emitted for every privilege change or upgrade so that off‑chain monitoring can quickly detect abuse. Finally, access control policies should be encoded in tests, fuzzing properties, and, where possible, formal specifications, verifying properties such as “no unprivileged address can ever drain funds or seize admin control.”
