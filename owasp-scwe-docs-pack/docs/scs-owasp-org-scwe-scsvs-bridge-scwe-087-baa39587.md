---
title: "SCWE-087: Missing Payload Size Validation in Cross-Chain Messaging (Denial of Service/Stuck Funds)"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:37.361Z"
---
*Last updated: August 19, 2026*


# SCWE-087: Missing Payload Size Validation in Cross-Chain Messaging (Denial of Service/Stuck Funds)

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#relationships "Permanent link")

-   CWE-1284: Improper Validation of Specified Quantity in Input
    [CWE-1284 Link](https://cwe.mitre.org/data/definitions/1284.html)
-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#description "Permanent link")

This weakness arises when smart contracts performing cross-chain messaging fail to validate the size of payloads before emitting or sending them. In protocols using relayer-based messaging (e.g., LayerZero, Wormhole), data is typically encoded and emitted as a payload on the source chain, then relayed and decoded on the destination chain. If the encoded payload exceeds the maximum allowed size (often 10,000 bytes or similar, depending on the bridge/messaging protocol), the message transmission or decoding can revert—often because the large payload causes out-of-gas consumption during processing or fails explicit size checks. In lock-mint architectures, this can lead to permanent loss of user funds due to inability to unlock or mint assets on the destination chain.

## Impact[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#impact "Permanent link")

-   **Denial of Service:** Oversized payloads will revert during cross-chain transmission, preventing legitimate state updates or token minting/unlocking on the destination chain.
-   **Stuck or Lost Funds:** In bridges using lock-and-mint or burn-and-mint designs, users’ assets may be locked on the source chain with no way to release or claim them on the destination due to repeated transaction failure.
-   **Operational Risk:** Malicious or unintentional submission of oversized payloads can be used to disrupt bridge operations, preventing protocol liveness or causing critical business logic to be inaccessible.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#remediation "Permanent link")

-   Enforce maximum payload size validation on both source and destination chains.
-   Perform defensive coding around payload encoding and decoding to catch out-of-gas or out-of-bound errors.
-   Consider fallback or reversion handling strategies to safely refund or unlock funds when such failures occur.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#examples "Permanent link")

🧪 **Example: User-Supplied Merkle Proof in `lockTokens()`**

❌ **Vulnerable Code (No Payload Size Validation)**

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-4)// SourceChain.sol [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-5)event Locked(address indexed user, uint256 amount, bytes payload); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-6)function lockTokens(uint256 amount, bytes calldata merkleProof) external {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-7)    require(amount > 0, "Invalid amount");    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-8)    // Lock tokens (ERC20 transferFrom)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-9)    require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-10)    // Encode user, amount, timestamp, and the supplied Merkle proof    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-11)    bytes memory payload = abi.encode(msg.sender, amount, block.timestamp, merkleProof);    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-12)    // ⚠️ No payload size validation!    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-13)    emit Locked(msg.sender, amount, payload); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-0-14)}`

Destination Chain: Decode and Mint

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-3)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-4)// DestinationChain.sol [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-5)function mintFromPayload(bytes calldata payload) external {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-6)    // Will revert if payload is too large for decode!    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-7)    (address user, uint256 amount, uint256 timestamp, bytes memory merkleProof) =        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-8)        abi.decode(payload, (address, uint256, uint256, bytes));    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-9)    // Verification of Merkle proof, then mint tokens    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-10)    _mint(user, amount); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-1-11)}`

✅ Safe Code (With Payload Size Validation)

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-3)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-4)// SourceChain.sol [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-5)event Locked(address indexed user, uint256 amount, bytes payload); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-6)function lockTokens(uint256 amount, bytes calldata merkleProof) external {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-7)    require(amount > 0, "Invalid amount");    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-8)    // Lock tokens (ERC20 transferFrom)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-9)    require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-10)    // Encode user, amount, timestamp, and the supplied Merkle proof    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-11)    bytes memory payload = abi.encode(msg.sender, amount, block.timestamp, merkleProof);    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-12)    // Check payload size    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-13)    require(payload.length <= 10_000, "Payload exceeds max allowed size");    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-14)    emit Locked(msg.sender, amount, payload); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-2-15)}`

Destination Chain: Decode and Mint (Optional Double Check)

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-3)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-4)// DestinationChain.sol [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-5)function mintFromPayload(bytes calldata payload) external {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-6)    require(payload.length <= 10_000, "Payload too large");    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-7)    (address user, uint256 amount, uint256 timestamp, bytes memory merkleProof) =        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-8)        abi.decode(payload, (address, uint256, uint256, bytes));    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-9)    // Proceed with Merkle proof verification and minting    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-10)    _mint(user, amount); [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-087/#__codelineno-3-11)}`
