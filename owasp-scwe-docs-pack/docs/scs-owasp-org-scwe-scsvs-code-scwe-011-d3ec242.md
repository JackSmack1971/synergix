---
title: "SCWE-011: Insecure ABI Encoding and Decoding"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:22.636Z"
---
*Last updated: August 19, 2026*


# SCWE-011: Insecure ABI Encoding and Decoding

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#relationships "Permanent link")

-   CWE-116: Improper Encoding or Escaping of Output [https://cwe.mitre.org/data/definitions/116.html](https://cwe.mitre.org/data/definitions/116.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#description "Permanent link")

Insecure ABI encoding and decoding occur when a smart contract improperly handles data serialization and deserialization, leading to vulnerabilities such as data corruption, type confusion, or reentrancy attacks. Solidity provides ABI encoding functions like `abi.encode()`, `abi.encodePacked()`, and `abi.decode()`, but improper usage can cause unexpected behavior.

Common issues with insecure ABI handling: - **Collision Risks in `abi.encodePacked()`**: Multiple concatenated parameters can lead to ambiguous encoding, making it vulnerable to hash collisions. - **Unchecked Decoding**: Improper use of `abi.decode()` can result in unintended memory corruption or type confusion. - **Lack of Input Validation**: Encoding user inputs without verification can introduce security flaws. - **Mismatched Data Types**: Decoding an incorrectly encoded data structure can lead to invalid memory access.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#remediation "Permanent link")

-   **Use `abi.encode()` Instead of `abi.encodePacked()` for Hashing**: Prevent collision risks by ensuring unique encoding.
-   **Validate Data Before Decoding**: Ensure the encoded data conforms to the expected structure before decoding.
-   **Match Encoding and Decoding Types**: Always use the correct type structure when decoding to avoid unintended behavior.
-   **Avoid Direct ABI Decoding of External Calls**: Use strict validation mechanisms when handling data from external contracts.

## Examples[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#examples "Permanent link")

### Example of Insecure ABI Encoding:[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#example-of-insecure-abi-encoding "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-0-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-0-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-0-3)contract InsecureABI {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-0-4)    function hashValues(string memory str, uint256 num) public pure returns (bytes32) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-0-5)        return keccak256(abi.encodePacked(str, num)); // Collision risk    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-0-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-0-7)}`

-   In this example, `abi.encodePacked()` creates a collision risk because different input combinations can produce the same hash.

### Refactored to Secure ABI Encoding:[¶](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#refactored-to-secure-abi-encoding "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-1-3)contract SecureABI {     [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-1-4)    function hashValues(string memory str, uint256 num) public pure returns (bytes32) {        [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-1-5)        return keccak256(abi.encode(str, num)); // Unique encoding, no collision    [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-1-6)    } [](https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-011/#__codelineno-1-7)}`

-   In this improved version, `abi.encode()` ensures a unique encoding structure, preventing hash collision attacks.
