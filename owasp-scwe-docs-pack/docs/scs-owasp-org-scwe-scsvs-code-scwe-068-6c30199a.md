---
title: "SCWE-068: State Variable Default Visibility"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:25.012Z"
---
*Last updated: August 19, 2026*


# SCWE-068: State Variable Default Visibility

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#relationships "Permanent link")

-   CWE-704: Incorrect Type Conversion or Cast
    [https://cwe.mitre.org/data/definitions/704.html](https://cwe.mitre.org/data/definitions/704.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#description "Permanent link")

In Solidity, state variables have a default visibility of `internal`, which means they can only be accessed within the contract or derived contracts (not by external callers). Omitting explicit visibility can lead to unintended behavior: for example, if a developer intends `private` but forgets to specify it, derived contracts can still access the variable; if they intend `public` but omit it, no getter is generated and external callers cannot read the value. Explicit visibility ensures the variable behaves as intended.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#remediation "Permanent link")

Always explicitly specify the visibility of state variables. The possible visibility options are: - `public`: Accessible by anyone, both externally and internally. - `internal`: Accessible only within the contract or derived contracts (default). - `private`: Accessible only within the contract.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-1)contract Vulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-2)    uint balance;  // Default internal; no getter — external callers cannot read it [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-4)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-5)        balance = 100;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-8)    function updateBalance(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-9)        balance = amount;  // Intended public? Forgot visibility — no automatic getter    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-0-11)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-1)contract Secure {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-2)    uint private balance;  // Explicitly set visibility to private [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-3)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-4)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-5)        balance = 100;    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-8)    function updateBalance(uint amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-9)        balance = amount;  // No external access to the variable    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-068/#__codelineno-1-11)}`
