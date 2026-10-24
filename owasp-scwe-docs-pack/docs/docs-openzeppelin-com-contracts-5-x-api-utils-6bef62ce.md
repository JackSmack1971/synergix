---
title: "Utils"
source_url: "https://docs.openzeppelin.com/contracts/5.x/api/utils"
host: "docs.openzeppelin.com"
depth: 2
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:48.893Z"
---
[](https://docs.openzeppelin.com/)

Select Ecosystem

Ethereum & EVM

[Home](https://docs.openzeppelin.com/)[Forum](https://forum.openzeppelin.com/)[Website](https://openzeppelin.com/)[Impact](https://docs.openzeppelin.com/impact)[Getting Started](https://docs.openzeppelin.com/contracts)

Solidity Contracts

OpenZeppelin Contracts

[Overview](https://docs.openzeppelin.com/contracts/5.x)[Contracts Wizard](https://docs.openzeppelin.com/contracts/5.x/wizard)[Extending Contracts](https://docs.openzeppelin.com/contracts/5.x/extending-contracts)[Using with Upgrades](https://docs.openzeppelin.com/contracts/5.x/upgradeable)[Backwards Compatibility](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility)[Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control)

[Account Abstraction](https://docs.openzeppelin.com/contracts/5.x/account-abstraction)

[Tokens](https://docs.openzeppelin.com/contracts/5.x/tokens)

[Governance](https://docs.openzeppelin.com/contracts/5.x/governance)[Utilities](https://docs.openzeppelin.com/contracts/5.x/utilities)

[Subgraphs](https://docs.openzeppelin.com/contracts/5.x/subgraphs)

[FAQ](https://docs.openzeppelin.com/contracts/5.x/faq)[Changelog](https://docs.openzeppelin.com/contracts/5.x/changelog)

[API Reference](https://docs.openzeppelin.com/contracts/5.x/api)

[Access](https://docs.openzeppelin.com/contracts/5.x/api/access)[Account](https://docs.openzeppelin.com/contracts/5.x/api/account)[Crosschain](https://docs.openzeppelin.com/contracts/5.x/api/crosschain)[Finance](https://docs.openzeppelin.com/contracts/5.x/api/finance)[Governance](https://docs.openzeppelin.com/contracts/5.x/api/governance)[Interfaces](https://docs.openzeppelin.com/contracts/5.x/api/interfaces)[Meta Transactions](https://docs.openzeppelin.com/contracts/5.x/api/metatx)[Proxy](https://docs.openzeppelin.com/contracts/5.x/api/proxy)

Token

[Utils](https://docs.openzeppelin.com/contracts/5.x/api/utils)

[Cryptography](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography)

Previous Versions

[Community Contracts](https://docs.openzeppelin.com/community-contracts)

[Upgrades Plugins](https://docs.openzeppelin.com/upgrades-plugins)

[Contracts Wizard](https://docs.openzeppelin.com/wizard)

Learn

Developer Libraries

[Ecosystem Adapters](https://docs.openzeppelin.com/ecosystem-adapters)

[UIKit](https://docs.openzeppelin.com/tools/uikit)

Open Source Tools

[Relayer](https://docs.openzeppelin.com/relayer/1.5.x)

[Monitor](https://docs.openzeppelin.com/monitor/1.3.x)

UI Builder

[Role Manager](https://docs.openzeppelin.com/role-manager)

[Chainlink CRE](https://docs.openzeppelin.com/chainlink-cre)

[Symbiotic Templates](https://docs.openzeppelin.com/symbiotic)

[](https://github.com/OpenZeppelin)

OpenZeppelin Contracts[API Reference](https://docs.openzeppelin.com/contracts/5.x/api)

# Utils

Smart contract utils utilities and implementations

Copy Markdown

[Open in Claude](https://claude.ai/new?q=Read+https%3A%2F%2Fraw.githubusercontent.com%2FOpenZeppelin%2Fdocs%2Frefs%2Fheads%2Fmain%2Fcontent%2Fcontracts%2F5.x%2Fapi%2Futils.mdx%2C+I+want+to+ask+questions+about+it.)

Miscellaneous contracts and libraries containing utility functions you can use to improve security, work with new data types, or safely use low-level primitives.

-   [`Math`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math), [`SignedMath`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath): Implementation of various arithmetic functions.
-   [`SafeCast`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast): Checked downcasting functions to avoid silent truncation.
-   [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces): Utility for tracking and verifying address nonces that only increment.
-   [`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed): Alternative to [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces), that support keyed nonces following [ERC-4337 specifications](https://eips.ethereum.org/EIPS/eip-4337#semi-abstracted-nonce-support).
-   [`Pausable`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable): A common emergency response mechanism that can pause functionality while a remediation is pending.
-   [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard): A modifier that can prevent reentrancy during certain functions.
-   [`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient): Variant of [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard) that uses transient storage ([EIP-1153](https://eips.ethereum.org/EIPS/eip-1153)).
-   [`ERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165), [`ERC165Checker`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker): Utilities for inspecting interfaces supported by contracts.
-   [`Accumulators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators): A library for merging an arbitrary dynamic number of bytes buffers.
-   [`BitMaps`](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps): A simple library to manage boolean value mapped to a numerical index in an efficient way.
-   [`Checkpoints`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints): A data structure to store values mapped to a strictly increasing key. Can be used for storing and accessing values over time.
-   [`CircularBuffer`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer): A data structure to store the last N values pushed to it.
-   [`DoubleEndedQueue`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue): An implementation of a [double ended queue](https://en.wikipedia.org/wiki/Double-ended_queue) whose values can be added or removed from both sides. Useful for FIFO and LIFO structures.
-   [`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap): A type like Solidity’s [`mapping`](https://solidity.readthedocs.io/en/latest/types.html#mapping-types), but with key-value *enumeration*: this will let you know how many entries a mapping has, and iterate over them (which is not possible with `mapping`).
-   [`EnumerableSet`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet): Like [`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap), but for [sets](https://en.wikipedia.org/wiki/Set_\(abstract_data_type\)). Can be used to store privileged accounts, issued IDs, etc.
-   [`Heap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap): A library that implements a [binary heap](https://en.wikipedia.org/wiki/Binary_heap) in storage.
-   [`MerkleTree`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree): A library with [Merkle Tree](https://wikipedia.org/wiki/Merkle_Tree) data structures and helper functions.
-   [`Address`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address): Collection of functions for overloading Solidity’s [`address`](https://docs.soliditylang.org/en/latest/types.html#address) type.
-   [`Arrays`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays): Collection of functions that operate on [`arrays`](https://docs.soliditylang.org/en/latest/types.html#arrays).
-   [`Base58`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58): On-chain base58 encoding and decoding.
-   [`Base64`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64): On-chain base64 and base64URL encoding according to [RFC-4648](https://datatracker.ietf.org/doc/html/rfc4648).
-   [`Blockhash`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash): A library for accessing historical block hashes beyond the standard 256 block limit utilizing EIP-2935’s historical blockhash functionality.
-   [`Bytes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes): Common operations on bytes objects.
-   [`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2), [`CAIP10`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10): Libraries for formatting and parsing CAIP-2 and CAIP-10 identifiers.
-   [`Calldata`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata): Helpers for manipulating calldata.
-   [`Comparators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators): A library that contains comparator functions to use with the [`Heap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap) library.
-   [`Context`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context): A utility for abstracting the sender and calldata in the current execution context.
-   [`Create2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2): Wrapper around the [`CREATE2` EVM opcode](https://blog.openzeppelin.com/getting-the-most-out-of-create2/) for safe use without having to deal with low-level assembly.
-   [`InteroperableAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress): Library for formatting and parsing ERC-7930 interoperable addresses.
-   [`LowLevelCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall): Collection of functions to perform calls with low-level assembly.
-   [`Memory`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory): A utility library to manipulate memory.
-   [`Multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall): Abstract contract with a utility to allow batching together multiple calls in a single transaction. Useful for allowing EOAs to perform multiple operations at once.
-   [`Packing`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing): A library for packing and unpacking multiple values into bytes32.
-   [`Panic`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic): A library to revert with [Solidity panic codes](https://docs.soliditylang.org/en/v0.8.20/control-structures.html#panic-via-assert-and-error-via-require).
-   [`RelayedCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall): A library for performing calls that use minimal and predictable relayers to hide the sender.
-   [`RLP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP): Library for encoding and decoding data in Ethereum’s Recursive Length Prefix format.
-   [`ShortStrings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings): Library to encode (and decode) short strings into (or from) a single bytes32 slot for optimizing costs. Short strings are limited to 31 characters.
-   [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation): Methods for deriving storage slot from ERC-7201 namespaces as well as from constructions such as mapping and arrays.
-   [`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot): Methods for accessing specific storage slots formatted as common primitive types.
-   [`Strings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings): Common operations for strings formatting.
-   [`Time`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time): A library that provides helpers for manipulating time-related objects, including a `Delay` type.
-   [`TransientSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot): Primitives for reading from and writing to transient storage (only value types are currently supported).

Because Solidity does not support generic types, [`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap) and [`EnumerableSet`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet) are specialized to a limited number of key-value types.

## [Math](https://docs.openzeppelin.com/contracts/5.x/api/utils#math)

[`Math`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math)

[`SignedMath`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath)

[`SafeCast`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast)

## [Security](https://docs.openzeppelin.com/contracts/5.x/api/utils#security)

[`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces)

[`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed)

[`Pausable`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable)

[`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard)

[`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient)

## [Introspection](https://docs.openzeppelin.com/contracts/5.x/api/utils#introspection)

This set of interfaces and contracts deal with [type introspection](https://en.wikipedia.org/wiki/Type_introspection) of contracts, that is, examining which functions can be called on them. This is usually referred to as a contract’s *interface*.

Ethereum contracts have no native concept of an interface, so applications must usually simply trust that they are not making an incorrect call. For trusted setups this is a non-issue, but often unknown and untrusted third-party addresses need to be interacted with. There may not even be any direct calls to them! (e.g. ERC-20 tokens may be sent to a contract that lacks a way to transfer them out of it, locking them forever). In these cases, a contract *declaring* its interface can be very helpful in preventing errors.

[`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165)

[`ERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165)

[`ERC165Checker`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker)

## [Data Structures](https://docs.openzeppelin.com/contracts/5.x/api/utils#data-structures)

[`Accumulators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators)

[`BitMaps`](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps)

[`Checkpoints`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints)

[`CircularBuffer`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer)

[`DoubleEndedQueue`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue)

[`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap)

[`EnumerableSet`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet)

[`Heap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap)

[`MerkleTree`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree)

## [Libraries](https://docs.openzeppelin.com/contracts/5.x/api/utils#libraries)

[`Address`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address)

[`Arrays`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays)

[`Base58`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58)

[`Base64`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64)

[`Blockhash`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash)

[`Bytes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes)

[`CAIP10`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10)

[`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2)

[`Calldata`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata)

[`Comparators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators)

[`Context`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context)

[`Create2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2)

[`InteroperableAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress)

[`LowLevelCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall)

[`Memory`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory)

[`Multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall)

[`Packing`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing)

[`Panic`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic)

[`RelayedCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall)

[`RLP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP)

[`ShortStrings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings)

[`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation)

[`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot)

[`Strings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings)

[`Time`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time)

[`TransientSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot)

## [`Address`](https://docs.openzeppelin.com/contracts/5.x/api/utils#address)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Address.sol)

```
import "@openzeppelin/contracts/utils/Address.sol";
```

Collection of functions related to the address type

### Functions

-   [sendValue(recipient, amount)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-sendValue-address-payable-uint256-)
-   [functionCall(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-)
-   [functionCallWithValue(target, data, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCallWithValue-address-bytes-uint256-)
-   [functionStaticCall(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionStaticCall-address-bytes-)
-   [functionDelegateCall(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionDelegateCall-address-bytes-)
-   [verifyCallResultFromTarget(target, success, returndata)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResultFromTarget-address-bool-bytes-)
-   [verifyCallResult(success, returndata)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResult-bool-bytes-)

### Errors

-   [AddressEmptyCode(target)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-AddressEmptyCode-address-)

sendValue(address payable recipient, uint256 amount)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-sendValue-address-payable-uint256-)

Replacement for Solidity's `transfer`: sends `amount` wei to `recipient`, forwarding all available gas and reverting on errors.

[EIP1884](https://eips.ethereum.org/EIPS/eip-1884) increases the gas cost of certain opcodes, possibly making contracts go over the 2300 gas limit imposed by `transfer`, making them unable to receive funds via `transfer`. [`Address.sendValue`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-sendValue-address-payable-uint256-) removes this limitation.

[Learn more](https://consensys.net/diligence/blog/2019/09/stop-using-soliditys-transfer-now/).

because control is transferred to `recipient`, care must be taken to not create reentrancy vulnerabilities. Consider using [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard) or the [checks-effects-interactions pattern](https://solidity.readthedocs.io/en/v0.8.20/security-considerations.html#use-the-checks-effects-interactions-pattern).

functionCall(address target, bytes data) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-)

Performs a Solidity function call using a low level `call`. A plain `call` is an unsafe replacement for a function call: use this function instead.

If `target` reverts with a revert reason or custom error, it is bubbled up by this function (like regular Solidity function calls). However, if the call reverted with no returned reason, this function reverts with a `Errors.FailedCall` error.

Returns the raw returned data. To convert to the expected return value, use [`abi.decode`](https://solidity.readthedocs.io/en/latest/units-and-global-variables.html?highlight=abi.decode#abi-encoding-and-decoding-functions).

Requirements:

-   `target` must be a contract.
-   calling `target` with `data` must not revert.

functionCallWithValue(address target, bytes data, uint256 value) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCallWithValue-address-bytes-uint256-)

Same as [`functionCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-), but also transferring `value` wei to `target`.

Requirements:

-   the calling contract must have an ETH balance of at least `value`.
-   the called Solidity function must be `payable`.

functionStaticCall(address target, bytes data) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionStaticCall-address-bytes-)

Same as [`functionCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-), but performing a static call.

functionDelegateCall(address target, bytes data) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionDelegateCall-address-bytes-)

Same as [`functionCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-), but performing a delegate call.

verifyCallResultFromTarget(address target, bool success, bytes returndata) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResultFromTarget-address-bool-bytes-)

Tool to verify that a low level call to smart-contract was successful, and reverts if the target was not a contract or bubbling up the revert reason (falling back to `Errors.FailedCall`) in case of an unsuccessful call.

This function is DEPRECATED and may be removed in the next major release.

verifyCallResult(bool success, bytes returndata) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResult-bool-bytes-)

Tool to verify that a low level call was successful, and reverts if it wasn't, either by bubbling the revert reason or with a default `Errors.FailedCall` error.

AddressEmptyCode(address target)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-AddressEmptyCode-address-)

There's no code at `target` (it is not a contract).

## [`Arrays`](https://docs.openzeppelin.com/contracts/5.x/api/utils#arrays)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Arrays.sol)

```
import "@openzeppelin/contracts/utils/Arrays.sol";
```

Collection of functions related to array types.

### Functions

-   [sort(array, comp)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---function--uint256-uint256--pure-returns--bool--)
-   [sort(array)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---)
-   [sort(array, comp)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---function--address-address--pure-returns--bool--)
-   [sort(array)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---)
-   [sort(array, comp)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---function--bytes32-bytes32--pure-returns--bool--)
-   [sort(array)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---)
-   [findUpperBound(array, element)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-findUpperBound-uint256---uint256-)
-   [lowerBound(array, element)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-)
-   [upperBound(array, element)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBound-uint256---uint256-)
-   [lowerBoundMemory(array, element)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBoundMemory-uint256---uint256-)
-   [upperBoundMemory(array, element)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBoundMemory-uint256---uint256-)
-   [slice(array, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-address---uint256-)
-   [slice(array, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-address---uint256-uint256-)
-   [slice(array, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-bytes32---uint256-)
-   [slice(array, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-bytes32---uint256-uint256-)
-   [slice(array, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-)
-   [slice(array, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-)
-   [splice(array, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-address---uint256-)
-   [splice(array, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-address---uint256-uint256-)
-   [replace(array, pos, replacement)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-address---uint256-address---)
-   [replace(array, pos, replacement, offset, length)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-address---uint256-address---uint256-uint256-)
-   [splice(array, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-bytes32---uint256-)
-   [splice(array, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-bytes32---uint256-uint256-)
-   [replace(array, pos, replacement)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-bytes32---uint256-bytes32---)
-   [replace(array, pos, replacement, offset, length)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-bytes32---uint256-bytes32---uint256-uint256-)
-   [splice(array, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-uint256---uint256-)
-   [splice(array, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-uint256---uint256-uint256-)
-   [replace(array, pos, replacement)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-uint256---uint256-uint256---)
-   [replace(array, pos, replacement, offset, length)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-uint256---uint256-uint256---uint256-uint256-)
-   [unsafeAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-address---uint256-)
-   [unsafeAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes32---uint256-)
-   [unsafeAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-uint256---uint256-)
-   [unsafeAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes---uint256-)
-   [unsafeAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-string---uint256-)
-   [unsafeMemoryAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-address---uint256-)
-   [unsafeMemoryAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes32---uint256-)
-   [unsafeMemoryAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-uint256---uint256-)
-   [unsafeMemoryAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes---uint256-)
-   [unsafeMemoryAccess(arr, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-string---uint256-)
-   [unsafeSetLength(array, len)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-address---uint256-)
-   [unsafeSetLength(array, len)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes32---uint256-)
-   [unsafeSetLength(array, len)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-uint256---uint256-)
-   [unsafeSetLength(array, len)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes---uint256-)
-   [unsafeSetLength(array, len)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-string---uint256-)

sort(uint256\[\] array, function (uint256,uint256) pure returns (bool) comp) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---function--uint256-uint256--pure-returns--bool--)

Sort an array of uint256 (in memory) following the provided comparator function.

This function does the sorting "in place", meaning that it overrides the input. The object is returned for convenience, but that returned value can be discarded safely if the caller has a memory pointer to the array.

this function's cost is `O(n · log(n))` in average and `O(n²)` in the worst case, with n the length of the array. Using it in view functions that are executed through `eth_call` is safe, but one should be very careful when executing this as part of a transaction. If the array being sorted is too large, the sort operation may consume more gas than is available in a block, leading to potential DoS.

Consider memory side-effects when using custom comparator functions that access memory in an unsafe way.

sort(uint256\[\] array) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---)

Variant of [`Arrays.sort`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---) that sorts an array of uint256 in increasing order.

sort(address\[\] array, function (address,address) pure returns (bool) comp) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---function--address-address--pure-returns--bool--)

Sort an array of address (in memory) following the provided comparator function.

This function does the sorting "in place", meaning that it overrides the input. The object is returned for convenience, but that returned value can be discarded safely if the caller has a memory pointer to the array.

this function's cost is `O(n · log(n))` in average and `O(n²)` in the worst case, with n the length of the array. Using it in view functions that are executed through `eth_call` is safe, but one should be very careful when executing this as part of a transaction. If the array being sorted is too large, the sort operation may consume more gas than is available in a block, leading to potential DoS.

Consider memory side-effects when using custom comparator functions that access memory in an unsafe way.

sort(address\[\] array) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---)

Variant of [`Arrays.sort`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---) that sorts an array of address in increasing order.

sort(bytes32\[\] array, function (bytes32,bytes32) pure returns (bool) comp) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---function--bytes32-bytes32--pure-returns--bool--)

Sort an array of bytes32 (in memory) following the provided comparator function.

This function does the sorting "in place", meaning that it overrides the input. The object is returned for convenience, but that returned value can be discarded safely if the caller has a memory pointer to the array.

this function's cost is `O(n · log(n))` in average and `O(n²)` in the worst case, with n the length of the array. Using it in view functions that are executed through `eth_call` is safe, but one should be very careful when executing this as part of a transaction. If the array being sorted is too large, the sort operation may consume more gas than is available in a block, leading to potential DoS.

Consider memory side-effects when using custom comparator functions that access memory in an unsafe way.

sort(bytes32\[\] array) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---)

Variant of [`Arrays.sort`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---) that sorts an array of bytes32 in increasing order.

findUpperBound(uint256\[\] array, uint256 element) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-findUpperBound-uint256---uint256-)

Searches a sorted `array` and returns the first index that contains a value greater or equal to `element`. If no such index exists (i.e. all values in the array are strictly less than `element`), the array length is returned. Time complexity O(log n).

The `array` is expected to be sorted in ascending order, and to contain no repeated elements.

Deprecated. This implementation behaves as [`Arrays.lowerBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-) but lacks support for repeated elements in the array. The [`Arrays.lowerBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-) function should be used instead.

lowerBound(uint256\[\] array, uint256 element) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-)

Searches an `array` sorted in ascending order and returns the first index that contains a value greater or equal than `element`. If no such index exists (i.e. all values in the array are strictly less than `element`), the array length is returned. Time complexity O(log n).

See C++'s [lower\_bound](https://en.cppreference.com/w/cpp/algorithm/lower_bound).

upperBound(uint256\[\] array, uint256 element) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBound-uint256---uint256-)

Searches an `array` sorted in ascending order and returns the first index that contains a value strictly greater than `element`. If no such index exists (i.e. all values in the array are strictly less than `element`), the array length is returned. Time complexity O(log n).

See C++'s [upper\_bound](https://en.cppreference.com/w/cpp/algorithm/upper_bound).

lowerBoundMemory(uint256\[\] array, uint256 element) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBoundMemory-uint256---uint256-)

Same as [`Arrays.lowerBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-), but with an array in memory.

upperBoundMemory(uint256\[\] array, uint256 element) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBoundMemory-uint256---uint256-)

Same as [`Arrays.upperBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBound-uint256---uint256-), but with an array in memory.

slice(address\[\] array, uint256 start) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-address---uint256-)

Copies the content of `array`, from `start` (included) to the end of `array` into a new address array in memory.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

slice(address\[\] array, uint256 start, uint256 end) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-address---uint256-uint256-)

Copies the content of `array`, from `start` (included) to `end` (excluded) into a new address array in memory. The `end` argument is truncated to the length of the `array`.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

slice(bytes32\[\] array, uint256 start) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-bytes32---uint256-)

Copies the content of `array`, from `start` (included) to the end of `array` into a new bytes32 array in memory.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

slice(bytes32\[\] array, uint256 start, uint256 end) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-bytes32---uint256-uint256-)

Copies the content of `array`, from `start` (included) to `end` (excluded) into a new bytes32 array in memory. The `end` argument is truncated to the length of the `array`.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

slice(uint256\[\] array, uint256 start) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-)

Copies the content of `array`, from `start` (included) to the end of `array` into a new uint256 array in memory.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

slice(uint256\[\] array, uint256 start, uint256 end) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-)

Copies the content of `array`, from `start` (included) to `end` (excluded) into a new uint256 array in memory. The `end` argument is truncated to the length of the `array`.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

splice(address\[\] array, uint256 start) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-address---uint256-)

Moves the content of `array`, from `start` (included) to the end of `array` to the start of that array, and shrinks the array length accordingly, effectively overwriting the array with array\[start:\].

This function modifies the provided array in place. If you need to preserve the original array, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead.

splice(address\[\] array, uint256 start, uint256 end) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-address---uint256-uint256-)

Moves the content of `array`, from `start` (included) to `end` (excluded) to the start of that array, and shrinks the array length accordingly, effectively overwriting the array with array\[start:end\]. The `end` argument is truncated to the length of the `array`.

This function modifies the provided array in place. If you need to preserve the original array, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead.

replace(address\[\] array, uint256 pos, address\[\] replacement) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-address---uint256-address---)

Replaces elements in `array` starting at `pos` with all elements from `replacement`.

Parameters are clamped to valid ranges (e.g. `pos` is clamped to `[0, array.length]`). If `pos >= array.length`, no replacement occurs and the array is returned unchanged.

This function modifies the provided array in place.

replace(address\[\] array, uint256 pos, address\[\] replacement, uint256 offset, uint256 length) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-address---uint256-address---uint256-uint256-)

Replaces elements in `array` starting at `pos` with elements from `replacement` starting at `offset`. Copies at most `length` elements from `replacement` to `array`.

Parameters are clamped to valid ranges (i.e. `pos` is clamped to `[0, array.length]`, `offset` is clamped to `[0, replacement.length]`, and `length` is clamped to `min(length, replacement.length - offset, array.length - pos)`). If `pos >= array.length` or `offset >= replacement.length`, no replacement occurs and the array is returned unchanged.

This function modifies the provided array in place.

splice(bytes32\[\] array, uint256 start) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-bytes32---uint256-)

Moves the content of `array`, from `start` (included) to the end of `array` to the start of that array, and shrinks the array length accordingly, effectively overwriting the array with array\[start:\].

This function modifies the provided array in place. If you need to preserve the original array, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead.

splice(bytes32\[\] array, uint256 start, uint256 end) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-bytes32---uint256-uint256-)

Moves the content of `array`, from `start` (included) to `end` (excluded) to the start of that array, and shrinks the array length accordingly, effectively overwriting the array with array\[start:end\]. The `end` argument is truncated to the length of the `array`.

This function modifies the provided array in place. If you need to preserve the original array, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead.

replace(bytes32\[\] array, uint256 pos, bytes32\[\] replacement) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-bytes32---uint256-bytes32---)

Replaces elements in `array` starting at `pos` with all elements from `replacement`.

Parameters are clamped to valid ranges (e.g. `pos` is clamped to `[0, array.length]`). If `pos >= array.length`, no replacement occurs and the array is returned unchanged.

This function modifies the provided array in place.

replace(bytes32\[\] array, uint256 pos, bytes32\[\] replacement, uint256 offset, uint256 length) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-bytes32---uint256-bytes32---uint256-uint256-)

Replaces elements in `array` starting at `pos` with elements from `replacement` starting at `offset`. Copies at most `length` elements from `replacement` to `array`.

Parameters are clamped to valid ranges (i.e. `pos` is clamped to `[0, array.length]`, `offset` is clamped to `[0, replacement.length]`, and `length` is clamped to `min(length, replacement.length - offset, array.length - pos)`). If `pos >= array.length` or `offset >= replacement.length`, no replacement occurs and the array is returned unchanged.

This function modifies the provided array in place.

splice(uint256\[\] array, uint256 start) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-uint256---uint256-)

Moves the content of `array`, from `start` (included) to the end of `array` to the start of that array, and shrinks the array length accordingly, effectively overwriting the array with array\[start:\].

This function modifies the provided array in place. If you need to preserve the original array, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead.

splice(uint256\[\] array, uint256 start, uint256 end) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-splice-uint256---uint256-uint256-)

Moves the content of `array`, from `start` (included) to `end` (excluded) to the start of that array, and shrinks the array length accordingly, effectively overwriting the array with array\[start:end\]. The `end` argument is truncated to the length of the `array`.

This function modifies the provided array in place. If you need to preserve the original array, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead.

replace(uint256\[\] array, uint256 pos, uint256\[\] replacement) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-uint256---uint256-uint256---)

Replaces elements in `array` starting at `pos` with all elements from `replacement`.

Parameters are clamped to valid ranges (e.g. `pos` is clamped to `[0, array.length]`). If `pos >= array.length`, no replacement occurs and the array is returned unchanged.

This function modifies the provided array in place.

replace(uint256\[\] array, uint256 pos, uint256\[\] replacement, uint256 offset, uint256 length) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-replace-uint256---uint256-uint256---uint256-uint256-)

Replaces elements in `array` starting at `pos` with elements from `replacement` starting at `offset`. Copies at most `length` elements from `replacement` to `array`.

Parameters are clamped to valid ranges (i.e. `pos` is clamped to `[0, array.length]`, `offset` is clamped to `[0, replacement.length]`, and `length` is clamped to `min(length, replacement.length - offset, array.length - pos)`). If `pos >= array.length` or `offset >= replacement.length`, no replacement occurs and the array is returned unchanged.

This function modifies the provided array in place.

unsafeAccess(address\[\] arr, uint256 pos) → struct StorageSlot.AddressSlot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-address---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeAccess(bytes32\[\] arr, uint256 pos) → struct StorageSlot.Bytes32Slot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes32---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeAccess(uint256\[\] arr, uint256 pos) → struct StorageSlot.Uint256Slot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-uint256---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeAccess(bytes\[\] arr, uint256 pos) → struct StorageSlot.BytesSlot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeAccess(string\[\] arr, uint256 pos) → struct StorageSlot.StringSlot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-string---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeMemoryAccess(address\[\] arr, uint256 pos) → address res

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-address---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeMemoryAccess(bytes32\[\] arr, uint256 pos) → bytes32 res

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes32---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeMemoryAccess(uint256\[\] arr, uint256 pos) → uint256 res

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-uint256---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeMemoryAccess(bytes\[\] arr, uint256 pos) → bytes res

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeMemoryAccess(string\[\] arr, uint256 pos) → string res

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-string---uint256-)

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

unsafeSetLength(address\[\] array, uint256 len)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-address---uint256-)

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, or initialize elements if length is increased.

unsafeSetLength(bytes32\[\] array, uint256 len)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes32---uint256-)

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, or initialize elements if length is increased.

unsafeSetLength(uint256\[\] array, uint256 len)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-uint256---uint256-)

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, or initialize elements if length is increased.

unsafeSetLength(bytes\[\] array, uint256 len)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes---uint256-)

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, or initialize elements if length is increased.

unsafeSetLength(string\[\] array, uint256 len)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-string---uint256-)

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, or initialize elements if length is increased.

## [`Base58`](https://docs.openzeppelin.com/contracts/5.x/api/utils#base58)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Base58.sol)

```
import "@openzeppelin/contracts/utils/Base58.sol";
```

Provides a set of functions to operate with Base58 strings.

Base58 is an encoding scheme that converts binary data into a human-readable text format. Similar to [`Base64`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64) but specifically designed for better human usability.

1.  Human-friendly alphabet: Excludes visually similar characters to reduce human error:
    -   No 0 (zero) vs O (capital o) confusion
    -   No I (capital i) vs l (lowercase L) confusion
    -   No non-alphanumeric characters like + or =
2.  URL-safe: Contains only alphanumeric characters, making it safe for URLs without encoding.

Initially based on [storyicon's implementation](https://github.com/storyicon/base58-solidity/commit/807428e5174e61867e4c606bdb26cba58a8c5cb1) (MIT). Based on the updated and improved [Vectorized version](https://github.com/Vectorized/solady/blob/208e4f31cfae26e4983eb95c3488a14fdc497ad7/src/utils/Base58.sol) (MIT).

### Functions

-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-encode-bytes-)
-   [decode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-decode-string-)

### Errors

-   [InvalidBase58Char()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-InvalidBase58Char-bytes1-)

encode(bytes input) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-encode-bytes-)

Encode a `bytes` buffer as a Base58 `string`.

decode(string input) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-decode-string-)

Decode a Base58 `string` into a `bytes` buffer.

InvalidBase58Char(bytes1)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-InvalidBase58Char-bytes1-)

Unrecognized Base58 character on decoding.

## [`Base64`](https://docs.openzeppelin.com/contracts/5.x/api/utils#base64)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Base64.sol)

```
import "@openzeppelin/contracts/utils/Base64.sol";
```

Provides a set of functions to operate with Base64 strings.

### Functions

-   [encode(data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-encode-bytes-)
-   [encodeURL(data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-encodeURL-bytes-)
-   [decode(data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-decode-string-)

### Errors

-   [InvalidBase64Char()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-InvalidBase64Char-bytes1-)

encode(bytes data) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-encode-bytes-)

Converts a `bytes` to its Base64 `string` representation.

encodeURL(bytes data) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-encodeURL-bytes-)

Converts a `bytes` to its Base64Url `string` representation. Output is not padded with `=` as specified in [rfc4648](https://www.rfc-editor.org/rfc/rfc4648).

decode(string data) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-decode-string-)

Converts a Base64 `string` to the `bytes` it represents.

-   Supports padded and unpadded inputs.
-   Supports both encoding ([`Base58.encode`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-encode-bytes-) and [`Base64.encodeURL`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-encodeURL-bytes-)) seamlessly.
-   Reverts with [`Base64.InvalidBase64Char`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-InvalidBase64Char-bytes1-) if the input contains an invalid character.

InvalidBase64Char(bytes1)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-InvalidBase64Char-bytes1-)

## [`Blockhash`](https://docs.openzeppelin.com/contracts/5.x/api/utils#blockhash)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Blockhash.sol)

```
import "@openzeppelin/contracts/utils/Blockhash.sol";
```

Library for accessing historical block hashes beyond the standard 256 block limit. Uses EIP-2935's history storage contract which maintains a ring buffer of the last 8191 block hashes in state.

For blocks within the last 256 blocks, it uses the native `BLOCKHASH` opcode. For blocks between 257 and 8191 blocks ago, it queries the EIP-2935 history storage. For blocks older than 8191 or future blocks, it returns zero, matching the `BLOCKHASH` behavior.

After EIP-2935 activation, it takes 8191 blocks to completely fill the history. Before that, only block hashes since the fork block will be available.

### Functions

-   [blockHash(blockNumber)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash-blockHash-uint256-)

blockHash(uint256 blockNumber) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash-blockHash-uint256-)

Retrieves the block hash for any historical block within the supported range.

The function gracefully handles future blocks and blocks beyond the history window by returning zero, consistent with the EVM's native `BLOCKHASH` behavior.

## [`Bytes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#bytes)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Bytes.sol)

```
import "@openzeppelin/contracts/utils/Bytes.sol";
```

Bytes operations.

### Functions

-   [indexOf(buffer, s)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-)
-   [indexOf(buffer, s, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-uint256-)
-   [lastIndexOf(buffer, s)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-)
-   [lastIndexOf(buffer, s, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-uint256-)
-   [slice(buffer, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-)
-   [slice(buffer, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-uint256-)
-   [splice(buffer, start)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-splice-bytes-uint256-)
-   [splice(buffer, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-splice-bytes-uint256-uint256-)
-   [replace(buffer, pos, replacement)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-replace-bytes-uint256-bytes-)
-   [replace(buffer, pos, replacement, offset, length)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-replace-bytes-uint256-bytes-uint256-uint256-)
-   [concat(buffers)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-concat-bytes---)
-   [toNibbles(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-toNibbles-bytes-)
-   [equal(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-equal-bytes-bytes-)
-   [reverseBytes32(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes32-bytes32-)
-   [reverseBytes16(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes16-bytes16-)
-   [reverseBytes8(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes8-bytes8-)
-   [reverseBytes4(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes4-bytes4-)
-   [reverseBytes2(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes2-bytes2-)
-   [clz(buffer)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-clz-bytes-)

indexOf(bytes buffer, bytes1 s) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-)

Forward search for `s` in `buffer`

-   If `s` is present in the buffer, returns the index of the first instance
-   If `s` is not present in the buffer, returns type(uint256).max

replicates the behavior of [Javascript's `Array.indexOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)

indexOf(bytes buffer, bytes1 s, uint256 pos) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-uint256-)

Forward search for `s` in `buffer` starting at position `pos`

-   If `s` is present in the buffer (at or after `pos`), returns the index of the next instance
-   If `s` is not present in the buffer (at or after `pos`), returns type(uint256).max

replicates the behavior of [Javascript's `Array.indexOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)

lastIndexOf(bytes buffer, bytes1 s) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-)

Backward search for `s` in `buffer`

-   If `s` is present in the buffer, returns the index of the last instance
-   If `s` is not present in the buffer, returns type(uint256).max

replicates the behavior of [Javascript's `Array.lastIndexOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf)

lastIndexOf(bytes buffer, bytes1 s, uint256 pos) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-uint256-)

Backward search for `s` in `buffer` starting at position `pos`

-   If `s` is present in the buffer (at or before `pos`), returns the index of the previous instance
-   If `s` is not present in the buffer (at or before `pos`), returns type(uint256).max

replicates the behavior of [Javascript's `Array.lastIndexOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf)

slice(bytes buffer, uint256 start) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-)

Copies the content of `buffer`, from `start` (included) to the end of `buffer` into a new bytes object in memory.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

slice(bytes buffer, uint256 start, uint256 end) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-uint256-)

Copies the content of `buffer`, from `start` (included) to `end` (excluded) into a new bytes object in memory. The `end` argument is truncated to the length of the `buffer`.

replicates the behavior of [Javascript's `Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

splice(bytes buffer, uint256 start) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-splice-bytes-uint256-)

Moves the content of `buffer`, from `start` (included) to the end of `buffer` to the start of that buffer, and shrinks the buffer length accordingly, effectively overriding the content of buffer with buffer\[start:\].

This function modifies the provided buffer in place. If you need to preserve the original buffer, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead

splice(bytes buffer, uint256 start, uint256 end) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-splice-bytes-uint256-uint256-)

Moves the content of `buffer`, from `start` (included) to `end` (excluded) to the start of that buffer, and shrinks the buffer length accordingly, effectively overriding the content of buffer with buffer\[start:end\]. The `end` argument is truncated to the length of the `buffer`.

This function modifies the provided buffer in place. If you need to preserve the original buffer, use [`Arrays.slice`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-slice-uint256---uint256-uint256-) instead

replace(bytes buffer, uint256 pos, bytes replacement) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-replace-bytes-uint256-bytes-)

Replaces bytes in `buffer` starting at `pos` with all bytes from `replacement`.

Parameters are clamped to valid ranges (i.e. `pos` is clamped to `[0, buffer.length]`). If `pos >= buffer.length`, no replacement occurs and the buffer is returned unchanged.

This function modifies the provided buffer in place.

replace(bytes buffer, uint256 pos, bytes replacement, uint256 offset, uint256 length) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-replace-bytes-uint256-bytes-uint256-uint256-)

Replaces bytes in `buffer` starting at `pos` with bytes from `replacement` starting at `offset`. Copies at most `length` bytes from `replacement` to `buffer`.

Parameters are clamped to valid ranges (i.e. `pos` is clamped to `[0, buffer.length]`, `offset` is clamped to `[0, replacement.length]`, and `length` is clamped to `min(length, replacement.length - offset, buffer.length - pos))`. If `pos >= buffer.length` or `offset >= replacement.length`, no replacement occurs and the buffer is returned unchanged.

This function modifies the provided buffer in place.

concat(bytes\[\] buffers) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-concat-bytes---)

Concatenate an array of bytes into a single bytes object.

For fixed bytes types, we recommend using the solidity built-in `bytes.concat` or (equivalent) `abi.encodePacked`.

this could be done in assembly with a single loop that expands starting at the FMP, but that would be significantly less readable. It might be worth benchmarking the savings of the full-assembly approach.

toNibbles(bytes input) → bytes output

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-toNibbles-bytes-)

Split each byte in `input` into two nibbles (4 bits each)

Example: hex"01234567" → hex"0001020304050607"

equal(bytes a, bytes b) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-equal-bytes-bytes-)

Returns true if the two byte buffers are equal.

reverseBytes32(bytes32 value) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes32-bytes32-)

Reverses the byte order of a bytes32 value, converting between little-endian and big-endian. Inspired by [Reverse Parallel](https://graphics.stanford.edu/~seander/bithacks.html#ReverseParallel)

reverseBytes16(bytes16 value) → bytes16

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes16-bytes16-)

Same as [`Bytes.reverseBytes32`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes32-bytes32-) but optimized for 128-bit values.

reverseBytes8(bytes8 value) → bytes8

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes8-bytes8-)

Same as [`Bytes.reverseBytes32`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes32-bytes32-) but optimized for 64-bit values.

reverseBytes4(bytes4 value) → bytes4

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes4-bytes4-)

Same as [`Bytes.reverseBytes32`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes32-bytes32-) but optimized for 32-bit values.

reverseBytes2(bytes2 value) → bytes2

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes2-bytes2-)

Same as [`Bytes.reverseBytes32`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-reverseBytes32-bytes32-) but optimized for 16-bit values.

clz(bytes buffer) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-clz-bytes-)

Counts the number of leading zero bits a bytes array. Returns `8 * buffer.length` if the buffer is all zeros.

## [`CAIP10`](https://docs.openzeppelin.com/contracts/5.x/api/utils#caip10)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/CAIP10.sol)

```
import "@openzeppelin/contracts/utils/CAIP10.sol";
```

Helper library to format and parse CAIP-10 identifiers

[CAIP-10](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-10.md) defines account identifiers as: account\_id: chain\_id + ":" + account\_address chain\_id: \[-a-z0-9\]8:\[-\_a-zA-Z0-9\]32 (See [`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2)) account\_address: \[-.%a-zA-Z0-9\]128

According to [CAIP-10's canonicalization section](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-10.md#canonicalization), the implementation remains at the developer's discretion. Please note that case variations may introduce ambiguity. For example, when building hashes to identify accounts or data associated to them, multiple representations of the same account would derive to different hashes. For EVM chains, we recommend using checksummed addresses for the "account\_address" part. They can be generated onchain using [`Strings.toChecksumHexString`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toChecksumHexString-address-).

### Functions

-   [local(account)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-local-address-)
-   [format(caip2, account)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-format-string-string-)
-   [parse(caip10)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-parse-string-)

local(address account) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-local-address-)

Return the CAIP-10 identifier for an account on the current (local) chain.

format(string caip2, string account) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-format-string-string-)

Return the CAIP-10 identifier for a given caip2 chain and account.

This function does not verify that the inputs are properly formatted.

parse(string caip10) → string caip2, string account

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-parse-string-)

Parse a CAIP-10 identifier into its components.

This function does not verify that the CAIP-10 input is properly formatted. The `caip2` return can be parsed using the [`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2) library.

## [`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#caip2)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/CAIP2.sol)

```
import "@openzeppelin/contracts/utils/CAIP2.sol";
```

Helper library to format and parse CAIP-2 identifiers

[CAIP-2](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-2.md) defines chain identifiers as: chain\_id: namespace + ":" + reference namespace: \[-a-z0-9\]8 reference: \[-\_a-zA-Z0-9\]32

In some cases, multiple CAIP-2 identifiers may all be valid representation of a single chain. For EVM chains, it is recommended to use `eip155:xxx` as the canonical representation (where `xxx` is the EIP-155 chain id). Consider the possible ambiguity when processing CAIP-2 identifiers or when using them in the context of hashes.

### Functions

-   [local()](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-local--)
-   [format(namespace, ref)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-format-string-string-)
-   [parse(caip2)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-parse-string-)

local() → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-local--)

Return the CAIP-2 identifier for the current (local) chain.

format(string namespace, string ref) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-format-string-string-)

