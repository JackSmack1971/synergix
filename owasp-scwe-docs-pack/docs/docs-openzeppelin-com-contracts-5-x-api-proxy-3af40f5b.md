---
title: "Proxy"
source_url: "https://docs.openzeppelin.com/contracts/5.x/api/proxy"
host: "docs.openzeppelin.com"
depth: 2
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:50.750Z"
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

# Proxy

Smart contract proxy utilities and implementations

Copy Markdown

[Open in Claude](https://claude.ai/new?q=Read+https%3A%2F%2Fraw.githubusercontent.com%2FOpenZeppelin%2Fdocs%2Frefs%2Fheads%2Fmain%2Fcontent%2Fcontracts%2F5.x%2Fapi%2Fproxy.mdx%2C+I+want+to+ask+questions+about+it.)

This is a low-level set of contracts implementing different proxy patterns with and without upgradeability. For an in-depth overview of this pattern check out the [Proxy Upgrade Pattern](https://docs.openzeppelin.com/upgrades-plugins/proxies) page.

Most of the proxies below are built on an abstract base contract.

-   [`Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy): Abstract contract implementing the core delegation functionality.

In order to avoid clashes with the storage variables of the implementation contract behind a proxy, we use [ERC-1967](https://eips.ethereum.org/EIPS/eip-1967) storage slots.

-   [`ERC1967Utils`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils): Internal functions to get and set the storage slots defined in ERC-1967.
-   [`ERC1967Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy): A proxy using ERC-1967 storage slots. Not upgradeable by default.

There are two alternative ways to add upgradeability to an ERC-1967 proxy. Their differences are explained below in [Transparent vs UUPS Proxies](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparent-vs-uups-proxies).

-   [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy): A proxy with a built-in immutable admin and upgrade interface.
-   [`UUPSUpgradeable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable): An upgradeability mechanism to be included in the implementation contract.

**🔥 CAUTION**
Using upgradeable proxies correctly and securely is a difficult task that requires deep knowledge of the proxy pattern, Solidity, and the EVM. Unless you want a lot of low level control, we recommend using the [OpenZeppelin Upgrades Plugins](https://docs.openzeppelin.com/upgrades-plugins) for Hardhat and Foundry.

A different family of proxies is beacon proxies. This pattern, popularized by Dharma, allows multiple proxies to be upgraded to a different implementation in a single transaction.

-   [`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy): A proxy that retrieves its implementation from a beacon contract.
-   [`UpgradeableBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon): A beacon contract with a built-in admin that can upgrade the [`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy) pointing to it.

In this pattern, the proxy contract doesn’t hold the implementation address in storage like an ERC-1967 proxy. Instead, the address is stored in a separate beacon contract. The `upgrade` operations are sent to the beacon instead of to the proxy contract, and all proxies that follow that beacon are automatically upgraded.

Outside the realm of upgradeability, proxies can also be useful to make cheap contract clones, such as those created by an on-chain factory contract that creates many instances of the same contract. These instances are designed to be both cheap to deploy, and cheap to call.

-   [`Clones`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones): A library that can deploy cheap minimal non-upgradeable proxies.

## [Transparent vs UUPS Proxies](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparent-vs-uups-proxies)

The original proxies included in OpenZeppelin followed the [Transparent Proxy Pattern](https://blog.openzeppelin.com/the-transparent-proxy-pattern/). While this pattern is still provided, our recommendation is now shifting towards UUPS proxies, which are both lightweight and versatile. The name UUPS comes from [ERC-1822](https://eips.ethereum.org/EIPS/eip-1822), which first documented the pattern.

While both of these share the same interface for upgrades, in UUPS proxies the upgrade is handled by the implementation, and can eventually be removed. Transparent proxies, on the other hand, include the upgrade and admin logic in the proxy itself. This means [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy) is more expensive to deploy than what is possible with UUPS proxies.

UUPS proxies are implemented using an [`ERC1967Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy). Note that this proxy is not by itself upgradeable. It is the role of the implementation to include, alongside the contract’s logic, all the code necessary to update the implementation’s address that is stored at a specific slot in the proxy’s storage space. This is where the [`UUPSUpgradeable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable) contract comes in. Inheriting from it (and overriding the [`_authorizeUpgrade`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_authorizeUpgrade-address-) function with the relevant access control mechanism) will turn your contract into a UUPS compliant implementation.

Note that since both proxies use the same storage slot for the implementation address, using a UUPS compliant implementation with a [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy) might allow non-admins to perform upgrade operations.

By default, the upgrade functionality included in [`UUPSUpgradeable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable) contains a security mechanism that will prevent any upgrades to a non UUPS compliant implementation. This prevents upgrades to an implementation contract that wouldn’t contain the necessary upgrade mechanism, as it would lock the upgradeability of the proxy forever. This security mechanism can be bypassed by either of:

-   Adding a flag mechanism in the implementation that will disable the upgrade function when triggered.
-   Upgrading to an implementation that features an upgrade mechanism without the additional security check, and then upgrading again to another implementation without the upgrade mechanism.

The current implementation of this security mechanism uses [ERC-1822](https://eips.ethereum.org/EIPS/eip-1822) to detect the storage slot used by the implementation. A previous implementation, now deprecated, relied on a rollback check. It is possible to upgrade from a contract using the old mechanism to a new one. The inverse is however not possible, as old implementations (before version 4.5) did not include the ERC-1822 interface.

## [Core](https://docs.openzeppelin.com/contracts/5.x/api/proxy#core)

[`Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy)

## [ERC-1967](https://docs.openzeppelin.com/contracts/5.x/api/proxy#erc-1967)

[`IERC1967`](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC1967)

[`ERC1967Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy)

[`ERC1967Utils`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils)

## [Transparent Proxy](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparent-proxy)

[`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy)

[`ProxyAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin)

## [Beacon](https://docs.openzeppelin.com/contracts/5.x/api/proxy#beacon)

[`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy)

[`IBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#IBeacon)

[`UpgradeableBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon)

## [Minimal Clones](https://docs.openzeppelin.com/contracts/5.x/api/proxy#minimal-clones)

[`Clones`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones)

## [Utils](https://docs.openzeppelin.com/contracts/5.x/api/proxy#utils)

[`Initializable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable)

[`UUPSUpgradeable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable)

## [`Clones`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#clones)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/Clones.sol)

```
import "@openzeppelin/contracts/proxy/Clones.sol";
```

[ERC-1167](https://eips.ethereum.org/EIPS/eip-1167) is a standard for deploying minimal proxy contracts, also known as "clones".

> To simply and cheaply clone contract functionality in an immutable way, this standard specifies a minimal bytecode implementation that delegates all calls to a known, fixed address.

The library includes functions to deploy a proxy using either `create` (traditional deployment) or `create2` (salted deterministic deployment). It also includes functions to predict the addresses of clones deployed using the deterministic method.

### Functions

-   [clone(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-clone-address-)
-   [clone(implementation, value)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-clone-address-uint256-)
-   [cloneDeterministic(implementation, salt)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministic-address-bytes32-)
-   [cloneDeterministic(implementation, salt, value)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministic-address-bytes32-uint256-)
-   [predictDeterministicAddress(implementation, salt, deployer)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddress-address-bytes32-address-)
-   [predictDeterministicAddress(implementation, salt)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddress-address-bytes32-)
-   [cloneWithImmutableArgs(implementation, args)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneWithImmutableArgs-address-bytes-)
-   [cloneWithImmutableArgs(implementation, args, value)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneWithImmutableArgs-address-bytes-uint256-)
-   [cloneDeterministicWithImmutableArgs(implementation, args, salt)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministicWithImmutableArgs-address-bytes-bytes32-)
-   [cloneDeterministicWithImmutableArgs(implementation, args, salt, value)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministicWithImmutableArgs-address-bytes-bytes32-uint256-)
-   [predictDeterministicAddressWithImmutableArgs(implementation, args, salt, deployer)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddressWithImmutableArgs-address-bytes-bytes32-address-)
-   [predictDeterministicAddressWithImmutableArgs(implementation, args, salt)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddressWithImmutableArgs-address-bytes-bytes32-)
-   [fetchCloneArgs(instance)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-fetchCloneArgs-address-)

### Errors

-   [CloneArgumentsTooLong()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-CloneArgumentsTooLong--)

clone(address implementation) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-clone-address-)

Deploys and returns the address of a clone that mimics the behavior of `implementation`.

This function uses the create opcode, which should never revert.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

clone(address implementation, uint256 value) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-clone-address-uint256-)

Same as [clone](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-clone-address-), but with a `value` parameter to send native currency to the new contract.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

Using a non-zero value at creation will require the contract using this function (e.g. a factory) to always have enough balance for new deployments. Consider exposing this function under a payable method.

cloneDeterministic(address implementation, bytes32 salt) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministic-address-bytes32-)

Deploys and returns the address of a clone that mimics the behavior of `implementation`.

This function uses the create2 opcode and a `salt` to deterministically deploy the clone. Using the same `implementation` and `salt` multiple times will revert, since the clones cannot be deployed twice at the same address.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

cloneDeterministic(address implementation, bytes32 salt, uint256 value) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministic-address-bytes32-uint256-)

Same as [cloneDeterministic](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministic-address-bytes32-), but with a `value` parameter to send native currency to the new contract.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

Using a non-zero value at creation will require the contract using this function (e.g. a factory) to always have enough balance for new deployments. Consider exposing this function under a payable method.

predictDeterministicAddress(address implementation, bytes32 salt, address deployer) → address predicted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddress-address-bytes32-address-)

