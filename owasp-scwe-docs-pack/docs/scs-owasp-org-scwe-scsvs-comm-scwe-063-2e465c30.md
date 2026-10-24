---
title: "SCWE-063: Insecure Event Emission"
source_url: "https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:32.619Z"
---
*Last updated: August 19, 2026*


# SCWE-063: Insecure Event Emission

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#relationships "Permanent link")

-   CWE-778: Insufficient Logging
    [https://cwe.mitre.org/data/definitions/778.html](https://cwe.mitre.org/data/definitions/778.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#description "Permanent link")

Events in Solidity play a critical role in logging contract activity and ensuring transparency. Improper event handling can lead to security risks such as:

1.  **Missing critical event emissions** – Making external monitoring difficult.
2.  **Emitting misleading or incorrect data** – Resulting in users or external systems making incorrect assumptions.
3.  **Logging sensitive information** – Leaking private or security-sensitive data.

Failure to handle events properly can affect contract auditing, debugging, and external monitoring tools, making it difficult to detect anomalies or track contract states correctly.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#remediation "Permanent link")

-   Emit events for all critical state changes, such as token transfers, ownership changes, or contract upgrades.
-   Ensure that the data logged in events accurately represents the actual contract state.
-   Avoid logging sensitive information such as private keys, hashes used for authentication, or confidential business logic.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-2)    mapping(address => uint) public balances;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-3)    event Withdraw(address indexed user, uint amount); [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-4)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-5)    function deposit() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-6)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-8)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-9)    function withdraw(uint _amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-10)        require(balances[msg.sender] >= _amount, "Insufficient funds");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-11)        payable(msg.sender).transfer(_amount);        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-12)        balances[msg.sender] -= _amount; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-13)        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-14)        // Incorrect event emission: Logs the requested amount instead of the actual withdrawn amount        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-15)        emit Withdraw(msg.sender, _amount);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-16)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-0-17)}`

### Issues in the Vulnerable Code[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#issues-in-the-vulnerable-code "Permanent link")

-   The Withdraw event logs `_amount`, which is the requested `withdrawal` amount, but if the transfer fails (due to gas limits, reentrancy, or an external issue), the event still logs it as if the withdrawal happened.
-   If an attacker exploits a discrepancy between event logs and actual state changes, they could mislead users, external indexers, or off-chain services.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-2)    mapping(address => uint) public balances;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-3)    event Withdraw(address indexed user, uint actualAmount); [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-4)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-5)    function deposit() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-6)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-7)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-9)    function withdraw(uint _amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-10)        require(balances[msg.sender] >= _amount, "Insufficient funds"); [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-11)        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-12)        (bool success, ) = payable(msg.sender).call{value: _amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-13)        require(success, "Transfer failed"); [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-14)        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-15)        balances[msg.sender] -= _amount; [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-16)        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-17)        // Logs the amount actually withdrawn (equals _amount on success)        [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-18)        emit Withdraw(msg.sender, _amount);    [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-19)    } [](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#__codelineno-1-20)}`

### Fixes in the Secure Code[¶](https://scs.owasp.org/SCWE/SCSVS-COMM/SCWE-063/#fixes-in-the-secure-code "Permanent link")

-   Uses `call{value: _amount}("")` to send funds safely and ensures success before updating the balance.
-   Updates state and emits the event only after a successful transfer; logs `_amount` (the actual withdrawn amount on success).
-   Prevents false event emissions by reverting on transfer failure before any state change or event.
