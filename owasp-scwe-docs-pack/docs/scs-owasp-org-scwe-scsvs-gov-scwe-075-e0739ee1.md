---
title: "SCWE-075: Incorrect Ether Balance Tracking"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:28.851Z"
---
*Last updated: August 19, 2026*


# SCWE-075: Incorrect Ether Balance Tracking

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#relationships "Permanent link")

-   CWE-852: Untrusted Control Sphere
    [https://cwe.mitre.org/data/definitions/852.html](https://cwe.mitre.org/data/definitions/852.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#description "Permanent link")

Incorrect Ether balance tracking occurs when a contract manually maintains an internal balance variable instead of relying on `address(this).balance`. This creates inconsistencies when Ether is received outside of expected functions (e.g., via `selfdestruct()`, `transfer()`, or direct deposits).

Attackers can exploit this by artificially inflating the contract's perceived balance, leading to unauthorized withdrawals or failed transactions. This issue is common in poorly designed deposit/withdraw systems that do not properly verify the actual contract balance.

## Attack Scenario[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#attack-scenario "Permanent link")

An attacker sends Ether to the contract using `selfdestruct()`, increasing its actual balance without updating the internal tracking variable. Later, a user tries to withdraw funds, but the contract incorrectly assumes it has more Ether than it actually does, causing unexpected failures or exploits.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#remediation "Permanent link")

-   **Use `address(this).balance`** instead of manually tracking Ether balance.
-   **Prevent external Ether deposits** by disabling the fallback function unless explicitly needed.
-   **Ensure proper accounting** by always reconciling balances before allowing withdrawals.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-1)// ❌ Vulnerable to incorrect balance tracking due to external Ether deposits [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-2)contract IncorrectBalanceTracking {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-3)    uint public balance;  // ❌ Manually tracking Ether balance [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-4)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-5)    function deposit() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-6)        balance += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-8)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-9)    function withdraw(uint _amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-10)        require(balance >= _amount, "Insufficient funds");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-11)        payable(msg.sender).transfer(_amount);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-12)        balance -= _amount;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-13)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-0-14)}`

**Why is this vulnerable?** - The contract does not account for direct Ether transfers outside deposit(). - An attacker can send Ether via `selfdestruct()`, inflating the contract balance without updating balance. - This can lead to withdrawals being blocked or excessive withdrawals.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-3)// ✅ Secure implementation: per-user accounting + address(this).balance for consistency [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-4)contract CorrectBalanceTracking {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-5)    mapping(address => uint) public balances; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-7)    function deposit() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-8)        balances[msg.sender] += msg.value;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-11)    function withdraw(uint _amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-12)        require(balances[msg.sender] >= _amount, "Insufficient funds");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-13)        require(address(this).balance >= _amount, "Contract balance insufficient");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-14)        balances[msg.sender] -= _amount;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-15)        (bool success, ) = payable(msg.sender).call{value: _amount}("");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-16)        require(success, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-18)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-19)    receive() external payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-20)        revert("Direct deposits not allowed");    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-21)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-075/#__codelineno-1-22)}`

**Why is this secure?** - Per-user `balances` mapping ensures only depositors can withdraw their funds. - Reconciles with `address(this).balance` before transfer to detect unexpected inflows (e.g. `selfdestruct`). - Uses `call{value}` for flexible gas; `receive()` reverts on direct deposits.

* * *