Computes the address of a clone deployed using [`Clones.cloneDeterministic`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministic-address-bytes32-uint256-).

predictDeterministicAddress(address implementation, bytes32 salt) → address predicted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddress-address-bytes32-)

Computes the address of a clone deployed using [`Clones.cloneDeterministic`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministic-address-bytes32-uint256-).

cloneWithImmutableArgs(address implementation, bytes args) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneWithImmutableArgs-address-bytes-)

Deploys and returns the address of a clone that mimics the behavior of `implementation` with custom immutable arguments. These are provided through `args` and cannot be changed after deployment. To access the arguments within the implementation, use [`Clones.fetchCloneArgs`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-fetchCloneArgs-address-).

This function uses the create opcode, which should never revert.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

cloneWithImmutableArgs(address implementation, bytes args, uint256 value) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneWithImmutableArgs-address-bytes-uint256-)

Same as [cloneWithImmutableArgs](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneWithImmutableArgs-address-bytes-), but with a `value` parameter to send native currency to the new contract.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

Using a non-zero value at creation will require the contract using this function (e.g. a factory) to always have enough balance for new deployments. Consider exposing this function under a payable method.

cloneDeterministicWithImmutableArgs(address implementation, bytes args, bytes32 salt) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministicWithImmutableArgs-address-bytes-bytes32-)

