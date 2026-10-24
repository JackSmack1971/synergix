---
title: "SCWE-053: Improper Deletion of Mappings"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:24.093Z"
---
*Last updated: August 19, 2026*


# SCWE-053: Improper Deletion of Mappings

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#relationships "Permanent link")

-   **CWE-459: Incomplete Cleanup**
    [https://cwe.mitre.org/data/definitions/459.html](https://cwe.mitre.org/data/definitions/459.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#description "Permanent link")

In Solidity, mappings (`mapping(address => uint256)`) do not store key-value pairs in a way that allows them to be iterated over or deleted in a straightforward manner. Deleting a mapping variable does not remove its entries; it only resets the reference to the mapping, leaving stale data accessible if another variable references the same mapping. Improper deletion of mappings can lead to storage inconsistencies, potential access control issues, and unintended behavior.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#remediation "Permanent link")

-   Instead of using `delete mappingVariable;`, explicitly set each key’s value to zero where necessary.
-   Consider additional data structures (e.g., arrays or linked lists) to track mapping keys if deletion is required.
-   Ensure mapping deletions do not leave residual data that can be accessed unexpectedly.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-3)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-4)    mapping(address => uint256) public balances; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-5)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-6)    function addBalance(address user, uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-7)        balances[user] = amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-9)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-10)    function resetBalances() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-11)        delete balances;  // ❌ This does not clear individual key-value pairs!    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-12)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-0-13)}`

**Why is this vulnerable?**

-   `delete balances;` only resets the storage reference but does not remove key-value pairs.
-   If another contract or function still references `balances`, the data remains accessible.
-   Unexpected behavior may arise where users assume balances have been erased but can still access the old data.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-3)contract SecureExample {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-4)    mapping(address => uint256) public balances;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-5)    address[] private users; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-7)    function addBalance(address user, uint256 amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-8)        if (balances[user] == 0) {            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-9)            users.push(user);        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-10)        }        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-11)        balances[user] = amount;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-12)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-14)    function resetBalances() public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-15)        for (uint256 i = 0; i < users.length; i++) {            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-16)            balances[users[i]] = 0;  // ✅ Explicitly clears each entry        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-17)        }        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-18)        delete users;  // ✅ Resets the tracking array    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-19)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-053/#__codelineno-1-20)}`

**Why is this safe?** - Tracks users in an array to allow explicit deletion of each mapping entry. - Ensures all key-value pairs are properly reset instead of just deleting the mapping reference. - Prevents residual data from being accessed unintentionally.

**By properly handling mapping deletions, developers can avoid unintended data persistence and ensure accurate contract state management.**