Return the CAIP-2 identifier for a given namespace and reference.

This function does not verify that the inputs are properly formatted.

parse(string caip2) → string namespace, string ref

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-parse-string-)

Parse a CAIP-2 identifier into its components.

This function does not verify that the CAIP-2 input is properly formatted.

## [`Calldata`](https://docs.openzeppelin.com/contracts/5.x/api/utils#calldata)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Calldata.sol)

```
import "@openzeppelin/contracts/utils/Calldata.sol";
```

Helper library for manipulating objects in calldata.

### Functions

-   [emptyBytes()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata-emptyBytes--)
-   [emptyString()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata-emptyString--)

emptyBytes() → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata-emptyBytes--)

emptyString() → string result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata-emptyString--)

## [`Comparators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#comparators)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Comparators.sol)

```
import "@openzeppelin/contracts/utils/Comparators.sol";
```

Provides a set of functions to compare values.

*Available since v5.1.*

### Functions

-   [lt(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-lt-uint256-uint256-)
-   [gt(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-gt-uint256-uint256-)

lt(uint256 a, uint256 b) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-lt-uint256-uint256-)

gt(uint256 a, uint256 b) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-gt-uint256-uint256-)

## [`Context`](https://docs.openzeppelin.com/contracts/5.x/api/utils#context)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Context.sol)

```
import "@openzeppelin/contracts/utils/Context.sol";
```

Provides information about the current execution context, including the sender of the transaction and its data. While these are generally available via msg.sender and msg.data, they should not be accessed in such a direct manner, since when dealing with meta-transactions the account sending and paying for execution may not be the actual sender (as far as an application is concerned).

This contract is only required for intermediate, library-like contracts.

### Functions

-   [\_msgSender()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgSender--)
-   [\_msgData()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgData--)
-   [\_contextSuffixLength()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_contextSuffixLength--)

\_msgSender() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgSender--)

\_msgData() → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgData--)

\_contextSuffixLength() → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_contextSuffixLength--)

## [`Create2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#create2)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Create2.sol)

```
import "@openzeppelin/contracts/utils/Create2.sol";
```

Helper to make usage of the `CREATE2` EVM opcode easier and safer. `CREATE2` can be used to compute in advance the address where a smart contract will be deployed, which allows for interesting new mechanisms known as 'counterfactual interactions'.

See the [EIP](https://eips.ethereum.org/EIPS/eip-1014#motivation) for more information.

### Functions

-   [deploy(amount, salt, bytecode)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-)
-   [computeAddress(salt, bytecodeHash)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-)
-   [computeAddress(salt, bytecodeHash, deployer)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-)

### Errors

-   [Create2EmptyBytecode()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-Create2EmptyBytecode--)

deploy(uint256 amount, bytes32 salt, bytes bytecode) → address addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-)

Deploys a contract using `CREATE2`. The address where the contract will be deployed can be known in advance via [`Create2.computeAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-).

The bytecode for a contract can be obtained from Solidity with `type(contractName).creationCode`.

Requirements:

-   `bytecode` must not be empty.
-   `salt` must have not been used for `bytecode` already.
-   the factory must have a balance of at least `amount`.
-   if `amount` is non-zero, `bytecode` must have a `payable` constructor.

computeAddress(bytes32 salt, bytes32 bytecodeHash) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-)

Returns the address where a contract will be stored if deployed via [`Create2.deploy`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-). Any change in the `bytecodeHash` or `salt` will result in a new destination address.

computeAddress(bytes32 salt, bytes32 bytecodeHash, address deployer) → address addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-)

Returns the address where a contract will be stored if deployed via [`Create2.deploy`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-) from a contract located at `deployer`. If `deployer` is this contract's address, returns the same value as [`Create2.computeAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-).

Create2EmptyBytecode()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-Create2EmptyBytecode--)

There's no code to deploy.

## [`Errors`](https://docs.openzeppelin.com/contracts/5.x/api/utils#errors)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Errors.sol)

```
import "@openzeppelin/contracts/utils/Errors.sol";
```

Collection of common custom errors used in multiple contracts

Backwards compatibility is not guaranteed in future versions of the library. It is recommended to avoid relying on the error API for critical functionality.

*Available since v5.1.*

### Errors

-   [InsufficientBalance(balance, needed)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-InsufficientBalance-uint256-uint256-)
-   [FailedCall()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-FailedCall--)
-   [FailedDeployment()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-FailedDeployment--)
-   [MissingPrecompile()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-MissingPrecompile-address-)

InsufficientBalance(uint256 balance, uint256 needed)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-InsufficientBalance-uint256-uint256-)

The ETH balance of the account is not enough to perform the operation.

FailedCall()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-FailedCall--)

A call to an address target failed. The target may have reverted.

FailedDeployment()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-FailedDeployment--)

The deployment failed.

MissingPrecompile(address)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Errors-MissingPrecompile-address-)

A necessary precompile is missing.

## [`LowLevelCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#lowlevelcall)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/LowLevelCall.sol)

```
import "@openzeppelin/contracts/utils/LowLevelCall.sol";
```

Library of low level call functions that implement different calling strategies to deal with the return data.

Using this library requires an advanced understanding of Solidity and how the EVM works. It is recommended to use the [`Address`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address) library instead.

### Functions

-   [callNoReturn(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callNoReturn-address-bytes-)
-   [callNoReturn(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callNoReturn-address-uint256-bytes-)
-   [callReturn64Bytes(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callReturn64Bytes-address-bytes-)
-   [callReturn64Bytes(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callReturn64Bytes-address-uint256-bytes-)
-   [staticcallNoReturn(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-staticcallNoReturn-address-bytes-)
-   [staticcallReturn64Bytes(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-staticcallReturn64Bytes-address-bytes-)
-   [delegatecallNoReturn(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-delegatecallNoReturn-address-bytes-)
-   [delegatecallReturn64Bytes(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-delegatecallReturn64Bytes-address-bytes-)
-   [returnDataSize()](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-returnDataSize--)
-   [returnData()](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-returnData--)
-   [bubbleRevert()](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-bubbleRevert--)
-   [bubbleRevert(returndata)](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-bubbleRevert-bytes-)

callNoReturn(address target, bytes data) → bool success

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callNoReturn-address-bytes-)

Performs a Solidity function call using a low level `call` and ignoring the return data.

callNoReturn(address target, uint256 value, bytes data) → bool success

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callNoReturn-address-uint256-bytes-)

Same as `callNoReturn-address-bytes`, but allows specifying the value to be sent in the call.

callReturn64Bytes(address target, bytes data) → bool success, bytes32 result1, bytes32 result2

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callReturn64Bytes-address-bytes-)

Performs a Solidity function call using a low level `call` and returns the first 64 bytes of the result in the scratch space of memory. Useful for functions that return a tuple with two single-word values.

Do not assume that the results are zero if `success` is false. Memory can be already allocated and this function doesn't zero it out.

callReturn64Bytes(address target, uint256 value, bytes data) → bool success, bytes32 result1, bytes32 result2

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-callReturn64Bytes-address-uint256-bytes-)

Same as `callReturn64Bytes-address-bytes`, but allows specifying the value to be sent in the call.

staticcallNoReturn(address target, bytes data) → bool success

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-staticcallNoReturn-address-bytes-)

Performs a Solidity function call using a low level `staticcall` and ignoring the return data.

staticcallReturn64Bytes(address target, bytes data) → bool success, bytes32 result1, bytes32 result2

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-staticcallReturn64Bytes-address-bytes-)

Performs a Solidity function call using a low level `staticcall` and returns the first 64 bytes of the result in the scratch space of memory. Useful for functions that return a tuple with two single-word values.

Do not assume that the results are zero if `success` is false. Memory can be already allocated and this function doesn't zero it out.

delegatecallNoReturn(address target, bytes data) → bool success

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-delegatecallNoReturn-address-bytes-)

Performs a Solidity function call using a low level `delegatecall` and ignoring the return data.

delegatecallReturn64Bytes(address target, bytes data) → bool success, bytes32 result1, bytes32 result2

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-delegatecallReturn64Bytes-address-bytes-)

Performs a Solidity function call using a low level `delegatecall` and returns the first 64 bytes of the result in the scratch space of memory. Useful for functions that return a tuple with two single-word values.

Do not assume that the results are zero if `success` is false. Memory can be already allocated and this function doesn't zero it out.

returnDataSize() → uint256 size

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-returnDataSize--)

Returns the size of the return data buffer.

returnData() → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-returnData--)

Returns a buffer containing the return data from the last call.

bubbleRevert()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-bubbleRevert--)

Revert with the return data from the last call.

bubbleRevert(bytes returndata)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#LowLevelCall-bubbleRevert-bytes-)

## [`Memory`](https://docs.openzeppelin.com/contracts/5.x/api/utils#memory)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Memory.sol)

```
import "@openzeppelin/contracts/utils/Memory.sol";
```

Utilities to manipulate memory.

Memory is a contiguous and dynamic byte array in which Solidity stores non-primitive types. This library provides functions to manipulate pointers to this dynamic array and work with slices of it.

Slices provide a view into a portion of memory without copying data, enabling efficient substring operations.

When manipulating memory pointers or slices, make sure to follow the Solidity documentation guidelines for [Memory Safety](https://docs.soliditylang.org/en/v0.8.20/assembly.html#memory-safety).

### Functions

-   [getFreeMemoryPointer()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-getFreeMemoryPointer--)
-   [unsafeSetFreeMemoryPointer(ptr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-unsafeSetFreeMemoryPointer-Memory-Pointer-)
-   [forward(ptr, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-forward-Memory-Pointer-uint256-)
-   [equal(ptr1, ptr2)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-equal-Memory-Pointer-Memory-Pointer-)
-   [asSlice(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-asSlice-bytes-)
-   [length(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-)
-   [slice(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-slice-Memory-Slice-uint256-)
-   [slice(self, offset, len)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-slice-Memory-Slice-uint256-uint256-)
-   [load(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-load-Memory-Slice-uint256-)
-   [toBytes(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-toBytes-Memory-Slice-)
-   [equal(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-equal-Memory-Slice-Memory-Slice-)
-   [isReserved(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-isReserved-Memory-Slice-)

getFreeMemoryPointer() → Memory.Pointer ptr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-getFreeMemoryPointer--)

Returns a `Pointer` to the current free `Pointer`.

unsafeSetFreeMemoryPointer(Memory.Pointer ptr)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-unsafeSetFreeMemoryPointer-Memory-Pointer-)

Sets the free `Pointer` to a specific value.

The solidity memory layout requires that the FMP is never set to a value lower than 0x80. Setting the FMP to a value lower than 0x80 may cause unexpected behavior. Deallocating all memory can be achieved by setting the FMP to 0x80.

Everything after the pointer may be overwritten.

forward(Memory.Pointer ptr, uint256 offset) → Memory.Pointer

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-forward-Memory-Pointer-uint256-)

Move a pointer forward by a given offset.

equal(Memory.Pointer ptr1, Memory.Pointer ptr2) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-equal-Memory-Pointer-Memory-Pointer-)

Equality comparator for memory pointers.

asSlice(bytes self) → Memory.Slice result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-asSlice-bytes-)

Get a slice representation of a bytes object in memory

length(Memory.Slice self) → uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-)

Returns the length of a given slice (equiv to self.length for calldata slices)

slice(Memory.Slice self, uint256 offset) → Memory.Slice

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-slice-Memory-Slice-uint256-)

Offset a memory slice (equivalent to self\[offset:\] for calldata slices)

slice(Memory.Slice self, uint256 offset, uint256 len) → Memory.Slice

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-slice-Memory-Slice-uint256-uint256-)

Offset and cut a Slice (equivalent to self\[offset:offset+len\] for calldata slices)

load(Memory.Slice self, uint256 offset) → bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-load-Memory-Slice-uint256-)

Read a bytes32 buffer from a given Slice at a specific offset

If offset > length(slice) - 0x20, part of the return value will be out of bound of the slice. These bytes are zeroed.

toBytes(Memory.Slice self) → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-toBytes-Memory-Slice-)

Extract the data corresponding to a Slice (allocate new memory)

equal(Memory.Slice a, Memory.Slice b) → bool result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-equal-Memory-Slice-Memory-Slice-)

Returns true if the two slices contain the same data.

isReserved(Memory.Slice self) → bool result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-isReserved-Memory-Slice-)

Returns true if the memory occupied by the slice is reserved (i.e. before the free memory pointer)

## [`Multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#multicall)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Multicall.sol)

```
import "@openzeppelin/contracts/utils/Multicall.sol";
```

Provides a function to batch together multiple calls in a single external call.

