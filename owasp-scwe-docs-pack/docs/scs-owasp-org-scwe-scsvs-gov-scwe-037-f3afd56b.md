---
title: "SCWE-037: Insufficient Protection Against Front-Running"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:28.487Z"
---
*Last updated: August 19, 2026*


# SCWE-037: Insufficient Protection Against Front-Running

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#description "Permanent link")

Insufficient protection against front-running refers to vulnerabilities that allow malicious actors to exploit the order of transactions for profit. This can lead to: - Unauthorized actions by malicious actors. - Loss of funds or data. - Exploitation of the contract’s logic.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#remediation "Permanent link")

-   **Use commit-reveal schemes:** Implement commit-reveal mechanisms to hide transaction details until they are finalized.
-   **Add delays:** Introduce time delays for critical operations to reduce the risk of front-running.
-   **Test thoroughly:** Conduct extensive testing to ensure front-running protection is effective.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#examples "Permanent link")

-   **Vulnerable to Front-Running**

    `[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-3)interface IERC20 {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-4)    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-5)    function balanceOf(address account) external view returns (uint256); [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-6)} [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-7)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-8)contract FrontRunningVulnerable {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-9)    IERC20 public token;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-10)    uint256 public price = 1 ether; // 1 token = 1 ETH [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-11)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-12)    constructor(address _token) {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-13)        token = IERC20(_token);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-14)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-15)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-16)    function buyTokens(uint256 amount) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-17)        require(msg.value >= amount * price, "Insufficient ETH");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-18)        token.transferFrom(address(this), msg.sender, amount);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-19)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-0-20)}`

    Why is this vulnerable?
-   Attackers see the transaction in the mempool and execute a transaction to buy first, raising the price.
-   Victim's transaction executes at a higher price or fails due to slippage.
-   Attacker sells at a profit, exploiting sandwich attacks.

-   **Protected Against Front-Running- Commit-Reveal to Hide Trade Intent**

    `[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-3)contract SecureTrade {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-4)    mapping(address => bytes32) public commitments;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-5)    uint256 public price = 1 ether; // 1 token = 1 ETH [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-7)    function commitTrade(bytes32 hash) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-8)        commitments[msg.sender] = hash;    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-9)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-11)    function executeTrade(uint256 amount, bytes32 secret) public payable {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-12)        require(commitments[msg.sender] == keccak256(abi.encodePacked(amount, secret)), "Invalid commitment");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-13)        require(msg.value >= amount * price, "Insufficient ETH"); [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-14)        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-15)        commitments[msg.sender] = 0; // Prevent reusing commitment        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-16)        // Execute trade after revealing the commitment    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-037/#__codelineno-1-18)}`

    Why is this better?

-   Traders commit to the trade off-chain before revealing the amount, preventing mempool sniping.
-   Transactions cannot be front-run because attackers don’t know the amount until revealed.

* * *
