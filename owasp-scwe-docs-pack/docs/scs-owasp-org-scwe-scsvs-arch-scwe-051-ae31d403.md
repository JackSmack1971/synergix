---
title: "SCWE-051: Improper Use of CREATE2 for Contract Deployment"
source_url: "https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:19.980Z"
---
*Last updated: August 19, 2026*


# SCWE-051: Improper Use of CREATE2 for Contract Deployment

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#relationships "Permanent link")

-   **CWE-706: Use of Incorrectly-Resolved Name or Reference**
    [https://cwe.mitre.org/data/definitions/706.html](https://cwe.mitre.org/data/definitions/706.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#description "Permanent link")

The `CREATE2` opcode allows for deterministic contract deployment, meaning the contract's address can be precomputed before deployment. However, improper handling of the salt parameter, constructor arguments, or contract bytecode can lead to vulnerabilities such as address predictability, re-deployment attacks, and malicious contract substitution. If an attacker can influence the salt or code, they may deploy a contract at a known address before the legitimate one, leading to security risks.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#remediation "Permanent link")

To prevent misuse of `CREATE2`:
\- Use unpredictable and unique salt values (e.g., incorporating nonces, sender addresses, or randomness).
\- Ensure the deployed contract logic remains consistent to prevent re-deployment attacks.
\- Hash important contract parameters into the salt to prevent unintended address collisions.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-3)contract Factory {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-4)    function deploy(bytes32 salt, bytes memory bytecode) public {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-5)        address deployed;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-6)        assembly {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-7)            deployed := create2(0, add(bytecode, 0x20), mload(bytecode), salt)        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-8)        }    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-9)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-0-10)}`

**Why is this vulnerable?**

-   If `salt` is predictable (e.g., user-supplied or a static value), an attacker can precompute and front-run the deployment.
-   The same contract address can be re-used by deploying different bytecode, leading to logic changes at a fixed address.
-   No validation ensures that the deployed contract is safe or expected.

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-3)contract SecureFactory {     [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-4)    function deploy(bytes32 salt, bytes memory bytecode) public returns (address) {        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-5)        require(bytecode.length > 0, "Bytecode cannot be empty"); [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-6)        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-7)        // Ensure the salt includes sender information to prevent front-running        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-8)        bytes32 secureSalt = keccak256(abi.encodePacked(msg.sender, salt)); [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-9)        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-10)        address deployed;        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-11)        assembly {            [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-12)            deployed := create2(0, add(bytecode, 0x20), mload(bytecode), secureSalt)        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-13)        } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-14)        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-15)        require(deployed != address(0), "Deployment failed");        [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-16)        return deployed;    [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-17)    } [](https://scs.owasp.org/SCWE/SCSVS-ARCH/SCWE-051/#__codelineno-1-18)}`

**Why is this safe?** - Uses `keccak256(abi.encodePacked(msg.sender, salt))` to make the salt unique per sender. - Ensures the contract bytecode is non-empty before deploying. - Validates that the deployed contract is nonzero, ensuring a successful deployment.

**By securing CREATE2 deployments, developers can prevent predictable contract addresses, front-running risks, and contract replacement vulnerabilities.**