Consider any assumption about calldata validation performed by the sender may be violated if it's not especially careful about sending transactions invoking [`Multicall.multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---). For example, a relay address that filters function selectors won't filter calls nested within a [`Multicall.multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---) operation.

Since 5.0.1 and 4.9.4, this contract identifies non-canonical contexts (i.e. `msg.sender` is not [`Context._msgSender`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgSender--)). If a non-canonical context is identified, the following self `delegatecall` appends the last bytes of `msg.data` to the subcall. This makes it safe to use with [`ERC2771Context`](https://docs.openzeppelin.com/contracts/5.x/api/metatx#ERC2771Context). Contexts that don't affect the resolution of [`Context._msgSender`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgSender--) are not propagated to subcalls.

### Functions

-   [multicall(data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---)

multicall(bytes\[\] data) → bytes\[\] results

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---)

Receives and executes a batch of function calls on this contract.

## [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#nonces)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Nonces.sol)

```
import "@openzeppelin/contracts/utils/Nonces.sol";
```

Provides tracking nonces for addresses. Nonces will only increment.

### Functions

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useCheckedNonce-address-uint256-)

### Errors

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-InvalidAccountNonce-address-uint256-)

nonces(address owner) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-nonces-address-)

Returns the next unused nonce for an address.

\_useNonce(address owner) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-)

Consumes a nonce.

Returns the current value and increments nonce.

\_useCheckedNonce(address owner, uint256 nonce)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useCheckedNonce-address-uint256-)

Same as [`Nonces._useNonce`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-) but checking that `nonce` is the next valid for `owner`.

InvalidAccountNonce(address account, uint256 currentNonce)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-InvalidAccountNonce-address-uint256-)

The nonce used for an `account` is not the expected current nonce.

## [`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#nonceskeyed)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/NoncesKeyed.sol)

```
import "@openzeppelin/contracts/utils/NoncesKeyed.sol";
```

Alternative to [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces), that supports key-ed nonces.

Follows the [ERC-4337's semi-abstracted nonce system](https://eips.ethereum.org/EIPS/eip-4337#semi-abstracted-nonce-support).

This contract inherits from [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces) and reuses its storage for the first nonce key (i.e. `0`). This makes upgrading from [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces) to [`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed) safe when using their upgradeable versions (e.g. `NoncesKeyedUpgradeable`). Doing so will NOT reset the current state of nonces, avoiding replay attacks where a nonce is reused after the upgrade.

### Functions

-   [nonces(owner, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-nonces-address-uint192-)
-   [\_useNonce(owner, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useNonce-address-uint192-)
-   [\_useCheckedNonce(owner, keyNonce)](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint256-)
-   [\_useCheckedNonce(owner, key, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint192-uint64-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-)

### Errors

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-InvalidAccountNonce-address-uint256-)

nonces(address owner, uint192 key) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-nonces-address-uint192-)

Returns the next unused nonce for an address and key. Result contains the key prefix.

\_useNonce(address owner, uint192 key) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useNonce-address-uint192-)

Consumes the next unused nonce for an address and key.

Returns the current value without the key prefix. Consumed nonce is increased, so calling this function twice with the same arguments will return different (sequential) results.

\_useCheckedNonce(address owner, uint256 keyNonce)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint256-)

Same as [`Nonces._useNonce`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-) but checking that `nonce` is the next valid for `owner`.

This version takes the key and the nonce in a single uint256 parameter:

-   use the first 24 bytes for the key
-   use the last 8 bytes for the nonce

\_useCheckedNonce(address owner, uint192 key, uint64 nonce)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint192-uint64-)

Same as [`Nonces._useNonce`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-) but checking that `nonce` is the next valid for `owner`.

This version takes the key and the nonce as two different parameters.

## [`Packing`](https://docs.openzeppelin.com/contracts/5.x/api/utils#packing)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Packing.sol)

```
import "@openzeppelin/contracts/utils/Packing.sol";
```

Helper library packing and unpacking multiple values into bytesXX.

Example usage:

```
library MyPacker {
    type MyType is bytes32;

    function _pack(address account, bytes4 selector, uint64 period) external pure returns (MyType) {
        bytes12 subpack = Packing.pack_4_8(selector, bytes8(period));
        bytes32 pack = Packing.pack_20_12(bytes20(account), subpack);
        return MyType.wrap(pack);
    }

    function _unpack(MyType self) external pure returns (address, bytes4, uint64) {
        bytes32 pack = MyType.unwrap(self);
        return (
            address(Packing.extract_32_20(pack, 0)),
            Packing.extract_32_4(pack, 20),
            uint64(Packing.extract_32_8(pack, 24))
        );
    }
}
```

*Available since v5.1.*

### Functions

-   [pack\_1\_1(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_1_1-bytes1-bytes1-)
-   [pack\_2\_2(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_2-bytes2-bytes2-)
-   [pack\_2\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_4-bytes2-bytes4-)
-   [pack\_2\_6(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_6-bytes2-bytes6-)
-   [pack\_2\_8(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_8-bytes2-bytes8-)
-   [pack\_2\_10(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_10-bytes2-bytes10-)
-   [pack\_2\_20(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_20-bytes2-bytes20-)
-   [pack\_2\_22(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_22-bytes2-bytes22-)
-   [pack\_4\_2(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_2-bytes4-bytes2-)
-   [pack\_4\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_4-bytes4-bytes4-)
-   [pack\_4\_6(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_6-bytes4-bytes6-)
-   [pack\_4\_8(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_8-bytes4-bytes8-)
-   [pack\_4\_12(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_12-bytes4-bytes12-)
-   [pack\_4\_16(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_16-bytes4-bytes16-)
-   [pack\_4\_20(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_20-bytes4-bytes20-)
-   [pack\_4\_24(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_24-bytes4-bytes24-)
-   [pack\_4\_28(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_28-bytes4-bytes28-)
-   [pack\_6\_2(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_2-bytes6-bytes2-)
-   [pack\_6\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_4-bytes6-bytes4-)
-   [pack\_6\_6(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_6-bytes6-bytes6-)
-   [pack\_6\_10(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_10-bytes6-bytes10-)
-   [pack\_6\_16(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_16-bytes6-bytes16-)
-   [pack\_6\_22(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_22-bytes6-bytes22-)
-   [pack\_8\_2(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_2-bytes8-bytes2-)
-   [pack\_8\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_4-bytes8-bytes4-)
-   [pack\_8\_8(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_8-bytes8-bytes8-)
-   [pack\_8\_12(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_12-bytes8-bytes12-)
-   [pack\_8\_16(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_16-bytes8-bytes16-)
-   [pack\_8\_20(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_20-bytes8-bytes20-)
-   [pack\_8\_24(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_24-bytes8-bytes24-)
-   [pack\_10\_2(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_2-bytes10-bytes2-)
-   [pack\_10\_6(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_6-bytes10-bytes6-)
-   [pack\_10\_10(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_10-bytes10-bytes10-)
-   [pack\_10\_12(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_12-bytes10-bytes12-)
-   [pack\_10\_22(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_22-bytes10-bytes22-)
-   [pack\_12\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_4-bytes12-bytes4-)
-   [pack\_12\_8(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_8-bytes12-bytes8-)
-   [pack\_12\_10(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_10-bytes12-bytes10-)
-   [pack\_12\_12(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_12-bytes12-bytes12-)
-   [pack\_12\_16(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_16-bytes12-bytes16-)
-   [pack\_12\_20(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_20-bytes12-bytes20-)
-   [pack\_16\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_4-bytes16-bytes4-)
-   [pack\_16\_6(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_6-bytes16-bytes6-)
-   [pack\_16\_8(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_8-bytes16-bytes8-)
-   [pack\_16\_12(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_12-bytes16-bytes12-)
-   [pack\_16\_16(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_16-bytes16-bytes16-)
-   [pack\_20\_2(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_2-bytes20-bytes2-)
-   [pack\_20\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_4-bytes20-bytes4-)
-   [pack\_20\_8(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_8-bytes20-bytes8-)
-   [pack\_20\_12(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_12-bytes20-bytes12-)
-   [pack\_22\_2(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_2-bytes22-bytes2-)
-   [pack\_22\_6(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_6-bytes22-bytes6-)
-   [pack\_22\_10(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_10-bytes22-bytes10-)
-   [pack\_24\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_4-bytes24-bytes4-)
-   [pack\_24\_8(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_8-bytes24-bytes8-)
-   [pack\_28\_4(left, right)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_28_4-bytes28-bytes4-)
-   [extract\_2\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_2_1-bytes2-uint8-)
-   [replace\_2\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_2_1-bytes2-bytes1-uint8-)
-   [extract\_4\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_4_1-bytes4-uint8-)
-   [replace\_4\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_1-bytes4-bytes1-uint8-)
-   [extract\_4\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_4_2-bytes4-uint8-)
-   [replace\_4\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_2-bytes4-bytes2-uint8-)
-   [extract\_6\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_1-bytes6-uint8-)
-   [replace\_6\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_1-bytes6-bytes1-uint8-)
-   [extract\_6\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_2-bytes6-uint8-)
-   [replace\_6\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_2-bytes6-bytes2-uint8-)
-   [extract\_6\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_4-bytes6-uint8-)
-   [replace\_6\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_4-bytes6-bytes4-uint8-)
-   [extract\_8\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_1-bytes8-uint8-)
-   [replace\_8\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_1-bytes8-bytes1-uint8-)
-   [extract\_8\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_2-bytes8-uint8-)
-   [replace\_8\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_2-bytes8-bytes2-uint8-)
-   [extract\_8\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_4-bytes8-uint8-)
-   [replace\_8\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_4-bytes8-bytes4-uint8-)
-   [extract\_8\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_6-bytes8-uint8-)
-   [replace\_8\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_6-bytes8-bytes6-uint8-)
-   [extract\_10\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_1-bytes10-uint8-)
-   [replace\_10\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_1-bytes10-bytes1-uint8-)
-   [extract\_10\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_2-bytes10-uint8-)
-   [replace\_10\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_2-bytes10-bytes2-uint8-)
-   [extract\_10\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_4-bytes10-uint8-)
-   [replace\_10\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_4-bytes10-bytes4-uint8-)
-   [extract\_10\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_6-bytes10-uint8-)
-   [replace\_10\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_6-bytes10-bytes6-uint8-)
-   [extract\_10\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_8-bytes10-uint8-)
-   [replace\_10\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_8-bytes10-bytes8-uint8-)
-   [extract\_12\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_1-bytes12-uint8-)
-   [replace\_12\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_1-bytes12-bytes1-uint8-)
-   [extract\_12\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_2-bytes12-uint8-)
-   [replace\_12\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_2-bytes12-bytes2-uint8-)
-   [extract\_12\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_4-bytes12-uint8-)
-   [replace\_12\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_4-bytes12-bytes4-uint8-)
-   [extract\_12\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_6-bytes12-uint8-)
-   [replace\_12\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_6-bytes12-bytes6-uint8-)
-   [extract\_12\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_8-bytes12-uint8-)
-   [replace\_12\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_8-bytes12-bytes8-uint8-)
-   [extract\_12\_10(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_10-bytes12-uint8-)
-   [replace\_12\_10(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_10-bytes12-bytes10-uint8-)
-   [extract\_16\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_1-bytes16-uint8-)
-   [replace\_16\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_1-bytes16-bytes1-uint8-)
-   [extract\_16\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_2-bytes16-uint8-)
-   [replace\_16\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_2-bytes16-bytes2-uint8-)
-   [extract\_16\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_4-bytes16-uint8-)
-   [replace\_16\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_4-bytes16-bytes4-uint8-)
-   [extract\_16\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_6-bytes16-uint8-)
-   [replace\_16\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_6-bytes16-bytes6-uint8-)
-   [extract\_16\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_8-bytes16-uint8-)
-   [replace\_16\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_8-bytes16-bytes8-uint8-)
-   [extract\_16\_10(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_10-bytes16-uint8-)
-   [replace\_16\_10(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_10-bytes16-bytes10-uint8-)
-   [extract\_16\_12(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_12-bytes16-uint8-)
-   [replace\_16\_12(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_12-bytes16-bytes12-uint8-)
-   [extract\_20\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_1-bytes20-uint8-)
-   [replace\_20\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_1-bytes20-bytes1-uint8-)
-   [extract\_20\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_2-bytes20-uint8-)
-   [replace\_20\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_2-bytes20-bytes2-uint8-)
-   [extract\_20\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_4-bytes20-uint8-)
-   [replace\_20\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_4-bytes20-bytes4-uint8-)
-   [extract\_20\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_6-bytes20-uint8-)
-   [replace\_20\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_6-bytes20-bytes6-uint8-)
-   [extract\_20\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_8-bytes20-uint8-)
-   [replace\_20\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_8-bytes20-bytes8-uint8-)
-   [extract\_20\_10(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_10-bytes20-uint8-)
-   [replace\_20\_10(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_10-bytes20-bytes10-uint8-)
-   [extract\_20\_12(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_12-bytes20-uint8-)
-   [replace\_20\_12(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_12-bytes20-bytes12-uint8-)
-   [extract\_20\_16(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_16-bytes20-uint8-)
-   [replace\_20\_16(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_16-bytes20-bytes16-uint8-)
-   [extract\_22\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_1-bytes22-uint8-)
-   [replace\_22\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_1-bytes22-bytes1-uint8-)
-   [extract\_22\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_2-bytes22-uint8-)
-   [replace\_22\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_2-bytes22-bytes2-uint8-)
-   [extract\_22\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_4-bytes22-uint8-)
-   [replace\_22\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_4-bytes22-bytes4-uint8-)
-   [extract\_22\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_6-bytes22-uint8-)
-   [replace\_22\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_6-bytes22-bytes6-uint8-)
-   [extract\_22\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_8-bytes22-uint8-)
-   [replace\_22\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_8-bytes22-bytes8-uint8-)
-   [extract\_22\_10(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_10-bytes22-uint8-)
-   [replace\_22\_10(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_10-bytes22-bytes10-uint8-)
-   [extract\_22\_12(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_12-bytes22-uint8-)
-   [replace\_22\_12(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_12-bytes22-bytes12-uint8-)
-   [extract\_22\_16(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_16-bytes22-uint8-)
-   [replace\_22\_16(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_16-bytes22-bytes16-uint8-)
-   [extract\_22\_20(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_20-bytes22-uint8-)
-   [replace\_22\_20(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_20-bytes22-bytes20-uint8-)
-   [extract\_24\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_1-bytes24-uint8-)
-   [replace\_24\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_1-bytes24-bytes1-uint8-)
-   [extract\_24\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_2-bytes24-uint8-)
-   [replace\_24\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_2-bytes24-bytes2-uint8-)
-   [extract\_24\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_4-bytes24-uint8-)
-   [replace\_24\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_4-bytes24-bytes4-uint8-)
-   [extract\_24\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_6-bytes24-uint8-)
-   [replace\_24\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_6-bytes24-bytes6-uint8-)
-   [extract\_24\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_8-bytes24-uint8-)
-   [replace\_24\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_8-bytes24-bytes8-uint8-)
-   [extract\_24\_10(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_10-bytes24-uint8-)
-   [replace\_24\_10(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_10-bytes24-bytes10-uint8-)
-   [extract\_24\_12(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_12-bytes24-uint8-)
-   [replace\_24\_12(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_12-bytes24-bytes12-uint8-)
-   [extract\_24\_16(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_16-bytes24-uint8-)
-   [replace\_24\_16(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_16-bytes24-bytes16-uint8-)
-   [extract\_24\_20(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_20-bytes24-uint8-)
-   [replace\_24\_20(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_20-bytes24-bytes20-uint8-)
-   [extract\_24\_22(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_22-bytes24-uint8-)
-   [replace\_24\_22(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_22-bytes24-bytes22-uint8-)
-   [extract\_28\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_1-bytes28-uint8-)
-   [replace\_28\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_1-bytes28-bytes1-uint8-)
-   [extract\_28\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_2-bytes28-uint8-)
-   [replace\_28\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_2-bytes28-bytes2-uint8-)
-   [extract\_28\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_4-bytes28-uint8-)
-   [replace\_28\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_4-bytes28-bytes4-uint8-)
-   [extract\_28\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_6-bytes28-uint8-)
-   [replace\_28\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_6-bytes28-bytes6-uint8-)
-   [extract\_28\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_8-bytes28-uint8-)
-   [replace\_28\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_8-bytes28-bytes8-uint8-)
-   [extract\_28\_10(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_10-bytes28-uint8-)
-   [replace\_28\_10(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_10-bytes28-bytes10-uint8-)
-   [extract\_28\_12(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_12-bytes28-uint8-)
-   [replace\_28\_12(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_12-bytes28-bytes12-uint8-)
-   [extract\_28\_16(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_16-bytes28-uint8-)
-   [replace\_28\_16(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_16-bytes28-bytes16-uint8-)
-   [extract\_28\_20(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_20-bytes28-uint8-)
-   [replace\_28\_20(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_20-bytes28-bytes20-uint8-)
-   [extract\_28\_22(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_22-bytes28-uint8-)
-   [replace\_28\_22(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_22-bytes28-bytes22-uint8-)
-   [extract\_28\_24(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_24-bytes28-uint8-)
-   [replace\_28\_24(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_24-bytes28-bytes24-uint8-)
-   [extract\_32\_1(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_1-bytes32-uint8-)
-   [replace\_32\_1(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_1-bytes32-bytes1-uint8-)
-   [extract\_32\_2(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_2-bytes32-uint8-)
-   [replace\_32\_2(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_2-bytes32-bytes2-uint8-)
-   [extract\_32\_4(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_4-bytes32-uint8-)
-   [replace\_32\_4(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_4-bytes32-bytes4-uint8-)
-   [extract\_32\_6(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_6-bytes32-uint8-)
-   [replace\_32\_6(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_6-bytes32-bytes6-uint8-)
-   [extract\_32\_8(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_8-bytes32-uint8-)
-   [replace\_32\_8(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_8-bytes32-bytes8-uint8-)
-   [extract\_32\_10(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_10-bytes32-uint8-)
-   [replace\_32\_10(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_10-bytes32-bytes10-uint8-)
-   [extract\_32\_12(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_12-bytes32-uint8-)
-   [replace\_32\_12(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_12-bytes32-bytes12-uint8-)
-   [extract\_32\_16(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_16-bytes32-uint8-)
-   [replace\_32\_16(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_16-bytes32-bytes16-uint8-)
-   [extract\_32\_20(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_20-bytes32-uint8-)
-   [replace\_32\_20(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_20-bytes32-bytes20-uint8-)
-   [extract\_32\_22(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_22-bytes32-uint8-)
-   [replace\_32\_22(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_22-bytes32-bytes22-uint8-)
-   [extract\_32\_24(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_24-bytes32-uint8-)
-   [replace\_32\_24(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_24-bytes32-bytes24-uint8-)
-   [extract\_32\_28(self, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_28-bytes32-uint8-)
-   [replace\_32\_28(self, value, offset)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_28-bytes32-bytes28-uint8-)

### Errors

-   [OutOfRangeAccess()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-OutOfRangeAccess--)

pack\_1\_1(bytes1 left, bytes1 right) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_1_1-bytes1-bytes1-)

pack\_2\_2(bytes2 left, bytes2 right) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_2-bytes2-bytes2-)

pack\_2\_4(bytes2 left, bytes4 right) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_4-bytes2-bytes4-)

pack\_2\_6(bytes2 left, bytes6 right) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_6-bytes2-bytes6-)

pack\_2\_8(bytes2 left, bytes8 right) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_8-bytes2-bytes8-)

pack\_2\_10(bytes2 left, bytes10 right) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_10-bytes2-bytes10-)

pack\_2\_20(bytes2 left, bytes20 right) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_20-bytes2-bytes20-)

pack\_2\_22(bytes2 left, bytes22 right) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_22-bytes2-bytes22-)

pack\_4\_2(bytes4 left, bytes2 right) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_2-bytes4-bytes2-)

pack\_4\_4(bytes4 left, bytes4 right) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_4-bytes4-bytes4-)

pack\_4\_6(bytes4 left, bytes6 right) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_6-bytes4-bytes6-)

pack\_4\_8(bytes4 left, bytes8 right) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_8-bytes4-bytes8-)

pack\_4\_12(bytes4 left, bytes12 right) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_12-bytes4-bytes12-)

pack\_4\_16(bytes4 left, bytes16 right) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_16-bytes4-bytes16-)

pack\_4\_20(bytes4 left, bytes20 right) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_20-bytes4-bytes20-)

pack\_4\_24(bytes4 left, bytes24 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_24-bytes4-bytes24-)

pack\_4\_28(bytes4 left, bytes28 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_28-bytes4-bytes28-)

pack\_6\_2(bytes6 left, bytes2 right) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_2-bytes6-bytes2-)

pack\_6\_4(bytes6 left, bytes4 right) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_4-bytes6-bytes4-)

pack\_6\_6(bytes6 left, bytes6 right) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_6-bytes6-bytes6-)

pack\_6\_10(bytes6 left, bytes10 right) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_10-bytes6-bytes10-)

pack\_6\_16(bytes6 left, bytes16 right) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_16-bytes6-bytes16-)

pack\_6\_22(bytes6 left, bytes22 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_22-bytes6-bytes22-)

pack\_8\_2(bytes8 left, bytes2 right) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_2-bytes8-bytes2-)

pack\_8\_4(bytes8 left, bytes4 right) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_4-bytes8-bytes4-)

pack\_8\_8(bytes8 left, bytes8 right) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_8-bytes8-bytes8-)

pack\_8\_12(bytes8 left, bytes12 right) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_12-bytes8-bytes12-)

pack\_8\_16(bytes8 left, bytes16 right) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_16-bytes8-bytes16-)

pack\_8\_20(bytes8 left, bytes20 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_20-bytes8-bytes20-)

pack\_8\_24(bytes8 left, bytes24 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_24-bytes8-bytes24-)

pack\_10\_2(bytes10 left, bytes2 right) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_2-bytes10-bytes2-)

pack\_10\_6(bytes10 left, bytes6 right) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_6-bytes10-bytes6-)

pack\_10\_10(bytes10 left, bytes10 right) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_10-bytes10-bytes10-)

pack\_10\_12(bytes10 left, bytes12 right) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_12-bytes10-bytes12-)

pack\_10\_22(bytes10 left, bytes22 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_22-bytes10-bytes22-)

pack\_12\_4(bytes12 left, bytes4 right) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_4-bytes12-bytes4-)

pack\_12\_8(bytes12 left, bytes8 right) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_8-bytes12-bytes8-)

pack\_12\_10(bytes12 left, bytes10 right) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_10-bytes12-bytes10-)

pack\_12\_12(bytes12 left, bytes12 right) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_12-bytes12-bytes12-)

pack\_12\_16(bytes12 left, bytes16 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_16-bytes12-bytes16-)

pack\_12\_20(bytes12 left, bytes20 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_20-bytes12-bytes20-)

pack\_16\_4(bytes16 left, bytes4 right) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_4-bytes16-bytes4-)

pack\_16\_6(bytes16 left, bytes6 right) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_6-bytes16-bytes6-)

pack\_16\_8(bytes16 left, bytes8 right) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_8-bytes16-bytes8-)

pack\_16\_12(bytes16 left, bytes12 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_12-bytes16-bytes12-)

pack\_16\_16(bytes16 left, bytes16 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_16-bytes16-bytes16-)

pack\_20\_2(bytes20 left, bytes2 right) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_2-bytes20-bytes2-)

pack\_20\_4(bytes20 left, bytes4 right) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_4-bytes20-bytes4-)

pack\_20\_8(bytes20 left, bytes8 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_8-bytes20-bytes8-)

pack\_20\_12(bytes20 left, bytes12 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_12-bytes20-bytes12-)

pack\_22\_2(bytes22 left, bytes2 right) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_2-bytes22-bytes2-)

pack\_22\_6(bytes22 left, bytes6 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_6-bytes22-bytes6-)

pack\_22\_10(bytes22 left, bytes10 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_10-bytes22-bytes10-)

pack\_24\_4(bytes24 left, bytes4 right) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_4-bytes24-bytes4-)

pack\_24\_8(bytes24 left, bytes8 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_8-bytes24-bytes8-)

pack\_28\_4(bytes28 left, bytes4 right) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_28_4-bytes28-bytes4-)

extract\_2\_1(bytes2 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_2_1-bytes2-uint8-)

replace\_2\_1(bytes2 self, bytes1 value, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_2_1-bytes2-bytes1-uint8-)

extract\_4\_1(bytes4 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_4_1-bytes4-uint8-)

replace\_4\_1(bytes4 self, bytes1 value, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_1-bytes4-bytes1-uint8-)

extract\_4\_2(bytes4 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_4_2-bytes4-uint8-)

replace\_4\_2(bytes4 self, bytes2 value, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_2-bytes4-bytes2-uint8-)

extract\_6\_1(bytes6 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_1-bytes6-uint8-)

replace\_6\_1(bytes6 self, bytes1 value, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_1-bytes6-bytes1-uint8-)

extract\_6\_2(bytes6 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_2-bytes6-uint8-)

replace\_6\_2(bytes6 self, bytes2 value, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_2-bytes6-bytes2-uint8-)

extract\_6\_4(bytes6 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_4-bytes6-uint8-)

replace\_6\_4(bytes6 self, bytes4 value, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_4-bytes6-bytes4-uint8-)

extract\_8\_1(bytes8 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_1-bytes8-uint8-)

replace\_8\_1(bytes8 self, bytes1 value, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_1-bytes8-bytes1-uint8-)

extract\_8\_2(bytes8 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_2-bytes8-uint8-)

replace\_8\_2(bytes8 self, bytes2 value, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_2-bytes8-bytes2-uint8-)

extract\_8\_4(bytes8 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_4-bytes8-uint8-)

replace\_8\_4(bytes8 self, bytes4 value, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_4-bytes8-bytes4-uint8-)

extract\_8\_6(bytes8 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_6-bytes8-uint8-)

replace\_8\_6(bytes8 self, bytes6 value, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_6-bytes8-bytes6-uint8-)

extract\_10\_1(bytes10 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_1-bytes10-uint8-)

replace\_10\_1(bytes10 self, bytes1 value, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_1-bytes10-bytes1-uint8-)

extract\_10\_2(bytes10 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_2-bytes10-uint8-)

replace\_10\_2(bytes10 self, bytes2 value, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_2-bytes10-bytes2-uint8-)

extract\_10\_4(bytes10 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_4-bytes10-uint8-)

replace\_10\_4(bytes10 self, bytes4 value, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_4-bytes10-bytes4-uint8-)

extract\_10\_6(bytes10 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_6-bytes10-uint8-)

replace\_10\_6(bytes10 self, bytes6 value, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_6-bytes10-bytes6-uint8-)

extract\_10\_8(bytes10 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_8-bytes10-uint8-)

replace\_10\_8(bytes10 self, bytes8 value, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_8-bytes10-bytes8-uint8-)

extract\_12\_1(bytes12 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_1-bytes12-uint8-)

replace\_12\_1(bytes12 self, bytes1 value, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_1-bytes12-bytes1-uint8-)

extract\_12\_2(bytes12 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_2-bytes12-uint8-)

replace\_12\_2(bytes12 self, bytes2 value, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_2-bytes12-bytes2-uint8-)

extract\_12\_4(bytes12 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_4-bytes12-uint8-)

replace\_12\_4(bytes12 self, bytes4 value, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_4-bytes12-bytes4-uint8-)

extract\_12\_6(bytes12 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_6-bytes12-uint8-)

replace\_12\_6(bytes12 self, bytes6 value, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_6-bytes12-bytes6-uint8-)

extract\_12\_8(bytes12 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_8-bytes12-uint8-)

replace\_12\_8(bytes12 self, bytes8 value, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_8-bytes12-bytes8-uint8-)

extract\_12\_10(bytes12 self, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_10-bytes12-uint8-)

replace\_12\_10(bytes12 self, bytes10 value, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_10-bytes12-bytes10-uint8-)

extract\_16\_1(bytes16 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_1-bytes16-uint8-)

replace\_16\_1(bytes16 self, bytes1 value, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_1-bytes16-bytes1-uint8-)

extract\_16\_2(bytes16 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_2-bytes16-uint8-)

replace\_16\_2(bytes16 self, bytes2 value, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_2-bytes16-bytes2-uint8-)

extract\_16\_4(bytes16 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_4-bytes16-uint8-)

replace\_16\_4(bytes16 self, bytes4 value, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_4-bytes16-bytes4-uint8-)

extract\_16\_6(bytes16 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_6-bytes16-uint8-)

replace\_16\_6(bytes16 self, bytes6 value, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_6-bytes16-bytes6-uint8-)

extract\_16\_8(bytes16 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_8-bytes16-uint8-)

replace\_16\_8(bytes16 self, bytes8 value, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_8-bytes16-bytes8-uint8-)

extract\_16\_10(bytes16 self, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_10-bytes16-uint8-)

replace\_16\_10(bytes16 self, bytes10 value, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_10-bytes16-bytes10-uint8-)

extract\_16\_12(bytes16 self, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_12-bytes16-uint8-)

replace\_16\_12(bytes16 self, bytes12 value, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_12-bytes16-bytes12-uint8-)

extract\_20\_1(bytes20 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_1-bytes20-uint8-)

replace\_20\_1(bytes20 self, bytes1 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_1-bytes20-bytes1-uint8-)

extract\_20\_2(bytes20 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_2-bytes20-uint8-)

replace\_20\_2(bytes20 self, bytes2 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_2-bytes20-bytes2-uint8-)

extract\_20\_4(bytes20 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_4-bytes20-uint8-)

replace\_20\_4(bytes20 self, bytes4 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_4-bytes20-bytes4-uint8-)

extract\_20\_6(bytes20 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_6-bytes20-uint8-)

replace\_20\_6(bytes20 self, bytes6 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_6-bytes20-bytes6-uint8-)

extract\_20\_8(bytes20 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_8-bytes20-uint8-)

replace\_20\_8(bytes20 self, bytes8 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_8-bytes20-bytes8-uint8-)

extract\_20\_10(bytes20 self, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_10-bytes20-uint8-)

replace\_20\_10(bytes20 self, bytes10 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_10-bytes20-bytes10-uint8-)

extract\_20\_12(bytes20 self, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_12-bytes20-uint8-)

replace\_20\_12(bytes20 self, bytes12 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_12-bytes20-bytes12-uint8-)

extract\_20\_16(bytes20 self, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_16-bytes20-uint8-)

replace\_20\_16(bytes20 self, bytes16 value, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_16-bytes20-bytes16-uint8-)

extract\_22\_1(bytes22 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_1-bytes22-uint8-)

replace\_22\_1(bytes22 self, bytes1 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_1-bytes22-bytes1-uint8-)

extract\_22\_2(bytes22 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_2-bytes22-uint8-)

replace\_22\_2(bytes22 self, bytes2 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_2-bytes22-bytes2-uint8-)

extract\_22\_4(bytes22 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_4-bytes22-uint8-)

replace\_22\_4(bytes22 self, bytes4 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_4-bytes22-bytes4-uint8-)

extract\_22\_6(bytes22 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_6-bytes22-uint8-)

replace\_22\_6(bytes22 self, bytes6 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_6-bytes22-bytes6-uint8-)

extract\_22\_8(bytes22 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_8-bytes22-uint8-)

replace\_22\_8(bytes22 self, bytes8 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_8-bytes22-bytes8-uint8-)

extract\_22\_10(bytes22 self, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_10-bytes22-uint8-)

replace\_22\_10(bytes22 self, bytes10 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_10-bytes22-bytes10-uint8-)

extract\_22\_12(bytes22 self, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_12-bytes22-uint8-)

replace\_22\_12(bytes22 self, bytes12 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_12-bytes22-bytes12-uint8-)

extract\_22\_16(bytes22 self, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_16-bytes22-uint8-)

replace\_22\_16(bytes22 self, bytes16 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_16-bytes22-bytes16-uint8-)

extract\_22\_20(bytes22 self, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_20-bytes22-uint8-)

replace\_22\_20(bytes22 self, bytes20 value, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_20-bytes22-bytes20-uint8-)

extract\_24\_1(bytes24 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_1-bytes24-uint8-)

replace\_24\_1(bytes24 self, bytes1 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_1-bytes24-bytes1-uint8-)

extract\_24\_2(bytes24 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_2-bytes24-uint8-)

replace\_24\_2(bytes24 self, bytes2 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_2-bytes24-bytes2-uint8-)

extract\_24\_4(bytes24 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_4-bytes24-uint8-)

replace\_24\_4(bytes24 self, bytes4 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_4-bytes24-bytes4-uint8-)

extract\_24\_6(bytes24 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_6-bytes24-uint8-)

replace\_24\_6(bytes24 self, bytes6 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_6-bytes24-bytes6-uint8-)

extract\_24\_8(bytes24 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_8-bytes24-uint8-)

replace\_24\_8(bytes24 self, bytes8 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_8-bytes24-bytes8-uint8-)

extract\_24\_10(bytes24 self, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_10-bytes24-uint8-)

replace\_24\_10(bytes24 self, bytes10 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_10-bytes24-bytes10-uint8-)

extract\_24\_12(bytes24 self, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_12-bytes24-uint8-)

replace\_24\_12(bytes24 self, bytes12 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_12-bytes24-bytes12-uint8-)

extract\_24\_16(bytes24 self, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_16-bytes24-uint8-)

replace\_24\_16(bytes24 self, bytes16 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_16-bytes24-bytes16-uint8-)

extract\_24\_20(bytes24 self, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_20-bytes24-uint8-)

replace\_24\_20(bytes24 self, bytes20 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_20-bytes24-bytes20-uint8-)

extract\_24\_22(bytes24 self, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_22-bytes24-uint8-)

replace\_24\_22(bytes24 self, bytes22 value, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_22-bytes24-bytes22-uint8-)

extract\_28\_1(bytes28 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_1-bytes28-uint8-)

replace\_28\_1(bytes28 self, bytes1 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_1-bytes28-bytes1-uint8-)

extract\_28\_2(bytes28 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_2-bytes28-uint8-)

replace\_28\_2(bytes28 self, bytes2 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_2-bytes28-bytes2-uint8-)

extract\_28\_4(bytes28 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_4-bytes28-uint8-)

replace\_28\_4(bytes28 self, bytes4 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_4-bytes28-bytes4-uint8-)

extract\_28\_6(bytes28 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_6-bytes28-uint8-)

replace\_28\_6(bytes28 self, bytes6 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_6-bytes28-bytes6-uint8-)

extract\_28\_8(bytes28 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_8-bytes28-uint8-)

replace\_28\_8(bytes28 self, bytes8 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_8-bytes28-bytes8-uint8-)

extract\_28\_10(bytes28 self, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_10-bytes28-uint8-)

replace\_28\_10(bytes28 self, bytes10 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_10-bytes28-bytes10-uint8-)

extract\_28\_12(bytes28 self, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_12-bytes28-uint8-)

replace\_28\_12(bytes28 self, bytes12 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_12-bytes28-bytes12-uint8-)

extract\_28\_16(bytes28 self, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_16-bytes28-uint8-)

replace\_28\_16(bytes28 self, bytes16 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_16-bytes28-bytes16-uint8-)

extract\_28\_20(bytes28 self, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_20-bytes28-uint8-)

replace\_28\_20(bytes28 self, bytes20 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_20-bytes28-bytes20-uint8-)

extract\_28\_22(bytes28 self, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_22-bytes28-uint8-)

replace\_28\_22(bytes28 self, bytes22 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_22-bytes28-bytes22-uint8-)

extract\_28\_24(bytes28 self, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_24-bytes28-uint8-)

replace\_28\_24(bytes28 self, bytes24 value, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_24-bytes28-bytes24-uint8-)

extract\_32\_1(bytes32 self, uint8 offset) → bytes1 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_1-bytes32-uint8-)

replace\_32\_1(bytes32 self, bytes1 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_1-bytes32-bytes1-uint8-)

extract\_32\_2(bytes32 self, uint8 offset) → bytes2 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_2-bytes32-uint8-)

replace\_32\_2(bytes32 self, bytes2 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_2-bytes32-bytes2-uint8-)

extract\_32\_4(bytes32 self, uint8 offset) → bytes4 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_4-bytes32-uint8-)

replace\_32\_4(bytes32 self, bytes4 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_4-bytes32-bytes4-uint8-)

extract\_32\_6(bytes32 self, uint8 offset) → bytes6 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_6-bytes32-uint8-)

replace\_32\_6(bytes32 self, bytes6 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_6-bytes32-bytes6-uint8-)

extract\_32\_8(bytes32 self, uint8 offset) → bytes8 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_8-bytes32-uint8-)

replace\_32\_8(bytes32 self, bytes8 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_8-bytes32-bytes8-uint8-)

extract\_32\_10(bytes32 self, uint8 offset) → bytes10 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_10-bytes32-uint8-)

replace\_32\_10(bytes32 self, bytes10 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_10-bytes32-bytes10-uint8-)

extract\_32\_12(bytes32 self, uint8 offset) → bytes12 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_12-bytes32-uint8-)

replace\_32\_12(bytes32 self, bytes12 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_12-bytes32-bytes12-uint8-)

extract\_32\_16(bytes32 self, uint8 offset) → bytes16 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_16-bytes32-uint8-)

replace\_32\_16(bytes32 self, bytes16 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_16-bytes32-bytes16-uint8-)

extract\_32\_20(bytes32 self, uint8 offset) → bytes20 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_20-bytes32-uint8-)

replace\_32\_20(bytes32 self, bytes20 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_20-bytes32-bytes20-uint8-)

extract\_32\_22(bytes32 self, uint8 offset) → bytes22 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_22-bytes32-uint8-)

replace\_32\_22(bytes32 self, bytes22 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_22-bytes32-bytes22-uint8-)

extract\_32\_24(bytes32 self, uint8 offset) → bytes24 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_24-bytes32-uint8-)

replace\_32\_24(bytes32 self, bytes24 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_24-bytes32-bytes24-uint8-)

extract\_32\_28(bytes32 self, uint8 offset) → bytes28 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_28-bytes32-uint8-)

replace\_32\_28(bytes32 self, bytes28 value, uint8 offset) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_28-bytes32-bytes28-uint8-)

OutOfRangeAccess()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-OutOfRangeAccess--)

## [`Panic`](https://docs.openzeppelin.com/contracts/5.x/api/utils#panic)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Panic.sol)

```
import "@openzeppelin/contracts/utils/Panic.sol";
```

Helper library for emitting standardized panic codes.

```
contract Example {
     using Panic for uint256;

     // Use any of the declared internal constants
     function foo() { Panic.GENERIC.panic(); }

     // Alternatively
     function foo() { Panic.panic(Panic.GENERIC); }
}
```

Follows the list from [libsolutil](https://github.com/ethereum/solidity/blob/v0.8.24/libsolutil/ErrorCodes.h).

*Available since v5.1.*

### Functions

-   [panic(code)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-panic-uint256-)

panic(uint256 code)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-panic-uint256-)

Reverts with a panic code. Recommended to use with the internal constants with predefined codes.

## [`Pausable`](https://docs.openzeppelin.com/contracts/5.x/api/utils#pausable)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Pausable.sol)

```
import "@openzeppelin/contracts/utils/Pausable.sol";
```

Contract module which allows children to implement an emergency stop mechanism that can be triggered by an authorized account.

This module is used through inheritance. It will make available the modifiers `whenNotPaused` and `whenPaused`, which can be applied to the functions of your contract. Note that they will not be pausable by simply including this module, only once the modifiers are put in place.

### Modifiers

-   [whenNotPaused()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-whenNotPaused--)
-   [whenPaused()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-whenPaused--)

### Functions

-   [paused()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-paused--)
-   [\_requireNotPaused()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_requireNotPaused--)
-   [\_requirePaused()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_requirePaused--)
-   [\_pause()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_pause--)
-   [\_unpause()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_unpause--)

### Events

-   [Paused(account)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-Paused-address-)
-   [Unpaused(account)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-Unpaused-address-)

### Errors

-   [EnforcedPause()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-EnforcedPause--)
-   [ExpectedPause()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-ExpectedPause--)

whenNotPaused()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-whenNotPaused--)

Modifier to make a function callable only when the contract is not paused.

Requirements:

-   The contract must not be paused.

whenPaused()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-whenPaused--)

Modifier to make a function callable only when the contract is paused.

Requirements:

-   The contract must be paused.

paused() → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-paused--)

Returns true if the contract is paused, and false otherwise.

\_requireNotPaused()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_requireNotPaused--)

Throws if the contract is paused.

\_requirePaused()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_requirePaused--)

Throws if the contract is not paused.

\_pause()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_pause--)

Triggers stopped state.

Requirements:

-   The contract must not be paused.

\_unpause()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_unpause--)

Returns to normal state.

Requirements:

-   The contract must be paused.

Paused(address account)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-Paused-address-)

Emitted when the pause is triggered by `account`.

Unpaused(address account)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-Unpaused-address-)

Emitted when the pause is lifted by `account`.

EnforcedPause()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-EnforcedPause--)

The operation failed because the contract is paused.

ExpectedPause()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-ExpectedPause--)

The operation failed because the contract is not paused.

## [`RLP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#rlp)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/RLP.sol)

```
import "@openzeppelin/contracts/utils/RLP.sol";
```

Library for encoding and decoding data in RLP format. Recursive Length Prefix (RLP) is the main encoding method used to serialize objects in Ethereum. It's used for encoding everything from transactions to blocks to Patricia-Merkle tries.

Inspired by

-   [https://github.com/succinctlabs/optimism-bedrock-contracts/blob/main/rlp/RLPWriter.sol](https://github.com/succinctlabs/optimism-bedrock-contracts/blob/main/rlp/RLPWriter.sol)
-   [https://github.com/succinctlabs/optimism-bedrock-contracts/blob/main/rlp/RLPReader.sol](https://github.com/succinctlabs/optimism-bedrock-contracts/blob/main/rlp/RLPReader.sol)

## [Canonical vs Non-Canonical Encodings](https://docs.openzeppelin.com/contracts/5.x/api/utils#canonical-vs-non-canonical-encodings)

According to the Ethereum Yellow Paper, a "canonical" RLP encoding is the unique, minimal representation of a value. For scalar values (integers), this means:

-   No leading zero bytes (e.g., `0x0123` should be encoded as 2 bytes, not `0x000123` as 3 bytes)
-   Single bytes less than 0x80 must be encoded directly without a prefix wrapper
-   Zero is represented as an empty byte array (prefix `0x80`)

A "non-canonical" encoding represents the same value but doesn't follow these minimality rules. For example, encoding the integer 1234 (0x04d2) with a leading zero as `0x830004d2` instead of the canonical `0x8204d2`.

This implementation takes a permissive approach to decoding, accepting some non-canonical encodings (e.g., scalar values with leading zero bytes) that would be rejected by strict implementations like go-ethereum. This design choice prioritizes compatibility with diverse RLP encoders in the ecosystem over strict adherence to the Yellow Paper specification's canonicalization requirements.

Users should be aware that:

-   Multiple different RLP encodings may decode to the same value (non-injective)
-   Encoding followed by decoding is guaranteed to work correctly
-   External RLP data from untrusted sources may have non-canonical encodings
-   Improperly wrapped single bytes (< 0x80) are still rejected as invalid

### Functions

-   [encoder()](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encoder--)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bool-)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-address-)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-uint256-)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bytes32-)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bytes-)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-string-)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bytes---)
-   [push(self, input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-struct-RLP-Encoder-)
-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bool-)
-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-address-)
-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-uint256-)
-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bytes32-)
-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bytes-)
-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-string-)
-   [encode(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bytes---)
-   [encode(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-struct-RLP-Encoder-)
-   [readBool(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBool-Memory-Slice-)
-   [readAddress(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readAddress-Memory-Slice-)
-   [readUint256(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readUint256-Memory-Slice-)
-   [readBytes32(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBytes32-Memory-Slice-)
-   [readBytes(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBytes-Memory-Slice-)
-   [readString(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readString-Memory-Slice-)
-   [readList(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readList-Memory-Slice-)
-   [decodeBool(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeBool-bytes-)
-   [decodeAddress(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeAddress-bytes-)
-   [decodeUint256(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeUint256-bytes-)
-   [decodeBytes32(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeBytes32-bytes-)
-   [decodeBytes(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeBytes-bytes-)
-   [decodeString(item)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeString-bytes-)
-   [decodeList(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeList-bytes-)

### Errors

-   [RLPInvalidEncoding()](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-RLPInvalidEncoding--)

encoder() → struct RLP.Encoder enc

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encoder--)

Create an empty RLP Encoder.

push(struct RLP.Encoder self, bool input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bool-)

Add a boolean to a given RLP Encoder.

push(struct RLP.Encoder self, address input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-address-)

Add an address to a given RLP Encoder.

push(struct RLP.Encoder self, uint256 input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-uint256-)

Add a uint256 to a given RLP Encoder.

push(struct RLP.Encoder self, bytes32 input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bytes32-)

Add a bytes32 to a given RLP Encoder.

push(struct RLP.Encoder self, bytes input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bytes-)

Add a bytes buffer to a given RLP Encoder.

push(struct RLP.Encoder self, string input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-string-)

Add a string to a given RLP Encoder.

push(struct RLP.Encoder self, bytes\[\] input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-bytes---)

Add an array of bytes to a given RLP Encoder.

push(struct RLP.Encoder self, struct RLP.Encoder input) → struct RLP.Encoder

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-struct-RLP-Encoder-)

Add an (input) Encoder to a (target) Encoder. The input is RLP encoded as a list of bytes, and added to the target Encoder.

encode(bool input) → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bool-)

Encode a boolean as RLP.

Boolean `true` is encoded as 0x01, `false` as 0x80 (equivalent to encoding integers 1 and 0). This follows the de facto ecosystem standard where booleans are treated as 0/1 integers.

encode(address input) → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-address-)

Encode an address as an RLP item of fixed size (20 bytes).

The address is encoded with its leading zeros (if it has any). If someone wants to encode the address as a scalar, they can cast it to an uint256 and then call the corresponding [`Base58.encode`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-encode-bytes-) function.

encode(uint256 input) → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-uint256-)

Encode an uint256 as an RLP scalar.

Unlike `encode-bytes32-`, this function uses scalar encoding that removes the prefix zeros.

encode(bytes32 input) → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bytes32-)

Encode a bytes32 as an RLP item of fixed size (32 bytes).

Unlike `encode-uint256-`, this function uses array encoding that preserves the prefix zeros.

encode(bytes input) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bytes-)

Encode a bytes buffer as RLP.

encode(string input) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-string-)

Encode a string as RLP. Type alias for `encode-bytes-`.

encode(bytes\[\] input) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-bytes---)

Encode an array of bytes as RLP. This function expects an array of already encoded bytes, not raw bytes. Users should call [`Base58.encode`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base58-encode-bytes-) on each element of the array before calling it.

encode(struct RLP.Encoder self) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-encode-struct-RLP-Encoder-)

Encode an encoder (list of bytes) as RLP

readBool(Memory.Slice item) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBool-Memory-Slice-)

Decode an RLP encoded bool. See `encode-bool`

This function treats any non-zero value as `true`, which is more permissive than some implementations (e.g., go-ethereum only accepts `0x00` for false and `0x01` for true). For example, `0x02`, `0x03`, etc. will all decode as `true`.

readAddress(Memory.Slice item) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readAddress-Memory-Slice-)

Decode an RLP encoded address. See `encode-address`

This function accepts both single-byte encodings (for values 0-127, including precompile addresses like 0x01) and the standard 21-byte encoding with the `0x94` prefix. For example, `0x01` decodes to `0x0000000000000000000000000000000000000001`.

Additionally, like [`RLP.readUint256`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readUint256-Memory-Slice-), this function accepts non-canonical encodings with leading zeros. For instance, both `0x01` and `0x940000000000000000000000000000000000000001` decode to the same address.

readUint256(Memory.Slice item) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readUint256-Memory-Slice-)

Decode an RLP encoded uint256. See `encode-uint256`

This function accepts non-canonical encodings with leading zero bytes for multi-byte values, which differs from the Ethereum Yellow Paper specification and some reference implementations like go-ethereum. For example, both `0x88ab54a98ceb1f0ad2` and `0x8900ab54a98ceb1f0ad2` will decode to the same uint256 value (12345678901234567890).

However, single bytes less than 0x80 must NOT be wrapped with a prefix. For example, `0x8100` is invalid (should be `0x00`), but `0x820000` is valid (two zero bytes).

This permissive behavior is intentional for compatibility with various RLP encoders in the ecosystem, but users should be aware that multiple RLP encodings may map to the same decoded value (non-injective decoding).

readBytes32(Memory.Slice item) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBytes32-Memory-Slice-)

Decode an RLP encoded bytes32. See `encode-bytes32`

Since this function delegates to [`RLP.readUint256`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readUint256-Memory-Slice-), it inherits the non-canonical encoding acceptance behavior for multi-byte values. Multiple RLP encodings with different leading zero bytes may decode to the same bytes32 value, but single bytes < 0x80 must not be wrapped with a prefix (e.g., `0x820000` is valid, but `0x8100` is not).

readBytes(Memory.Slice item) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBytes-Memory-Slice-)

