---
title: "Cryptographic Practices"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:17.106Z"
---
# Cryptographic Practices

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#description "Permanent link")

Cryptographic practices in smart contracts ensure that sensitive operations, such as authentication, data integrity, and randomness, are protected from malicious manipulation. Secure key management, signature verification, and proper random number generation are essential to prevent vulnerabilities like unauthorized access, replay attacks, and exploitation of weaknesses in cryptographic operations.

Improper cryptographic practices can lead to severe consequences, including unauthorized transactions, predictable outcomes, and security breaches.

### **Example: Improper Signature Verification**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#example-improper-signature-verification "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#__codelineno-0-1)function verifySignature(address signer, bytes32 message, bytes memory signature) public pure returns (bool) {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#__codelineno-0-2)    bytes32 messageHash = keccak256(abi.encodePacked(message));    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#__codelineno-0-3)    address recoveredSigner = ecrecover(messageHash, uint8(signature[64]), bytes32(signature[0]), bytes32(signature[32]));    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#__codelineno-0-4)    return recoveredSigner == signer; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#__codelineno-0-5)}`

In this example, the `ecrecover` function is used without ensuring that the signature is valid, which may lead to vulnerabilities like signature malleability or invalid data recovery.

### **Impact**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#impact "Permanent link")

-   **Unauthorized Access**: Weak cryptographic practices can allow attackers to forge signatures or impersonate users, leading to unauthorized actions within the contract.
-   **Reentrancy Attacks**: If cryptographic functions are used to validate external calls, attackers could exploit weak or improperly implemented logic to re-enter the contract.
-   **Manipulation of Outcomes**: Predictable or weak random number generation could allow attackers to manipulate outcomes in systems relying on randomness, such as lotteries or gaming dApps.
-   **Replay Attacks**: Insufficient signature validation can result in replay attacks where signed messages are reused across different contexts, allowing attackers to perform unintended actions.

### **Remediation**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/overview/#remediation "Permanent link")

-   **Key Management**: Ensure that private keys are securely stored, never hardcoded in contracts, and use hardware solutions for key management.
-   **Signature Verification**: Implement proper checks for signature validity, including handling signature malleability by using nonces or hashed messages.
-   **Randomness**: Use secure sources of entropy, such as Chainlink VRF (Verifiable Random Function), to ensure the randomness cannot be manipulated.
-   **Compliance with Standards**: Ensure compliance with cryptographic standards like EIP-712 to prevent signature malleability and other vulnerabilities.
