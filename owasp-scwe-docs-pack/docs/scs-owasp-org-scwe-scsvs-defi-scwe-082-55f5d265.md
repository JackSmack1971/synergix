---
title: "SCWE-082: Lack of Proper Gas Management"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.396Z"
---
*Last updated: August 19, 2026*


# SCWE-082: Lack of Proper Gas Management

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#description "Permanent link")

Gas management is crucial in smart contracts to ensure that they do not run out of gas or cause excessive consumption. If gas consumption is not properly controlled, a contract can fail to execute or can be exploited by attackers to cause denial of service (DoS).

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#remediation "Permanent link")

Properly estimate the gas required for functions and set appropriate gas limits. Use `require` or other mechanisms to handle gas consumption failures and ensure that gas usage remains within acceptable bounds.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-0-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-0-2)    function execute() public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-0-3)        while (true) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-0-4)            // Excessive gas consumption, no limit set        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-0-5)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-0-7)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-2)    uint public counter; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-3)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-4)    function execute(uint _iterations) public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-5)        require(_iterations <= 100, "Too many iterations"); // Limit iterations to avoid excessive gas usage        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-6)        for (uint i = 0; i < _iterations; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-7)            counter++;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-8)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-082/#__codelineno-1-10)}`