Decodes an RLP encoded bytes. See `encode-bytes`

readString(Memory.Slice item) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readString-Memory-Slice-)

Decodes an RLP encoded string. See `encode-string`

readList(Memory.Slice item) → Memory.Slice\[\] list

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readList-Memory-Slice-)

Decodes an RLP encoded list in a memory slice into an array of RLP Items.

The returned array contains slice references into the original payload, not copied bytes. Any further modification of the input buffer may cause the output result to become invalid.

decodeBool(bytes item) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeBool-bytes-)

Decode an RLP encoded bool from bytes. See [`RLP.readBool`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBool-Memory-Slice-)

decodeAddress(bytes item) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeAddress-bytes-)

Decode an RLP encoded address from bytes. See [`RLP.readAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readAddress-Memory-Slice-)

decodeUint256(bytes item) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeUint256-bytes-)

Decode an RLP encoded uint256 from bytes. See [`RLP.readUint256`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readUint256-Memory-Slice-)

decodeBytes32(bytes item) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeBytes32-bytes-)

Decode an RLP encoded bytes32 from bytes. See [`RLP.readBytes32`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBytes32-Memory-Slice-)

decodeBytes(bytes item) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeBytes-bytes-)

Decode an RLP encoded bytes from bytes. See [`RLP.readBytes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readBytes-Memory-Slice-)

decodeString(bytes item) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeString-bytes-)

Decode an RLP encoded string from bytes. See [`RLP.readString`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readString-Memory-Slice-)

decodeList(bytes value) → Memory.Slice\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-decodeList-bytes-)

Decode an RLP encoded list from bytes. See [`RLP.readList`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-readList-Memory-Slice-)

The returned array contains slice references into the original payload, not copied bytes. Any further modification of the input buffer may cause the output result to become invalid.

RLPInvalidEncoding()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-RLPInvalidEncoding--)

The item is not properly formatted and cannot be decoded.

## [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#reentrancyguard)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/ReentrancyGuard.sol)

```
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
```

Contract module that helps prevent reentrant calls to a function.

Inheriting from `ReentrancyGuard` will make the [`ReentrancyGuard.nonReentrant`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--) modifier available, which can be applied to functions to make sure there are no nested (reentrant) calls to them.

Note that because there is a single `nonReentrant` guard, functions marked as `nonReentrant` may not call one another. This can be worked around by making those functions `private`, and then adding `external` `nonReentrant` entry points to them.

If EIP-1153 (transient storage) is available on the chain you're deploying at, consider using [`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient) instead.

If you would like to learn more about reentrancy and alternative ways to protect against it, check out our blog post [Reentrancy After Istanbul](https://blog.openzeppelin.com/reentrancy-after-istanbul/).

Deprecated. This storage-based reentrancy guard will be removed and replaced by the [`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient) variant in v6.0.

@custom:stateless

### Modifiers

-   [nonReentrant()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--)
-   [nonReentrantView()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrantView--)

### Functions

-   [constructor()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-constructor--)
-   [\_reentrancyGuardEntered()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-_reentrancyGuardEntered--)
-   [\_reentrancyGuardStorageSlot()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-_reentrancyGuardStorageSlot--)

### Errors

-   [ReentrancyGuardReentrantCall()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-ReentrancyGuardReentrantCall--)

nonReentrant()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--)

Prevents a contract from calling itself, directly or indirectly. Calling a `nonReentrant` function from another `nonReentrant` function is not supported. It is possible to prevent this from happening by making the `nonReentrant` function external, and making it call a `private` function that does the actual work.

nonReentrantView()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrantView--)

A `view` only version of [`ReentrancyGuard.nonReentrant`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--). Use to block view functions from being called, preventing reading from inconsistent contract state.

This is a "view" modifier and does not change the reentrancy status. Use it only on view functions. For payable or non-payable functions, use the standard [`ReentrancyGuard.nonReentrant`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--) modifier instead.

constructor()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-constructor--)

\_reentrancyGuardEntered() → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-_reentrancyGuardEntered--)

Returns true if the reentrancy guard is currently set to "entered", which indicates there is a `nonReentrant` function in the call stack.

\_reentrancyGuardStorageSlot() → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-_reentrancyGuardStorageSlot--)

ReentrancyGuardReentrantCall()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-ReentrancyGuardReentrantCall--)

Unauthorized reentrant call.

## [`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#reentrancyguardtransient)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/ReentrancyGuardTransient.sol)

```
import "@openzeppelin/contracts/utils/ReentrancyGuardTransient.sol";
```

Variant of [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard) that uses transient storage.

This variant only works on networks where EIP-1153 is available.

*Available since v5.1.*

@custom:stateless

### Modifiers

-   [nonReentrant()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-nonReentrant--)
-   [nonReentrantView()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-nonReentrantView--)

### Functions

-   [\_reentrancyGuardEntered()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-_reentrancyGuardEntered--)
-   [\_reentrancyGuardStorageSlot()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-_reentrancyGuardStorageSlot--)

### Errors

-   [ReentrancyGuardReentrantCall()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-ReentrancyGuardReentrantCall--)

nonReentrant()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-nonReentrant--)

Prevents a contract from calling itself, directly or indirectly. Calling a `nonReentrant` function from another `nonReentrant` function is not supported. It is possible to prevent this from happening by making the `nonReentrant` function external, and making it call a `private` function that does the actual work.

nonReentrantView()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-nonReentrantView--)

A `view` only version of [`ReentrancyGuard.nonReentrant`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--). Use to block view functions from being called, preventing reading from inconsistent contract state.

This is a "view" modifier and does not change the reentrancy status. Use it only on view functions. For payable or non-payable functions, use the standard [`ReentrancyGuard.nonReentrant`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--) modifier instead.

\_reentrancyGuardEntered() → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-_reentrancyGuardEntered--)

Returns true if the reentrancy guard is currently set to "entered", which indicates there is a `nonReentrant` function in the call stack.

\_reentrancyGuardStorageSlot() → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-_reentrancyGuardStorageSlot--)

ReentrancyGuardReentrantCall()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-ReentrancyGuardReentrantCall--)

Unauthorized reentrant call.

## [`RelayedCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#relayedcall)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/RelayedCall.sol)

```
import "@openzeppelin/contracts/utils/RelayedCall.sol";
```

Library for performing external calls through dynamically deployed relay contracts that hide the original caller's address from the target contract. This pattern is used in ERC-4337's EntryPoint for account factory calls and ERC-6942 for safe factory interactions.

When privileged contracts need to make arbitrary external calls based on user input, calling the target directly can be risky because the target sees the privileged contract as `msg.sender` and could exploit this trust relationship. This library solves this by deploying minimal relay contracts that act as intermediaries, ensuring the target only sees the unprivileged relay address as `msg.sender`.

For example, instead of `target.call(data)` where the target sees this contract as `msg.sender`, use [`RelayedCall.relayCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-bytes32-) where the target sees a relay address as `msg.sender`.

This library uses the PUSH0 opcode that was introduced in the Shanghai hardfork. While this instruction is now widely supported, developers using the library on exotic chains should verify that their target chain has supports for EIP-3855.

### Functions

-   [relayCall(target, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-bytes-)
-   [relayCall(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-)
-   [relayCall(target, data, salt)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-bytes-bytes32-)
-   [relayCall(target, value, data, salt)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-bytes32-)
-   [getRelayer()](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-getRelayer--)
-   [getRelayer(salt)](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-getRelayer-bytes32-)

relayCall(address target, bytes data) → bool, bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-bytes-)

Relays a call to the target contract through a dynamically deployed relay contract.

relayCall(address target, uint256 value, bytes data) → bool, bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-)

Same as [`RelayedCall.relayCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-bytes32-) but with a value.

relayCall(address target, bytes data, bytes32 salt) → bool, bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-bytes-bytes32-)

Same as [`RelayedCall.relayCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-bytes32-) but with a salt.

relayCall(address target, uint256 value, bytes data, bytes32 salt) → bool, bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-bytes32-)

Same as [`RelayedCall.relayCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-relayCall-address-uint256-bytes-bytes32-) but with a salt and a value.

getRelayer() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-getRelayer--)

Same as [`RelayedCall.getRelayer`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-getRelayer-bytes32-) but with a `bytes32(0)` default salt.

getRelayer(bytes32 salt) → address relayer

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#RelayedCall-getRelayer-bytes32-)

Returns the relayer address for a given salt.

## [`ShortString`](https://docs.openzeppelin.com/contracts/5.x/api/utils#shortstring)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/ShortStrings.sol)

```
import "@openzeppelin/contracts/utils/ShortStrings.sol";
```

## [`ShortStrings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#shortstrings)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/ShortStrings.sol)

```
import "@openzeppelin/contracts/utils/ShortStrings.sol";
```

This library provides functions to convert short memory strings into a `ShortString` type that can be used as an immutable variable.

Strings of arbitrary length can be optimized using this library if they are short enough (up to 31 bytes) by packing them with their length (1 byte) in a single EVM word (32 bytes). Additionally, a fallback mechanism can be used for every other case.

Usage example:

```
contract Named {
    using ShortStrings for *;

    ShortString private immutable _name;
    string private _nameFallback;

    constructor(string memory contractName) {
        _name = contractName.toShortStringWithFallback(_nameFallback);
    }

    function name() external view returns (string memory) {
        return _name.toStringWithFallback(_nameFallback);
    }
}
```

### Functions

-   [toShortString(str)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortString-string-)
-   [toString(sstr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toString-ShortString-)
-   [byteLength(sstr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLength-ShortString-)
-   [toShortStringWithFallback(value, store)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-)
-   [toStringWithFallback(value, store)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toStringWithFallback-ShortString-string-)
-   [byteLengthWithFallback(value, store)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLengthWithFallback-ShortString-string-)

### Errors

-   [StringTooLong(str)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-StringTooLong-string-)
-   [InvalidShortString()](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-InvalidShortString--)

toShortString(string str) → ShortString

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortString-string-)

Encode a string of at most 31 chars into a `ShortString`.

This will trigger a `StringTooLong` error is the input string is too long.

toString(ShortString sstr) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toString-ShortString-)

Decode a `ShortString` back to a "normal" string.

byteLength(ShortString sstr) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLength-ShortString-)

Return the length of a `ShortString`.

toShortStringWithFallback(string value, string store) → ShortString

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-)

Encode a string into a `ShortString`, or write it to storage if it is too long.

toStringWithFallback(ShortString value, string store) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toStringWithFallback-ShortString-string-)

Decode a string that was encoded to `ShortString` or written to storage using [`ShortStrings.toShortStringWithFallback`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-).

byteLengthWithFallback(ShortString value, string store) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLengthWithFallback-ShortString-string-)

Return the length of a string that was encoded to `ShortString` or written to storage using [`ShortStrings.toShortStringWithFallback`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-).

This will return the "byte length" of the string. This may not reflect the actual length in terms of actual characters as the UTF-8 encoding of a single character can span over multiple bytes.

StringTooLong(string str)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-StringTooLong-string-)

InvalidShortString()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-InvalidShortString--)

## [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#slotderivation)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/SlotDerivation.sol)

```
import "@openzeppelin/contracts/utils/SlotDerivation.sol";
```

Library for computing storage (and transient storage) locations from namespaces and deriving slots corresponding to standard patterns. The derivation method for array and mapping matches the storage layout used by the solidity language / compiler.

