---
title: "SCWE-035: Insecure Delegatecall Usage"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.348Z"
---
*Last updated: August 19, 2026*


# SCWE-035: Insecure Delegatecall Usage

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#relationships "Permanent link")

-   CWE-250: Execution with Unnecessary Privileges
    [CWE-250 Link](https://cwe.mitre.org/data/definitions/250.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#description "Permanent link")

Insecure delegatecall usage refers to vulnerabilities that arise when using `delegatecall` to execute code from another contract. This can lead to: - Unauthorized access to sensitive functions. - Exploitation of vulnerabilities in the called contract. - Loss of funds or data.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#remediation "Permanent link")

-   **Validate targets:** Ensure the target contract is trusted and secure.
-   **Restrict permissions:** Restrict `delegatecall` usage to trusted addresses.
-   **Test thoroughly:** Conduct extensive testing to ensure `delegatecall` is used securely.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#examples "Permanent link")

-   **Insecure Delegatecall Usage**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-3)contract InsecureDelegatecall {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-4)    function executeDelegatecall(address target, bytes memory data) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-5)        (bool success, ) = target.delegatecall(data); // ❌ No validation, attacker-controlled contract can be used        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-6)        require(success, "Delegatecall failed");    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-0-8)}`

-   Anyone can call `executeDelegatecall()` with a malicious contract, which will execute arbitrary code within the caller’s context.
-   Can lead to theft of funds, privilege escalation, or state corruption.

-   **Secure Delegatecall Usage**

    `[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-3)contract SecureDelegatecall {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-4)    address public owner;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-5)    address public trustedTarget; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-7)    modifier onlyOwner() {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-8)        require(msg.sender == owner, "Not authorized");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-9)        _;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-10)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-11)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-12)    constructor(address _trustedTarget) {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-13)        owner = msg.sender;        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-14)        trustedTarget = _trustedTarget;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-15)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-16)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-17)    function updateTrustedTarget(address _newTarget) public onlyOwner {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-18)        require(isTrusted(_newTarget), "Untrusted target");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-19)        trustedTarget = _newTarget;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-20)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-21)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-22)    function executeDelegatecall(bytes memory data) public onlyOwner {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-23)        require(trustedTarget != address(0), "Invalid target");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-24)        (bool success, ) = trustedTarget.delegatecall(data);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-25)        require(success, "Delegatecall failed");    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-26)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-27)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-28)    function isTrusted(address _target) internal pure returns (bool) {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-29)        // Implement further checks if needed        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-30)        return _target != address(0);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-31)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-035/#__codelineno-1-32)}`


Fixes: - Only the contract owner can update trustedTarget. - Validation of trusted target before executing delegatecall. - Prevents arbitrary execution by restricting calls to trustedTarget.
