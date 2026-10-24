---
title: "SCWE-057: Write to Arbitrary Storage Location"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:39.186Z"
---
*Last updated: August 19, 2026*


# SCWE-057: Write to Arbitrary Storage Location

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#description "Permanent link")

Writing to arbitrary storage locations can occur when a contract fails to properly validate inputs before interacting with storage variables. An attacker may exploit this vulnerability to overwrite sensitive storage slots, leading to unintended contract behavior, state manipulation, or loss of funds.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#remediation "Permanent link")

To mitigate this vulnerability, ensure that all inputs to storage-related operations are properly validated. Avoid allowing external users to specify arbitrary storage locations. Use access control mechanisms to restrict who can modify sensitive state variables and ensure that only trusted users or contract functions can write to critical storage locations.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-1)contract ArbitraryStorageWrite {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-2)    uint256 public balance; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-4)    function setStorage(uint256 storageLocation, uint256 value) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-5)        assembly {            [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-6)            sstore(storageLocation, value)  // Writing to arbitrary storage location        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-7)        }    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-0-9)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-1)contract SecureStorageWrite {     [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-2)    uint256 public balance;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-3)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-4)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-5)    modifier onlyOwner() {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-6)        require(msg.sender == owner, "Not the owner");        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-7)        _;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-10)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-11)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-14)    function setBalance(uint256 value) public onlyOwner {        [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-15)        balance = value;  // Only the owner can modify the balance    [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-16)    } [](https://scs.owasp.org/SCWE/SCSVS-COMP/SCWE-057/#__codelineno-1-17)}`
