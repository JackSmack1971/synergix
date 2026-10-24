---
title: "SCWE-029: Lack of Decentralized Oracle Sources"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:35.302Z"
---
*Last updated: August 19, 2026*


# SCWE-029: Lack of Decentralized Oracle Sources

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#description "Permanent link")

Lack of decentralized oracle sources refers to the reliance on a single oracle for critical data, which can be manipulated or compromised. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of the contract's logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#remediation "Permanent link")

-   **Use multiple oracles:** Leverage multiple decentralized oracles for critical data.
-   **Validate inputs:** Ensure all oracle data is properly validated before use.
-   **Implement fallback mechanisms:** Use fallback oracles in case of failure.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#examples "Permanent link")

-   **Single Oracle Source/ Single Point of Failure**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-3)interface Oracle {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-4)    function getPrice() external view returns (uint); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-5)} [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-6)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-7)contract SingleOracle {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-8)    Oracle public priceOracle; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-10)    constructor(address _oracle) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-11)        priceOracle = Oracle(_oracle);    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-12)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-13)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-14)    function getPrice() public view returns (uint) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-15)        return priceOracle.getPrice(); // Single source of truth    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-0-17)}`


Why is this vulnerable? - If the oracle fails, is compromised, or is manipulated, the contract has no fallback. - Attackers could hijack the single oracle and return malicious data.

-   **Decentralized Oracle Sources- Using Multiple Oracles & Fallbacks**

    `[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-3)interface Oracle {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-4)    function getPrice() external view returns (uint); [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-5)} [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-6)[](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-7)contract MultiOracle {     [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-8)    Oracle[] public priceOracles; [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-10)    constructor(address[] memory _oracles) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-11)        for (uint i = 0; i < _oracles.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-12)            priceOracles.push(Oracle(_oracles[i]));        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-13)        }    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-15)    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-16)    function getPrice() public view returns (uint) {        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-17)        uint totalPrice = 0;        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-18)        for (uint i = 0; i < priceOracles.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-19)            totalPrice += priceOracles[i].getPrice();        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-20)        }        [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-21)        return totalPrice / priceOracles.length; // Averaging multiple oracles    [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-22)    } [](https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-029/#__codelineno-1-23)}`

    Fixes:
-   Uses multiple oracles and computes an average to prevent manipulation.
-   If one oracle fails or gets compromised, the contract still functions correctly.

* * *
