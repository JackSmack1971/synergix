---
title: "Access Control and Authentication Vulnerabilties"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:15.862Z"
---
# Access Control and Authentication Vulnerabilties

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#description "Permanent link")

Improper access control is a critical security vulnerability in smart contracts that occurs when unauthorized users can access or modify sensitive functions or data. This issue typically arises when the code does not enforce strict access restrictions based on user permissions.

Access control vulnerabilities are especially significant in scenarios involving governance or critical operations, such as:

-   Minting tokens
-   Voting on proposals
-   Withdrawing funds
-   Pausing or upgrading contracts
-   Changing contract ownership

**Example: Code Without Proper Access Control**

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#__codelineno-0-1)function burn(address account, uint256 amount) public  [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#__codelineno-0-2){     [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#__codelineno-0-3)    // No access control is implemented for the burn function    [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#__codelineno-0-4)    _burn(account, amount);  [](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#__codelineno-0-5)}`

### Impact[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#impact "Permanent link")

-   Attackers can gain unauthorized access to critical functions and data within the contract, compromising its integrity and security.
-   Vulnerabilities can lead to the theft of funds or assets controlled by the contract, causing significant financial damage to users and stakeholders.

### Remediation[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#remediation "Permanent link")

-   Ensure initialization functions can only be called once and exclusively by authorized entities.
-   Use established access control patterns like Ownable or RBAC (Role-Based Access Control) in your contracts to manage permissions and ensure that only authorized users can access certain functions. This can be done by adding appropriate access control modifiers, such as onlyOwner or custom roles to sensitive functions.

### Examples of Smart Contracts That Fell Victim to Improper Access Control Attacks:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-AUTH/overview/#examples-of-smart-contracts-that-fell-victim-to-improper-access-control-attacks "Permanent link")

-   [HospoWise Hack Analysis](https://blog.solidityscan.com/access-control-vulnerabilities-in-smart-contracts-a31757f5d707)
-   [LAND NFT Hack Analysis](https://blog.solidityscan.com/land-hack-analysis-missing-access-control-66fb9555a3e3)
