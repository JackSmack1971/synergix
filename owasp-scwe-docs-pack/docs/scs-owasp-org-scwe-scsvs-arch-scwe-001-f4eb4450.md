---
title: "SCWE-001: Improper Contract Architecture"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:18.925Z"
---
*Last updated: August 19, 2026*


# SCWE-001: Improper Contract Architecture

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#relationships "Permanent link")

-   CWE-1008: Architectural Concepts [https://cwe.mitre.org/data/definitions/1008.html](https://cwe.mitre.org/data/definitions/1008.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#description "Permanent link")

Improper contract architecture refers to the flawed design of a smart contract’s structure, which compromises its security, scalability, and maintainability. This often occurs due to monolithic designs, inefficient inheritance structures, and poor separation of concerns. Such flaws create challenges in managing, upgrading, and auditing the contract. Key issues associated with improper architecture include:

-   Difficulty in upgrading the contract without introducing risks.
-   Increased complexity leading to hidden attack surfaces.
-   Lack of flexibility in contract logic, making it hard to isolate bugs or exploits.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#remediation "Permanent link")

-   **Modular design:** Break down contracts into smaller, more manageable modules to ensure a clean separation of concerns.
-   **Proxy pattern implementation:** Use proxies to allow contract upgrades while preserving contract state.
-   **Separate logic and state:** Keep business logic and data storage separate to improve scalability and maintainability.
-   **Periodic code review and refactoring:** Regularly assess the architecture and refactor to maintain efficiency and security.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#examples "Permanent link")

### Improper Contract Architecture[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#improper-contract-architecture "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-3)contract MonolithicContract {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-4)    uint public balance;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-7)    mapping(address => uint) public allowances; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-8)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-9)    constructor() {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-10)        owner = msg.sender;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-12)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-13)    function deposit(uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-14)        balance += value;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-15)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-16)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-17)    function withdraw(uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-18)        require(balance >= value, "Insufficient funds");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-19)        balance -= value;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-20)        (bool ok, ) = msg.sender.call{value: value}("");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-21)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-22)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-23)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-24)    function transfer(address to, uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-25)        require(balance >= value, "Insufficient funds");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-26)        balance -= value;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-27)        (bool ok1, ) = payable(to).call{value: value}("");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-28)        require(ok1, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-29)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-30)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-31)    function approve(address spender, uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-32)        allowances[spender] = value;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-33)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-34)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-35)    function transferFrom(address from, address to, uint value) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-36)        require(allowances[from] >= value, "Allowance exceeded");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-37)        allowances[from] -= value;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-38)        (bool ok2, ) = payable(to).call{value: value}("");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-39)        require(ok2, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-40)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-41)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-42)    function upgradeLogic() public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-43)        require(msg.sender == owner, "Not authorized");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-44)        // Upgrading logic is impossible without deploying a new contract.    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-45)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-0-46)}`

**Problem**: The contract has a monolithic design, tightly coupling storage, business logic, and access control. This makes upgrading or fixing specific parts difficult.

### Improved Modular Contract Architecture[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#improved-modular-contract-architecture "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-3)contract ModularVault {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-4)    uint public balance;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-5)    address public owner; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-7)    modifier onlyOwner() { require(msg.sender == owner, "Not authorized"); _; } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-8)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-9)    constructor() { owner = msg.sender; } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-11)    function deposit(uint value) external { _deposit(value); }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-12)    function withdraw(uint value) external { _withdraw(value); } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-13)    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-14)    function _deposit(uint value) internal { balance += value; }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-15)    function _withdraw(uint value) internal {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-16)        require(balance >= value, "Insufficient funds");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-17)        balance -= value;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-18)        (bool ok, ) = msg.sender.call{value: value}("");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-19)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-20)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-001/#__codelineno-1-21)}`

**Solution**: Use modular internal functions (`_deposit`, `_withdraw`) to separate concerns. For full upgradeability with preserved state, implement a proxy pattern (see SCWE-005).
