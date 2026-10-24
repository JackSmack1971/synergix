---
title: "SCWE-081: Improper Handling of Nonce"
source_url: "https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:29.234Z"
---
*Last updated: August 19, 2026*


# SCWE-081: Improper Handling of Nonce

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#description "Permanent link")

Nonce values are used to ensure that transactions are processed in the correct order and prevent replay attacks. Improper handling or validation of nonces can lead to issues such as transaction replay or improper sequencing of transactions, which can be exploited by attackers.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#remediation "Permanent link")

Always validate nonce values to ensure that they are correctly incremented and avoid reusing nonces. Ensure that nonce handling is robust, especially in cases where external calls are involved, to prevent replay attacks or transaction malleability.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-1)contract Example {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-2)    mapping(address => uint256) public nonces; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-3)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-4)    function transfer(address _to, uint256 _amount) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-5)        uint256 nonce = nonces[msg.sender]; // Nonce is not validated properly        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-6)        nonces[msg.sender] = nonce + 1;     // This could allow replay attacks        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-7)        // Transfer logic    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-8)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-0-9)}`

### Fixed Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#fixed-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-4)contract SecureExample {     [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-5)    mapping(address => uint256) public nonces; [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-6)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-7)    function transfer(        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-8)        address _to,        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-9)        uint256 _amount,        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-10)        uint256 _nonce,        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-11)        bytes memory _signature    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-12)    ) public {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-13)        require(_nonce == nonces[msg.sender], "Invalid nonce"); [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-14)        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-15)        // Hash the message        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-16)        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender, _to, _amount, _nonce));        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-17)        bytes32 ethSignedMessageHash = keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash)); [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-18)        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-19)        // Recover the signer's address        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-20)        address signer = recoverSigner(ethSignedMessageHash, _signature);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-21)        require(signer == msg.sender, "Invalid signature"); [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-22)        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-23)        nonces[msg.sender] = _nonce + 1;        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-24)        // Transfer logic    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-25)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-26)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-27)    function recoverSigner(bytes32 _ethSignedMessageHash, bytes memory _signature) internal pure returns (address) {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-28)        (bytes32 r, bytes32 s, uint8 v) = splitSignature(_signature);        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-29)        return ecrecover(_ethSignedMessageHash, v, r, s);    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-30)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-31)    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-32)    function splitSignature(bytes memory sig) internal pure returns (bytes32 r, bytes32 s, uint8 v) {        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-33)        require(sig.length == 65, "Invalid signature length");        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-34)        assembly {            [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-35)            r := mload(add(sig, 32))            [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-36)            s := mload(add(sig, 64))            [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-37)            v := byte(0, mload(add(sig, 96)))        [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-38)        }    [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-39)    } [](https://scs.owasp.org/SCWE/SCSVS-GOV/SCWE-081/#__codelineno-1-40)}`

Why is this better? - Nonce is no longer user input: It is validated as part of a signed message, preventing arbitrary replay attempts. - Prevents transaction replay attacks: By signing the message, an attacker cannot reuse an old transaction because the signature includes the nonce. - Ensures integrity & authenticity: The contract only processes the transaction if the signed message is valid and matches the expected sender.

* * *
