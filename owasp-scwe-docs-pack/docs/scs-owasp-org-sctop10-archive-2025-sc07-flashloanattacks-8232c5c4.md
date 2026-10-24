---
title: "SC07:2025 Flash Loan Attacks"
source_url: "https://scs.owasp.org/sctop10/archive/2025/SC07-FlashLoanAttacks/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:02.806Z"
---
# SC07:2025 Flash Loan Attacks

## Vulnerability: Flash Loan Attacks[¶](https://scs.owasp.org/sctop10/archive/2025/SC07-FlashLoanAttacks/#vulnerability-flash-loan-attacks "Permanent link")

### Description:[¶](https://scs.owasp.org/sctop10/archive/2025/SC07-FlashLoanAttacks/#description "Permanent link")

Flash loan attacks exploit the ability to borrow large sums of funds without collateral within a single transaction. These attacks leverage the atomic nature of blockchain transactions, where all operations must succeed or fail together. By combining flash loans with other vulnerabilities like oracle manipulation, reentrancy, or faulty logic, attackers can manipulate contract behavior and drain funds.

### Examples of Flash Loan Exploits:[¶](https://scs.owasp.org/sctop10/archive/2025/SC07-FlashLoanAttacks/#examples-of-flash-loan-exploits "Permanent link")

1.  **Oracle Manipulation:** Using borrowed funds to skew price oracles, triggering under-collateralized liquidations.
2.  **Liquidity Pool Draining:** Leveraging flash loans to remove liquidity or exploit poorly designed AMM mechanics.
3.  **Arbitrage Exploits:** Exploiting price discrepancies across platforms by manipulating liquidity.

### Impact:[¶](https://scs.owasp.org/sctop10/archive/2025/SC07-FlashLoanAttacks/#impact "Permanent link")

-   **Loss of Funds:** Exploiters can drain protocol reserves or manipulate collateralized loans to steal assets.
-   **Market Disruptions:** Temporary price manipulation or liquidity depletion affecting users and platforms.
-   **Ecosystem Damage:** Loss of trust in protocols, resulting in reduced user adoption and financial impact.

### Remediation:[¶](https://scs.owasp.org/sctop10/archive/2025/SC07-FlashLoanAttacks/#remediation "Permanent link")

-   **Avoid reliance on flash loans in critical logic:** Restrict sensitive functions to operate only within validated and predictable conditions.
-   **Robust Oracle Design:** Use time-weighted average prices (TWAP) or decentralized oracles resistant to manipulation.
-   **Comprehensive Testing:** Include tests simulating flash loan scenarios and edge cases.
-   **Access Control:** Limit access to critical functions to prevent unauthorized or malicious transactions.

### Examples of Flash Loan Exploits:[¶](https://scs.owasp.org/sctop10/archive/2025/SC07-FlashLoanAttacks/#examples-of-flash-loan-exploits_1 "Permanent link")

1.  [UwUlend Hack](https://blog.solidityscan.com/uwulend-hack-analysis-77eb9181a717): A Comprehensive [Hack Analysis](https://blog.solidityscan.com/uwulend-hack-analysis-77eb9181a717)
2.  [Doughfina Hack](https://blog.solidityscan.com/doughfina-hack-analysis-685ed56adb19): A Comprehensive [Hack Analysis](https://blog.solidityscan.com/doughfina-hack-analysis-685ed56adb19)
