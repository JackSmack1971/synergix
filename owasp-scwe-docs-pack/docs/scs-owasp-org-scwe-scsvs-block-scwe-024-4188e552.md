---
title: "SCWE-024: Weak Randomness Sources"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:36.250Z"
---
*Last updated: August 19, 2026*


# SCWE-024: Weak Randomness Sources

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#relationships "Permanent link")

-   CWE-336: Predictable Random Number Generator
    [CWE-336 Link](https://cwe.mitre.org/data/definitions/336.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#description "Permanent link")

Weak randomness sources refer to the use of predictable or insecure sources of randomness, such as block timestamps or block hashes. This can lead to: - Exploitation of the contract's logic. - Loss of funds or data. - Reduced trust in the contract's security.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#remediation "Permanent link")

-   **Use secure randomness:** Leverage secure randomness sources like Chainlink VRF.
-   **Avoid block variables:** Do not rely on block timestamps or hashes for randomness.
-   **Test thoroughly:** Conduct extensive testing to ensure randomness is secure.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#examples "Permanent link")

-   **Weak Randomness**

    `[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#__codelineno-0-3)contract WeakRandomness {     [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#__codelineno-0-4)    function generateRandomNumber() public view returns (uint) {        [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#__codelineno-0-5)        return uint(keccak256(abi.encodePacked(block.timestamp, block.difficulty))); // Insecure: post-merge use block.prevrandao; both are insecure for value-at-stake randomness    [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-BLOCK/SCWE-024/#__codelineno-0-7)}`

-   **Secure Randomness** \`\`\`solidity pragma solidity ^0.8.0;


import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol"; // Note: Chainlink VRF V1 is deprecated; use VRF V2 (VRFConsumerBaseV2) in production

contract SecureRandomness is VRFConsumerBase { bytes32 internal keyHash; uint256 internal fee; uint256 public randomResult;

    ` constructor(address vrfCoordinator, address linkToken, bytes32 _keyHash, uint256 _fee)         VRFConsumerBase(vrfCoordinator, linkToken) {         keyHash = _keyHash;         fee = _fee;     }      function getRandomNumber() public returns (bytes32 requestId) {         require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK");         return requestRandomness(keyHash, fee);     }      function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {         randomResult = randomness;     } } ``` `

* * *