Deploys and returns the address of a clone that mimics the behavior of `implementation` with custom immutable arguments. These are provided through `args` and cannot be changed after deployment. To access the arguments within the implementation, use [`Clones.fetchCloneArgs`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-fetchCloneArgs-address-).

This function uses the create2 opcode and a `salt` to deterministically deploy the clone. Using the same `implementation`, `args` and `salt` multiple times will revert, since the clones cannot be deployed twice at the same address.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

cloneDeterministicWithImmutableArgs(address implementation, bytes args, bytes32 salt, uint256 value) → address instance

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministicWithImmutableArgs-address-bytes-bytes32-uint256-)

Same as [cloneDeterministicWithImmutableArgs](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministicWithImmutableArgs-address-bytes-bytes32-), but with a `value` parameter to send native currency to the new contract.

This function does not check if `implementation` has code. A clone that points to an address without code cannot be initialized. Initialization calls may appear to be successful when, in reality, they have no effect and leave the clone uninitialized, allowing a third party to initialize it later.

Using a non-zero value at creation will require the contract using this function (e.g. a factory) to always have enough balance for new deployments. Consider exposing this function under a payable method.

predictDeterministicAddressWithImmutableArgs(address implementation, bytes args, bytes32 salt, address deployer) → address predicted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddressWithImmutableArgs-address-bytes-bytes32-address-)

Computes the address of a clone deployed using [`Clones.cloneDeterministicWithImmutableArgs`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministicWithImmutableArgs-address-bytes-bytes32-uint256-).

predictDeterministicAddressWithImmutableArgs(address implementation, bytes args, bytes32 salt) → address predicted

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-predictDeterministicAddressWithImmutableArgs-address-bytes-bytes32-)

Computes the address of a clone deployed using [`Clones.cloneDeterministicWithImmutableArgs`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-cloneDeterministicWithImmutableArgs-address-bytes-bytes32-uint256-).

fetchCloneArgs(address instance) → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-fetchCloneArgs-address-)

Get the immutable args attached to a clone.

-   If `instance` is a clone that was deployed using `clone` or `cloneDeterministic`, this function will return an empty array.
-   If `instance` is a clone that was deployed using `cloneWithImmutableArgs` or `cloneDeterministicWithImmutableArgs`, this function will return the args array used at creation.
-   If `instance` is NOT a clone deployed using this library, the behavior is undefined. This function should only be used to check addresses that are known to be clones.

CloneArgumentsTooLong()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Clones-CloneArgumentsTooLong--)

## [`ERC1967Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#erc1967proxy)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/ERC1967/ERC1967Proxy.sol)

```
import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
```

This contract implements an upgradeable proxy. It is upgradeable because calls are delegated to an implementation address that can be changed. This address is stored in storage in the location specified by [ERC-1967](https://eips.ethereum.org/EIPS/eip-1967), so that it doesn't conflict with the storage layout of the implementation behind the proxy.

### Functions

-   [constructor(implementation, \_data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-constructor-address-bytes-)
-   [\_implementation()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_implementation--)
-   [\_unsafeAllowUninitialized()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_unsafeAllowUninitialized--)

Proxy

-   [\_delegate(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_delegate-address-)
-   [\_fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_fallback--)
-   [fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-fallback--)

### Errors

-   [ERC1967ProxyUninitialized()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-ERC1967ProxyUninitialized--)

constructor(address implementation, bytes \_data)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-constructor-address-bytes-)

Initializes the upgradeable proxy with an initial implementation specified by `implementation`.

Provided `_data` is passed in a delegate call to `implementation`. This will typically be an encoded function call, and allows initializing the storage of the proxy like a Solidity constructor. By default construction will fail if `_data` is empty. This behavior can be overridden using a custom [`ERC1967Proxy._unsafeAllowUninitialized`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_unsafeAllowUninitialized--) that returns true. In that case, empty `_data` is ignored and no delegate call to the implementation is performed during construction.

Requirements:

-   If `data` is empty, `msg.value` must be zero.

\_implementation() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_implementation--)

Returns the current implementation address.

To get this value clients can read directly from the storage slot shown below (specified by ERC-1967) using the [`eth_getStorageAt`](https://eth.wiki/json-rpc/API#eth_getstorageat) RPC call. `0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc`

\_unsafeAllowUninitialized() → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_unsafeAllowUninitialized--)

Returns whether the proxy can be left uninitialized.

Override this function to allow the proxy to be left uninitialized. Consider uninitialized proxies might be susceptible to man-in-the-middle threats where the proxy is replaced with a malicious one.

ERC1967ProxyUninitialized()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-ERC1967ProxyUninitialized--)

The proxy is left uninitialized.

## [`ERC1967Utils`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#erc1967utils)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/ERC1967/ERC1967Utils.sol)

```
import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Utils.sol";
```

