---
title: "SCWE-094: Insufficient Gas Limit Validation in LayerZero Message Sending"
source_url: "https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:37.483Z"
---
*Last updated: August 19, 2026*


# SCWE-094: Insufficient Gas Limit Validation in LayerZero Message Sending

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [CWE-20 Link](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#description "Permanent link")

This weakness arises when a smart contract using LayerZero for cross-chain communication fails to validate the minimum gas limit in the adapter parameters. Attackers (or misconfigured clients) can specify an adapter params gas value that is too low for the destination chain execution. As a result, message processing reverts before reaching business logic or error-handling, and the message is recorded as a failed payload on the destination chain. Accumulating failed payloads can disrupt protocol liveness by blocking the cross-chain communication pathway until manual intervention is performed.

## Impact[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#impact "Permanent link")

-   **Denial of Service:** Destination chain message execution reverts due to insufficient gas, preventing critical state changes or callbacks.
-   **Message Backlog/Failed Payloads:** Messages accumulate in failed payload storage/queues, increasing operational burden.
-   **Operational Risk:** Requires manual retries, clearing, or rescue flows to restore liveness; prolonged outages can impact user operations (e.g., bridging, synchronization, DeFi actions).

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#remediation "Permanent link")

-   **Validate minimum gas limit:** Decode LayerZero adapter parameters and enforce a protocol-defined minimum gas limit per message type.
-   **Use safe defaults:** Provide default adapter params with adequate gas and reject user-supplied values below the threshold.
-   **Granular minima:** If different message types have varying complexity, define per-endpoint or per-function minimum gas values.
-   **Robust failure handling:** Implement operational procedures and tooling to safely retry or clear failed payloads without compromising security.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#examples "Permanent link")

🧪 Example

❌ Vulnerable Code (Lack of gas limit validation allows pathway blocking)

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-3)import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol"; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-4)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-5)contract VulnerableLzApp is NonblockingLzApp {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-6)    constructor(address _endpoint) NonblockingLzApp(_endpoint) {} [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-7)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-8)    function sendMessage(uint16 _dstChainId, bytes calldata _payload, bytes calldata _adapterParams) external payable {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-9)        // No validation on _adapterParams, attacker can specify low gas        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-10)        _lzSend(_dstChainId, _payload, payable(msg.sender), address(0), _adapterParams, msg.value);    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-11)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-0-12)}`

✅ Safe Code (Enforces minimum gas limit to prevent blocking)

`[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-1)// SPDX-License-Identifier: MIT [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-3)import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol"; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-5)contract FixedLzApp is NonblockingLzApp {     [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-6)    uint256 public constant MIN_GAS_LIMIT = 200000; [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-7)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-8)    constructor(address _endpoint) NonblockingLzApp(_endpoint) {} [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-9)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-10)    function sendMessage(uint16 _dstChainId, bytes calldata _payload, bytes calldata _adapterParams) external payable {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-11)        require(_extractGasLimit(_adapterParams) >= MIN_GAS_LIMIT, "low gas");        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-12)        _lzSend(_dstChainId, _payload, payable(msg.sender), address(0), _adapterParams, msg.value);    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-13)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-14)    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-15)    function _extractGasLimit(bytes calldata _adapterParams) internal pure returns (uint256 gasLimit) {        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-16)        require(_adapterParams.length >= 34, "bad params");        [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-17)        assembly { gasLimit := calldataload(add(_adapterParams.offset, 2)) }    [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-18)    } [](https://scs.owasp.org/SCWE/SCSVS-BRIDGE/SCWE-094/#__codelineno-1-19)}`
