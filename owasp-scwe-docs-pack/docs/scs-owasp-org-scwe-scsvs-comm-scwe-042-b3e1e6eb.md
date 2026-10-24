---
title: "SCWE-042: Insecure Use of External Calls"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.490Z"
---
*Last updated: August 19, 2026*


# SCWE-042: Insecure Use of External Calls

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#relationships "Permanent link")

-   CWE-829: Inclusion of Functionality from Untrusted Control Sphere
    [CWE-829 Link](https://cwe.mitre.org/data/definitions/829.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#description "Permanent link")

Insecure use of external calls refers to vulnerabilities that arise when calling external contracts without proper validation or safeguards. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of vulnerabilities in the called contract.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#remediation "Permanent link")

-   **Validate targets:** Ensure the target contract is trusted and secure.
-   **Use secure libraries:** Leverage well-audited libraries for external calls.
-   **Test thoroughly:** Conduct extensive testing to ensure external calls are secure.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#examples "Permanent link")

-   **Insecure External Call**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-3)contract InsecureExternalCall {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-4)    function callExternal(address target, bytes memory data) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-5)        (bool success, ) = target.call(data); // No validation        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-6)        require(success, "Call failed");    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-0-8)}`

-   **Secure External Call**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-3)interface ITrustedContract {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-4)    function executeAction(uint256 param) external; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-5)} [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-6)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-7)contract SecureExternalCall {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-8)    address public immutable trustedTarget;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-9)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-11)    constructor(address _trustedTarget) {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-12)        trustedTarget = _trustedTarget;        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-13)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-14)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-15)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-16)    modifier onlyOwner() {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-17)        require(msg.sender == owner, "Unauthorized");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-18)        _;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-19)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-20)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-21)    function callExternal(uint256 param) public onlyOwner {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-22)        ITrustedContract(trustedTarget).executeAction(param);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-23)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-042/#__codelineno-1-24)}`

    Why is this secure?

-   No arbitrary data input—Only predefined `function executeAction(uint256)` can be called.
-   Access control added—Only the owner can execute external calls.
-   Interface-based call—Avoids raw `.call()`, reducing attack vectors.
-   Immutable trusted address—Prevents runtime modifications to the target contract.

* * *
