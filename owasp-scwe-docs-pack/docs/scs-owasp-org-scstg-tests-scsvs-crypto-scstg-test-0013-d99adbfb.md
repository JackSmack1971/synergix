---
title: "SCSTG-TEST-0013: Secure Signature Verification"
source_url: "https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:17.242Z"
---
*Last updated: August 19, 2026*

[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013.md "Edit this page")

# SCSTG-TEST-0013: Secure Signature Verification

### **Description**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#description "Permanent link")

Cryptographic practices are essential in ensuring the confidentiality, integrity, and authenticity of interactions within decentralized systems. Weaknesses in cryptographic implementations, key management, or signature verification can lead to vulnerabilities such as unauthorized access, data manipulation, or attacks that compromise the security of transactions. This test focuses on verifying secure cryptographic practices, including key management, signature verification, and secure random number generation in smart contracts.

* * *

### **Test 1: Verify Secure Signature Verification**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#test-1-verify-secure-signature-verification "Permanent link")

#### Vulnerable Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#vulnerable-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-3)contract SignatureVerification {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-4)    function verifySignature(address _signer, bytes32 _message, bytes memory _signature) public pure returns (bool) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-5)        // Directly using ecrecover, without checking for message format, leads to potential attack vectors        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-6)        address recovered = ecrecover(_message, uint8(_signature[0]), bytes32(_signature[1]), bytes32(_signature[2]));        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-7)        return recovered == _signer;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-0-9)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#why-its-vulnerable "Permanent link")

-   The contract uses `ecrecover` directly without verifying the message structure.
-   Attackers could use a replay attack by reusing the signature from another message to authenticate different transactions.
-   The lack of proper checks makes the contract vulnerable to attacks where the attacker can forge or replay signatures.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#fixed-code "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-3)contract SecureSignatureVerification {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-4)    // Use of EIP-712 for standard signature verification with specific message formats    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-5)    function verifySignature(address _signer, bytes32 _message, bytes memory _signature) public pure returns (bool) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-6)        bytes32 messageHash = keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", _message));        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-7)        address recovered = ecrecover(messageHash, uint8(_signature[0]), bytes32(_signature[1]), bytes32(_signature[2]));        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-8)        return recovered == _signer;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-9)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-1-10)}`

### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#how-to-check "Permanent link")

-   **Code Review:** Verify that signatures are being properly validated using standards like EIP-712, and that the contract uses `ecrecover` securely. Ensure that messages are hashed and prefixed correctly before recovery.
-   **Dynamic Testing:** Test with replayed or malformed signatures to verify that the contract rejects such transactions.

* * *

#### Vulnerable Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#vulnerable-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-3)contract RandomNumberGenerator {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-4)    uint256 public randomValue; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-5)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-6)    function generateRandomNumber() public {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-7)        randomValue = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)));    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-8)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-2-9)}`

### **Why It’s Vulnerable**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#why-its-vulnerable_1 "Permanent link")

-   The contract uses block properties like `block.timestamp` and `block.difficulty` (post-merge: `block.prevrandao`) to generate random numbers, which can be manipulated by validators.
-   This weak random number generation can lead to predictable values, making the contract vulnerable to attacks such as manipulation of lottery or gambling outcomes.

#### Fixed Code:[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#fixed-code_1 "Permanent link")

`[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-2)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-3)import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol"; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-4)import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol"; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-5)[](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-6)contract SecureRandomNumberGenerator is VRFConsumerBaseV2 {     [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-7)    VRFCoordinatorV2Interface immutable COORDINATOR;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-8)    uint64 immutable s_subscriptionId;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-9)    bytes32 immutable s_keyHash;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-10)    uint256 public randomValue;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-11)    uint256 public s_requestId; [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-12)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-13)    constructor(        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-14)        address vrfCoordinator,        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-15)        uint64 subscriptionId,        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-16)        bytes32 keyHash    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-17)    ) VRFConsumerBaseV2(vrfCoordinator) {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-18)        COORDINATOR = VRFCoordinatorV2Interface(vrfCoordinator);        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-19)        s_subscriptionId = subscriptionId;        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-20)        s_keyHash = keyHash;    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-21)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-22)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-23)    function requestRandomNumber() external {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-24)        s_requestId = COORDINATOR.requestRandomWords(            [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-25)            s_keyHash,            [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-26)            s_subscriptionId,            [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-27)            3,      // requestConfirmations            [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-28)            100000, // callbackGasLimit            [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-29)            1      // numWords        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-30)        );    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-31)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-32)    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-33)    function fulfillRandomWords(uint256, uint256[] memory randomWords) internal override {        [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-34)        randomValue = randomWords[0];    [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-35)    } [](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#__codelineno-3-36)}`

### **How to Check**[¶](https://scs.owasp.org/SCSTG/tests/SCSVS-CRYPTO/SCSTG-TEST-0013/#how-to-check_1 "Permanent link")

-   **Code Review:** Ensure that random numbers are not derived from predictable values like block properties. Check if external secure sources like `Chainlink VRF` are being used for randomness.
-   **Dynamic Testing:** Test contract behavior under adversarial conditions to ensure the randomness cannot be predicted or manipulated.