This library provides getters and event emitting update functions for [ERC-1967](https://eips.ethereum.org/EIPS/eip-1967) slots.

### Functions

-   [getImplementation()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-getImplementation--)
-   [upgradeToAndCall(newImplementation, data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-upgradeToAndCall-address-bytes-)
-   [getAdmin()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-getAdmin--)
-   [changeAdmin(newAdmin)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-changeAdmin-address-)
-   [getBeacon()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-getBeacon--)
-   [upgradeBeaconToAndCall(newBeacon, data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-upgradeBeaconToAndCall-address-bytes-)

### Errors

-   [ERC1967InvalidImplementation(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967InvalidImplementation-address-)
-   [ERC1967InvalidAdmin(admin)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967InvalidAdmin-address-)
-   [ERC1967InvalidBeacon(beacon)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967InvalidBeacon-address-)
-   [ERC1967NonPayable()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967NonPayable--)

getImplementation() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-getImplementation--)

Returns the current implementation address.

upgradeToAndCall(address newImplementation, bytes data)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-upgradeToAndCall-address-bytes-)

Performs implementation upgrade with additional setup call if data is nonempty. This function is payable only if the setup call is performed, otherwise `msg.value` is rejected to avoid stuck value in the contract.

Emits an [`IERC1967.Upgraded`](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC1967-Upgraded-address-) event.

getAdmin() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-getAdmin--)

Returns the current admin.

To get this value clients can read directly from the storage slot shown below (specified by ERC-1967) using the [`eth_getStorageAt`](https://ethereum.org/developers/docs/apis/json-rpc/#eth_getstorageat) RPC call. `0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103`

changeAdmin(address newAdmin)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-changeAdmin-address-)

Changes the admin of the proxy.

Emits an [`IERC1967.AdminChanged`](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC1967-AdminChanged-address-address-) event.

getBeacon() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-getBeacon--)

Returns the current beacon.

upgradeBeaconToAndCall(address newBeacon, bytes data)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-upgradeBeaconToAndCall-address-bytes-)

Change the beacon and trigger a setup call if data is nonempty. This function is payable only if the setup call is performed, otherwise `msg.value` is rejected to avoid stuck value in the contract.

Emits an [`IERC1967.BeaconUpgraded`](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC1967-BeaconUpgraded-address-) event.

Invoking this function has no effect on an instance of [`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy) since v5, since it uses an immutable beacon without looking at the value of the ERC-1967 beacon slot for efficiency.

ERC1967InvalidImplementation(address implementation)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967InvalidImplementation-address-)

The `implementation` of the proxy is invalid.

ERC1967InvalidAdmin(address admin)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967InvalidAdmin-address-)

The `admin` of the proxy is invalid.

ERC1967InvalidBeacon(address beacon)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967InvalidBeacon-address-)

The `beacon` of the proxy is invalid.

ERC1967NonPayable()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-ERC1967NonPayable--)

An upgrade function sees `msg.value > 0` that may be lost.

## [`Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#proxy)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/Proxy.sol)

```
import "@openzeppelin/contracts/proxy/Proxy.sol";
```

This abstract contract provides a fallback function that delegates all calls to another contract using the EVM instruction `delegatecall`. We refer to the second contract as the *implementation* behind the proxy, and it has to be specified by overriding the virtual [`ERC1967Proxy._implementation`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_implementation--) function.

Additionally, delegation to the implementation can be triggered manually through the [`Proxy._fallback`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_fallback--) function, or to a different contract through the [`Proxy._delegate`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_delegate-address-) function.

The success and return data of the delegated call will be returned back to the caller of the proxy.

### Functions

-   [\_delegate(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_delegate-address-)
-   [\_implementation()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_implementation--)
-   [\_fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_fallback--)
-   [fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-fallback--)

\_delegate(address implementation)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_delegate-address-)

Delegates the current call to `implementation`.

This function does not return to its internal call site, it will return directly to the external caller.

\_implementation() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_implementation--)

This is a virtual function that should be overridden so it returns the address to which the fallback function and [`Proxy._fallback`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_fallback--) should delegate.

\_fallback()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_fallback--)

Delegates the current call to the address returned by `_implementation()`.

This function does not return to its internal call site, it will return directly to the external caller.

fallback()

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-fallback--)

Fallback function that delegates calls to the address returned by `_implementation()`. Will run if no other function in the contract matches the call data.

## [`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#beaconproxy)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/beacon/BeaconProxy.sol)

```
import "@openzeppelin/contracts/proxy/beacon/BeaconProxy.sol";
```

This contract implements a proxy that gets the implementation address for each call from an [`UpgradeableBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon).

The beacon address can only be set once during construction, and cannot be changed afterwards. It is stored in an immutable variable to avoid unnecessary storage reads, and also in the beacon storage slot specified by [ERC-1967](https://eips.ethereum.org/EIPS/eip-1967) so that it can be accessed externally.

Since the beacon address can never be changed, you must ensure that you either control the beacon, or trust the beacon to not upgrade the implementation maliciously.

Do not use the implementation logic to modify the beacon storage slot. Doing so would leave the proxy in an inconsistent state where the beacon storage slot does not match the beacon address.

### Functions

-   [constructor(beacon, data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy-constructor-address-bytes-)
-   [\_implementation()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy-_implementation--)
-   [\_getBeacon()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy-_getBeacon--)

Proxy

-   [\_delegate(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_delegate-address-)
-   [\_fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_fallback--)
-   [fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-fallback--)

constructor(address beacon, bytes data)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy-constructor-address-bytes-)

Initializes the proxy with `beacon`.

If `data` is nonempty, it's used as data in a delegate call to the implementation returned by the beacon. This will typically be an encoded function call, and allows initializing the storage of the proxy like a Solidity constructor.

Requirements:

-   `beacon` must be a contract with the interface [`IBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#IBeacon).
-   If `data` is empty, `msg.value` must be zero.

\_implementation() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy-_implementation--)

Returns the current implementation address of the associated beacon.

\_getBeacon() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy-_getBeacon--)

Returns the beacon.

## [`IBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ibeacon)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/beacon/IBeacon.sol)

```
import "@openzeppelin/contracts/proxy/beacon/IBeacon.sol";
```

This is the interface that [`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy) expects of its beacon.

### Functions

-   [implementation()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#IBeacon-implementation--)

implementation() → address

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#IBeacon-implementation--)

Must return an address that can be used as a delegate call target.

[`UpgradeableBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon) will check that this address is a contract.