See [Solidity docs for mappings and dynamic arrays.](https://docs.soliditylang.org/en/v0.8.20/internals/layout_in_storage.html#mappings-and-dynamic-arrays).

Example usage:

```
contract Example {
    // Add the library methods
    using StorageSlot for bytes32;
    using SlotDerivation for *;

    // Declare a namespace
    string private constant _NAMESPACE = "<namespace>"; // eg. OpenZeppelin.Slot

    function setValueInNamespace(uint256 key, address newValue) internal {
        _NAMESPACE.erc7201Slot().deriveMapping(key).getAddressSlot().value = newValue;
    }

    function getValueInNamespace(uint256 key) internal view returns (address) {
        return _NAMESPACE.erc7201Slot().deriveMapping(key).getAddressSlot().value;
    }
}
```

Consider using this library along with [`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot).

This library provides a way to manipulate storage locations in a non-standard way. Tooling for checking upgrade safety will ignore the slots accessed through this library.

*Available since v5.1.*

### Functions

-   [erc7201Slot(namespace)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-erc7201Slot-string-)
-   [offset(slot, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-offset-bytes32-uint256-)
-   [deriveArray(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveArray-bytes32-)
-   [deriveMapping(slot, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-address-)
-   [deriveMapping(slot, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bool-)
-   [deriveMapping(slot, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes32-)
-   [deriveMapping(slot, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-uint256-)
-   [deriveMapping(slot, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-int256-)
-   [deriveMapping(slot, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-string-)
-   [deriveMapping(slot, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes-)

erc7201Slot(string namespace) → bytes32 slot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-erc7201Slot-string-)

Derive an ERC-7201 slot from a string (namespace).

offset(bytes32 slot, uint256 pos) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-offset-bytes32-uint256-)

Add an offset to a slot to get the n-th element of a structure or an array.

deriveArray(bytes32 slot) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveArray-bytes32-)

Derive the location of the first element in an array from the slot where the length is stored.

deriveMapping(bytes32 slot, address key) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-address-)

Derive the location of a mapping element from the key.

deriveMapping(bytes32 slot, bool key) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bool-)

Derive the location of a mapping element from the key.

deriveMapping(bytes32 slot, bytes32 key) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes32-)

Derive the location of a mapping element from the key.

deriveMapping(bytes32 slot, uint256 key) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-uint256-)

Derive the location of a mapping element from the key.

deriveMapping(bytes32 slot, int256 key) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-int256-)

Derive the location of a mapping element from the key.

deriveMapping(bytes32 slot, string key) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-string-)

Derive the location of a mapping element from the key.

deriveMapping(bytes32 slot, bytes key) → bytes32 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes-)

Derive the location of a mapping element from the key.

## [`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#storageslot)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/StorageSlot.sol)

```
import "@openzeppelin/contracts/utils/StorageSlot.sol";
```

Library for reading and writing primitive types to specific storage slots.

Storage slots are often used to avoid storage conflict when dealing with upgradeable contracts. This library helps with reading and writing to such slots without the need for inline assembly.

The functions in this library return Slot structs that contain a `value` member that can be used to read or write.

Example usage to set ERC-1967 implementation slot:

```
contract ERC1967 {
    // Define the slot. Alternatively, use the SlotDerivation library to derive the slot.
    bytes32 internal constant _IMPLEMENTATION_SLOT = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc;

    function _getImplementation() internal view returns (address) {
        return StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value;
    }

    function _setImplementation(address newImplementation) internal {
        require(newImplementation.code.length > 0);
        StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value = newImplementation;
    }
}
```

Consider using this library along with [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation).

### Functions

-   [getAddressSlot(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getAddressSlot-bytes32-)
-   [getBooleanSlot(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBooleanSlot-bytes32-)
-   [getBytes32Slot(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytes32Slot-bytes32-)
-   [getUint256Slot(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getUint256Slot-bytes32-)
-   [getInt256Slot(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getInt256Slot-bytes32-)
-   [getStringSlot(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-bytes32-)
-   [getStringSlot(store)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-string-)
-   [getBytesSlot(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes32-)
-   [getBytesSlot(store)](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes-)

getAddressSlot(bytes32 slot) → struct StorageSlot.AddressSlot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getAddressSlot-bytes32-)

Returns an `AddressSlot` with member `value` located at `slot`.

getBooleanSlot(bytes32 slot) → struct StorageSlot.BooleanSlot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBooleanSlot-bytes32-)

Returns a `BooleanSlot` with member `value` located at `slot`.

getBytes32Slot(bytes32 slot) → struct StorageSlot.Bytes32Slot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytes32Slot-bytes32-)

Returns a `Bytes32Slot` with member `value` located at `slot`.

getUint256Slot(bytes32 slot) → struct StorageSlot.Uint256Slot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getUint256Slot-bytes32-)

Returns a `Uint256Slot` with member `value` located at `slot`.

getInt256Slot(bytes32 slot) → struct StorageSlot.Int256Slot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getInt256Slot-bytes32-)

Returns a `Int256Slot` with member `value` located at `slot`.

getStringSlot(bytes32 slot) → struct StorageSlot.StringSlot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-bytes32-)

Returns a `StringSlot` with member `value` located at `slot`.

getStringSlot(string store) → struct StorageSlot.StringSlot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-string-)

Returns an `StringSlot` representation of the string storage pointer `store`.

getBytesSlot(bytes32 slot) → struct StorageSlot.BytesSlot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes32-)

Returns a `BytesSlot` with member `value` located at `slot`.

getBytesSlot(bytes store) → struct StorageSlot.BytesSlot r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes-)

Returns an `BytesSlot` representation of the bytes storage pointer `store`.

## [`Strings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#strings)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/Strings.sol)

```
import "@openzeppelin/contracts/utils/Strings.sol";
```

String operations.

### Functions

-   [toString(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toString-uint256-)
-   [toStringSigned(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toStringSigned-int256-)
-   [toHexString(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-)
-   [toHexString(value, length)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-uint256-)
-   [toHexString(addr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-address-)
-   [toChecksumHexString(addr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toChecksumHexString-address-)
-   [toHexString(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-bytes-)
-   [equal(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-equal-string-string-)
-   [parseUint(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-)
-   [parseUint(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-uint256-uint256-)
-   [tryParseUint(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-)
-   [tryParseUint(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-uint256-uint256-)
-   [parseInt(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-)
-   [parseInt(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-uint256-uint256-)
-   [tryParseInt(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-)
-   [tryParseInt(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-uint256-uint256-)
-   [parseHexUint(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-)
-   [parseHexUint(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-uint256-uint256-)
-   [tryParseHexUint(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-)
-   [tryParseHexUint(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-uint256-uint256-)
-   [parseAddress(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-)
-   [parseAddress(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-uint256-uint256-)
-   [tryParseAddress(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-)
-   [tryParseAddress(input, begin, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-uint256-uint256-)
-   [escapeJSON(input)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-escapeJSON-string-)

### Errors

-   [StringsInsufficientHexLength(value, length)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInsufficientHexLength-uint256-uint256-)
-   [StringsInvalidChar()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidChar--)
-   [StringsInvalidAddressFormat()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidAddressFormat--)

toString(uint256 value) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toString-uint256-)

Converts a `uint256` to its ASCII `string` decimal representation.

toStringSigned(int256 value) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toStringSigned-int256-)

Converts a `int256` to its ASCII `string` decimal representation.

toHexString(uint256 value) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-)

Converts a `uint256` to its ASCII `string` hexadecimal representation.

toHexString(uint256 value, uint256 length) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-uint256-)

Converts a `uint256` to its ASCII `string` hexadecimal representation with fixed length.

toHexString(address addr) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-address-)

Converts an `address` with fixed length of 20 bytes to its not checksummed ASCII `string` hexadecimal representation.

toChecksumHexString(address addr) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toChecksumHexString-address-)

Converts an `address` with fixed length of 20 bytes to its checksummed ASCII `string` hexadecimal representation, according to EIP-55.

toHexString(bytes input) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-bytes-)

Converts a `bytes` buffer to its ASCII `string` hexadecimal representation.

equal(string a, string b) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-equal-string-string-)

Returns true if the two strings are equal.

parseUint(string input) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-)

Parse a decimal string and returns the value as a `uint256`.

Requirements:

-   The string must be formatted as `[0-9]*`
-   The result must fit into an `uint256` type

parseUint(string input, uint256 begin, uint256 end) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-uint256-uint256-)

Variant of `parseUint-string` that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements:

-   The substring must be formatted as `[0-9]*`
-   The result must fit into an `uint256` type

tryParseUint(string input) → bool success, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-)

Variant of `parseUint-string` that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

tryParseUint(string input, uint256 begin, uint256 end) → bool success, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-uint256-uint256-)

Variant of `parseUint-string-uint256-uint256` that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

parseInt(string input) → int256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-)

Parse a decimal string and returns the value as a `int256`.

Requirements:

-   The string must be formatted as `[-+]?[0-9]*`
-   The result must fit in an `int256` type.

parseInt(string input, uint256 begin, uint256 end) → int256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-uint256-uint256-)

Variant of `parseInt-string` that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements:

-   The substring must be formatted as `[-+]?[0-9]*`
-   The result must fit in an `int256` type.

tryParseInt(string input) → bool success, int256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-)

Variant of `parseInt-string` that returns false if the parsing fails because of an invalid character or if the result does not fit in a `int256`.

This function will revert if the absolute value of the result does not fit in a `uint256`.

tryParseInt(string input, uint256 begin, uint256 end) → bool success, int256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-uint256-uint256-)

Variant of `parseInt-string-uint256-uint256` that returns false if the parsing fails because of an invalid character or if the result does not fit in a `int256`.

This function will revert if the absolute value of the result does not fit in a `uint256`.

parseHexUint(string input) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-)

Parse a hexadecimal string (with or without "0x" prefix), and returns the value as a `uint256`.

Requirements:

-   The string must be formatted as `(0x)?[0-9a-fA-F]*`
-   The result must fit in an `uint256` type.

parseHexUint(string input, uint256 begin, uint256 end) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-uint256-uint256-)

Variant of `parseHexUint-string` that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements:

-   The substring must be formatted as `(0x)?[0-9a-fA-F]*`
-   The result must fit in an `uint256` type.

tryParseHexUint(string input) → bool success, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-)

Variant of `parseHexUint-string` that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

tryParseHexUint(string input, uint256 begin, uint256 end) → bool success, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-uint256-uint256-)

Variant of `parseHexUint-string-uint256-uint256` that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

parseAddress(string input) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-)

Parse a hexadecimal string (with or without "0x" prefix), and returns the value as an `address`.

Requirements:

-   The string must be formatted as `(0x)?[0-9a-fA-F]`40\`\`

parseAddress(string input, uint256 begin, uint256 end) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-uint256-uint256-)

Variant of `parseAddress-string` that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements:

-   The substring must be formatted as `(0x)?[0-9a-fA-F]`40\`\`

tryParseAddress(string input) → bool success, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-)

Variant of `parseAddress-string` that returns false if the parsing fails because the input is not a properly formatted address. See `parseAddress-string` requirements.

tryParseAddress(string input, uint256 begin, uint256 end) → bool success, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-uint256-uint256-)

Variant of `parseAddress-string-uint256-uint256` that returns false if the parsing fails because input is not a properly formatted address. See `parseAddress-string-uint256-uint256` requirements.

escapeJSON(string input) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-escapeJSON-string-)

Escape special characters in JSON strings. This can be useful to prevent JSON injection in NFT metadata.

This function should only be used in double quoted JSON strings. Single quotes are not escaped.

This function escapes backslashes (including those in \\uXXXX sequences) and the characters in ranges defined in section 2.5 of RFC-4627 (U+0000 to U+001F, U+0022 and U+005C). All control characters in U+0000 to U+001F are escaped (\\b, \\t, \\n, \\f, \\r use short form; others use \\u00XX). ECMAScript's `JSON.parse` does recover escaped unicode characters that are not in this range, but other tooling may provide different results.

StringsInsufficientHexLength(uint256 value, uint256 length)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInsufficientHexLength-uint256-uint256-)

The `value` string doesn't fit in the specified `length`.

StringsInvalidChar()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidChar--)

The string being parsed contains characters that are not in scope of the given base.

StringsInvalidAddressFormat()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidAddressFormat--)

The string being parsed is not a properly formatted address.

## [`TransientSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#transientslot)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/TransientSlot.sol)

```
import "@openzeppelin/contracts/utils/TransientSlot.sol";
```

Library for reading and writing value-types to specific transient storage slots.

Transient slots are often used to store temporary values that are removed after the current transaction. This library helps with reading and writing to such slots without the need for inline assembly.

-   Example reading and writing values using transient storage:

```
contract Lock {
    using TransientSlot for *;

    // Define the slot. Alternatively, use the SlotDerivation library to derive the slot.
    bytes32 internal constant _LOCK_SLOT = 0xf4678858b2b588224636b8522b729e7722d32fc491da849ed75b3fdf3c84f542;

    modifier locked() {
        require(!_LOCK_SLOT.asBoolean().tload());

        _LOCK_SLOT.asBoolean().tstore(true);
        _;
        _LOCK_SLOT.asBoolean().tstore(false);
    }
}
```

Consider using this library along with [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation).

### Functions

-   [asAddress(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asAddress-bytes32-)
-   [asBoolean(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBoolean-bytes32-)
-   [asBytes32(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBytes32-bytes32-)
-   [asUint256(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asUint256-bytes32-)
-   [asInt256(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asInt256-bytes32-)
-   [tload(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-AddressSlot-)
-   [tstore(slot, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-AddressSlot-address-)
-   [tload(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-BooleanSlot-)
-   [tstore(slot, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-BooleanSlot-bool-)
-   [tload(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Bytes32Slot-)
-   [tstore(slot, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Bytes32Slot-bytes32-)
-   [tload(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Uint256Slot-)
-   [tstore(slot, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Uint256Slot-uint256-)
-   [tload(slot)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Int256Slot-)
-   [tstore(slot, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Int256Slot-int256-)

asAddress(bytes32 slot) → TransientSlot.AddressSlot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asAddress-bytes32-)

Cast an arbitrary slot to a AddressSlot.

asBoolean(bytes32 slot) → TransientSlot.BooleanSlot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBoolean-bytes32-)

Cast an arbitrary slot to a BooleanSlot.

asBytes32(bytes32 slot) → TransientSlot.Bytes32Slot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBytes32-bytes32-)

Cast an arbitrary slot to a Bytes32Slot.

asUint256(bytes32 slot) → TransientSlot.Uint256Slot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asUint256-bytes32-)

Cast an arbitrary slot to a Uint256Slot.

asInt256(bytes32 slot) → TransientSlot.Int256Slot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asInt256-bytes32-)

Cast an arbitrary slot to a Int256Slot.

tload(TransientSlot.AddressSlot slot) → address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-AddressSlot-)

Load the value held at location `slot` in transient storage.

tstore(TransientSlot.AddressSlot slot, address value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-AddressSlot-address-)

Store `value` at location `slot` in transient storage.

tload(TransientSlot.BooleanSlot slot) → bool value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-BooleanSlot-)

Load the value held at location `slot` in transient storage.

tstore(TransientSlot.BooleanSlot slot, bool value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-BooleanSlot-bool-)

Store `value` at location `slot` in transient storage.

tload(TransientSlot.Bytes32Slot slot) → bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Bytes32Slot-)

Load the value held at location `slot` in transient storage.

tstore(TransientSlot.Bytes32Slot slot, bytes32 value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Bytes32Slot-bytes32-)

Store `value` at location `slot` in transient storage.

tload(TransientSlot.Uint256Slot slot) → uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Uint256Slot-)

Load the value held at location `slot` in transient storage.

tstore(TransientSlot.Uint256Slot slot, uint256 value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Uint256Slot-uint256-)

Store `value` at location `slot` in transient storage.

tload(TransientSlot.Int256Slot slot) → int256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Int256Slot-)

Load the value held at location `slot` in transient storage.

tstore(TransientSlot.Int256Slot slot, int256 value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Int256Slot-int256-)

Store `value` at location `slot` in transient storage.

## [`InteroperableAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#interoperableaddress)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/draft-InteroperableAddress.sol)

```
import "@openzeppelin/contracts/utils/draft-InteroperableAddress.sol";
```

Helper library to format and parse [ERC-7930](https://ethereum-magicians.org/t/erc-7930-interoperable-addresses/23365) interoperable addresses.

### Functions

-   [formatV1(chainType, chainReference, addr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatV1-bytes2-bytes-bytes-)
-   [formatEvmV1(chainid, addr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatEvmV1-uint256-address-)
-   [formatEvmV1(chainid)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatEvmV1-uint256-)
-   [formatEvmV1(addr)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatEvmV1-address-)
-   [parseV1(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseV1-bytes-)
-   [parseV1Calldata(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseV1Calldata-bytes-)
-   [tryParseV1(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseV1-bytes-)
-   [tryParseV1Calldata(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseV1Calldata-bytes-)
-   [parseEvmV1(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseEvmV1-bytes-)
-   [parseEvmV1Calldata(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseEvmV1Calldata-bytes-)
-   [tryParseEvmV1(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseEvmV1-bytes-)
-   [tryParseEvmV1Calldata(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseEvmV1Calldata-bytes-)

### Errors

-   [InteroperableAddressParsingError()](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-InteroperableAddressParsingError-bytes-)
-   [InteroperableAddressEmptyReferenceAndAddress()](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-InteroperableAddressEmptyReferenceAndAddress--)

formatV1(bytes2 chainType, bytes chainReference, bytes addr) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatV1-bytes2-bytes-bytes-)

Format an ERC-7930 interoperable address (version 1) from its components `chainType`, `chainReference` and `addr`. This is a generic function that supports any chain type, chain reference and address supported by ERC-7930, including interoperable addresses with empty chain reference or empty address.

formatEvmV1(uint256 chainid, address addr) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatEvmV1-uint256-address-)

Variant of `formatV1-bytes2-bytes-bytes-` specific to EVM chains. Returns the ERC-7930 interoperable address (version 1) for a given chainid and ethereum address.

formatEvmV1(uint256 chainid) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatEvmV1-uint256-)

Variant of `formatV1-bytes2-bytes-bytes-` that specifies an EVM chain without an address.

formatEvmV1(address addr) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-formatEvmV1-address-)

Variant of `formatV1-bytes2-bytes-bytes-` that specifies an EVM address without a chain reference.

parseV1(bytes self) → bytes2 chainType, bytes chainReference, bytes addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseV1-bytes-)

Parse a ERC-7930 interoperable address (version 1) into its different components. Reverts if the input is not following a version 1 of ERC-7930.

Trailing bytes after a valid v1 encoding are ignored. The same decoded address may therefore correspond to multiple distinct input byte strings.

parseV1Calldata(bytes self) → bytes2 chainType, bytes chainReference, bytes addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseV1Calldata-bytes-)

Variant of [`InteroperableAddress.parseV1`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseV1-bytes-) that handles calldata slices to reduce memory copy costs.

tryParseV1(bytes self) → bool success, bytes2 chainType, bytes chainReference, bytes addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseV1-bytes-)

Variant of [`InteroperableAddress.parseV1`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseV1-bytes-) that does not revert on invalid input. Instead, it returns `false` as the first return value to indicate parsing failure when the input does not follow version 1 of ERC-7930.

tryParseV1Calldata(bytes self) → bool success, bytes2 chainType, bytes chainReference, bytes addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseV1Calldata-bytes-)

Variant of [`InteroperableAddress.tryParseV1`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseV1-bytes-) that handles calldata slices to reduce memory copy costs.

parseEvmV1(bytes self) → uint256 chainId, address addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseEvmV1-bytes-)

Parse a ERC-7930 interoperable address (version 1) corresponding to an EIP-155 chain. The `chainId` and `addr` return values will be zero if the input doesn't include a chainReference or an address, respectively.

Trailing bytes after a valid v1 encoding are ignored. The same decoded (chainId, addr) may therefore correspond to multiple distinct input byte strings.

Requirements:

-   The input must be a valid ERC-7930 interoperable address (version 1)
-   The underlying chainType must be "eip-155"

parseEvmV1Calldata(bytes self) → uint256 chainId, address addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseEvmV1Calldata-bytes-)

Variant of [`InteroperableAddress.parseEvmV1`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseEvmV1-bytes-) that handles calldata slices to reduce memory copy costs.

tryParseEvmV1(bytes self) → bool success, uint256 chainId, address addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseEvmV1-bytes-)

Variant of [`InteroperableAddress.parseEvmV1`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-parseEvmV1-bytes-) that does not revert on invalid input. Instead, it returns `false` as the first return value to indicate parsing failure when the input does not follow version 1 of ERC-7930.

tryParseEvmV1Calldata(bytes self) → bool success, uint256 chainId, address addr

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseEvmV1Calldata-bytes-)

Variant of [`InteroperableAddress.tryParseEvmV1`](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-tryParseEvmV1-bytes-) that handles calldata slices to reduce memory copy costs.

InteroperableAddressParsingError(bytes)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-InteroperableAddressParsingError-bytes-)

InteroperableAddressEmptyReferenceAndAddress()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#InteroperableAddress-InteroperableAddressEmptyReferenceAndAddress--)

## [`ERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#erc165)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/introspection/ERC165.sol)

```
import "@openzeppelin/contracts/utils/introspection/ERC165.sol";
```

Implementation of the [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) interface.

Contracts that want to implement ERC-165 should inherit from this contract and override [`ERC165.supportsInterface`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165-supportsInterface-bytes4-) to check for the additional interface id that will be supported. For example:

```
function supportsInterface(bytes4 interfaceId) public view virtual override returns (bool) {
    return interfaceId == type(MyInterface).interfaceId || super.supportsInterface(interfaceId);
}
```

### Functions

-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165-supportsInterface-bytes4-)

supportsInterface(bytes4 interfaceId) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165-supportsInterface-bytes4-)

Returns true if this contract implements the interface defined by `interfaceId`. See the corresponding [ERC section](https://eips.ethereum.org/EIPS/eip-165#how-interfaces-are-identified) to learn more about how these ids are created.

This function call must use less than 30 000 gas.

## [`ERC165Checker`](https://docs.openzeppelin.com/contracts/5.x/api/utils#erc165checker)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/introspection/ERC165Checker.sol)

```
import "@openzeppelin/contracts/utils/introspection/ERC165Checker.sol";
```

Library used to query support of an interface declared via [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165).

Note that these functions return the actual result of the query: they do not `revert` if an interface is not supported. It is up to the caller to decide what to do in these cases.

### Functions

-   [supportsERC165(account)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165-address-)
-   [supportsInterface(account, interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsInterface-address-bytes4-)
-   [getSupportedInterfaces(account, interfaceIds)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-getSupportedInterfaces-address-bytes4---)
-   [supportsAllInterfaces(account, interfaceIds)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsAllInterfaces-address-bytes4---)
-   [supportsERC165InterfaceUnchecked(account, interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165InterfaceUnchecked-address-bytes4-)

supportsERC165(address account) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165-address-)

Returns true if `account` supports the [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) interface.

supportsInterface(address account, bytes4 interfaceId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsInterface-address-bytes4-)

Returns true if `account` supports the interface defined by `interfaceId`. Support for [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) itself is queried automatically.

See [`IERC165.supportsInterface`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165-supportsInterface-bytes4-).

getSupportedInterfaces(address account, bytes4\[\] interfaceIds) → bool\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-getSupportedInterfaces-address-bytes4---)

Returns a boolean array where each value corresponds to the interfaces passed in and whether they're supported or not. This allows you to batch check interfaces for a contract where your expectation is that some interfaces may not be supported.

See [`IERC165.supportsInterface`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165-supportsInterface-bytes4-).

supportsAllInterfaces(address account, bytes4\[\] interfaceIds) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsAllInterfaces-address-bytes4---)

Returns true if `account` supports all the interfaces defined in `interfaceIds`. Support for [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) itself is queried automatically.

Batch-querying can lead to gas savings by skipping repeated checks for [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) support.

See [`IERC165.supportsInterface`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165-supportsInterface-bytes4-).

supportsERC165InterfaceUnchecked(address account, bytes4 interfaceId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165InterfaceUnchecked-address-bytes4-)

Assumes that account contains a contract that supports ERC-165, otherwise the behavior of this method is undefined. This precondition can be checked with [`ERC165Checker.supportsERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165-address-).

Some precompiled contracts will falsely indicate support for a given interface, so caution should be exercised when using this function.

Interface identification is specified in ERC-165.

## [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ierc165)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/introspection/IERC165.sol)

```
import "@openzeppelin/contracts/utils/introspection/IERC165.sol";
```

Interface of the ERC-165 standard, as defined in the [ERC](https://eips.ethereum.org/EIPS/eip-165).

Implementers can declare support of contract interfaces, which can then be queried by others ([`ERC165Checker`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker)).

For an implementation, see [`ERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165).

### Functions

-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165-supportsInterface-bytes4-)

supportsInterface(bytes4 interfaceId) → bool

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165-supportsInterface-bytes4-)

Returns true if this contract implements the interface defined by `interfaceId`. See the corresponding [ERC section](https://eips.ethereum.org/EIPS/eip-165#how-interfaces-are-identified) to learn more about how these ids are created.

This function call must use less than 30 000 gas.

## [`Math`](https://docs.openzeppelin.com/contracts/5.x/api/utils#math-1)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/math/Math.sol)

```
import "@openzeppelin/contracts/utils/math/Math.sol";
```

Standard math utilities missing in the Solidity language.

### Functions

-   [add512(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-add512-uint256-uint256-)
-   [mul512(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mul512-uint256-uint256-)
-   [tryAdd(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryAdd-uint256-uint256-)
-   [trySub(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-trySub-uint256-uint256-)
-   [tryMul(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMul-uint256-uint256-)
-   [tryDiv(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryDiv-uint256-uint256-)
-   [tryMod(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMod-uint256-uint256-)
-   [saturatingAdd(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingAdd-uint256-uint256-)
-   [saturatingSub(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingSub-uint256-uint256-)
-   [saturatingMul(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingMul-uint256-uint256-)
-   [ternary(condition, a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ternary-bool-uint256-uint256-)
-   [max(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-max-uint256-uint256-)
-   [min(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-min-uint256-uint256-)
-   [average(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-average-uint256-uint256-)
-   [ceilDiv(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ceilDiv-uint256-uint256-)
-   [mulDiv(x, y, denominator)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-)
-   [mulDiv(x, y, denominator, rounding)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-enum-Math-Rounding-)
-   [mulShr(x, y, n)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-)
-   [mulShr(x, y, n, rounding)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-enum-Math-Rounding-)
-   [invMod(a, n)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invMod-uint256-uint256-)
-   [invModPrime(a, p)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invModPrime-uint256-uint256-)
-   [modExp(b, e, m)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-uint256-uint256-uint256-)
-   [tryModExp(b, e, m)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-uint256-uint256-uint256-)
-   [modExp(b, e, m)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-bytes-bytes-bytes-)
-   [tryModExp(b, e, m)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-bytes-bytes-bytes-)
-   [sqrt(a)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-)
-   [sqrt(a, rounding)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-enum-Math-Rounding-)
-   [log2(x)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-)
-   [log2(value, rounding)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-enum-Math-Rounding-)
-   [log10(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-)
-   [log10(value, rounding)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-enum-Math-Rounding-)
-   [log256(x)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-)
-   [log256(value, rounding)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-enum-Math-Rounding-)
-   [unsignedRoundsUp(rounding)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-unsignedRoundsUp-enum-Math-Rounding-)
-   [clz(x)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-clz-uint256-)

add512(uint256 a, uint256 b) → uint256 high, uint256 low

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-add512-uint256-uint256-)

Return the 512-bit addition of two uint256.

The result is stored in two 256 variables such that sum = high \* 2²⁵⁶ + low.

mul512(uint256 a, uint256 b) → uint256 high, uint256 low

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mul512-uint256-uint256-)

Return the 512-bit multiplication of two uint256.

The result is stored in two 256 variables such that product = high \* 2²⁵⁶ + low.

tryAdd(uint256 a, uint256 b) → bool success, uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryAdd-uint256-uint256-)

Returns the addition of two unsigned integers, with a success flag (no overflow).

trySub(uint256 a, uint256 b) → bool success, uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-trySub-uint256-uint256-)

Returns the subtraction of two unsigned integers, with a success flag (no overflow).

tryMul(uint256 a, uint256 b) → bool success, uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMul-uint256-uint256-)

Returns the multiplication of two unsigned integers, with a success flag (no overflow).

tryDiv(uint256 a, uint256 b) → bool success, uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryDiv-uint256-uint256-)

Returns the division of two unsigned integers, with a success flag (no division by zero).

tryMod(uint256 a, uint256 b) → bool success, uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMod-uint256-uint256-)

Returns the remainder of dividing two unsigned integers, with a success flag (no division by zero).

saturatingAdd(uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingAdd-uint256-uint256-)

Unsigned saturating addition, bounds to `2²⁵⁶ - 1` instead of overflowing.

saturatingSub(uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingSub-uint256-uint256-)

Unsigned saturating subtraction, bounds to zero instead of overflowing.

saturatingMul(uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingMul-uint256-uint256-)

Unsigned saturating multiplication, bounds to `2²⁵⁶ - 1` instead of overflowing.

ternary(bool condition, uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ternary-bool-uint256-uint256-)

Branchless ternary evaluation for `condition ? a : b`. Gas costs are constant.

This function may reduce bytecode size and consume less gas when used standalone. However, the compiler may optimize Solidity ternary operations (i.e. `condition ? a : b`) to only compute one branch when needed, making this function more expensive.

max(uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-max-uint256-uint256-)

Returns the largest of two numbers.

min(uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-min-uint256-uint256-)

Returns the smallest of two numbers.

average(uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-average-uint256-uint256-)

Returns the average of two numbers. The result is rounded towards zero.

ceilDiv(uint256 a, uint256 b) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ceilDiv-uint256-uint256-)

Returns the ceiling of the division of two numbers.

This differs from standard division with `/` in that it rounds towards infinity instead of rounding towards zero.

mulDiv(uint256 x, uint256 y, uint256 denominator) → uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-)

Calculates floor(x \* y / denominator) with full precision. Throws if result overflows a uint256 or denominator == 0.

Original credit to Remco Bloemen under MIT license ([https://xn--2-umb.com/21/muldiv](https://xn--2-umb.com/21/muldiv)) with further edits by Uniswap Labs also under MIT license.

mulDiv(uint256 x, uint256 y, uint256 denominator, enum Math.Rounding rounding) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-enum-Math-Rounding-)

Calculates x \* y / denominator with full precision, following the selected rounding direction.

mulShr(uint256 x, uint256 y, uint8 n) → uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-)

Calculates floor(x \* y >> n) with full precision. Throws if result overflows a uint256.

mulShr(uint256 x, uint256 y, uint8 n, enum Math.Rounding rounding) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-enum-Math-Rounding-)

Calculates x \* y >> n with full precision, following the selected rounding direction.

invMod(uint256 a, uint256 n) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invMod-uint256-uint256-)

Calculate the modular multiplicative inverse of a number in Z/nZ.

If n is a prime, then Z/nZ is a field. In that case all elements are inversible, except 0. If n is not a prime, then Z/nZ is not a field, and some elements might not be inversible.

If the input value is not inversible, 0 is returned.

If you know for sure that n is (big) a prime, it may be cheaper to use Fermat's little theorem and get the inverse using `Math.modExp(a, n - 2, n)`. See [`Math.invModPrime`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invModPrime-uint256-uint256-).

invModPrime(uint256 a, uint256 p) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invModPrime-uint256-uint256-)

Variant of [`Math.invMod`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invMod-uint256-uint256-). More efficient, but only works if `p` is known to be a prime greater than `2`.

From [Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem), we know that if p is prime, then `a**(p-1) ≡ 1 mod p`. As a consequence, we have `a * a**(p-2) ≡ 1 mod p`, which means that `a**(p-2)` is the modular multiplicative inverse of a in Fp.

this function does NOT check that `p` is a prime greater than `2`.

modExp(uint256 b, uint256 e, uint256 m) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-uint256-uint256-uint256-)

Returns the modular exponentiation of the specified base, exponent and modulus (b \*\* e % m)

Requirements:

-   modulus can't be zero
-   underlying staticcall to precompile must succeed

The result is only valid if the underlying call succeeds. When using this function, make sure the chain you're using it on supports the precompiled contract for modular exponentiation at address 0x05 as specified in [EIP-198](https://eips.ethereum.org/EIPS/eip-198). Otherwise, the underlying function will succeed given the lack of a revert, but the result may be incorrectly interpreted as 0.

tryModExp(uint256 b, uint256 e, uint256 m) → bool success, uint256 result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-uint256-uint256-uint256-)

Returns the modular exponentiation of the specified base, exponent and modulus (b \*\* e % m). It includes a success flag indicating if the operation succeeded. Operation will be marked as failed if trying to operate modulo 0 or if the underlying precompile reverted.

The result is only valid if the success flag is true. When using this function, make sure the chain you're using it on supports the precompiled contract for modular exponentiation at address 0x05 as specified in [EIP-198](https://eips.ethereum.org/EIPS/eip-198). Otherwise, the underlying function will succeed given the lack of a revert, but the result may be incorrectly interpreted as 0.

modExp(bytes b, bytes e, bytes m) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-bytes-bytes-bytes-)

Variant of [`Math.modExp`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-bytes-bytes-bytes-) that supports inputs of arbitrary length.

tryModExp(bytes b, bytes e, bytes m) → bool success, bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-bytes-bytes-bytes-)

Variant of [`Math.tryModExp`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-bytes-bytes-bytes-) that supports inputs of arbitrary length.

sqrt(uint256 a) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-)

