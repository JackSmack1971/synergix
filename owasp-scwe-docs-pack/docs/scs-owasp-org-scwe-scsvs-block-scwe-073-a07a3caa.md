---
title: "SCWE-073: Message Call with Hardcoded Gas Amount"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.625Z"
---
*Last updated: August 19, 2026*


# SCWE-073: Message Call with Hardcoded Gas Amount

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#description "Permanent link")

In Solidity, calling external contracts with a hardcoded gas value can lead to various issues, such as running out of gas or allowing a malicious contract to manipulate gas consumption. Hardcoding the gas amount is inflexible and may lead to resource exhaustion or cause the transaction to fail when the gas limit is insufficient for the operation.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#remediation "Permanent link")

Instead of hardcoding gas values, it is better to allow the gas to be automatically determined or adjust the gas dynamically depending on the needs of the transaction. This ensures that the transaction can complete successfully while avoiding unnecessary resource consumption.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-2)    address public target; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-4)    function callTarget() public {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-5)        // Hardcoding the gas value for the message call        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-6)        target.call{gas: 100000}("");  // Vulnerable to resource consumption issues    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-0-8)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-2)    address public target; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-3)    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-4)    function callTarget() public {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-5)        // Let Solidity handle gas consumption dynamically        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-6)        target.call("");  // Gas amount handled by the EVM dynamically    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-073/#__codelineno-1-8)}`
