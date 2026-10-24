---
title: "SCWE-115: Weak VRF Parameterization or Callback Validation"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.940Z"
---
*Last updated: August 19, 2026*


# SCWE-115: Weak VRF Parameterization or Callback Validation

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#relationships "Permanent link")

-   CWE-330: Use of Insufficiently Random Values
    [https://cwe.mitre.org/data/definitions/330.html](https://cwe.mitre.org/data/definitions/330.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#description "Permanent link")

Using VRF services without validating `requestId`, sender, or subscription can let attackers spoof fulfillments or drain subscription balances. Misconfigured key hashes, gas limits, or shared subscriptions can cause predictable failures and force fallback logic that leaks randomness.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#remediation "Permanent link")

-   Bind VRF fulfillments to tracked `requestId` values and trusted coordinator addresses.
-   Use dedicated subscriptions, appropriate key hashes, and sane callback gas limits.
-   Revert on unexpected fulfillments and avoid using fallback pseudo-randomness.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-2)import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-4)contract Lottery is VRFConsumerBaseV2 {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-5)    uint256 public randomWord; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-7)    function fulfillRandomWords(uint256, uint256[] memory words) internal override {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-8)        randomWord = words[0]; // no requestId or sender validation    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-0-10)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-2)import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol"; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-4)contract Lottery is VRFConsumerBaseV2 {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-5)    uint256 public pending; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-7)    function request() external { pending = COORDINATOR.requestRandomWords(/* params */); } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-9)    function fulfillRandomWords(uint256 requestId, uint256[] memory words) internal override {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-10)        require(requestId == pending, "unknown request");        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-11)        pending = 0;        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-12)        // use words[0]...    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-115/#__codelineno-1-14)}`
