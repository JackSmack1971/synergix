---
title: "SCWE-077: Lack of Rate Limiting"
source_url: "https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:38.278Z"
---
*Last updated: August 19, 2026*


# SCWE-077: Lack of Rate Limiting

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#relationships "Permanent link")

-   **CWE-770: Allocation of Resources Without Limits or Throttling**
    [https://cwe.mitre.org/data/definitions/770.html](https://cwe.mitre.org/data/definitions/770.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#description "Permanent link")

Lack of rate limiting in a smart contract can lead to **Denial of Service (DoS)** attacks, excessive gas consumption, or contract state bloating. Without a mechanism to restrict the frequency of function calls, an attacker can flood the contract with transactions, causing delays, increased gas fees, or complete unavailability of critical functions.

This vulnerability is particularly dangerous in **DeFi protocols**, where unlimited function calls could drain funds, abuse governance mechanisms, or overload on-chain processing.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#remediation "Permanent link")

-   Implement **rate-limiting mechanisms** such as **time-based constraints** (e.g., requiring a cooldown period between calls).
-   Use **counters with expiration timestamps** to track and restrict repetitive actions.
-   Introduce **gas fees or staking requirements** to deter spam transactions.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-2)    mapping(address => uint) public userRequests; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-4)    // ❌ No rate limiting: users can spam this function indefinitely    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-5)    function request() public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-6)        userRequests[msg.sender]++;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-7)        // No restrictions or cooldowns, allowing abuse    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-0-9)}`

**Why is this vulnerable?** - No restrictions on how frequently a user can call `request()`. - An attacker can spam transactions, leading to high gas costs and DoS. - Storage bloat from excessive `userRequests` mappings.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-1)contract SecureExample {     [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-2)    struct RequestData {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-3)        uint count;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-4)        uint lastReset;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-5)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-7)    mapping(address => RequestData) public userRequests;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-8)    uint public constant REQUEST_LIMIT = 5;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-9)    uint public constant TIME_WINDOW = 1 hours; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-11)    // ✅ Implement rate limiting with a cooldown period    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-12)    function request() public {        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-13)        RequestData storage requestData = userRequests[msg.sender]; [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-14)        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-15)        if (block.timestamp > requestData.lastReset + TIME_WINDOW) {            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-16)            requestData.count = 0;  // Reset count after time window            [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-17)            requestData.lastReset = block.timestamp;        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-18)        } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-19)        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-20)        require(requestData.count < REQUEST_LIMIT, "Rate limit exceeded");        [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-21)        requestData.count++;    [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-22)    } [](https://scs.owasp.org/SCWE/SCSVS-DEFI/SCWE-077/#__codelineno-1-23)}`

**Why is this safe?** - Tracks request timestamps, resetting counts after a fixed period. - Restricts excessive calls, preventing abuse and DoS attacks. - Efficient state management, reducing unnecessary storage costs.

**By enforcing rate limits, contracts can prevent spam attacks and ensure fair access to on-chain resources.**