## [`UpgradeableBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#upgradeablebeacon)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/beacon/UpgradeableBeacon.sol)

```
import "@openzeppelin/contracts/proxy/beacon/UpgradeableBeacon.sol";
```

This contract is used in conjunction with one or more instances of [`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#BeaconProxy) to determine their implementation contract, which is where they will delegate all function calls.

An owner is able to change the implementation the beacon points to, thus upgrading the proxies that use this beacon.

### Functions

-   [constructor(implementation\_, initialOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-constructor-address-address-)
-   [implementation()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-implementation--)
-   [upgradeTo(newImplementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-upgradeTo-address-)

Ownable

-   [owner()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-owner--)
-   [\_checkOwner()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-_checkOwner--)
-   [renounceOwnership()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-renounceOwnership--)
-   [transferOwnership(newOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-transferOwnership-address-)
-   [\_transferOwnership(newOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-_transferOwnership-address-)

### Events

-   [Upgraded(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-Upgraded-address-)

Ownable

-   [OwnershipTransferred(previousOwner, newOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-OwnershipTransferred-address-address-)

### Errors

-   [BeaconInvalidImplementation(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-BeaconInvalidImplementation-address-)

Ownable

-   [OwnableUnauthorizedAccount(account)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-OwnableUnauthorizedAccount-address-)
-   [OwnableInvalidOwner(owner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-OwnableInvalidOwner-address-)

constructor(address implementation\_, address initialOwner)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-constructor-address-address-)

Sets the address of the initial implementation, and the initial owner who can upgrade the beacon.

implementation() → address

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-implementation--)

Returns the current implementation address.

upgradeTo(address newImplementation)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-upgradeTo-address-)

Upgrades the beacon to a new implementation.

Emits an [`UpgradeableBeacon.Upgraded`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-Upgraded-address-) event.

Requirements:

-   msg.sender must be the owner of the contract.
-   `newImplementation` must be a contract.

Upgraded(address indexed implementation)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-Upgraded-address-)

Emitted when the implementation returned by the beacon is changed.

BeaconInvalidImplementation(address implementation)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-BeaconInvalidImplementation-address-)

The `implementation` of the beacon is invalid.

## [`ProxyAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#proxyadmin)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/transparent/ProxyAdmin.sol)

```
import "@openzeppelin/contracts/proxy/transparent/ProxyAdmin.sol";
```

This is an auxiliary contract meant to be assigned as the admin of a [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy). For an explanation of why you would want to use this see the documentation for [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy).

### Functions

-   [constructor(initialOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin-constructor-address-)
-   [upgradeAndCall(proxy, implementation, data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin-upgradeAndCall-contract-ITransparentUpgradeableProxy-address-bytes-)
-   [UPGRADE\_INTERFACE\_VERSION()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin-UPGRADE_INTERFACE_VERSION-string)

Ownable

-   [owner()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-owner--)
-   [\_checkOwner()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-_checkOwner--)
-   [renounceOwnership()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-renounceOwnership--)
-   [transferOwnership(newOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-transferOwnership-address-)
-   [\_transferOwnership(newOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-_transferOwnership-address-)

### Events

Ownable

-   [OwnershipTransferred(previousOwner, newOwner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-OwnershipTransferred-address-address-)

### Errors

Ownable

-   [OwnableUnauthorizedAccount(account)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-OwnableUnauthorizedAccount-address-)
-   [OwnableInvalidOwner(owner)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Ownable-OwnableInvalidOwner-address-)

constructor(address initialOwner)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin-constructor-address-)

Sets the initial owner who can perform upgrades.

upgradeAndCall(contract ITransparentUpgradeableProxy proxy, address implementation, bytes data)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin-upgradeAndCall-contract-ITransparentUpgradeableProxy-address-bytes-)

Upgrades `proxy` to `implementation` and calls a function on the new implementation. See [`TransparentUpgradeableProxy._dispatchUpgradeToAndCall`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-_dispatchUpgradeToAndCall--).

Requirements:

-   This contract must be the admin of `proxy`.
-   If `data` is empty, `msg.value` must be zero.

UPGRADE\_INTERFACE\_VERSION() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin-UPGRADE_INTERFACE_VERSION-string)

The version of the upgrade interface of the contract. If this getter is missing, both `upgrade(address,address)` and `upgradeAndCall(address,address,bytes)` are present, and `upgrade` must be used if no function should be called, while `upgradeAndCall` will invoke the `receive` function if the third argument is the empty byte string. If the getter returns `"5.0.0"`, only `upgradeAndCall(address,address,bytes)` is present, and the third argument must be the empty byte string if no function should be called, making it impossible to invoke the `receive` function during an upgrade.

## [`ITransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#itransparentupgradeableproxy)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/transparent/TransparentUpgradeableProxy.sol)

```
import "@openzeppelin/contracts/proxy/transparent/TransparentUpgradeableProxy.sol";
```

Interface for [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy). In order to implement transparency, [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy) does not implement this interface directly, and its upgradeability mechanism is implemented by an internal dispatch mechanism. The compiler is unaware that these functions are implemented by [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy) and will not include them in the ABI so this interface must be used to interact with it.

### Functions

-   [upgradeToAndCall(newImplementation, data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ITransparentUpgradeableProxy-upgradeToAndCall-address-bytes-)

### Events

IERC1967

-   [Upgraded(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#IERC1967-Upgraded-address-)
-   [AdminChanged(previousAdmin, newAdmin)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#IERC1967-AdminChanged-address-address-)
-   [BeaconUpgraded(beacon)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#IERC1967-BeaconUpgraded-address-)

upgradeToAndCall(address newImplementation, bytes data)

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ITransparentUpgradeableProxy-upgradeToAndCall-address-bytes-)

See [`UUPSUpgradeable.upgradeToAndCall`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-upgradeToAndCall-address-bytes-)

## [`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparentupgradeableproxy)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/transparent/TransparentUpgradeableProxy.sol)

```
import "@openzeppelin/contracts/proxy/transparent/TransparentUpgradeableProxy.sol";
```

This contract implements a proxy that is upgradeable through an associated [`ProxyAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin) instance.

To avoid [proxy selector clashing](https://medium.com/nomic-labs-blog/malicious-backdoors-in-ethereum-proxies-62629adf3357), which can potentially be used in an attack, this contract uses the [transparent proxy pattern](https://blog.openzeppelin.com/the-transparent-proxy-pattern/). This pattern implies two things that go hand in hand:

1.  If any account other than the admin calls the proxy, the call will be forwarded to the implementation, even if that call matches the [`ITransparentUpgradeableProxy.upgradeToAndCall`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ITransparentUpgradeableProxy-upgradeToAndCall-address-bytes-) function exposed by the proxy itself.
2.  If the admin calls the proxy, it can call the `upgradeToAndCall` function, but any other call won't be forwarded to the implementation. If the admin tries to call a function on the implementation it will fail with an error indicating the proxy admin cannot fallback to the target implementation.

These properties mean that the admin account can only be used for upgrading the proxy, so it's best if it's a dedicated account that is not used for anything else. This will avoid headaches due to sudden errors when trying to call a function from the proxy implementation. For this reason, the proxy deploys an instance of [`ProxyAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin) and allows upgrades only if they come through it. You should think of the `ProxyAdmin` instance as the administrative interface of the proxy, including the ability to change who can trigger upgrades by transferring ownership.

The real interface of this proxy is that defined in `ITransparentUpgradeableProxy`. This contract does not inherit from that interface, and instead `upgradeToAndCall` is implicitly implemented using a custom dispatch mechanism in `_fallback`. Consequently, the compiler will not produce an ABI for this contract. This is necessary to fully implement transparency without decoding reverts caused by selector clashes between the proxy and the implementation.

This proxy does not inherit from [`Context`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context) deliberately. The [`ProxyAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin) of this contract won't send a meta-transaction in any way, and any other meta-transaction setup should be made in the implementation contract.

This contract avoids unnecessary storage reads by setting the admin only during construction as an immutable variable, preventing any changes thereafter. However, the admin slot defined in ERC-1967 can still be overwritten by the implementation logic pointed to by this proxy. In such cases, the contract may end up in an undesirable state where the admin slot is different from the actual admin. Relying on the value of the admin slot is generally fine if the implementation is trusted.

It is not recommended to extend this contract to add additional external functions. If you do so, the compiler will not check that there are no selector conflicts, due to the note above. A selector clash between any new function and the functions declared in [`ITransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ITransparentUpgradeableProxy) will be resolved in favor of the new one. This could render the `upgradeToAndCall` function inaccessible, preventing upgradeability and compromising transparency.

### Functions

-   [constructor(\_logic, initialOwner, \_data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-constructor-address-address-bytes-)
-   [\_proxyAdmin()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-_proxyAdmin--)
-   [\_fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-_fallback--)

ERC1967Proxy

-   [\_implementation()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_implementation--)
-   [\_unsafeAllowUninitialized()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-_unsafeAllowUninitialized--)

Proxy

-   [\_delegate(implementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-_delegate-address-)
-   [fallback()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Proxy-fallback--)

### Errors

-   [ProxyDeniedAdminAccess()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-ProxyDeniedAdminAccess--)

ERC1967Proxy

-   [ERC1967ProxyUninitialized()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-ERC1967ProxyUninitialized--)

constructor(address \_logic, address initialOwner, bytes \_data)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-constructor-address-address-bytes-)

Initializes an upgradeable proxy managed by an instance of a [`ProxyAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ProxyAdmin) with an `initialOwner`, backed by the implementation at `_logic`, and optionally initialized with `_data` as explained in [`ERC1967Proxy.constructor`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-constructor-address-bytes-).

\_proxyAdmin() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-_proxyAdmin--)

Returns the admin of this proxy.

\_fallback()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-_fallback--)

If caller is the admin process the call internally, otherwise transparently fallback to the proxy behavior.

ProxyDeniedAdminAccess()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#TransparentUpgradeableProxy-ProxyDeniedAdminAccess--)

The proxy caller is the current admin, and can't fallback to the proxy target.

## [`Initializable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#initializable)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/utils/Initializable.sol)

```
import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
```

This is a base contract to aid in writing upgradeable contracts, or any kind of contract that will be deployed behind a proxy. Since proxied contracts do not make use of a constructor, it's common to move constructor logic to an external initializer function, usually called `initialize`. It then becomes necessary to protect this initializer function so it can only be called once. The [`Initializable.initializer`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-initializer--) modifier provided by this contract will have this effect.

The initialization functions use a version number. Once a version number is used, it is consumed and cannot be reused. This mechanism prevents re-execution of each "step" but allows the creation of new initialization steps in case an upgrade adds a module that needs to be initialized.

For example:

\[.hljs-theme-light.nopadding\]

```
contract MyToken is ERC20Upgradeable {
    function initialize() initializer public {
        __ERC20_init("MyToken", "MTK");
    }
}

contract MyTokenV2 is MyToken, ERC20PermitUpgradeable {
    function initializeV2() reinitializer(2) public {
        __ERC20Permit_init("MyToken");
    }
}
```

To avoid leaving the proxy in an uninitialized state, the initializer function should be called as early as possible by providing the encoded function call as the `_data` argument to [`ERC1967Proxy.constructor`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy-constructor-address-bytes-).

When used with inheritance, manual care must be taken to not invoke a parent initializer twice, or to ensure that all initializers are idempotent. This is not verified automatically as constructors are by Solidity.

Avoid leaving a contract uninitialized.

An uninitialized contract can be taken over by an attacker. This applies to both a proxy and its implementation contract, which may impact the proxy. To prevent the implementation contract from being used, you should invoke the [`Initializable._disableInitializers`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_disableInitializers--) function in the constructor to automatically lock it when it is deployed:

\[.hljs-theme-light.nopadding\]

```
/// @custom:oz-upgrades-unsafe-allow constructor
constructor() {
    _disableInitializers();
}
```

### Modifiers

-   [initializer()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-initializer--)
-   [reinitializer(version)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-reinitializer-uint64-)
-   [onlyInitializing()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-onlyInitializing--)

### Functions

-   [\_checkInitializing()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_checkInitializing--)
-   [\_disableInitializers()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_disableInitializers--)
-   [\_getInitializedVersion()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_getInitializedVersion--)
-   [\_isInitializing()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_isInitializing--)
-   [\_initializableStorageSlot()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_initializableStorageSlot--)

### Events

-   [Initialized(version)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-Initialized-uint64-)

### Errors

-   [InvalidInitialization()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-InvalidInitialization--)
-   [NotInitializing()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-NotInitializing--)

initializer()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-initializer--)

A modifier that defines a protected initializer function that can be invoked at most once. In its scope, `onlyInitializing` functions can be used to initialize parent contracts.

Similar to `reinitializer(1)`, except that in the context of a constructor an `initializer` may be invoked any number of times. This behavior in the constructor can be useful during testing and is not expected to be used in production.

Emits an [`Initializable.Initialized`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-Initialized-uint64-) event.

reinitializer(uint64 version)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-reinitializer-uint64-)

A modifier that defines a protected reinitializer function that can be invoked at most once, and only if the contract hasn't been initialized to a greater version before. In its scope, `onlyInitializing` functions can be used to initialize parent contracts.

A reinitializer may be used after the original initialization step. This is essential to configure modules that are added through upgrades and that require initialization.

When `version` is 1, this modifier is similar to `initializer`, except that functions marked with `reinitializer` cannot be nested. If one is invoked in the context of another, execution will revert.

Note that versions can jump in increments greater than 1; this implies that if multiple reinitializers coexist in a contract, executing them in the right order is up to the developer or operator.

Setting the version to 2\*\*64 - 1 will prevent any future reinitialization.

Emits an [`Initializable.Initialized`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-Initialized-uint64-) event.

onlyInitializing()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-onlyInitializing--)

Modifier to protect an initialization function so that it can only be invoked by functions with the [`Initializable.initializer`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-initializer--) and [`Initializable.reinitializer`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-reinitializer-uint64-) modifiers, directly or indirectly.

\_checkInitializing()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_checkInitializing--)

Reverts if the contract is not in an initializing state. See [`Initializable.onlyInitializing`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-onlyInitializing--).

\_disableInitializers()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_disableInitializers--)

Locks the contract, preventing any future reinitialization. This cannot be part of an initializer call. Calling this in the constructor of a contract will prevent that contract from being initialized or reinitialized to any version. It is recommended to use this to lock implementation contracts that are designed to be called through proxies.

Emits an [`Initializable.Initialized`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-Initialized-uint64-) event the first time it is successfully executed.

\_getInitializedVersion() → uint64

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_getInitializedVersion--)

Returns the highest version that has been initialized. See [`Initializable.reinitializer`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-reinitializer-uint64-).

\_isInitializing() → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_isInitializing--)

Returns `true` if the contract is currently initializing. See [`Initializable.onlyInitializing`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-onlyInitializing--).

\_initializableStorageSlot() → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-_initializableStorageSlot--)

Pointer to storage slot. Allows integrators to override it with a custom storage location.

Consider following the ERC-7201 formula to derive storage locations.

Initialized(uint64 version)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-Initialized-uint64-)