Returns the square root of a number. If the number is not a perfect square, the value is rounded towards zero.

This method is based on Newton's method for computing square roots; the algorithm is restricted to only using integer operations.

sqrt(uint256 a, enum Math.Rounding rounding) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-enum-Math-Rounding-)

Calculates sqrt(a), following the selected rounding direction.

log2(uint256 x) → uint256 r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-)

Return the log in base 2 of a positive value rounded towards zero. Returns 0 if given 0.

log2(uint256 value, enum Math.Rounding rounding) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-enum-Math-Rounding-)

Return the log in base 2, following the selected rounding direction, of a positive value. Returns 0 if given 0.

log10(uint256 value) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-)

Return the log in base 10 of a positive value rounded towards zero. Returns 0 if given 0.

log10(uint256 value, enum Math.Rounding rounding) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-enum-Math-Rounding-)

Return the log in base 10, following the selected rounding direction, of a positive value. Returns 0 if given 0.

log256(uint256 x) → uint256 r

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-)

Return the log in base 256 of a positive value rounded towards zero. Returns 0 if given 0.

Adding one to the result gives the number of pairs of hex symbols needed to represent `value` as a hex string.

log256(uint256 value, enum Math.Rounding rounding) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-enum-Math-Rounding-)

Return the log in base 256, following the selected rounding direction, of a positive value. Returns 0 if given 0.

unsignedRoundsUp(enum Math.Rounding rounding) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-unsignedRoundsUp-enum-Math-Rounding-)

Returns whether a provided rounding mode is considered rounding up for unsigned integers.

clz(uint256 x) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-clz-uint256-)

Counts the number of leading zero bits in a uint256.

## [`SafeCast`](https://docs.openzeppelin.com/contracts/5.x/api/utils#safecast)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/math/SafeCast.sol)

```
import "@openzeppelin/contracts/utils/math/SafeCast.sol";
```

Wrappers over Solidity's uintXX/intXX/bool casting operators with added overflow checks.

Downcasting from uint256/int256 in Solidity does not revert on overflow. This can easily result in undesired exploitation or bugs, since developers usually assume that overflows raise errors. `SafeCast` restores this intuition by reverting the transaction when such an operation overflows.

Using this library instead of the unchecked operations eliminates an entire class of bugs, so it's recommended to use it always.

### Functions

-   [toUint248(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint248-uint256-)
-   [toUint240(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint240-uint256-)
-   [toUint232(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint232-uint256-)
-   [toUint224(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint224-uint256-)
-   [toUint216(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint216-uint256-)
-   [toUint208(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint208-uint256-)
-   [toUint200(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint200-uint256-)
-   [toUint192(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint192-uint256-)
-   [toUint184(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint184-uint256-)
-   [toUint176(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint176-uint256-)
-   [toUint168(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint168-uint256-)
-   [toUint160(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint160-uint256-)
-   [toUint152(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint152-uint256-)
-   [toUint144(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint144-uint256-)
-   [toUint136(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint136-uint256-)
-   [toUint128(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint128-uint256-)
-   [toUint120(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint120-uint256-)
-   [toUint112(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint112-uint256-)
-   [toUint104(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint104-uint256-)
-   [toUint96(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint96-uint256-)
-   [toUint88(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint88-uint256-)
-   [toUint80(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint80-uint256-)
-   [toUint72(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint72-uint256-)
-   [toUint64(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint64-uint256-)
-   [toUint56(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint56-uint256-)
-   [toUint48(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint48-uint256-)
-   [toUint40(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint40-uint256-)
-   [toUint32(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint32-uint256-)
-   [toUint24(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint24-uint256-)
-   [toUint16(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint16-uint256-)
-   [toUint8(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint8-uint256-)
-   [toUint256(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint256-int256-)
-   [toInt248(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt248-int256-)
-   [toInt240(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt240-int256-)
-   [toInt232(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt232-int256-)
-   [toInt224(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt224-int256-)
-   [toInt216(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt216-int256-)
-   [toInt208(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt208-int256-)
-   [toInt200(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt200-int256-)
-   [toInt192(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt192-int256-)
-   [toInt184(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt184-int256-)
-   [toInt176(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt176-int256-)
-   [toInt168(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt168-int256-)
-   [toInt160(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt160-int256-)
-   [toInt152(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt152-int256-)
-   [toInt144(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt144-int256-)
-   [toInt136(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt136-int256-)
-   [toInt128(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt128-int256-)
-   [toInt120(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt120-int256-)
-   [toInt112(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt112-int256-)
-   [toInt104(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt104-int256-)
-   [toInt96(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt96-int256-)
-   [toInt88(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt88-int256-)
-   [toInt80(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt80-int256-)
-   [toInt72(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt72-int256-)
-   [toInt64(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt64-int256-)
-   [toInt56(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt56-int256-)
-   [toInt48(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt48-int256-)
-   [toInt40(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt40-int256-)
-   [toInt32(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt32-int256-)
-   [toInt24(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt24-int256-)
-   [toInt16(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt16-int256-)
-   [toInt8(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt8-int256-)
-   [toInt256(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt256-uint256-)
-   [toUint(b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint-bool-)

### Errors

-   [SafeCastOverflowedUintDowncast(bits, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintDowncast-uint8-uint256-)
-   [SafeCastOverflowedIntToUint(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntToUint-int256-)
-   [SafeCastOverflowedIntDowncast(bits, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntDowncast-uint8-int256-)
-   [SafeCastOverflowedUintToInt(value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintToInt-uint256-)

toUint248(uint256 value) → uint248

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint248-uint256-)

Returns the downcasted uint248 from uint256, reverting on overflow (when the input is greater than largest uint248).

Counterpart to Solidity's `uint248` operator.

Requirements:

-   input must fit into 248 bits

toUint240(uint256 value) → uint240

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint240-uint256-)

Returns the downcasted uint240 from uint256, reverting on overflow (when the input is greater than largest uint240).

Counterpart to Solidity's `uint240` operator.

Requirements:

-   input must fit into 240 bits

toUint232(uint256 value) → uint232

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint232-uint256-)

Returns the downcasted uint232 from uint256, reverting on overflow (when the input is greater than largest uint232).

Counterpart to Solidity's `uint232` operator.

Requirements:

-   input must fit into 232 bits

toUint224(uint256 value) → uint224

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint224-uint256-)

Returns the downcasted uint224 from uint256, reverting on overflow (when the input is greater than largest uint224).

Counterpart to Solidity's `uint224` operator.

Requirements:

-   input must fit into 224 bits

toUint216(uint256 value) → uint216

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint216-uint256-)

Returns the downcasted uint216 from uint256, reverting on overflow (when the input is greater than largest uint216).

Counterpart to Solidity's `uint216` operator.

Requirements:

-   input must fit into 216 bits

toUint208(uint256 value) → uint208

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint208-uint256-)

Returns the downcasted uint208 from uint256, reverting on overflow (when the input is greater than largest uint208).

Counterpart to Solidity's `uint208` operator.

Requirements:

-   input must fit into 208 bits

toUint200(uint256 value) → uint200

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint200-uint256-)

Returns the downcasted uint200 from uint256, reverting on overflow (when the input is greater than largest uint200).

Counterpart to Solidity's `uint200` operator.

Requirements:

-   input must fit into 200 bits

toUint192(uint256 value) → uint192

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint192-uint256-)

Returns the downcasted uint192 from uint256, reverting on overflow (when the input is greater than largest uint192).

Counterpart to Solidity's `uint192` operator.

Requirements:

-   input must fit into 192 bits

toUint184(uint256 value) → uint184

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint184-uint256-)

Returns the downcasted uint184 from uint256, reverting on overflow (when the input is greater than largest uint184).

Counterpart to Solidity's `uint184` operator.

Requirements:

-   input must fit into 184 bits

toUint176(uint256 value) → uint176

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint176-uint256-)

Returns the downcasted uint176 from uint256, reverting on overflow (when the input is greater than largest uint176).

Counterpart to Solidity's `uint176` operator.

Requirements:

-   input must fit into 176 bits

toUint168(uint256 value) → uint168

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint168-uint256-)

Returns the downcasted uint168 from uint256, reverting on overflow (when the input is greater than largest uint168).

Counterpart to Solidity's `uint168` operator.

Requirements:

-   input must fit into 168 bits

toUint160(uint256 value) → uint160

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint160-uint256-)

Returns the downcasted uint160 from uint256, reverting on overflow (when the input is greater than largest uint160).

Counterpart to Solidity's `uint160` operator.

Requirements:

-   input must fit into 160 bits

toUint152(uint256 value) → uint152

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint152-uint256-)

Returns the downcasted uint152 from uint256, reverting on overflow (when the input is greater than largest uint152).

Counterpart to Solidity's `uint152` operator.

Requirements:

-   input must fit into 152 bits

toUint144(uint256 value) → uint144

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint144-uint256-)

Returns the downcasted uint144 from uint256, reverting on overflow (when the input is greater than largest uint144).

Counterpart to Solidity's `uint144` operator.

Requirements:

-   input must fit into 144 bits

toUint136(uint256 value) → uint136

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint136-uint256-)

Returns the downcasted uint136 from uint256, reverting on overflow (when the input is greater than largest uint136).

Counterpart to Solidity's `uint136` operator.

Requirements:

-   input must fit into 136 bits

toUint128(uint256 value) → uint128

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint128-uint256-)

Returns the downcasted uint128 from uint256, reverting on overflow (when the input is greater than largest uint128).

Counterpart to Solidity's `uint128` operator.

Requirements:

-   input must fit into 128 bits

toUint120(uint256 value) → uint120

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint120-uint256-)

Returns the downcasted uint120 from uint256, reverting on overflow (when the input is greater than largest uint120).

Counterpart to Solidity's `uint120` operator.

Requirements:

-   input must fit into 120 bits

toUint112(uint256 value) → uint112

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint112-uint256-)

Returns the downcasted uint112 from uint256, reverting on overflow (when the input is greater than largest uint112).

Counterpart to Solidity's `uint112` operator.

Requirements:

-   input must fit into 112 bits

toUint104(uint256 value) → uint104

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint104-uint256-)

Returns the downcasted uint104 from uint256, reverting on overflow (when the input is greater than largest uint104).

Counterpart to Solidity's `uint104` operator.

Requirements:

-   input must fit into 104 bits

toUint96(uint256 value) → uint96

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint96-uint256-)

Returns the downcasted uint96 from uint256, reverting on overflow (when the input is greater than largest uint96).

Counterpart to Solidity's `uint96` operator.

Requirements:

-   input must fit into 96 bits

toUint88(uint256 value) → uint88

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint88-uint256-)

Returns the downcasted uint88 from uint256, reverting on overflow (when the input is greater than largest uint88).

Counterpart to Solidity's `uint88` operator.

Requirements:

-   input must fit into 88 bits

toUint80(uint256 value) → uint80

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint80-uint256-)

Returns the downcasted uint80 from uint256, reverting on overflow (when the input is greater than largest uint80).

Counterpart to Solidity's `uint80` operator.

Requirements:

-   input must fit into 80 bits

toUint72(uint256 value) → uint72

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint72-uint256-)

Returns the downcasted uint72 from uint256, reverting on overflow (when the input is greater than largest uint72).

Counterpart to Solidity's `uint72` operator.

Requirements:

-   input must fit into 72 bits

toUint64(uint256 value) → uint64

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint64-uint256-)

Returns the downcasted uint64 from uint256, reverting on overflow (when the input is greater than largest uint64).

Counterpart to Solidity's `uint64` operator.

Requirements:

-   input must fit into 64 bits

toUint56(uint256 value) → uint56

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint56-uint256-)

Returns the downcasted uint56 from uint256, reverting on overflow (when the input is greater than largest uint56).

Counterpart to Solidity's `uint56` operator.

Requirements:

-   input must fit into 56 bits

toUint48(uint256 value) → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint48-uint256-)

Returns the downcasted uint48 from uint256, reverting on overflow (when the input is greater than largest uint48).

Counterpart to Solidity's `uint48` operator.

Requirements:

-   input must fit into 48 bits

toUint40(uint256 value) → uint40

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint40-uint256-)

Returns the downcasted uint40 from uint256, reverting on overflow (when the input is greater than largest uint40).

Counterpart to Solidity's `uint40` operator.

Requirements:

-   input must fit into 40 bits

toUint32(uint256 value) → uint32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint32-uint256-)

Returns the downcasted uint32 from uint256, reverting on overflow (when the input is greater than largest uint32).

Counterpart to Solidity's `uint32` operator.

Requirements:

-   input must fit into 32 bits

toUint24(uint256 value) → uint24

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint24-uint256-)

Returns the downcasted uint24 from uint256, reverting on overflow (when the input is greater than largest uint24).

Counterpart to Solidity's `uint24` operator.

Requirements:

-   input must fit into 24 bits

toUint16(uint256 value) → uint16

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint16-uint256-)

Returns the downcasted uint16 from uint256, reverting on overflow (when the input is greater than largest uint16).

Counterpart to Solidity's `uint16` operator.

Requirements:

-   input must fit into 16 bits

toUint8(uint256 value) → uint8

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint8-uint256-)

Returns the downcasted uint8 from uint256, reverting on overflow (when the input is greater than largest uint8).

Counterpart to Solidity's `uint8` operator.

Requirements:

-   input must fit into 8 bits

toUint256(int256 value) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint256-int256-)

Converts a signed int256 into an unsigned uint256.

Requirements:

-   input must be greater than or equal to 0.

toInt248(int256 value) → int248 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt248-int256-)

Returns the downcasted int248 from int256, reverting on overflow (when the input is less than smallest int248 or greater than largest int248).

Counterpart to Solidity's `int248` operator.

Requirements:

-   input must fit into 248 bits

toInt240(int256 value) → int240 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt240-int256-)

Returns the downcasted int240 from int256, reverting on overflow (when the input is less than smallest int240 or greater than largest int240).

Counterpart to Solidity's `int240` operator.

Requirements:

-   input must fit into 240 bits

toInt232(int256 value) → int232 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt232-int256-)

Returns the downcasted int232 from int256, reverting on overflow (when the input is less than smallest int232 or greater than largest int232).

Counterpart to Solidity's `int232` operator.

Requirements:

-   input must fit into 232 bits

toInt224(int256 value) → int224 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt224-int256-)

Returns the downcasted int224 from int256, reverting on overflow (when the input is less than smallest int224 or greater than largest int224).

Counterpart to Solidity's `int224` operator.

Requirements:

-   input must fit into 224 bits

toInt216(int256 value) → int216 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt216-int256-)

Returns the downcasted int216 from int256, reverting on overflow (when the input is less than smallest int216 or greater than largest int216).

Counterpart to Solidity's `int216` operator.

Requirements:

-   input must fit into 216 bits

toInt208(int256 value) → int208 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt208-int256-)

Returns the downcasted int208 from int256, reverting on overflow (when the input is less than smallest int208 or greater than largest int208).

Counterpart to Solidity's `int208` operator.

Requirements:

-   input must fit into 208 bits

toInt200(int256 value) → int200 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt200-int256-)

Returns the downcasted int200 from int256, reverting on overflow (when the input is less than smallest int200 or greater than largest int200).

Counterpart to Solidity's `int200` operator.

Requirements:

-   input must fit into 200 bits

toInt192(int256 value) → int192 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt192-int256-)

Returns the downcasted int192 from int256, reverting on overflow (when the input is less than smallest int192 or greater than largest int192).

Counterpart to Solidity's `int192` operator.

Requirements:

-   input must fit into 192 bits

toInt184(int256 value) → int184 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt184-int256-)

Returns the downcasted int184 from int256, reverting on overflow (when the input is less than smallest int184 or greater than largest int184).

Counterpart to Solidity's `int184` operator.

Requirements:

-   input must fit into 184 bits

toInt176(int256 value) → int176 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt176-int256-)

Returns the downcasted int176 from int256, reverting on overflow (when the input is less than smallest int176 or greater than largest int176).

Counterpart to Solidity's `int176` operator.

Requirements:

-   input must fit into 176 bits

toInt168(int256 value) → int168 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt168-int256-)

Returns the downcasted int168 from int256, reverting on overflow (when the input is less than smallest int168 or greater than largest int168).

Counterpart to Solidity's `int168` operator.

Requirements:

-   input must fit into 168 bits

toInt160(int256 value) → int160 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt160-int256-)

Returns the downcasted int160 from int256, reverting on overflow (when the input is less than smallest int160 or greater than largest int160).

Counterpart to Solidity's `int160` operator.

Requirements:

-   input must fit into 160 bits

toInt152(int256 value) → int152 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt152-int256-)

Returns the downcasted int152 from int256, reverting on overflow (when the input is less than smallest int152 or greater than largest int152).

Counterpart to Solidity's `int152` operator.

Requirements:

-   input must fit into 152 bits

toInt144(int256 value) → int144 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt144-int256-)

Returns the downcasted int144 from int256, reverting on overflow (when the input is less than smallest int144 or greater than largest int144).

Counterpart to Solidity's `int144` operator.

Requirements:

-   input must fit into 144 bits

toInt136(int256 value) → int136 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt136-int256-)

Returns the downcasted int136 from int256, reverting on overflow (when the input is less than smallest int136 or greater than largest int136).

Counterpart to Solidity's `int136` operator.

Requirements:

-   input must fit into 136 bits

toInt128(int256 value) → int128 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt128-int256-)

Returns the downcasted int128 from int256, reverting on overflow (when the input is less than smallest int128 or greater than largest int128).

Counterpart to Solidity's `int128` operator.

Requirements:

-   input must fit into 128 bits

toInt120(int256 value) → int120 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt120-int256-)

Returns the downcasted int120 from int256, reverting on overflow (when the input is less than smallest int120 or greater than largest int120).

Counterpart to Solidity's `int120` operator.

Requirements:

-   input must fit into 120 bits

toInt112(int256 value) → int112 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt112-int256-)

Returns the downcasted int112 from int256, reverting on overflow (when the input is less than smallest int112 or greater than largest int112).

Counterpart to Solidity's `int112` operator.

Requirements:

-   input must fit into 112 bits

toInt104(int256 value) → int104 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt104-int256-)

Returns the downcasted int104 from int256, reverting on overflow (when the input is less than smallest int104 or greater than largest int104).

Counterpart to Solidity's `int104` operator.

Requirements:

-   input must fit into 104 bits

toInt96(int256 value) → int96 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt96-int256-)

Returns the downcasted int96 from int256, reverting on overflow (when the input is less than smallest int96 or greater than largest int96).

Counterpart to Solidity's `int96` operator.

Requirements:

-   input must fit into 96 bits

toInt88(int256 value) → int88 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt88-int256-)

Returns the downcasted int88 from int256, reverting on overflow (when the input is less than smallest int88 or greater than largest int88).

Counterpart to Solidity's `int88` operator.

Requirements:

-   input must fit into 88 bits

toInt80(int256 value) → int80 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt80-int256-)

Returns the downcasted int80 from int256, reverting on overflow (when the input is less than smallest int80 or greater than largest int80).

Counterpart to Solidity's `int80` operator.

Requirements:

-   input must fit into 80 bits

toInt72(int256 value) → int72 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt72-int256-)

Returns the downcasted int72 from int256, reverting on overflow (when the input is less than smallest int72 or greater than largest int72).

Counterpart to Solidity's `int72` operator.

Requirements:

-   input must fit into 72 bits

toInt64(int256 value) → int64 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt64-int256-)

Returns the downcasted int64 from int256, reverting on overflow (when the input is less than smallest int64 or greater than largest int64).

Counterpart to Solidity's `int64` operator.

Requirements:

-   input must fit into 64 bits

toInt56(int256 value) → int56 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt56-int256-)

Returns the downcasted int56 from int256, reverting on overflow (when the input is less than smallest int56 or greater than largest int56).

Counterpart to Solidity's `int56` operator.

Requirements:

-   input must fit into 56 bits

toInt48(int256 value) → int48 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt48-int256-)

Returns the downcasted int48 from int256, reverting on overflow (when the input is less than smallest int48 or greater than largest int48).

Counterpart to Solidity's `int48` operator.

Requirements:

-   input must fit into 48 bits

toInt40(int256 value) → int40 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt40-int256-)

Returns the downcasted int40 from int256, reverting on overflow (when the input is less than smallest int40 or greater than largest int40).

Counterpart to Solidity's `int40` operator.

Requirements:

-   input must fit into 40 bits

toInt32(int256 value) → int32 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt32-int256-)

Returns the downcasted int32 from int256, reverting on overflow (when the input is less than smallest int32 or greater than largest int32).

Counterpart to Solidity's `int32` operator.

Requirements:

-   input must fit into 32 bits

toInt24(int256 value) → int24 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt24-int256-)

Returns the downcasted int24 from int256, reverting on overflow (when the input is less than smallest int24 or greater than largest int24).

Counterpart to Solidity's `int24` operator.

Requirements:

-   input must fit into 24 bits

toInt16(int256 value) → int16 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt16-int256-)

Returns the downcasted int16 from int256, reverting on overflow (when the input is less than smallest int16 or greater than largest int16).

Counterpart to Solidity's `int16` operator.

Requirements:

-   input must fit into 16 bits

toInt8(int256 value) → int8 downcasted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt8-int256-)

Returns the downcasted int8 from int256, reverting on overflow (when the input is less than smallest int8 or greater than largest int8).

Counterpart to Solidity's `int8` operator.

Requirements:

-   input must fit into 8 bits

toInt256(uint256 value) → int256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt256-uint256-)

Converts an unsigned uint256 into a signed int256.

Requirements:

-   input must be less than or equal to maxInt256.

toUint(bool b) → uint256 u

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint-bool-)

Cast a boolean (false or true) to a uint256 (0 or 1) with no jump.

SafeCastOverflowedUintDowncast(uint8 bits, uint256 value)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintDowncast-uint8-uint256-)

Value doesn't fit in a uint of `bits` size.

SafeCastOverflowedIntToUint(int256 value)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntToUint-int256-)

An int value doesn't fit in a uint of `bits` size.

SafeCastOverflowedIntDowncast(uint8 bits, int256 value)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntDowncast-uint8-int256-)

Value doesn't fit in an int of `bits` size.

SafeCastOverflowedUintToInt(uint256 value)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintToInt-uint256-)

A uint value doesn't fit in an int of `bits` size.

## [`SignedMath`](https://docs.openzeppelin.com/contracts/5.x/api/utils#signedmath)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/math/SignedMath.sol)

```
import "@openzeppelin/contracts/utils/math/SignedMath.sol";
```

Standard signed math utilities missing in the Solidity language.

### Functions

-   [ternary(condition, a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-ternary-bool-int256-int256-)
-   [max(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-max-int256-int256-)
-   [min(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-min-int256-int256-)
-   [average(a, b)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-average-int256-int256-)
-   [abs(n)](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-abs-int256-)

ternary(bool condition, int256 a, int256 b) → int256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-ternary-bool-int256-int256-)

Branchless ternary evaluation for `a ? b : c`. Gas costs are constant.

This function may reduce bytecode size and consume less gas when used standalone. However, the compiler may optimize Solidity ternary operations (i.e. `a ? b : c`) to only compute one branch when needed, making this function more expensive.

max(int256 a, int256 b) → int256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-max-int256-int256-)

Returns the largest of two signed numbers.

min(int256 a, int256 b) → int256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-min-int256-int256-)

Returns the smallest of two signed numbers.

average(int256 a, int256 b) → int256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-average-int256-int256-)

Returns the average of two signed numbers without overflow. The result is rounded towards zero.

abs(int256 n) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-abs-int256-)

Returns the absolute unsigned value of a signed value.

## [`Accumulators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#accumulators)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/Accumulators.sol)

```
import "@openzeppelin/contracts/utils/structs/Accumulators.sol";
```

Structure concatenating an arbitrary number of bytes buffers with limited memory allocation.

The Accumulators library provides a memory-efficient alternative to repeated concatenation of bytes. Instead of copying data on each concatenation (O(n\*\*2) complexity), it builds a linked list of references to existing data and performs a single memory allocation during flattening (O(n) complexity).

Uses 0x00 as sentinel value for empty state (i.e. null pointers)

#### [How it works](https://docs.openzeppelin.com/contracts/5.x/api/utils#how-it-works)

