---
title: "SCWE-058: DoS with Block Gas Limit"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.041Z"
---
*Last updated: August 19, 2026*


# SCWE-058: DoS with Block Gas Limit

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#relationships "Permanent link")

-   CWE-400: Uncontrolled Resource Consumption
    [https://cwe.mitre.org/data/definitions/400.html](https://cwe.mitre.org/data/definitions/400.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#description "Permanent link")

Denial of Service (DoS) with block gas limit occurs when a contract is designed in such a way that its execution depends on a large amount of gas, potentially exceeding the block gas limit. This can result in the transaction failing, causing the contract to become unavailable or unusable. Attackers can exploit this vulnerability by creating transactions that consume excessive gas, effectively locking the contract or preventing normal operation.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#remediation "Permanent link")

To mitigate this vulnerability, ensure that operations that depend on gas consumption are efficient and that gas limits are taken into account when designing contract logic. Avoid functions that require large amounts of gas to complete, and consider implementing features like batching or chunking operations to spread the gas usage across multiple transactions.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-3)contract GasLimitDoS {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-4)    uint256[] public data; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-6)    function addData(uint256[] memory newData) public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-7)        for (uint256 i = 0; i < newData.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-8)            data.push(newData[i]);  // Can consume a large amount of gas if the array is large        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-9)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-0-11)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-3)contract GasLimitSafe {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-4)    uint256[] public data;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-5)    uint256 public constant MAX_BATCH = 100; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-7)    function addData(uint256[] memory newData) public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-8)        require(newData.length <= MAX_BATCH, "Batch too large; split into smaller calls");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-9)        for (uint256 i = 0; i < newData.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-10)            data.push(newData[i]);        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-11)        }    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-058/#__codelineno-1-13)}`
