---
title: "SCWE-146: Improper Use of try/catch Leading to Silent Failures"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:27.828Z"
---
*Last updated: August 19, 2026*


# SCWE-146: Improper Use of try/catch Leading to Silent Failures

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#relationships "Permanent link")

-   CWE-390: Detection of Error Condition Without Action
    [https://cwe.mitre.org/data/definitions/390.html](https://cwe.mitre.org/data/definitions/390.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#description "Permanent link")

Solidity 0.6+ `try/catch` allows catching reverts from external calls. If the catch block does not properly handle the failure—e.g., proceeds without reverting, leaves state inconsistent, or swallows the error without logging—the contract can continue execution under incorrect assumptions. Silent failures can lead to fund loss, corrupted state, or exploitable inconsistencies.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#remediation "Permanent link")

-   In catch blocks, either revert with a clear message or update state to reflect the failure (e.g., mark operation as failed, emit event).
-   Avoid proceeding with critical logic when the external call failed unless the failure is explicitly handled and documented.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-3)contract Aggregator {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-4)    function swap(address router, bytes calldata data) external {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-5)        try IRouter(router).swap(data) returns (uint256 amountOut) {            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-6)            transferToUser(msg.sender, amountOut);        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-7)        } catch {            [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-8)            // Silent: user gets nothing but tx succeeds; state may be inconsistent        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-9)        }    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-0-11)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-1-1)function swap(address router, bytes calldata data) external {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-1-2)    try IRouter(router).swap(data) returns (uint256 amountOut) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-1-3)        transferToUser(msg.sender, amountOut);    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-1-4)    } catch {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-1-5)        revert("Swap failed");    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-1-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-146/#__codelineno-1-7)}`

**Fix:** Revert in the catch block so the transaction fails. Avoid `catch (bytes memory reason)` with string concatenation—`reason` may be a custom error selector, not a string.