1.  Create an empty accumulator with null head/tail pointers
2.  Add data using [`RLP.push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-struct-RLP-Encoder-) (append) or [`Accumulators.shift`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-shift-struct-Accumulators-Accumulator-Memory-Slice-) (prepend). It creates linked list nodes
3.  Each node stores a reference to existing data (no copying)
4.  Call [`Accumulators.flatten`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-flatten-struct-Accumulators-Accumulator-) to materialize the final concatenated result in a single operation

#### [Performance](https://docs.openzeppelin.com/contracts/5.x/api/utils#performance)

-   Addition: O(1) per operation (just pointer manipulation)
-   Flattening: O(n) single pass with one memory allocation
-   Memory: Minimal overhead until flattening (only stores references)

### Functions

-   [accumulator()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-accumulator--)
-   [push(self, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-push-struct-Accumulators-Accumulator-bytes-)
-   [push(self, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-push-struct-Accumulators-Accumulator-Memory-Slice-)
-   [shift(self, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-shift-struct-Accumulators-Accumulator-bytes-)
-   [shift(self, data)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-shift-struct-Accumulators-Accumulator-Memory-Slice-)
-   [flatten(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-flatten-struct-Accumulators-Accumulator-)

accumulator() → struct Accumulators.Accumulator self

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-accumulator--)

Create a new (empty) accumulator

push(struct Accumulators.Accumulator self, bytes data) → struct Accumulators.Accumulator

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-push-struct-Accumulators-Accumulator-bytes-)

Add a bytes buffer to (the end of) an Accumulator

push(struct Accumulators.Accumulator self, Memory.Slice data) → struct Accumulators.Accumulator

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-push-struct-Accumulators-Accumulator-Memory-Slice-)

Add a memory slice to (the end of) an Accumulator

shift(struct Accumulators.Accumulator self, bytes data) → struct Accumulators.Accumulator

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-shift-struct-Accumulators-Accumulator-bytes-)

Add a bytes buffer to (the beginning of) an Accumulator

shift(struct Accumulators.Accumulator self, Memory.Slice data) → struct Accumulators.Accumulator

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-shift-struct-Accumulators-Accumulator-Memory-Slice-)

Add a memory slice to (the beginning of) an Accumulator

flatten(struct Accumulators.Accumulator self) → bytes result

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Accumulators-flatten-struct-Accumulators-Accumulator-)

Flatten all the bytes entries in an Accumulator into a single buffer

## [`BitMaps`](https://docs.openzeppelin.com/contracts/5.x/api/utils#bitmaps)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/BitMaps.sol)

```
import "@openzeppelin/contracts/utils/structs/BitMaps.sol";
```

Library for managing uint256 to bool mapping in a compact and efficient way, provided the keys are sequential. Largely inspired by Uniswap's [merkle-distributor](https://github.com/Uniswap/merkle-distributor/blob/master/contracts/MerkleDistributor.sol).

BitMaps pack 256 booleans across each bit of a single 256-bit slot of `uint256` type. Hence booleans corresponding to 256 *sequential* indices would only consume a single slot, unlike the regular `bool` which would consume an entire slot for a single value.

This results in gas savings in two ways:

-   Setting a zero value to non-zero only once every 256 times
-   Accessing the same warm slot for every 256 *sequential* indices

### Functions

-   [get(bitmap, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-get-struct-BitMaps-BitMap-uint256-)
-   [setTo(bitmap, index, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-setTo-struct-BitMaps-BitMap-uint256-bool-)
-   [set(bitmap, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-set-struct-BitMaps-BitMap-uint256-)
-   [unset(bitmap, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-unset-struct-BitMaps-BitMap-uint256-)

get(struct BitMaps.BitMap bitmap, uint256 index) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-get-struct-BitMaps-BitMap-uint256-)

Returns whether the bit at `index` is set.

setTo(struct BitMaps.BitMap bitmap, uint256 index, bool value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-setTo-struct-BitMaps-BitMap-uint256-bool-)

Sets the bit at `index` to the boolean `value`.

set(struct BitMaps.BitMap bitmap, uint256 index)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-set-struct-BitMaps-BitMap-uint256-)

Sets the bit at `index`.

unset(struct BitMaps.BitMap bitmap, uint256 index)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-unset-struct-BitMaps-BitMap-uint256-)

Unsets the bit at `index`.

## [`Checkpoints`](https://docs.openzeppelin.com/contracts/5.x/api/utils#checkpoints)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/Checkpoints.sol)

```
import "@openzeppelin/contracts/utils/structs/Checkpoints.sol";
```

This library defines the `Trace*` struct, for checkpointing values as they change at different points in time, and later looking up past values by block number. See [`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes) as an example.

To create a history of checkpoints define a variable type `Checkpoints.Trace*` in your contract, and store a new checkpoint for the current transaction block using the [`RLP.push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-struct-RLP-Encoder-) function.

### Functions

-   [push(self, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace256-uint256-uint256-)
-   [lowerLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace256-uint256-)
-   [upperLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace256-uint256-)
-   [upperLookupRecent(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace256-uint256-)
-   [latest(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace256-)
-   [latestCheckpoint(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace256-)
-   [length(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace256-)
-   [at(self, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace256-uint32-)
-   [push(self, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace224-uint32-uint224-)
-   [lowerLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace224-uint32-)
-   [upperLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace224-uint32-)
-   [upperLookupRecent(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace224-uint32-)
-   [latest(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace224-)
-   [latestCheckpoint(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace224-)
-   [length(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace224-)
-   [at(self, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace224-uint32-)
-   [push(self, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace208-uint48-uint208-)
-   [lowerLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace208-uint48-)
-   [upperLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace208-uint48-)
-   [upperLookupRecent(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace208-uint48-)
-   [latest(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace208-)
-   [latestCheckpoint(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace208-)
-   [length(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace208-)
-   [at(self, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace208-uint32-)
-   [push(self, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace160-uint96-uint160-)
-   [lowerLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace160-uint96-)
-   [upperLookup(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-)
-   [upperLookupRecent(self, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace160-uint96-)
-   [latest(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace160-)
-   [latestCheckpoint(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace160-)
-   [length(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace160-)
-   [at(self, pos)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace160-uint32-)

### Errors

-   [CheckpointUnorderedInsertion()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-CheckpointUnorderedInsertion--)

push(struct Checkpoints.Trace256 self, uint256 key, uint256 value) → uint256 oldValue, uint256 newValue

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace256-uint256-uint256-)

Pushes a (`key`, `value`) pair into a Trace256 so that it is stored as the checkpoint.

Returns previous value and new value.

Never accept `key` as a user input, since an arbitrary `type(uint256).max` key set will disable the library.

lowerLookup(struct Checkpoints.Trace256 self, uint256 key) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace256-uint256-)

Returns the value in the first (oldest) checkpoint with key greater or equal than the search key, or zero if there is none.

upperLookup(struct Checkpoints.Trace256 self, uint256 key) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace256-uint256-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

upperLookupRecent(struct Checkpoints.Trace256 self, uint256 key) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace256-uint256-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

This is a variant of [`Checkpoints.upperLookup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-) that is optimized to find "recent" checkpoint (checkpoints with high keys).

latest(struct Checkpoints.Trace256 self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace256-)

Returns the value in the most recent checkpoint, or zero if there are no checkpoints.

latestCheckpoint(struct Checkpoints.Trace256 self) → bool exists, uint256 \_key, uint256 \_value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace256-)

Returns whether there is a checkpoint in the structure (i.e. it is not empty), and if so the key and value in the most recent checkpoint.

length(struct Checkpoints.Trace256 self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace256-)

Returns the number of checkpoints.

at(struct Checkpoints.Trace256 self, uint32 pos) → struct Checkpoints.Checkpoint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace256-uint32-)

Returns checkpoint at given position.

push(struct Checkpoints.Trace224 self, uint32 key, uint224 value) → uint224 oldValue, uint224 newValue

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace224-uint32-uint224-)

Pushes a (`key`, `value`) pair into a Trace224 so that it is stored as the checkpoint.

Returns previous value and new value.

Never accept `key` as a user input, since an arbitrary `type(uint32).max` key set will disable the library.

lowerLookup(struct Checkpoints.Trace224 self, uint32 key) → uint224

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace224-uint32-)

Returns the value in the first (oldest) checkpoint with key greater or equal than the search key, or zero if there is none.

upperLookup(struct Checkpoints.Trace224 self, uint32 key) → uint224

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace224-uint32-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

upperLookupRecent(struct Checkpoints.Trace224 self, uint32 key) → uint224

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace224-uint32-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

This is a variant of [`Checkpoints.upperLookup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-) that is optimized to find "recent" checkpoint (checkpoints with high keys).

latest(struct Checkpoints.Trace224 self) → uint224

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace224-)

Returns the value in the most recent checkpoint, or zero if there are no checkpoints.

latestCheckpoint(struct Checkpoints.Trace224 self) → bool exists, uint32 \_key, uint224 \_value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace224-)

Returns whether there is a checkpoint in the structure (i.e. it is not empty), and if so the key and value in the most recent checkpoint.

length(struct Checkpoints.Trace224 self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace224-)

Returns the number of checkpoints.

at(struct Checkpoints.Trace224 self, uint32 pos) → struct Checkpoints.Checkpoint224

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace224-uint32-)

Returns checkpoint at given position.

push(struct Checkpoints.Trace208 self, uint48 key, uint208 value) → uint208 oldValue, uint208 newValue

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace208-uint48-uint208-)

Pushes a (`key`, `value`) pair into a Trace208 so that it is stored as the checkpoint.

Returns previous value and new value.

Never accept `key` as a user input, since an arbitrary `type(uint48).max` key set will disable the library.

lowerLookup(struct Checkpoints.Trace208 self, uint48 key) → uint208

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace208-uint48-)

Returns the value in the first (oldest) checkpoint with key greater or equal than the search key, or zero if there is none.

upperLookup(struct Checkpoints.Trace208 self, uint48 key) → uint208

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace208-uint48-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

upperLookupRecent(struct Checkpoints.Trace208 self, uint48 key) → uint208

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace208-uint48-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

This is a variant of [`Checkpoints.upperLookup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-) that is optimized to find "recent" checkpoint (checkpoints with high keys).

latest(struct Checkpoints.Trace208 self) → uint208

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace208-)

Returns the value in the most recent checkpoint, or zero if there are no checkpoints.

latestCheckpoint(struct Checkpoints.Trace208 self) → bool exists, uint48 \_key, uint208 \_value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace208-)

Returns whether there is a checkpoint in the structure (i.e. it is not empty), and if so the key and value in the most recent checkpoint.

length(struct Checkpoints.Trace208 self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace208-)

Returns the number of checkpoints.

at(struct Checkpoints.Trace208 self, uint32 pos) → struct Checkpoints.Checkpoint208

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace208-uint32-)

Returns checkpoint at given position.

push(struct Checkpoints.Trace160 self, uint96 key, uint160 value) → uint160 oldValue, uint160 newValue

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace160-uint96-uint160-)

Pushes a (`key`, `value`) pair into a Trace160 so that it is stored as the checkpoint.

Returns previous value and new value.

Never accept `key` as a user input, since an arbitrary `type(uint96).max` key set will disable the library.

lowerLookup(struct Checkpoints.Trace160 self, uint96 key) → uint160

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace160-uint96-)

Returns the value in the first (oldest) checkpoint with key greater or equal than the search key, or zero if there is none.

upperLookup(struct Checkpoints.Trace160 self, uint96 key) → uint160

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

upperLookupRecent(struct Checkpoints.Trace160 self, uint96 key) → uint160

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace160-uint96-)

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

This is a variant of [`Checkpoints.upperLookup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-) that is optimized to find "recent" checkpoint (checkpoints with high keys).

latest(struct Checkpoints.Trace160 self) → uint160

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace160-)

Returns the value in the most recent checkpoint, or zero if there are no checkpoints.

latestCheckpoint(struct Checkpoints.Trace160 self) → bool exists, uint96 \_key, uint160 \_value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace160-)

Returns whether there is a checkpoint in the structure (i.e. it is not empty), and if so the key and value in the most recent checkpoint.

length(struct Checkpoints.Trace160 self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace160-)

Returns the number of checkpoints.

at(struct Checkpoints.Trace160 self, uint32 pos) → struct Checkpoints.Checkpoint160

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace160-uint32-)

Returns checkpoint at given position.

CheckpointUnorderedInsertion()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-CheckpointUnorderedInsertion--)

A value was attempted to be inserted on a past checkpoint.

## [`CircularBuffer`](https://docs.openzeppelin.com/contracts/5.x/api/utils#circularbuffer)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/CircularBuffer.sol)

```
import "@openzeppelin/contracts/utils/structs/CircularBuffer.sol";
```

A fixed-size buffer for keeping `bytes32` items in storage.

This data structure allows for pushing elements to it, and when its length exceeds the specified fixed size, new items take the place of the oldest element in the buffer, keeping at most `N` elements in the structure.

Elements can't be removed but the data structure can be cleared. See [`CircularBuffer.clear`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-).

Complexity:

-   insertion ([`RLP.push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-struct-RLP-Encoder-)): O(1)
-   lookup ([`CircularBuffer.last`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-last-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)): O(1)
-   inclusion ([`CircularBuffer.includes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)): O(N) (worst case)
-   reset ([`CircularBuffer.clear`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-)): O(1)

The struct is called `Bytes32CircularBuffer`. Other types can be cast to and from `bytes32`. This data structure can only be used in storage, and not in memory.

Example usage:

```
contract Example {
    // Add the library methods
    using CircularBuffer for CircularBuffer.Bytes32CircularBuffer;

    // Declare a buffer storage variable
    CircularBuffer.Bytes32CircularBuffer private myBuffer;

    constructor() {
        myBuffer.setup(16); // Initialize the buffer with a non-zero fixed size (e.g., 16)
    }

    function pushValue(bytes32 value) external {
        myBuffer.push(value); // Safe to push because the buffer was initialized in the constructor
    }
}
```

Make sure to call [`CircularBuffer.setup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-setup-struct-CircularBuffer-Bytes32CircularBuffer-uint256-) on your buffer during construction/initialization

*Available since v5.1.*

### Functions

-   [setup(self, size)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-setup-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)
-   [clear(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-)
-   [push(self, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-push-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)
-   [count(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-count-struct-CircularBuffer-Bytes32CircularBuffer-)
-   [length(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-length-struct-CircularBuffer-Bytes32CircularBuffer-)
-   [last(self, i)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-last-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)
-   [includes(self, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)

### Errors

-   [InvalidBufferSize()](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-InvalidBufferSize--)

setup(struct CircularBuffer.Bytes32CircularBuffer self, uint256 size)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-setup-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)

Initialize a new CircularBuffer of a given size.

If the CircularBuffer was already setup and used, calling that function again will reset it to a blank state.

The size of the buffer will affect the execution of [`CircularBuffer.includes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-) function, as it has a complexity of O(N). Consider a large buffer size may render the function unusable.

clear(struct CircularBuffer.Bytes32CircularBuffer self)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-)

Clear all data in the buffer without resetting memory, keeping the existing size.

push(struct CircularBuffer.Bytes32CircularBuffer self, bytes32 value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-push-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)

Push a new value to the buffer. If the buffer is already full, the new value replaces the oldest value in the buffer.

count(struct CircularBuffer.Bytes32CircularBuffer self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-count-struct-CircularBuffer-Bytes32CircularBuffer-)

Number of values currently in the buffer. This value is 0 for an empty buffer, and cannot exceed the size of the buffer.

length(struct CircularBuffer.Bytes32CircularBuffer self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-length-struct-CircularBuffer-Bytes32CircularBuffer-)

Length of the buffer. This is the maximum number of elements kept in the buffer.

last(struct CircularBuffer.Bytes32CircularBuffer self, uint256 i) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-last-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)

Getter for the i-th value in the buffer, from the end.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if trying to access an element that was not pushed, or that was dropped to make room for newer elements.

includes(struct CircularBuffer.Bytes32CircularBuffer self, bytes32 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)

Check if a given value is in the buffer.

InvalidBufferSize()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-InvalidBufferSize--)

Error emitted when trying to setup a buffer with a size of 0.

## [`DoubleEndedQueue`](https://docs.openzeppelin.com/contracts/5.x/api/utils#doubleendedqueue)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/DoubleEndedQueue.sol)

```
import "@openzeppelin/contracts/utils/structs/DoubleEndedQueue.sol";
```

A sequence of items with the ability to efficiently push and pop items (i.e. insert and remove) on both ends of the sequence (called front and back). Among other access patterns, it can be used to implement efficient LIFO and FIFO queues. Storage use is optimized, and all operations are O(1) constant time. This includes [`CircularBuffer.clear`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-), given that the existing queue contents are left in storage.

The struct is called `Bytes32Deque`. Other types can be cast to and from `bytes32`. This data structure can only be used in storage, and not in memory.

```
DoubleEndedQueue.Bytes32Deque queue;
```

### Functions

-   [pushBack(deque, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushBack-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)
-   [tryPushBack(deque, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPushBack-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)
-   [popBack(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popBack-struct-DoubleEndedQueue-Bytes32Deque-)
-   [tryPopBack(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPopBack-struct-DoubleEndedQueue-Bytes32Deque-)
-   [pushFront(deque, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushFront-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)
-   [tryPushFront(deque, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPushFront-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)
-   [popFront(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popFront-struct-DoubleEndedQueue-Bytes32Deque-)
-   [tryPopFront(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPopFront-struct-DoubleEndedQueue-Bytes32Deque-)
-   [front(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-front-struct-DoubleEndedQueue-Bytes32Deque-)
-   [tryFront(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryFront-struct-DoubleEndedQueue-Bytes32Deque-)
-   [back(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-back-struct-DoubleEndedQueue-Bytes32Deque-)
-   [tryBack(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryBack-struct-DoubleEndedQueue-Bytes32Deque-)
-   [at(deque, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-at-struct-DoubleEndedQueue-Bytes32Deque-uint256-)
-   [tryAt(deque, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryAt-struct-DoubleEndedQueue-Bytes32Deque-uint256-)
-   [clear(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-clear-struct-DoubleEndedQueue-Bytes32Deque-)
-   [length(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-length-struct-DoubleEndedQueue-Bytes32Deque-)
-   [empty(deque)](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-empty-struct-DoubleEndedQueue-Bytes32Deque-)

pushBack(struct DoubleEndedQueue.Bytes32Deque deque, bytes32 value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushBack-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)

Inserts an item at the end of the queue.

Reverts with [`Panic.RESOURCE_ERROR`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-RESOURCE_ERROR-uint256) if the queue is full.

tryPushBack(struct DoubleEndedQueue.Bytes32Deque deque, bytes32 value) → bool success

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPushBack-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)

Attempts to insert an item at the end of the queue.

Returns `false` if the queue is full. Never reverts.

popBack(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popBack-struct-DoubleEndedQueue-Bytes32Deque-)

Removes the item at the end of the queue and returns it.

Reverts with [`Panic.EMPTY_ARRAY_POP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-EMPTY_ARRAY_POP-uint256) if the queue is empty.

tryPopBack(struct DoubleEndedQueue.Bytes32Deque deque) → bool success, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPopBack-struct-DoubleEndedQueue-Bytes32Deque-)

Attempts to remove the item at the end of the queue and return it.

Returns `(false, 0x00)` if the queue is empty. Never reverts.

pushFront(struct DoubleEndedQueue.Bytes32Deque deque, bytes32 value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushFront-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)

Inserts an item at the beginning of the queue.

Reverts with [`Panic.RESOURCE_ERROR`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-RESOURCE_ERROR-uint256) if the queue is full.

tryPushFront(struct DoubleEndedQueue.Bytes32Deque deque, bytes32 value) → bool success

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPushFront-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)

Attempts to insert an item at the beginning of the queue.

Returns `false` if the queue is full. Never reverts.

popFront(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popFront-struct-DoubleEndedQueue-Bytes32Deque-)

Removes the item at the beginning of the queue and returns it.

Reverts with [`Panic.EMPTY_ARRAY_POP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-EMPTY_ARRAY_POP-uint256) if the queue is empty.

tryPopFront(struct DoubleEndedQueue.Bytes32Deque deque) → bool success, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryPopFront-struct-DoubleEndedQueue-Bytes32Deque-)

Attempts to remove the item at the beginning of the queue and return it.

Returns `(false, 0x00)` if the queue is empty. Never reverts.

front(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-front-struct-DoubleEndedQueue-Bytes32Deque-)

Returns the item at the beginning of the queue.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if the queue is empty.

tryFront(struct DoubleEndedQueue.Bytes32Deque deque) → bool success, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryFront-struct-DoubleEndedQueue-Bytes32Deque-)

Attempts to return the item at the beginning of the queue.

Returns `(false, 0x00)` if the queue is empty. Never reverts.

back(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-back-struct-DoubleEndedQueue-Bytes32Deque-)

Returns the item at the end of the queue.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if the queue is empty.

tryBack(struct DoubleEndedQueue.Bytes32Deque deque) → bool success, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryBack-struct-DoubleEndedQueue-Bytes32Deque-)

Attempts to return the item at the end of the queue.

Returns `(false, 0x00)` if the queue is empty. Never reverts.

at(struct DoubleEndedQueue.Bytes32Deque deque, uint256 index) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-at-struct-DoubleEndedQueue-Bytes32Deque-uint256-)

Return the item at a position in the queue given by `index`, with the first item at 0 and last item at `length(deque) - 1`.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if the index is out of bounds.

tryAt(struct DoubleEndedQueue.Bytes32Deque deque, uint256 index) → bool success, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-tryAt-struct-DoubleEndedQueue-Bytes32Deque-uint256-)

Attempts to return the item at a position in the queue given by `index`, with the first item at 0 and the last item at `length(deque) - 1`.

Returns `(false, 0x00)` if the index is out of bounds. Never reverts.

clear(struct DoubleEndedQueue.Bytes32Deque deque)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-clear-struct-DoubleEndedQueue-Bytes32Deque-)

Resets the queue back to being empty.

The current items are left behind in storage. This does not affect the functioning of the queue, but misses out on potential gas refunds.

length(struct DoubleEndedQueue.Bytes32Deque deque) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-length-struct-DoubleEndedQueue-Bytes32Deque-)

Returns the number of items in the queue.

empty(struct DoubleEndedQueue.Bytes32Deque deque) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-empty-struct-DoubleEndedQueue-Bytes32Deque-)

Returns true if the queue is empty.

## [`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#enumerablemap)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/EnumerableMap.sol)

```
import "@openzeppelin/contracts/utils/structs/EnumerableMap.sol";
```

Library for managing an enumerable variant of Solidity's [`mapping`](https://solidity.readthedocs.io/en/latest/types.html#mapping-types) type.

Maps have the following properties:

-   Entries are added, removed, and checked for existence in constant time (O(1)).
-   Entries are enumerated in O(n). No guarantees are made on the ordering.
-   Map can be cleared (all entries removed) in O(n).

```
contract Example {
    // Add the library methods
    using EnumerableMap for EnumerableMap.UintToAddressMap;

    // Declare a set state variable
    EnumerableMap.UintToAddressMap private myMap;
}
```

The following map types are supported:

-   `uint256 -> address` (`UintToAddressMap`) since v3.0.0
-   `address -> uint256` (`AddressToUintMap`) since v4.6.0
-   `bytes32 -> bytes32` (`Bytes32ToBytes32Map`) since v4.6.0
-   `uint256 -> uint256` (`UintToUintMap`) since v4.7.0
-   `bytes32 -> uint256` (`Bytes32ToUintMap`) since v4.7.0
-   `uint256 -> bytes32` (`UintToBytes32Map`) since v5.1.0
-   `address -> address` (`AddressToAddressMap`) since v5.1.0
-   `address -> bytes32` (`AddressToBytes32Map`) since v5.1.0
-   `bytes32 -> address` (`Bytes32ToAddressMap`) since v5.1.0
-   `bytes -> bytes` (`BytesToBytesMap`) since v5.4.0
-   `bytes4 -> address` (`Bytes4ToAddressMap`) since v5.6.0

Trying to delete such a structure from storage will likely result in data corruption, rendering the structure unusable. See [ethereum/solidity#11843](https://github.com/ethereum/solidity/pull/11843) for more info.

In order to clean an EnumerableMap, you can either remove all elements one by one or create a fresh instance using an array of EnumerableMap.

### Functions

-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-bytes32-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToBytes32Map-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToBytes32Map-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToUintMap-uint256-uint256-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToUintMap-uint256-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToUintMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToUintMap-uint256-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToUintMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToUintMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToUintMap-uint256-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToUintMap-uint256-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToAddressMap-uint256-address-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToAddressMap-uint256-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToAddressMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToAddressMap-uint256-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToAddressMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToAddressMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToAddressMap-uint256-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToAddressMap-uint256-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToBytes32Map-uint256-bytes32-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToBytes32Map-uint256-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToBytes32Map-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToBytes32Map-uint256-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToBytes32Map-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToBytes32Map-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToBytes32Map-uint256-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToBytes32Map-uint256-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToUintMap-address-uint256-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToUintMap-address-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToUintMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToUintMap-address-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToUintMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToUintMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToUintMap-address-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToUintMap-address-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToAddressMap-address-address-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToAddressMap-address-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToAddressMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToAddressMap-address-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToAddressMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToAddressMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToAddressMap-address-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToAddressMap-address-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToBytes32Map-address-bytes32-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToBytes32Map-address-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToBytes32Map-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToBytes32Map-address-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToBytes32Map-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToBytes32Map-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToBytes32Map-address-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToBytes32Map-address-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToUintMap-bytes32-uint256-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToUintMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToUintMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToUintMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-address-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToAddressMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToAddressMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToAddressMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-address-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes4ToAddressMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes4ToAddressMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes4ToAddressMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes4ToAddressMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes4ToAddressMap-uint256-uint256-)
-   [set(map, key, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-BytesToBytesMap-bytes-bytes-)
-   [remove(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-BytesToBytesMap-bytes-)
-   [clear(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-BytesToBytesMap-)
-   [contains(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-BytesToBytesMap-bytes-)
-   [length(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-)
-   [at(map, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-BytesToBytesMap-uint256-)
-   [tryGet(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-BytesToBytesMap-bytes-)
-   [get(map, key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-BytesToBytesMap-bytes-)
-   [keys(map)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-)
-   [keys(map, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-uint256-uint256-)

### Errors

-   [EnumerableMapNonexistentKey(key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentKey-bytes32-)
-   [EnumerableMapNonexistentBytesKey(key)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentBytesKey-bytes-)

set(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key, bytes32 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-bytes32-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

Removes a key-value pair from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.Bytes32ToBytes32Map map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToBytes32Map-)

Removes all the entries from a map. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.Bytes32ToBytes32Map map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToBytes32Map-)

Returns the number of key-value pairs in the map. O(1).

at(struct EnumerableMap.Bytes32ToBytes32Map map, uint256 index) → bytes32 key, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-)

Returns the key-value pair stored at position `index` in the map. O(1).

Note that there are no guarantees on the ordering of entries inside the array, and it may change when more entries are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bool exists, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.Bytes32ToBytes32Map map) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.Bytes32ToBytes32Map map, uint256 start, uint256 end) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.UintToUintMap map, uint256 key, uint256 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToUintMap-uint256-uint256-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.UintToUintMap map, uint256 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToUintMap-uint256-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.UintToUintMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToUintMap-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.UintToUintMap map, uint256 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToUintMap-uint256-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.UintToUintMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToUintMap-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.UintToUintMap map, uint256 index) → uint256 key, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToUintMap-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.UintToUintMap map, uint256 key) → bool exists, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToUintMap-uint256-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.UintToUintMap map, uint256 key) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToUintMap-uint256-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.UintToUintMap map) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.UintToUintMap map, uint256 start, uint256 end) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.UintToAddressMap map, uint256 key, address value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToAddressMap-uint256-address-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.UintToAddressMap map, uint256 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToAddressMap-uint256-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.UintToAddressMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToAddressMap-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.UintToAddressMap map, uint256 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToAddressMap-uint256-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.UintToAddressMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToAddressMap-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.UintToAddressMap map, uint256 index) → uint256 key, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToAddressMap-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.UintToAddressMap map, uint256 key) → bool exists, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToAddressMap-uint256-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.UintToAddressMap map, uint256 key) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToAddressMap-uint256-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.UintToAddressMap map) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.UintToAddressMap map, uint256 start, uint256 end) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.UintToBytes32Map map, uint256 key, bytes32 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToBytes32Map-uint256-bytes32-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToBytes32Map-uint256-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.UintToBytes32Map map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToBytes32Map-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToBytes32Map-uint256-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.UintToBytes32Map map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToBytes32Map-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.UintToBytes32Map map, uint256 index) → uint256 key, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToBytes32Map-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bool exists, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToBytes32Map-uint256-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToBytes32Map-uint256-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.UintToBytes32Map map) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.UintToBytes32Map map, uint256 start, uint256 end) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.AddressToUintMap map, address key, uint256 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToUintMap-address-uint256-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.AddressToUintMap map, address key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToUintMap-address-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.AddressToUintMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToUintMap-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.AddressToUintMap map, address key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToUintMap-address-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.AddressToUintMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToUintMap-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.AddressToUintMap map, uint256 index) → address key, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToUintMap-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.AddressToUintMap map, address key) → bool exists, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToUintMap-address-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.AddressToUintMap map, address key) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToUintMap-address-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.AddressToUintMap map) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.AddressToUintMap map, uint256 start, uint256 end) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.AddressToAddressMap map, address key, address value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToAddressMap-address-address-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.AddressToAddressMap map, address key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToAddressMap-address-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.AddressToAddressMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToAddressMap-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.AddressToAddressMap map, address key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToAddressMap-address-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.AddressToAddressMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToAddressMap-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.AddressToAddressMap map, uint256 index) → address key, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToAddressMap-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.AddressToAddressMap map, address key) → bool exists, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToAddressMap-address-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.AddressToAddressMap map, address key) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToAddressMap-address-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.AddressToAddressMap map) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.AddressToAddressMap map, uint256 start, uint256 end) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.AddressToBytes32Map map, address key, bytes32 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToBytes32Map-address-bytes32-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.AddressToBytes32Map map, address key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToBytes32Map-address-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.AddressToBytes32Map map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToBytes32Map-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.AddressToBytes32Map map, address key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToBytes32Map-address-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.AddressToBytes32Map map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToBytes32Map-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.AddressToBytes32Map map, uint256 index) → address key, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToBytes32Map-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.AddressToBytes32Map map, address key) → bool exists, bytes32 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToBytes32Map-address-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.AddressToBytes32Map map, address key) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToBytes32Map-address-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.AddressToBytes32Map map) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.AddressToBytes32Map map, uint256 start, uint256 end) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key, uint256 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToUintMap-bytes32-uint256-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.Bytes32ToUintMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToUintMap-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.Bytes32ToUintMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToUintMap-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.Bytes32ToUintMap map, uint256 index) → bytes32 key, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToUintMap-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → bool exists, uint256 value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.Bytes32ToUintMap map) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.Bytes32ToUintMap map, uint256 start, uint256 end) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key, address value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-address-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.Bytes32ToAddressMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToAddressMap-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.Bytes32ToAddressMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToAddressMap-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.Bytes32ToAddressMap map, uint256 index) → bytes32 key, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToAddressMap-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → bool exists, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.Bytes32ToAddressMap map) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.Bytes32ToAddressMap map, uint256 start, uint256 end) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.Bytes4ToAddressMap map, bytes4 key, address value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-address-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.Bytes4ToAddressMap map, bytes4 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.Bytes4ToAddressMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes4ToAddressMap-)

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.Bytes4ToAddressMap map, bytes4 key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.Bytes4ToAddressMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes4ToAddressMap-)

