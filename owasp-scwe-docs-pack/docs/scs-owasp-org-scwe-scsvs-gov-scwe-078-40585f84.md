---
title: "SCWE-078: Improper Handling of Ether Transfers"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:28.977Z"
---
*Last updated: August 19, 2026*


# SCWE-078: Improper Handling of Ether Transfers

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#relationships "Permanent link")

-   CWE-703: Improper Check or Handling of Exceptional Conditions
    [https://cwe.mitre.org/data/definitions/703.html](https://cwe.mitre.org/data/definitions/703.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#description "Permanent link")

Improper handling of Ether transfers in Solidity can lead to unexpected behaviors, such as failed transactions or loss of funds. For instance, when using `transfer()` or `send()`, failure to check for successful execution or not handling exceptions correctly can cause Ether to be locked or lost in the contract.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#remediation "Permanent link")

Always handle exceptions properly when transferring Ether. Ensure that you check for success or failure using `require()` or `assert()` after Ether transfers. Additionally, use `call()` with a specified gas limit for greater flexibility and error handling.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-4)    function transferEther(address payable _to) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-5)        // Fails silently if transfer fails        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-6)        _to.transfer(msg.value);  // No error handling, can cause issues    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-0-8)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-4)    function transferEther(address payable _to) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-5)        (bool success, ) = _to.call{value: msg.value}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-6)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-078/#__codelineno-1-8)}`