Triggered when the contract has been initialized or reinitialized.

InvalidInitialization()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-InvalidInitialization--)

The contract is already initialized.

NotInitializing()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#Initializable-NotInitializing--)

The contract is not initializing.

## [`UUPSUpgradeable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#uupsupgradeable)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/proxy/utils/UUPSUpgradeable.sol)

```
import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";
```

An upgradeability mechanism designed for UUPS proxies. The functions included here can perform an upgrade of an [`ERC1967Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Proxy), when this contract is set as the implementation behind such a proxy.

A security mechanism ensures that an upgrade does not turn off upgradeability accidentally, although this risk is reinstated if the upgrade retains upgradeability but removes the security mechanism, e.g. by replacing `UUPSUpgradeable` with a custom implementation of upgrades.

The [`UUPSUpgradeable._authorizeUpgrade`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_authorizeUpgrade-address-) function must be overridden to include access restriction to the upgrade mechanism.

@custom:stateless

### Modifiers

-   [onlyProxy()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-onlyProxy--)
-   [notDelegated()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-notDelegated--)

### Functions

-   [proxiableUUID()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-proxiableUUID--)
-   [upgradeToAndCall(newImplementation, data)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-upgradeToAndCall-address-bytes-)
-   [\_checkProxy()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_checkProxy--)
-   [\_checkNotDelegated()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_checkNotDelegated--)
-   [\_authorizeUpgrade(newImplementation)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_authorizeUpgrade-address-)
-   [UPGRADE\_INTERFACE\_VERSION()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-UPGRADE_INTERFACE_VERSION-string)

### Errors

-   [UUPSUnauthorizedCallContext()](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-UUPSUnauthorizedCallContext--)
-   [UUPSUnsupportedProxiableUUID(slot)](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-UUPSUnsupportedProxiableUUID-bytes32-)

onlyProxy()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-onlyProxy--)

Check that the execution is being performed through a delegatecall call and that the execution context is a proxy contract with an implementation (as defined in ERC-1967) pointing to self. This should only be the case for UUPS and transparent proxies that are using the current contract as their implementation. Execution of a function through ERC-1167 minimal proxies (clones) would not normally pass this test, but is not guaranteed to fail.

notDelegated()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-notDelegated--)

Check that the execution is not being performed through a delegate call. This allows a function to be callable on the implementing contract but not through proxies.

proxiableUUID() → bytes32

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-proxiableUUID--)

Implementation of the ERC-1822 [`UUPSUpgradeable.proxiableUUID`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-proxiableUUID--) function. This returns the storage slot used by the implementation. It is used to validate the implementation's compatibility when performing an upgrade.

A proxy pointing at a proxiable contract should not be considered proxiable itself, because this risks bricking a proxy that upgrades to it, by delegating to itself until out of gas. Thus it is critical that this function revert if invoked through a proxy. This is guaranteed by the `notDelegated` modifier.

upgradeToAndCall(address newImplementation, bytes data)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-upgradeToAndCall-address-bytes-)

Upgrade the implementation of the proxy to `newImplementation`, and subsequently execute the function call encoded in `data`.

Calls [`UUPSUpgradeable._authorizeUpgrade`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_authorizeUpgrade-address-).

Emits an [`UpgradeableBeacon.Upgraded`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UpgradeableBeacon-Upgraded-address-) event.

\_checkProxy()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_checkProxy--)

Reverts if the execution is not performed via delegatecall or the execution context is not of a proxy with an ERC-1967 compliant implementation pointing to self.

\_checkNotDelegated()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_checkNotDelegated--)

Reverts if the execution is performed via delegatecall. See [`UUPSUpgradeable.notDelegated`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-notDelegated--).

\_authorizeUpgrade(address newImplementation)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-_authorizeUpgrade-address-)

Function that should revert when `msg.sender` is not authorized to upgrade the contract. Called by [`ERC1967Utils.upgradeToAndCall`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ERC1967Utils-upgradeToAndCall-address-bytes-).

Normally, this function will use an [access control](https://docs.openzeppelin.com/contracts/5.x/api/access) modifier such as [`Ownable.onlyOwner`](https://docs.openzeppelin.com/contracts/5.x/api/access#Ownable-onlyOwner--).

```
function _authorizeUpgrade(address) internal onlyOwner {}
```

UPGRADE\_INTERFACE\_VERSION() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-UPGRADE_INTERFACE_VERSION-string)

The version of the upgrade interface of the contract. If this getter is missing, both `upgradeTo(address)` and `upgradeToAndCall(address,bytes)` are present, and `upgradeTo` must be used if no function should be called, while `upgradeToAndCall` will invoke the `receive` function if the second argument is the empty byte string. If the getter returns `"5.0.0"`, only `upgradeToAndCall(address,bytes)` is present, and the second argument must be the empty byte string if no function should be called, making it impossible to invoke the `receive` function during an upgrade.

UUPSUnauthorizedCallContext()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-UUPSUnauthorizedCallContext--)

The call is from an unauthorized context.

UUPSUnsupportedProxiableUUID(bytes32 slot)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/proxy#UUPSUpgradeable-UUPSUnsupportedProxiableUUID-bytes32-)

The storage `slot` is unsupported as a UUID.

[

Meta Transactions

Previous Page

](https://docs.openzeppelin.com/contracts/5.x/api/metatx)[

Common

Next Page

](https://docs.openzeppelin.com/contracts/5.x/api/token/common)

### On this page

[Transparent vs UUPS Proxies](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparent-vs-uups-proxies)[Core](https://docs.openzeppelin.com/contracts/5.x/api/proxy#core)[ERC-1967](https://docs.openzeppelin.com/contracts/5.x/api/proxy#erc-1967)[Transparent Proxy](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparent-proxy)[Beacon](https://docs.openzeppelin.com/contracts/5.x/api/proxy#beacon)[Minimal Clones](https://docs.openzeppelin.com/contracts/5.x/api/proxy#minimal-clones)[Utils](https://docs.openzeppelin.com/contracts/5.x/api/proxy#utils)[`Clones`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#clones)[`ERC1967Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#erc1967proxy)[`ERC1967Utils`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#erc1967utils)[`Proxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#proxy)[`BeaconProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#beaconproxy)[`IBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#ibeacon)[`UpgradeableBeacon`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#upgradeablebeacon)[`ProxyAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#proxyadmin)[`ITransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#itransparentupgradeableproxy)[`TransparentUpgradeableProxy`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#transparentupgradeableproxy)[`Initializable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#initializable)[`UUPSUpgradeable`](https://docs.openzeppelin.com/contracts/5.x/api/proxy#uupsupgradeable)