Returns the number of elements in the map. O(1).

at(struct EnumerableMap.Bytes4ToAddressMap map, uint256 index) → bytes4 key, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes4ToAddressMap-uint256-)

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.Bytes4ToAddressMap map, bytes4 key) → bool exists, address value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.Bytes4ToAddressMap map, bytes4 key) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes4ToAddressMap-bytes4-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.Bytes4ToAddressMap map) → bytes4\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes4ToAddressMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.Bytes4ToAddressMap map, uint256 start, uint256 end) → bytes4\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes4ToAddressMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

set(struct EnumerableMap.BytesToBytesMap map, bytes key, bytes value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-BytesToBytesMap-bytes-bytes-)

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

remove(struct EnumerableMap.BytesToBytesMap map, bytes key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-BytesToBytesMap-bytes-)

Removes a key-value pair from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

clear(struct EnumerableMap.BytesToBytesMap map)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-BytesToBytesMap-)

Removes all the entries from a map. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableMap.BytesToBytesMap map, bytes key) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-BytesToBytesMap-bytes-)

Returns true if the key is in the map. O(1).

length(struct EnumerableMap.BytesToBytesMap map) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-)

Returns the number of key-value pairs in the map. O(1).

at(struct EnumerableMap.BytesToBytesMap map, uint256 index) → bytes key, bytes value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-BytesToBytesMap-uint256-)

Returns the key-value pair stored at position `index` in the map. O(1).

Note that there are no guarantees on the ordering of entries inside the array, and it may change when more entries are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

tryGet(struct EnumerableMap.BytesToBytesMap map, bytes key) → bool exists, bytes value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-BytesToBytesMap-bytes-)

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

get(struct EnumerableMap.BytesToBytesMap map, bytes key) → bytes value

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-BytesToBytesMap-bytes-)

Returns the value associated with `key`. O(1).

Requirements:

-   `key` must be in the map.

keys(struct EnumerableMap.BytesToBytesMap map) → bytes\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-)

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

keys(struct EnumerableMap.BytesToBytesMap map, uint256 start, uint256 end) → bytes\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-uint256-uint256-)

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

EnumerableMapNonexistentKey(bytes32 key)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentKey-bytes32-)

Query for a nonexistent map key.

EnumerableMapNonexistentBytesKey(bytes key)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentBytesKey-bytes-)

Query for a nonexistent map key.

## [`EnumerableSet`](https://docs.openzeppelin.com/contracts/5.x/api/utils#enumerableset)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/EnumerableSet.sol)

```
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";
```

Library for managing [sets](https://en.wikipedia.org/wiki/Set_\(abstract_data_type\)) of primitive types.

Sets have the following properties:

-   Elements are added, removed, and checked for existence in constant time (O(1)).
-   Elements are enumerated in O(n). No guarantees are made on the ordering.
-   Set can be cleared (all elements removed) in O(n).

```
contract Example {
    // Add the library methods
    using EnumerableSet for EnumerableSet.AddressSet;

    // Declare a set state variable
    EnumerableSet.AddressSet private mySet;
}
```

The following types are supported:

-   `bytes32` (`Bytes32Set`) since v3.3.0
-   `address` (`AddressSet`) since v3.3.0
-   `uint256` (`UintSet`) since v3.3.0
-   `string` (`StringSet`) since v5.4.0
-   `bytes` (`BytesSet`) since v5.4.0
-   `bytes4` (`Bytes4Set`) since v5.6.0

Trying to delete such a structure from storage will likely result in data corruption, rendering the structure unusable. See [ethereum/solidity#11843](https://github.com/ethereum/solidity/pull/11843) for more info.

In order to clean an EnumerableSet, you can either remove all elements one by one or create a fresh instance using an array of EnumerableSet.

### Functions

-   [add(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-Bytes32Set-bytes32-)
-   [remove(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-Bytes32Set-bytes32-)
-   [clear(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-Bytes32Set-)
-   [contains(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-Bytes32Set-bytes32-)
-   [length(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-Bytes32Set-)
-   [at(set, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-Bytes32Set-uint256-)
-   [values(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-)
-   [values(set, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-uint256-uint256-)
-   [add(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-Bytes4Set-bytes4-)
-   [remove(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-Bytes4Set-bytes4-)
-   [clear(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-Bytes4Set-)
-   [contains(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-Bytes4Set-bytes4-)
-   [length(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-Bytes4Set-)
-   [at(set, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-Bytes4Set-uint256-)
-   [values(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes4Set-)
-   [values(set, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes4Set-uint256-uint256-)
-   [add(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-AddressSet-address-)
-   [remove(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-AddressSet-address-)
-   [clear(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-AddressSet-)
-   [contains(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-AddressSet-address-)
-   [length(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-AddressSet-)
-   [at(set, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-AddressSet-uint256-)
-   [values(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-)
-   [values(set, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-uint256-uint256-)
-   [add(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-UintSet-uint256-)
-   [remove(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-UintSet-uint256-)
-   [clear(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-UintSet-)
-   [contains(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-UintSet-uint256-)
-   [length(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-UintSet-)
-   [at(set, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-UintSet-uint256-)
-   [values(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-)
-   [values(set, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-uint256-uint256-)
-   [add(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-StringSet-string-)
-   [remove(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-StringSet-string-)
-   [clear(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-StringSet-)
-   [contains(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-StringSet-string-)
-   [length(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-StringSet-)
-   [at(set, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-StringSet-uint256-)
-   [values(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-)
-   [values(set, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-uint256-uint256-)
-   [add(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-BytesSet-bytes-)
-   [remove(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-BytesSet-bytes-)
-   [clear(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-BytesSet-)
-   [contains(set, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-BytesSet-bytes-)
-   [length(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-)
-   [at(set, index)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-BytesSet-uint256-)
-   [values(set)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-)
-   [values(set, start, end)](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-uint256-uint256-)

add(struct EnumerableSet.Bytes32Set set, bytes32 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-Bytes32Set-bytes32-)

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

remove(struct EnumerableSet.Bytes32Set set, bytes32 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-Bytes32Set-bytes32-)

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

clear(struct EnumerableSet.Bytes32Set set)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-Bytes32Set-)

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableSet.Bytes32Set set, bytes32 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-Bytes32Set-bytes32-)

Returns true if the value is in the set. O(1).

length(struct EnumerableSet.Bytes32Set set) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-Bytes32Set-)

Returns the number of values in the set. O(1).

at(struct EnumerableSet.Bytes32Set set, uint256 index) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-Bytes32Set-uint256-)

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

values(struct EnumerableSet.Bytes32Set set) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-)

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

values(struct EnumerableSet.Bytes32Set set, uint256 start, uint256 end) → bytes32\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-uint256-uint256-)

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

add(struct EnumerableSet.Bytes4Set set, bytes4 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-Bytes4Set-bytes4-)

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

remove(struct EnumerableSet.Bytes4Set set, bytes4 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-Bytes4Set-bytes4-)

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

clear(struct EnumerableSet.Bytes4Set set)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-Bytes4Set-)

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableSet.Bytes4Set set, bytes4 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-Bytes4Set-bytes4-)

Returns true if the value is in the set. O(1).

length(struct EnumerableSet.Bytes4Set set) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-Bytes4Set-)

Returns the number of values in the set. O(1).

at(struct EnumerableSet.Bytes4Set set, uint256 index) → bytes4

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-Bytes4Set-uint256-)

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

values(struct EnumerableSet.Bytes4Set set) → bytes4\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes4Set-)

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

values(struct EnumerableSet.Bytes4Set set, uint256 start, uint256 end) → bytes4\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes4Set-uint256-uint256-)

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

add(struct EnumerableSet.AddressSet set, address value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-AddressSet-address-)

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

remove(struct EnumerableSet.AddressSet set, address value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-AddressSet-address-)

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

clear(struct EnumerableSet.AddressSet set)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-AddressSet-)

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableSet.AddressSet set, address value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-AddressSet-address-)

Returns true if the value is in the set. O(1).

length(struct EnumerableSet.AddressSet set) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-AddressSet-)

Returns the number of values in the set. O(1).

at(struct EnumerableSet.AddressSet set, uint256 index) → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-AddressSet-uint256-)

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

values(struct EnumerableSet.AddressSet set) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-)

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

values(struct EnumerableSet.AddressSet set, uint256 start, uint256 end) → address\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-uint256-uint256-)

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

add(struct EnumerableSet.UintSet set, uint256 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-UintSet-uint256-)

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

remove(struct EnumerableSet.UintSet set, uint256 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-UintSet-uint256-)

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

clear(struct EnumerableSet.UintSet set)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-UintSet-)

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableSet.UintSet set, uint256 value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-UintSet-uint256-)

Returns true if the value is in the set. O(1).

length(struct EnumerableSet.UintSet set) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-UintSet-)

Returns the number of values in the set. O(1).

at(struct EnumerableSet.UintSet set, uint256 index) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-UintSet-uint256-)

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

values(struct EnumerableSet.UintSet set) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-)

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

values(struct EnumerableSet.UintSet set, uint256 start, uint256 end) → uint256\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-uint256-uint256-)

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

add(struct EnumerableSet.StringSet set, string value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-StringSet-string-)

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

remove(struct EnumerableSet.StringSet set, string value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-StringSet-string-)

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

clear(struct EnumerableSet.StringSet set)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-StringSet-)

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableSet.StringSet set, string value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-StringSet-string-)

Returns true if the value is in the set. O(1).

length(struct EnumerableSet.StringSet set) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-StringSet-)

Returns the number of values on the set. O(1).

at(struct EnumerableSet.StringSet set, uint256 index) → string

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-StringSet-uint256-)

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

values(struct EnumerableSet.StringSet set) → string\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-)

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

values(struct EnumerableSet.StringSet set, uint256 start, uint256 end) → string\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-uint256-uint256-)

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

add(struct EnumerableSet.BytesSet set, bytes value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-BytesSet-bytes-)

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

remove(struct EnumerableSet.BytesSet set, bytes value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-BytesSet-bytes-)

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

clear(struct EnumerableSet.BytesSet set)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-BytesSet-)

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

contains(struct EnumerableSet.BytesSet set, bytes value) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-BytesSet-bytes-)

Returns true if the value is in the set. O(1).

length(struct EnumerableSet.BytesSet set) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-)

Returns the number of values on the set. O(1).

at(struct EnumerableSet.BytesSet set, uint256 index) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-BytesSet-uint256-)

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

-   `index` must be strictly less than [`Memory.length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Memory-length-Memory-Slice-).

values(struct EnumerableSet.BytesSet set) → bytes\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-)

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

values(struct EnumerableSet.BytesSet set, uint256 start, uint256 end) → bytes\[\]

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-uint256-uint256-)

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

## [`Heap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#heap)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/Heap.sol)

```
import "@openzeppelin/contracts/utils/structs/Heap.sol";
```

Library for managing [binary heap](https://en.wikipedia.org/wiki/Binary_heap) that can be used as [priority queue](https://en.wikipedia.org/wiki/Priority_queue).

Heaps are represented as a tree of values where the first element (index 0) is the root, and where the node at index i is the child of the node at index (i-1)/2 and the parent of nodes at index 2*i+1 and 2*i+2. Each node stores an element of the heap.

The structure is ordered so that, per the comparator, each node has lower priority than its parent; as a consequence, the highest-priority value is at the root. This value can be looked up in constant time (O(1)) at `heap.tree[0]`. By default, the comparator is `Comparators.lt`, which treats smaller values as higher priority (min-heap). Using `Comparators.gt` yields a max-heap.

The structure is designed to perform the following operations with the corresponding complexities:

-   peek (get the highest priority value): O(1)
-   insert (insert a value): O(log(n))
-   pop (remove the highest priority value): O(log(n))
-   replace (replace the highest priority value with a new value): O(log(n))
-   length (get the number of elements): O(1)
-   clear (remove all elements): O(1)

This library allows for the use of custom comparator functions. Given that manipulating memory can lead to unexpected behavior. Consider verifying that the comparator does not manipulate the Heap's state directly and that it follows the Solidity memory safety rules.

*Available since v5.1.*

### Functions

-   [peek(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-peek-struct-Heap-Uint256Heap-)
-   [pop(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-)
-   [pop(self, comp)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function--uint256-uint256--view-returns--bool--)
-   [insert(self, value)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-)
-   [insert(self, value, comp)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--)
-   [replace(self, newValue)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-)
-   [replace(self, newValue, comp)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--)
-   [length(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-length-struct-Heap-Uint256Heap-)
-   [clear(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-clear-struct-Heap-Uint256Heap-)

peek(struct Heap.Uint256Heap self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-peek-struct-Heap-Uint256Heap-)

Lookup the root element of the heap.

pop(struct Heap.Uint256Heap self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-)

Remove (and return) the root element for the heap using the default comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

pop(struct Heap.Uint256Heap self, function (uint256,uint256) view returns (bool) comp) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function--uint256-uint256--view-returns--bool--)

Remove (and return) the root element for the heap using the provided comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

insert(struct Heap.Uint256Heap self, uint256 value)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-)

Insert a new element in the heap using the default comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

insert(struct Heap.Uint256Heap self, uint256 value, function (uint256,uint256) view returns (bool) comp)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--)

Insert a new element in the heap using the provided comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

replace(struct Heap.Uint256Heap self, uint256 newValue) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-)

Return the root element for the heap, and replace it with a new value, using the default comparator. This is equivalent to using [`Heap.pop`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function--uint256-uint256--view-returns--bool--) and [`Heap.insert`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--), but requires only one rebalancing operation.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

replace(struct Heap.Uint256Heap self, uint256 newValue, function (uint256,uint256) view returns (bool) comp) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--)

Return the root element for the heap, and replace it with a new value, using the provided comparator. This is equivalent to using [`Heap.pop`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function--uint256-uint256--view-returns--bool--) and [`Heap.insert`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--), but requires only one rebalancing operation.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

length(struct Heap.Uint256Heap self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-length-struct-Heap-Uint256Heap-)

Returns the number of elements in the heap.

clear(struct Heap.Uint256Heap self)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-clear-struct-Heap-Uint256Heap-)

Removes all elements in the heap.

## [`MerkleTree`](https://docs.openzeppelin.com/contracts/5.x/api/utils#merkletree)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/structs/MerkleTree.sol)

```
import "@openzeppelin/contracts/utils/structs/MerkleTree.sol";
```

Library for managing [Merkle Tree](https://wikipedia.org/wiki/Merkle_Tree) data structures.

Each tree is a complete binary tree with the ability to sequentially insert leaves, changing them from a zero to a non-zero value and updating its root. This structure allows inserting commitments (or other entries) that are not stored, but can be proven to be part of the tree at a later time if the root is kept. See [`MerkleProof`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#MerkleProof).

A tree is defined by the following parameters:

-   Depth: The number of levels in the tree, it also defines the maximum number of leaves as 2\*\*depth.
-   Zero value: The value that represents an empty leaf. Used to avoid regular zero values to be part of the tree.
-   Hashing function: A cryptographic hash function used to produce internal nodes. Defaults to [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-).

Building trees using non-commutative hashing functions (i.e. `H(a, b) != H(b, a)`) is supported. However, proving the inclusion of a leaf in such trees is not possible with the [`MerkleProof`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#MerkleProof) library since it only supports *commutative* hashing functions.

*Available since v5.1.*

### Functions

-   [setup(self, treeDepth, zero)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-)
-   [setup(self, treeDepth, zero, fnHash)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-function--bytes32-bytes32--view-returns--bytes32--)
-   [push(self, leaf)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-)
-   [push(self, leaf, fnHash)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-function--bytes32-bytes32--view-returns--bytes32--)
-   [update(self, index, oldValue, newValue, proof)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---)
-   [update(self, index, oldValue, newValue, proof, fnHash)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function--bytes32-bytes32--view-returns--bytes32--)
-   [depth(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-depth-struct-MerkleTree-Bytes32PushTree-)

### Errors

-   [MerkleTreeUpdateInvalidIndex(index, length)](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidIndex-uint256-uint256-)
-   [MerkleTreeUpdateInvalidProof()](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidProof--)

setup(struct MerkleTree.Bytes32PushTree self, uint8 treeDepth, bytes32 zero) → bytes32 initialRoot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-)

Initialize a [`MerkleTree.Bytes32PushTree`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-Bytes32PushTree) using [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-) to hash internal nodes. The capacity of the tree (i.e. number of leaves) is set to `2**treeDepth`.

Calling this function on MerkleTree that was already setup and used will reset it to a blank state.

Once a tree is setup, any push to it must use the same hashing function. This means that values should be pushed to it using the default [push](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-) function.

The zero value should be carefully chosen since it will be stored in the tree representing empty leaves. It should be a value that is not expected to be part of the tree.

setup(struct MerkleTree.Bytes32PushTree self, uint8 treeDepth, bytes32 zero, function (bytes32,bytes32) view returns (bytes32) fnHash) → bytes32 initialRoot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-function--bytes32-bytes32--view-returns--bytes32--)

Same as [setup](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-), but allows to specify a custom hashing function.

Once a tree is setup, any push to it must use the same hashing function. This means that values should be pushed to it using the custom push function, which should be the same one as used during the setup.

Providing a custom hashing function is a security-sensitive operation since it may compromise the soundness of the tree.

Consider verifying that the hashing function does not manipulate the memory state directly and that it follows the Solidity memory safety rules. Otherwise, it may lead to unexpected behavior.

push(struct MerkleTree.Bytes32PushTree self, bytes32 leaf) → uint256 index, bytes32 newRoot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-)

Insert a new leaf in the tree, and compute the new root. Returns the position of the inserted leaf in the tree, and the resulting root.

Hashing the leaf before calling this function is recommended as a protection against second pre-image attacks.

This variant uses [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-) to hash internal nodes. It should only be used on merkle trees that were setup using the same (default) hashing function (i.e. by calling [the default setup](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-) function).

push(struct MerkleTree.Bytes32PushTree self, bytes32 leaf, function (bytes32,bytes32) view returns (bytes32) fnHash) → uint256 index, bytes32 newRoot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-function--bytes32-bytes32--view-returns--bytes32--)

Insert a new leaf in the tree, and compute the new root. Returns the position of the inserted leaf in the tree, and the resulting root.

Hashing the leaf before calling this function is recommended as a protection against second pre-image attacks.

This variant uses a custom hashing function to hash internal nodes. It should only be called with the same function as the one used during the initial setup of the merkle tree.

update(struct MerkleTree.Bytes32PushTree self, uint256 index, bytes32 oldValue, bytes32 newValue, bytes32\[\] proof) → bytes32 oldRoot, bytes32 newRoot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---)

Change the value of the leaf at position `index` from `oldValue` to `newValue`. Returns the recomputed "old" root (before the update) and "new" root (after the update). The caller must verify that the reconstructed old root is the last known one.

The `proof` must be an up-to-date inclusion proof for the leaf being updated. This means that this function is vulnerable to front-running. Any [`RLP.push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-struct-RLP-Encoder-) or [`MerkleTree.update`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function--bytes32-bytes32--view-returns--bytes32--) operation (that changes the root of the tree) would render all "in flight" updates invalid.

This variant uses [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-) to hash internal nodes. It should only be used on merkle trees that were setup using the same (default) hashing function (i.e. by calling [the default setup](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-) function).

update(struct MerkleTree.Bytes32PushTree self, uint256 index, bytes32 oldValue, bytes32 newValue, bytes32\[\] proof, function (bytes32,bytes32) view returns (bytes32) fnHash) → bytes32 oldRoot, bytes32 newRoot

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function--bytes32-bytes32--view-returns--bytes32--)

Change the value of the leaf at position `index` from `oldValue` to `newValue`. Returns the recomputed "old" root (before the update) and "new" root (after the update). The caller must verify that the reconstructed old root is the last known one.

The `proof` must be an up-to-date inclusion proof for the leaf being update. This means that this function is vulnerable to front-running. Any [`RLP.push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#RLP-push-struct-RLP-Encoder-struct-RLP-Encoder-) or [`MerkleTree.update`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function--bytes32-bytes32--view-returns--bytes32--) operation (that changes the root of the tree) would render all "in flight" updates invalid.

This variant uses a custom hashing function to hash internal nodes. It should only be called with the same function as the one used during the initial setup of the merkle tree.

depth(struct MerkleTree.Bytes32PushTree self) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-depth-struct-MerkleTree-Bytes32PushTree-)

Tree's depth (set at initialization)

MerkleTreeUpdateInvalidIndex(uint256 index, uint256 length)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidIndex-uint256-uint256-)

Error emitted when trying to update a leaf that was not previously pushed.

MerkleTreeUpdateInvalidProof()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidProof--)

Error emitted when the proof used during an update is invalid (could not reproduce the side).

## [`Time`](https://docs.openzeppelin.com/contracts/5.x/api/utils#time)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/utils/types/Time.sol)

```
import "@openzeppelin/contracts/utils/types/Time.sol";
```

This library provides helpers for manipulating time-related objects.

It uses the following types:

-   `uint48` for timepoints
-   `uint32` for durations

While the library doesn't provide specific types for timepoints and duration, it does provide:

-   a `Delay` type to represent duration that can be programmed to change value automatically at a given point
-   additional helper functions

### Functions

-   [timestamp()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-timestamp--)
-   [blockNumber()](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-blockNumber--)
-   [toDelay(duration)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-toDelay-uint32-)
-   [getFull(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-getFull-Time-Delay-)
-   [get(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-get-Time-Delay-)
-   [withUpdate(self, newValue, minSetback)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-withUpdate-Time-Delay-uint32-uint32-)
-   [unpack(self)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-unpack-Time-Delay-)
-   [pack(valueBefore, valueAfter, effect)](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-pack-uint32-uint32-uint48-)

timestamp() → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-timestamp--)

Get the block timestamp as a Timepoint.

blockNumber() → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-blockNumber--)

Get the block number as a Timepoint.

toDelay(uint32 duration) → Time.Delay

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-toDelay-uint32-)

Wrap a duration into a Delay to add the one-step "update in the future" feature

getFull(Time.Delay self) → uint32 valueBefore, uint32 valueAfter, uint48 effect

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-getFull-Time-Delay-)

Get the current value plus the pending value and effect timepoint if there is a scheduled change. If the effect timepoint is 0, then the pending value should not be considered.

get(Time.Delay self) → uint32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-get-Time-Delay-)

Get the current value.

withUpdate(Time.Delay self, uint32 newValue, uint32 minSetback) → Time.Delay updatedDelay, uint48 effect

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-withUpdate-Time-Delay-uint32-uint32-)

Update a Delay object so that it takes a new duration after a timepoint that is automatically computed to enforce the old delay at the moment of the update. Returns the updated Delay object and the timestamp when the new delay becomes effective.

unpack(Time.Delay self) → uint32 valueBefore, uint32 valueAfter, uint48 effect

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-unpack-Time-Delay-)

Split a delay into its components: valueBefore, valueAfter and effect (transition timepoint).

pack(uint32 valueBefore, uint32 valueAfter, uint48 effect) → Time.Delay

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-pack-uint32-uint32-uint48-)

pack the components into a Delay object.

[

ERC6909

Previous Page

](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC6909)[

Cryptography

Next Page

](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography)

### On this page

[Math](https://docs.openzeppelin.com/contracts/5.x/api/utils#math)[Security](https://docs.openzeppelin.com/contracts/5.x/api/utils#security)[Introspection](https://docs.openzeppelin.com/contracts/5.x/api/utils#introspection)[Data Structures](https://docs.openzeppelin.com/contracts/5.x/api/utils#data-structures)[Libraries](https://docs.openzeppelin.com/contracts/5.x/api/utils#libraries)[`Address`](https://docs.openzeppelin.com/contracts/5.x/api/utils#address)[`Arrays`](https://docs.openzeppelin.com/contracts/5.x/api/utils#arrays)[`Base58`](https://docs.openzeppelin.com/contracts/5.x/api/utils#base58)[`Base64`](https://docs.openzeppelin.com/contracts/5.x/api/utils#base64)[`Blockhash`](https://docs.openzeppelin.com/contracts/5.x/api/utils#blockhash)[`Bytes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#bytes)[`CAIP10`](https://docs.openzeppelin.com/contracts/5.x/api/utils#caip10)[`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#caip2)[`Calldata`](https://docs.openzeppelin.com/contracts/5.x/api/utils#calldata)[`Comparators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#comparators)[`Context`](https://docs.openzeppelin.com/contracts/5.x/api/utils#context)[`Create2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#create2)[`Errors`](https://docs.openzeppelin.com/contracts/5.x/api/utils#errors)[`LowLevelCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#lowlevelcall)[`Memory`](https://docs.openzeppelin.com/contracts/5.x/api/utils#memory)[`Multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#multicall)[`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#nonces)[`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#nonceskeyed)[`Packing`](https://docs.openzeppelin.com/contracts/5.x/api/utils#packing)[`Panic`](https://docs.openzeppelin.com/contracts/5.x/api/utils#panic)[`Pausable`](https://docs.openzeppelin.com/contracts/5.x/api/utils#pausable)[`RLP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#rlp)[Canonical vs Non-Canonical Encodings](https://docs.openzeppelin.com/contracts/5.x/api/utils#canonical-vs-non-canonical-encodings)[`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#reentrancyguard)[`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#reentrancyguardtransient)[`RelayedCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#relayedcall)[`ShortString`](https://docs.openzeppelin.com/contracts/5.x/api/utils#shortstring)[`ShortStrings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#shortstrings)[`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#slotderivation)[`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#storageslot)[`Strings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#strings)[`TransientSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#transientslot)[`InteroperableAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#interoperableaddress)[`ERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#erc165)[`ERC165Checker`](https://docs.openzeppelin.com/contracts/5.x/api/utils#erc165checker)[`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ierc165)[`Math`](https://docs.openzeppelin.com/contracts/5.x/api/utils#math-1)[`SafeCast`](https://docs.openzeppelin.com/contracts/5.x/api/utils#safecast)[`SignedMath`](https://docs.openzeppelin.com/contracts/5.x/api/utils#signedmath)[`Accumulators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#accumulators)[How it works](https://docs.openzeppelin.com/contracts/5.x/api/utils#how-it-works)[Performance](https://docs.openzeppelin.com/contracts/5.x/api/utils#performance)[`BitMaps`](https://docs.openzeppelin.com/contracts/5.x/api/utils#bitmaps)[`Checkpoints`](https://docs.openzeppelin.com/contracts/5.x/api/utils#checkpoints)[`CircularBuffer`](https://docs.openzeppelin.com/contracts/5.x/api/utils#circularbuffer)[`DoubleEndedQueue`](https://docs.openzeppelin.com/contracts/5.x/api/utils#doubleendedqueue)[`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#enumerablemap)[`EnumerableSet`](https://docs.openzeppelin.com/contracts/5.x/api/utils#enumerableset)[`Heap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#heap)[`MerkleTree`](https://docs.openzeppelin.com/contracts/5.x/api/utils#merkletree)[`Time`](https://docs.openzeppelin.com/contracts/5.x/api/utils#time)
