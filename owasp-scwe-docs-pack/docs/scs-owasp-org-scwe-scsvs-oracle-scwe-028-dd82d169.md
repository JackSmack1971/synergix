---
title: "SCWE-028: Price Oracle Manipulation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.184Z"
---
*Last updated: August 19, 2026*


# SCWE-028: Price Oracle Manipulation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#description "Permanent link")

Price Oracle manipulation refers to the exploitation of vulnerabilities in price oracles to manipulate contract logic. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of the contract's logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#remediation "Permanent link")

-   **Use decentralized oracles:** Leverage multiple decentralized oracles for price data.
-   **Validate inputs:** Ensure all oracle data is properly validated before use.
-   **Implement circuit breakers:** Add mechanisms to halt operations in case of suspicious activity.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#examples "Permanent link")

-   **Vulnerable to Oracle Manipulation**\- Exploiting Weak Price Feeds

-   Flash Loan-Based Price Manipulation

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-3)interface Oracle {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-4)    function getPrice() external view returns (uint); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-5)} [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-6)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-7)contract VulnerableLending {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-8)    Oracle public priceOracle;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-9)    mapping(address => uint) public balances; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-10)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-11)    constructor(address _oracle) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-12)        priceOracle = Oracle(_oracle);    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-14)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-15)    function deposit() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-16)        balances[msg.sender] += msg.value * priceOracle.getPrice();    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-17)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-18)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-19)    function withdraw(uint amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-20)        require(balances[msg.sender] >= amount, "Insufficient balance");        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-21)        balances[msg.sender] -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-22)        (bool ok, ) = msg.sender.call{value: amount / priceOracle.getPrice()}(""); // Uses current price        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-23)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-24)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-0-25)}`


Why is this vulnerable?

-   Flash loan attack: The attacker can manipulate the price before calling withdraw(), draining funds.
-   No validation mechanism to reject manipulated prices.

-   **Protected Against Oracle Manipulation** — Fixed Code: Price Deviation Guards

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-3)interface Oracle {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-4)    function getPrice() external view returns (uint); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-5)} [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-6)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-7)contract SecureLending {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-8)    Oracle public priceOracle;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-9)    mapping(address => uint) public balances;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-10)    uint public lastValidPrice; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-12)    constructor(address _oracle) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-13)        priceOracle = Oracle(_oracle);        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-14)        lastValidPrice = priceOracle.getPrice();    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-15)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-16)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-17)    function updatePrice() external {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-18)        uint newPrice = priceOracle.getPrice();        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-19)        require(newPrice > lastValidPrice * 95 / 100 && newPrice < lastValidPrice * 105 / 100, "Price deviation too high");        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-20)        lastValidPrice = newPrice;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-21)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-22)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-23)    function deposit() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-24)        updatePrice(); // refresh price before use        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-25)        balances[msg.sender] += msg.value * lastValidPrice;    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-26)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-27)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-28)    function withdraw(uint amount) external {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-29)        updatePrice(); // refresh price before use        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-30)        require(balances[msg.sender] >= amount, "Insufficient balance");        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-31)        balances[msg.sender] -= amount;        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-32)        (bool ok, ) = msg.sender.call{value: amount / lastValidPrice}("");        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-33)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-34)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/#__codelineno-1-35)}`


Fixes: - Implements price deviation guards (5% max change) to reject manipulated or stale prices. - Calls `updatePrice()` before deposit/withdraw to ensure `lastValidPrice` is current.

* * *
