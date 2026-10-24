---
title: "SCWE-134: Low-Level Call to Non-Contract Address"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:33.455Z"
---
*Last updated: August 19, 2026*


# SCWE-134: Low-Level Call to Non-Contract Address

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#relationships "Permanent link")

-   CWE-252: Unchecked Return Value
    [https://cwe.mitre.org/data/definitions/252.html](https://cwe.mitre.org/data/definitions/252.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#description "Permanent link")

When using low-level `call`, `staticcall`, or `delegatecall` to a user-supplied or dynamic address, the target may be an EOA (externally owned account) with no contract code. In that case, the call returns `success = true` and empty return data, but no code executes. Contracts that assume the target performed logic (e.g., a callback, validation, or state change) can proceed under false assumptions, leading to bypassed checks, unexecuted logic, or incorrect accounting.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#remediation "Permanent link")

-   Verify that the target address contains code using `extcodesize` (or `address.code.length` in Solidity 0.8.12+) before low-level calls.
-   Use allowlists for callable targets instead of accepting arbitrary addresses.
-   Prefer high-level interface calls when the target is known to be a contract.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#examples "Permanent link")

### Vulnerable[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#vulnerable "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-3)contract PluginRegistry {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-4)    function executeViaPlugin(address plugin, bytes calldata data) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-5)        (bool ok, ) = plugin.call(data);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-6)        require(ok, "plugin failed");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-7)        // If plugin is an EOA, call "succeeds" but no code ran — logic may be bypassed    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-0-9)}`

### Fixed[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#fixed "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-3)contract PluginRegistry {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-4)    function executeViaPlugin(address plugin, bytes calldata data) external {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-5)        require(plugin.code.length > 0, "target has no code");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-6)        (bool ok, ) = plugin.call(data);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-7)        require(ok, "plugin failed");    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-8)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-134/#__codelineno-1-9)}`
