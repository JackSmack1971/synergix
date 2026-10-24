---
title: "Governance"
source_url: "https://docs.openzeppelin.com/contracts/5.x/api/governance"
host: "docs.openzeppelin.com"
depth: 2
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:51.185Z"
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

# Governance

Smart contract governance utilities and implementations

Copy Markdown

[Open in Claude](https://claude.ai/new?q=Read+https%3A%2F%2Fraw.githubusercontent.com%2FOpenZeppelin%2Fdocs%2Frefs%2Fheads%2Fmain%2Fcontent%2Fcontracts%2F5.x%2Fapi%2Fgovernance.mdx%2C+I+want+to+ask+questions+about+it.)

This directory includes primitives for on-chain governance.

## [Governor](https://docs.openzeppelin.com/contracts/5.x/api/governance#governor)

This modular system of Governor contracts allows the deployment on-chain voting protocols similar to [Compound’s Governor Alpha & Bravo](https://compound.finance/docs/governance) and beyond, through the ability to easily customize multiple aspects of the protocol.

For a guided experience, set up your Governor contract using [Contracts Wizard](https://wizard.openzeppelin.com/#governor).

For a written walkthrough, check out our guide on [How to set up on-chain governance](https://docs.openzeppelin.com/contracts/5.x/governance).

-   [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor): The core contract that contains all the logic and primitives. It is abstract and requires choosing one of each of the modules below, or custom ones.

Votes modules determine the source of voting power, and sometimes quorum number.

-   [`GovernorVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes): Extracts voting weight from an [`IVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes) contract.
-   [`GovernorVotesQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction): Combines with `GovernorVotes` to set the quorum as a fraction of the total token supply.
-   [`GovernorVotesSuperQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction): Combines `GovernorSuperQuorum` with `GovernorVotesQuorumFraction` to set the super quorum as a fraction of the total token supply.

Counting modules determine valid voting options.

-   [`GovernorCountingSimple`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple): Simple voting mechanism with 3 voting options: Against, For and Abstain.
-   [`GovernorCountingFractional`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional): A more modular voting system that allows a user to vote with only part of its voting power, and to split that weight arbitrarily between the 3 different options (Against, For and Abstain).
-   [`GovernorCountingOverridable`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable): An extended version of `GovernorCountingSimple` which allows delegatees to override their delegates while the vote is live. Must be used in conjunction with [`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended).

Timelock extensions add a delay for governance decisions to be executed. The workflow is extended to require a `queue` step before execution. With these modules, proposals are executed by the external timelock contract, thus it is the timelock that has to hold the assets that are being governed.

-   [`GovernorTimelockAccess`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess): Connects with an instance of an [`AccessManager`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager). This allows restrictions (and delays) enforced by the manager to be considered by the Governor and integrated into the AccessManager’s "schedule + execute" workflow.
-   [`GovernorTimelockControl`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl): Connects with an instance of [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController). Allows multiple proposers and executors, in addition to the Governor itself.
-   [`GovernorTimelockCompound`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound): Connects with an instance of Compound’s [`Timelock`](https://github.com/compound-finance/compound-protocol/blob/master/contracts/Timelock.sol) contract.

Other extensions can customize the behavior or interface in multiple ways.

-   [`GovernorStorage`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage): Stores the proposal details onchain and provides enumerability of the proposals. This can be useful for some L2 chains where storage is cheap compared to calldata.
-   [`GovernorSettings`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings): Manages some of the settings (voting delay, voting period duration, and proposal threshold) in a way that can be updated through a governance proposal, without requiring an upgrade.
-   [`GovernorPreventLateQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum): Ensures there is a minimum voting period after quorum is reached as a security protection against large voters.
-   [`GovernorProposalGuardian`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian): Adds a proposal guardian that can cancel proposals at any stage in their lifecycle--this permission is passed on to the proposers if the guardian is not set.
-   [`GovernorSuperQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum): Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) with a super quorum. Proposals that meet the super quorum (and have a majority of for votes) advance to the `Succeeded` state before the proposal deadline.
-   [`GovernorNoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed): An extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) with support for keyed nonces in addition to traditional nonces when voting by signature.

In addition to modules and extensions, the core contract requires a few virtual functions to be implemented to your particular specifications:

-   [`votingDelay()`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay-): Delay (in ERC-6372 clock) since the proposal is submitted until voting power is fixed and voting starts. This can be used to enforce a delay after a proposal is published for users to buy tokens, or delegate their votes.
-   [`votingPeriod()`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod-): Delay (in ERC-6372 clock) since the proposal starts until voting ends.
-   [`quorum(uint256 timepoint)`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-): Quorum required for a proposal to be successful. This function includes a `timepoint` argument (see ERC-6372) so the quorum can adapt through time, for example, to follow a token’s `totalSupply`.

Functions of the `Governor` contract do not include access control. If you want to restrict access, you should add these checks by overloading the particular functions. Among these, [`Governor._cancel`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-) is internal by default, and you will have to expose it (with the right access control mechanism) yourself if this function is needed.

### [Core](https://docs.openzeppelin.com/contracts/5.x/api/governance#core)

[`IGovernor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor)

[`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor)

### [Modules](https://docs.openzeppelin.com/contracts/5.x/api/governance#modules)

[`GovernorCountingSimple`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple)

[`GovernorCountingFractional`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional)

[`GovernorCountingOverridable`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable)

[`GovernorVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes)

[`GovernorVotesQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction)

[`GovernorVotesSuperQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction)

### [Extensions](https://docs.openzeppelin.com/contracts/5.x/api/governance#extensions)

[`GovernorTimelockAccess`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess)

[`GovernorTimelockControl`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl)

[`GovernorTimelockCompound`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound)

[`GovernorSettings`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings)

[`GovernorPreventLateQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum)

[`GovernorStorage`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage)

[`GovernorProposalGuardian`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian)

[`GovernorSuperQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum)

[`GovernorNoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed)

## [Utils](https://docs.openzeppelin.com/contracts/5.x/api/governance#utils)

[`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes)

[`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended)

## [Timelock](https://docs.openzeppelin.com/contracts/5.x/api/governance#timelock)

In a governance system, the [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController) contract is in charge of introducing a delay between a proposal and its execution. It can be used with or without a [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor).

[`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController)

#### [Terminology](https://docs.openzeppelin.com/contracts/5.x/api/governance#terminology)

-   **Operation:** A transaction (or a set of transactions) that is the subject of the timelock. It has to be scheduled by a proposer and executed by an executor. The timelock enforces a minimum delay between the proposition and the execution. If the operation contains multiple transactions (batch mode), they are executed atomically. Operations are identified by the hash of their content.
-   **Operation status:**
    -   **Unset:** An operation that is not part of the timelock mechanism.
    -   **Waiting:** An operation that has been scheduled, before the timer expires.
    -   **Ready:** An operation that has been scheduled, after the timer expires.
    -   **Pending:** An operation that is either waiting or ready.
    -   **Done:** An operation that has been executed.
-   **Predecessor**: An (optional) dependency between operations. An operation can depend on another operation (its predecessor), forcing the execution order of these two operations.
-   **Role**:
    -   **Admin:** An address (smart contract or EOA) that is in charge of granting the roles of Proposer and Executor.
    -   **Proposer:** An address (smart contract or EOA) that is in charge of scheduling (and cancelling) operations.
    -   **Executor:** An address (smart contract or EOA) that is in charge of executing operations once the timelock has expired. This role can be given to the zero address to allow anyone to execute operations.

#### [Operation structure](https://docs.openzeppelin.com/contracts/5.x/api/governance#operation-structure)

Operation executed by the [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController) can contain one or multiple subsequent calls. Depending on whether you need multiple calls to be executed atomically, you can either use simple or batched operations.

Both operations contain:

-   **Target**, the address of the smart contract that the timelock should operate on.
-   **Value**, in wei, that should be sent with the transaction. Most of the time this will be 0. Ether can be deposited before-end or passed along when executing the transaction.
-   **Data**, containing the encoded function selector and parameters of the call. This can be produced using a number of tools. For example, a maintenance operation granting role `ROLE` to `ACCOUNT` can be encoded using web3js as follows:

```
const data = timelock.contract.methods.grantRole(ROLE, ACCOUNT).encodeABI()
```

-   **Predecessor**, that specifies a dependency between operations. This dependency is optional. Use `bytes32(0)` if the operation does not have any dependency.
-   **Salt**, used to disambiguate two otherwise identical operations. This can be any random value.

In the case of batched operations, `target`, `value` and `data` are specified as arrays, which must be of the same length.

#### [Operation lifecycle](https://docs.openzeppelin.com/contracts/5.x/api/governance#operation-lifecycle)

Timelocked operations are identified by a unique id (their hash) and follow a specific lifecycle:

`Unset` -> `Pending` -> `Pending` + `Ready` -> `Done`

-   By calling [`schedule`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-schedule-address-uint256-bytes-bytes32-bytes32-uint256-) (or [`scheduleBatch`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-scheduleBatch-address---uint256---bytes---bytes32-bytes32-uint256-)), a proposer moves the operation from the `Unset` to the `Pending` state. This starts a timer that must be longer than the minimum delay. The timer expires at a timestamp accessible through the [`getTimestamp`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-getTimestamp-bytes32-) method.
-   Once the timer expires, the operation automatically gets the `Ready` state. At this point, it can be executed.
-   By calling [`execute`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockController-execute-address-uint256-bytes-bytes32-bytes32-) (or [`executeBatch`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-executeBatch-address---uint256---bytes---bytes32-bytes32-)), an executor triggers the operation’s underlying transactions and moves it to the `Done` state. If the operation has a predecessor, it has to be in the `Done` state for this transition to succeed.
-   [`cancel`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockController-cancel-bytes32-) allows proposers to cancel any `Pending` operation. This resets the operation to the `Unset` state. It is thus possible for a proposer to re-schedule an operation that has been cancelled. In this case, the timer restarts when the operation is rescheduled.

Operations status can be queried using the functions:

-   [`isOperationPending(bytes32)`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationPending-bytes32-)
-   [`isOperationReady(bytes32)`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationReady-bytes32-)
-   [`isOperationDone(bytes32)`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationDone-bytes32-)

#### [Roles](https://docs.openzeppelin.com/contracts/5.x/api/governance#roles)

##### [Admin](https://docs.openzeppelin.com/contracts/5.x/api/governance#admin)

The admins are in charge of managing proposers and executors. For the timelock to be self-governed, this role should only be given to the timelock itself. Upon deployment, the admin role can be granted to any address (in addition to the timelock itself). After further configuration and testing, this optional admin should renounce its role such that all further maintenance operations have to go through the timelock process.

##### [Proposer](https://docs.openzeppelin.com/contracts/5.x/api/governance#proposer)

The proposers are in charge of scheduling (and cancelling) operations. This is a critical role, that should be given to governing entities. This could be an EOA, a multisig, or a DAO.

**Proposer fight:** Having multiple proposers, while providing redundancy in case one becomes unavailable, can be dangerous. Proposers have a say on all operations--they could cancel operations they disagree with, including operations to remove them from the list of proposers.

This role is identified by the **PROPOSER\_ROLE** value: `0xb09aa5aeb3702cfd50b6b62bc4532604938f21248a27a1d5ca736082b6819cc1`

##### [Executor](https://docs.openzeppelin.com/contracts/5.x/api/governance#executor)

The executors are in charge of executing the operations scheduled by the proposers once the timelock expires. Logic dictates that multisig or DAO that are proposers should also be executors in order to guarantee operations that have been scheduled will eventually be executed. However, having additional executors can reduce the cost (the executing transaction does not require validation by the multisig or DAO that proposed it), while ensuring whoever is in charge of execution cannot trigger actions that have not been scheduled by the proposers. Alternatively, it is possible to allow *any* address to execute a proposal once the timelock has expired by granting the executor role to the zero address.

This role is identified by the **EXECUTOR\_ROLE** value: `0xd8aa0f3194971a2a116679f7c2090f6939c8d4e01a2a8d7e41d55e5351469e63`

A live contract without at least one proposer and one executor is locked. Make sure these roles are filled by reliable entities before the deployer renounces its administrative rights in favour of the timelock contract itself. See the [`AccessControl`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessControl) documentation to learn more about role management.

## [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governor-1)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/Governor.sol)

```
import "@openzeppelin/contracts/governance/Governor.sol";
```

Core of the governance system, designed to be extended through various modules.

This contract is abstract and requires several functions to be implemented in various modules:

-   A counting module must implement [`Governor._quorumReached`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-), [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-) and [`Governor._countVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   A voting module must implement [`Governor._getVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   Additionally, [`Governor.votingPeriod`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--), [`Governor.votingDelay`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--), and [`Governor.quorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-) must also be implemented

### Modifiers

-   [onlyGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onlyGovernance--)

### Functions

-   [constructor(name\_)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-constructor-string-)
-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

onlyGovernance()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onlyGovernance--)

Restricts a function so it can only be executed through governance proposals. For example, governance parameter setters in [`GovernorSettings`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings) are protected using this modifier.

The governance executing address may be different from the Governor's own address, for example it could be a timelock. This can be customized by modules by overriding [`Governor._executor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--). The executor is only able to invoke these functions during the execution of the governor's [`Governor.execute`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-) function, and not under any other circumstances. Thus, for example, additional timelock proposers are not able to change governance parameters without going through the governance protocol (since v4.6).

constructor(string name\_)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-constructor-string-)

Sets the value for [`Governor.name`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--) and [`Governor.version`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)

receive()

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)

Function to receive ETH that will be handled by the governor (disabled if executor is a third party contract)

supportsInterface(bytes4 interfaceId) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)

Returns true if this contract implements the interface defined by `interfaceId`. See the corresponding [ERC section](https://eips.ethereum.org/EIPS/eip-165#how-interfaces-are-identified) to learn more about how these ids are created.

This function call must use less than 30 000 gas.

name() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)

Name of the governor instance (used in building the EIP-712 domain separator).

version() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)

Version of the governor instance (used in building the EIP-712 domain separator). Default: "1"

hashProposal(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)

See [`IGovernor.hashProposal`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hashProposal-address---uint256---bytes---bytes32-).

The proposal id is produced by hashing the ABI encoded `targets` array, the `values` array, the `calldatas` array and the descriptionHash (bytes32 which itself is the keccak256 hash of the description string). This proposal id can be produced from the proposal data which is part of the [`IGovernor.ProposalCreated`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-) event. It can even be computed in advance, before the proposal is submitted.

Note that the chainId and the governor address are not part of the proposal id computation. Consequently, the same proposal (with same operation and same description) will have the same id if submitted on multiple governors across multiple networks. This also means that in order to execute the same operation twice (on the same governor) the proposer will have to change the description in order to avoid proposal id conflicts.

getProposalId(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)

Function used to get the proposal id from the proposal details.

state(uint256 proposalId) → enum IGovernor.ProposalState

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)

Current state of a proposal, following Compound's convention

proposalThreshold() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)

The number of votes required in order for a voter to become a proposer.

proposalSnapshot(uint256 proposalId) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)

Timepoint used to retrieve user's votes and quorum. If using block number (as per Compound's Comp), the snapshot is performed at the end of this block. Hence, voting for this proposal starts at the beginning of the following block.

proposalDeadline(uint256 proposalId) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)

Timepoint at which votes close. If using block number, votes close at the end of this block, so it is possible to cast a vote during this block.

proposalProposer(uint256 proposalId) → address

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)

The account that created a proposal.

proposalEta(uint256 proposalId) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)

The time when a queued proposal becomes executable ("ETA"). Unlike [`Governor.proposalSnapshot`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-) and [`Governor.proposalDeadline`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-), this doesn't use the governor clock, and instead relies on the executor's clock which may be different. In most cases this will be a timestamp.

proposalNeedsQueuing(uint256) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)

Whether a proposal needs to be queued before execution.

\_checkGovernance()

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)

Reverts if the `msg.sender` is not the executor. In case the executor is not this contract itself, the function reverts if `msg.data` is not whitelisted as a result of an [`Governor.execute`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-) operation. See [`Governor.onlyGovernance`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onlyGovernance--).

\_quorumReached(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)

Amount of votes already cast passes the threshold limit.

\_voteSucceeded(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)

Is the proposal successful or not.

\_getVotes(address account, uint256 timepoint, bytes params) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)

Get the voting weight of `account` at a specific `timepoint`, for a vote as described by `params`.

\_countVote(uint256 proposalId, address account, uint8 support, uint256 totalWeight, bytes params) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)

Register a vote for `proposalId` by `account` with a given `support`, voting `weight` and voting `params`.

Note: Support is generic and can represent various things depending on the voting system used.

\_tallyUpdated(uint256 proposalId)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)

Hook that should be called every time the tally for a proposal is updated.

Note: This function must run successfully. Reverts will result in the bricking of governance

\_defaultParams() → bytes

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)

Default additional encoded parameters used by castVote methods that don't include them

Note: Should be overridden by specific implementations to use an appropriate value, the meaning of the additional params, in the context of that implementation

propose(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, string description) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)

See [`IGovernor.propose`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-propose-address---uint256---bytes---string-). This function has opt-in frontrunning protection, described in [`Governor._isValidDescriptionForProposer`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-).

\_propose(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, string description, address proposer) → uint256 proposalId

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)

Internal propose mechanism. Can be overridden to add more logic on proposal creation.

Emits a [`IGovernor.ProposalCreated`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-) event.

queue(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)

Queue a proposal. Some governors require this step to be performed before execution can happen. If queuing is not necessary, this function may revert. Queuing a proposal requires the quorum to be reached, the vote to be successful, and the deadline to be reached.

Emits a [`IGovernor.ProposalQueued`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-) event.

\_queueOperations(uint256, address\[\], uint256\[\], bytes\[\], bytes32) → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)

Internal queuing mechanism. Can be overridden (without a super call) to modify the way queuing is performed (for example adding a vault/timelock).

This is empty by default, and must be overridden to implement queuing.

This function returns a timestamp that describes the expected ETA for execution. If the returned value is 0 (which is the default value), the core will consider queueing did not succeed, and the public [`Governor.queue`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-) function will revert.

Calling this function directly will NOT check the current state of the proposal, or emit the `ProposalQueued` event. Queuing a proposal should be done using [`Governor.queue`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-).

execute(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)

Execute a successful proposal. This requires the quorum to be reached, the vote to be successful, and the deadline to be reached. Depending on the governor it might also be required that the proposal was queued and that some delay passed.

Emits a [`IGovernor.ProposalExecuted`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-) event.

Some modules can modify the requirements for execution, for example by adding an additional timelock.

\_executeOperations(uint256, address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)

Internal execution mechanism. Can be overridden (without a super call) to modify the way execution is performed (for example adding a vault/timelock).

Calling this function directly will NOT check the current state of the proposal, set the executed flag to true or emit the `ProposalExecuted` event. Executing a proposal should be done using [`Governor.execute`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-).

cancel(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)

Cancel a proposal. A proposal is cancellable by the proposer, but only while it is Pending state, i.e. before the vote starts.

Emits a [`IGovernor.ProposalCanceled`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-) event.

\_cancel(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)

Internal cancel mechanism with minimal restrictions. A proposal can be cancelled in any state other than Canceled, Expired, or Executed. Once cancelled a proposal can't be re-submitted.

Emits a [`IGovernor.ProposalCanceled`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-) event.

getVotes(address account, uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)

Voting power of an `account` at a specific `timepoint`.

Note: this can be implemented in a number of ways, for example by reading the delegated balance from one (or multiple), [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes) tokens.

getVotesWithParams(address account, uint256 timepoint, bytes params) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)

Voting power of an `account` at a specific `timepoint` given additional encoded parameters.

castVote(uint256 proposalId, uint8 support) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)

Cast a vote

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

castVoteWithReason(uint256 proposalId, uint8 support, string reason) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)

Cast a vote with a reason

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

castVoteWithReasonAndParams(uint256 proposalId, uint8 support, string reason, bytes params) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)

Cast a vote with a reason and additional encoded parameters

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) or [`IGovernor.VoteCastWithParams`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-) event depending on the length of params.

castVoteBySig(uint256 proposalId, uint8 support, address voter, bytes signature) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)

Cast a vote using the voter's signature, including ERC-1271 signature support.

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

castVoteWithReasonAndParamsBySig(uint256 proposalId, uint8 support, address voter, string reason, bytes params, bytes signature) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)

Cast a vote with a reason and additional encoded parameters using the voter's signature, including ERC-1271 signature support.

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) or [`IGovernor.VoteCastWithParams`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-) event depending on the length of params.

\_validateVoteSig(uint256 proposalId, uint8 support, address voter, bytes signature) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)

Validate the `signature` used in [`Governor.castVoteBySig`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-) function.

\_validateExtendedVoteSig(uint256 proposalId, uint8 support, address voter, string reason, bytes params, bytes signature) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)

Validate the `signature` used in [`Governor.castVoteWithReasonAndParamsBySig`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-) function.

\_castVote(uint256 proposalId, address account, uint8 support, string reason) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)

Internal vote casting mechanism: Check that the vote is pending, that it has not been cast yet, retrieve voting weight using [`IGovernor.getVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getVotes-address-uint256-) and call the [`Governor._countVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-) internal function. Uses the \_defaultParams().

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

\_castVote(uint256 proposalId, address account, uint8 support, string reason, bytes params) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)

Internal vote casting mechanism: Check that the vote is pending, that it has not been cast yet, retrieve voting weight using [`IGovernor.getVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getVotes-address-uint256-) and call the [`Governor._countVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-) internal function.

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

relay(address target, uint256 value, bytes data)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)

Relays a transaction or function call to an arbitrary target. In cases where the governance executor is some contract other than the governor itself, like when using a timelock, this function can be invoked in a governance proposal to recover tokens or Ether that was sent to the governor contract by mistake. Note that if the executor is simply the governor itself, use of `relay` is redundant.

\_executor() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)

Address through which the governor executes action. Will be overloaded by module that executes actions through another contract such as a timelock.

onERC721Received(address, address, uint256, bytes) → bytes4

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)

See [`IERC721Receiver.onERC721Received`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#IERC721Receiver-onERC721Received-address-address-uint256-bytes-). Receiving tokens is disabled if the governance executor is other than the governor itself (eg. when using with a timelock).

onERC1155Received(address, address, uint256, uint256, bytes) → bytes4

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)

See [`IERC1155Receiver.onERC1155Received`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155Receiver-onERC1155Received-address-address-uint256-uint256-bytes-). Receiving tokens is disabled if the governance executor is other than the governor itself (eg. when using with a timelock).

onERC1155BatchReceived(address, address, uint256\[\], uint256\[\], bytes) → bytes4

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)

See [`IERC1155Receiver.onERC1155BatchReceived`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155Receiver-onERC1155BatchReceived-address-address-uint256---uint256---bytes-). Receiving tokens is disabled if the governance executor is other than the governor itself (eg. when using with a timelock).

\_encodeStateBitmap(enum IGovernor.ProposalState proposalState) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)

Encodes a `ProposalState` into a `bytes32` representation where each bit enabled corresponds to the underlying position in the `ProposalState` enum. For example:

0x000...10000 ^^^^^^------ ... ^----- Succeeded ^---- Defeated ^--- Canceled ^-- Active ^- Pending

\_validateStateBitmap(uint256 proposalId, bytes32 allowedStates) → enum IGovernor.ProposalState

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)

Check that the current state of a proposal matches the requirements described by the `allowedStates` bitmap. This bitmap should be built using `_encodeStateBitmap`.

If requirements are not met, reverts with a [`IGovernor.GovernorUnexpectedProposalState`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-) error.

\_isValidDescriptionForProposer(address proposer, string description) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)

Check if the proposer is authorized to submit a proposal with the given description.

If the proposal description ends with `#proposer=0x???`, where `0x???` is an address written as a hex string (case insensitive), then the submission of this proposal will only be authorized to said address.

This is used for frontrunning protection. By adding this pattern at the end of their proposal, one can ensure that no other address can submit the same proposal. An attacker would have to either remove or change that part, which would result in a different proposal id.

If the description does not match this pattern, it is unrestricted and anyone can submit it. This includes:

-   If the `0x???` part is not a valid hex string.
-   If the `0x???` part is a valid hex string, but does not contain exactly 40 hex digits.
-   If it ends with the expected suffix followed by newlines or other whitespace.
-   If it ends with some other similar suffix, e.g. `#other=abc`.
-   If it does not end with any such suffix.

\_validateCancel(uint256 proposalId, address caller) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)

Check if the `caller` can cancel the proposal with the given `proposalId`.

The default implementation allows the proposal proposer to cancel the proposal during the pending state.

clock() → uint48

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)

Clock used for flagging checkpoints. Can be overridden to implement timestamp based checkpoints (and voting).

CLOCK\_MODE() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)

Description of the clock

votingDelay() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)

Delay, between the proposal is created and the vote starts. The unit this duration is expressed in depends on the clock (see ERC-6372) this contract uses.

This can be increased to leave time for users to buy voting power, or delegate it, before the voting of a proposal starts.

While this interface returns a uint256, timepoints are stored as uint48 following the ERC-6372 clock type. Consequently this value must fit in a uint48 (when added to the current clock). See [`IERC6372.clock`](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC6372-clock--).

votingPeriod() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)

Delay between the vote start and vote end. The unit this duration is expressed in depends on the clock (see ERC-6372) this contract uses.

The [`Governor.votingDelay`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--) can delay the start of the vote. This must be considered when setting the voting duration compared to the voting delay.

This value is stored when the proposal is submitted so that possible changes to the value do not affect proposals that have already been submitted. The type used to save it is a uint32. Consequently, while this interface returns a uint256, the value it returns should fit in a uint32.

quorum(uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)

Minimum number of cast voted required for a proposal to be successful.

The `timepoint` parameter corresponds to the snapshot used for counting vote. This allows to scale the quorum depending on values such as the totalSupply of a token at this timepoint (see [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes)).

BALLOT\_TYPEHASH() → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)

EXTENDED\_BALLOT\_TYPEHASH() → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

## [`IGovernor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#igovernor)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/IGovernor.sol)

```
import "@openzeppelin/contracts/governance/IGovernor.sol";
```

Interface of the [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) core.

Event parameters lack the `indexed` keyword for compatibility with GovernorBravo events. Making event parameters `indexed` affects how events are decoded, potentially breaking existing indexers.

### Functions

-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-version--)
-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalEta-uint256-)
-   [proposalNeedsQueuing(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalNeedsQueuing-uint256-)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-quorum-uint256-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getVotesWithParams-address-uint256-bytes-)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-propose-address---uint256---bytes---string-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-queue-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-execute-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-cancel-address---uint256---bytes---bytes32-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)

IERC6372

-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC6372-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC6372-CLOCK_MODE--)

IERC165

-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC165-supportsInterface-bytes4-)

### Events

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

### Errors

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

name() → string

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-name--)

Name of the governor instance (used in building the EIP-712 domain separator).

version() → string

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-version--)

Version of the governor instance (used in building the EIP-712 domain separator). Default: "1"

COUNTING\_MODE() → string

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)

A description of the possible `support` values for [`Governor.castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-) and the way these votes are counted, meant to be consumed by UIs to show correct vote options and interpret the results. The string is a URL-encoded sequence of key-value pairs that each describe one aspect, for example `support=bravo&quorum=for,abstain`.

There are 2 standard keys: `support` and `quorum`.

-   `support=bravo` refers to the vote options 0 = Against, 1 = For, 2 = Abstain, as in `GovernorBravo`.
-   `quorum=bravo` means that only For votes are counted towards quorum.
-   `quorum=for,abstain` means that both For and Abstain votes are counted towards quorum.

If a counting module makes use of encoded `params`, it should include this under a `params` key with a unique name that describes the behavior. For example:

-   `params=fractional` might refer to a scheme where votes are divided fractionally between for/against/abstain.
-   `params=erc721` might refer to a scheme where specific NFTs are delegated to vote.

The string can be decoded by the standard [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) JavaScript class.

hashProposal(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hashProposal-address---uint256---bytes---bytes32-)

Hashing function used to (re)build the proposal id from the proposal details.

For all off-chain and external calls, use [`Governor.getProposalId`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-).

getProposalId(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getProposalId-address---uint256---bytes---bytes32-)

Function used to get the proposal id from the proposal details.

state(uint256 proposalId) → enum IGovernor.ProposalState

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-state-uint256-)

Current state of a proposal, following Compound's convention

proposalThreshold() → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalThreshold--)

The number of votes required in order for a voter to become a proposer.

proposalSnapshot(uint256 proposalId) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalSnapshot-uint256-)

Timepoint used to retrieve user's votes and quorum. If using block number (as per Compound's Comp), the snapshot is performed at the end of this block. Hence, voting for this proposal starts at the beginning of the following block.

proposalDeadline(uint256 proposalId) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalDeadline-uint256-)

Timepoint at which votes close. If using block number, votes close at the end of this block, so it is possible to cast a vote during this block.

proposalProposer(uint256 proposalId) → address

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalProposer-uint256-)

The account that created a proposal.

proposalEta(uint256 proposalId) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalEta-uint256-)

The time when a queued proposal becomes executable ("ETA"). Unlike [`Governor.proposalSnapshot`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-) and [`Governor.proposalDeadline`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-), this doesn't use the governor clock, and instead relies on the executor's clock which may be different. In most cases this will be a timestamp.

proposalNeedsQueuing(uint256 proposalId) → bool

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalNeedsQueuing-uint256-)

Whether a proposal needs to be queued before execution.

votingDelay() → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-votingDelay--)

Delay, between the proposal is created and the vote starts. The unit this duration is expressed in depends on the clock (see ERC-6372) this contract uses.

This can be increased to leave time for users to buy voting power, or delegate it, before the voting of a proposal starts.

While this interface returns a uint256, timepoints are stored as uint48 following the ERC-6372 clock type. Consequently this value must fit in a uint48 (when added to the current clock). See [`IERC6372.clock`](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC6372-clock--).

votingPeriod() → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-votingPeriod--)

Delay between the vote start and vote end. The unit this duration is expressed in depends on the clock (see ERC-6372) this contract uses.

The [`Governor.votingDelay`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--) can delay the start of the vote. This must be considered when setting the voting duration compared to the voting delay.

This value is stored when the proposal is submitted so that possible changes to the value do not affect proposals that have already been submitted. The type used to save it is a uint32. Consequently, while this interface returns a uint256, the value it returns should fit in a uint32.

quorum(uint256 timepoint) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-quorum-uint256-)

Minimum number of cast voted required for a proposal to be successful.

The `timepoint` parameter corresponds to the snapshot used for counting vote. This allows to scale the quorum depending on values such as the totalSupply of a token at this timepoint (see [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes)).

getVotes(address account, uint256 timepoint) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getVotes-address-uint256-)

Voting power of an `account` at a specific `timepoint`.

Note: this can be implemented in a number of ways, for example by reading the delegated balance from one (or multiple), [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes) tokens.

getVotesWithParams(address account, uint256 timepoint, bytes params) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-getVotesWithParams-address-uint256-bytes-)

Voting power of an `account` at a specific `timepoint` given additional encoded parameters.

hasVoted(uint256 proposalId, address account) → bool

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Returns whether `account` has cast a vote on `proposalId`.

propose(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, string description) → uint256 proposalId

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-propose-address---uint256---bytes---string-)

Create a new proposal. Vote starts after a delay specified by [`IGovernor.votingDelay`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-votingDelay--) and lasts for a duration specified by [`IGovernor.votingPeriod`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-votingPeriod--).

Emits a [`IGovernor.ProposalCreated`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-) event.

The state of the Governor and `targets` may change between the proposal creation and its execution. This may be the result of third party actions on the targeted contracts, or other governor proposals. For example, the balance of this contract could be updated or its access control permissions may be modified, possibly compromising the proposal's ability to execute successfully (e.g. the governor doesn't have enough value to cover a proposal with multiple transfers).

queue(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256 proposalId

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-queue-address---uint256---bytes---bytes32-)

Queue a proposal. Some governors require this step to be performed before execution can happen. If queuing is not necessary, this function may revert. Queuing a proposal requires the quorum to be reached, the vote to be successful, and the deadline to be reached.

Emits a [`IGovernor.ProposalQueued`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-) event.

execute(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256 proposalId

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-execute-address---uint256---bytes---bytes32-)

Execute a successful proposal. This requires the quorum to be reached, the vote to be successful, and the deadline to be reached. Depending on the governor it might also be required that the proposal was queued and that some delay passed.

Emits a [`IGovernor.ProposalExecuted`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-) event.

Some modules can modify the requirements for execution, for example by adding an additional timelock.

cancel(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256 proposalId

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-cancel-address---uint256---bytes---bytes32-)

Cancel a proposal. A proposal is cancellable by the proposer, but only while it is Pending state, i.e. before the vote starts.

Emits a [`IGovernor.ProposalCanceled`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-) event.

castVote(uint256 proposalId, uint8 support) → uint256 balance

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVote-uint256-uint8-)

Cast a vote

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

castVoteWithReason(uint256 proposalId, uint8 support, string reason) → uint256 balance

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteWithReason-uint256-uint8-string-)

Cast a vote with a reason

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

castVoteWithReasonAndParams(uint256 proposalId, uint8 support, string reason, bytes params) → uint256 balance

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)

Cast a vote with a reason and additional encoded parameters

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) or [`IGovernor.VoteCastWithParams`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-) event depending on the length of params.

castVoteBySig(uint256 proposalId, uint8 support, address voter, bytes signature) → uint256 balance

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteBySig-uint256-uint8-address-bytes-)

Cast a vote using the voter's signature, including ERC-1271 signature support.

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) event.

castVoteWithReasonAndParamsBySig(uint256 proposalId, uint8 support, address voter, string reason, bytes params, bytes signature) → uint256 balance

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)

Cast a vote with a reason and additional encoded parameters using the voter's signature, including ERC-1271 signature support.

Emits a [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) or [`IGovernor.VoteCastWithParams`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-) event depending on the length of params.

ProposalCreated(uint256 proposalId, address proposer, address\[\] targets, uint256\[\] values, string\[\] signatures, bytes\[\] calldatas, uint256 voteStart, uint256 voteEnd, string description)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)

Emitted when a proposal is created.

ProposalQueued(uint256 proposalId, uint256 etaSeconds)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)

Emitted when a proposal is queued.

ProposalExecuted(uint256 proposalId)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)

Emitted when a proposal is executed.

ProposalCanceled(uint256 proposalId)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)

Emitted when a proposal is canceled.

VoteCast(address indexed voter, uint256 proposalId, uint8 support, uint256 weight, string reason)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)

Emitted when a vote is cast without params.

Note: `support` values should be seen as buckets. Their interpretation depends on the voting module used.

VoteCastWithParams(address indexed voter, uint256 proposalId, uint8 support, uint256 weight, string reason, bytes params)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

Emitted when a vote is cast with params.

Note: `support` values should be seen as buckets. Their interpretation depends on the voting module used. `params` are additional encoded parameters. Their interpretation also depends on the voting module used.

GovernorInvalidProposalLength(uint256 targets, uint256 calldatas, uint256 values)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)

Empty proposal or a mismatch between the parameters length for a proposal call.

GovernorAlreadyCastVote(address voter)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)

The vote was already cast.

GovernorDisabledDeposit()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)

Token deposits are disabled in this contract.

GovernorOnlyExecutor(address account)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)

The `account` is not the governance executor.

GovernorNonexistentProposal(uint256 proposalId)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)

The `proposalId` doesn't exist.

GovernorUnexpectedProposalState(uint256 proposalId, enum IGovernor.ProposalState current, bytes32 expectedStates)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)

The current state of a proposal is not the required for performing an operation. The `expectedStates` is a bitmap with the bits enabled for each ProposalState enum position counting from right to left.

If `expectedState` is `bytes32(0)`, the proposal is expected to not be in any state (i.e. not exist). This is the case when a proposal that is expected to be unset is already initiated (the proposal is duplicated).

See [`Governor._encodeStateBitmap`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-).

GovernorInvalidVotingPeriod(uint256 votingPeriod)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)

The voting period set is not a valid period.

GovernorInsufficientProposerVotes(address proposer, uint256 votes, uint256 threshold)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)

The `proposer` does not have the required votes to create a proposal.

GovernorRestrictedProposer(address proposer)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)

The `proposer` is not allowed to create a proposal.

GovernorInvalidVoteType()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)

The vote type used is not valid for the corresponding counting module.

GovernorInvalidVoteParams()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)

The provided params buffer is not supported by the counting module.

GovernorQueueNotImplemented()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)

Queue operation is not implemented for this governor. Execute should be called directly.

GovernorNotQueuedProposal(uint256 proposalId)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)

The proposal hasn't been queued yet.

GovernorAlreadyQueuedProposal(uint256 proposalId)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)

The proposal has already been queued.

GovernorInvalidSignature(address voter)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)

The provided signature is not valid for the expected `voter`. If the `voter` is a contract, the signature is not valid using [`IERC1271.isValidSignature`](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC1271-isValidSignature-bytes32-bytes-).

GovernorUnableToCancel(uint256 proposalId, address account)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

The given `account` is unable to cancel the proposal with given `proposalId`.

## [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#timelockcontroller)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/TimelockController.sol)

```
import "@openzeppelin/contracts/governance/TimelockController.sol";
```

Contract module which acts as a timelocked controller. When set as the owner of an `Ownable` smart contract, it enforces a timelock on all `onlyOwner` maintenance operations. This gives time for users of the controlled contract to exit before a potentially dangerous maintenance operation is applied.

By default, this contract is self administered, meaning administration tasks have to go through the timelock process. The proposer (resp executor) role is in charge of proposing (resp executing) operations. A common use case is to position this [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController) as the owner of a smart contract, with a multisig or a DAO as the sole proposer.

### Modifiers

-   [onlyRoleOrOpenRole(role)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-onlyRoleOrOpenRole-bytes32-)

### Functions

-   [constructor(minDelay, proposers, executors, admin)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-constructor-uint256-address---address---address-)
-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-supportsInterface-bytes4-)
-   [isOperation(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperation-bytes32-)
-   [isOperationPending(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationPending-bytes32-)
-   [isOperationReady(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationReady-bytes32-)
-   [isOperationDone(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationDone-bytes32-)
-   [getTimestamp(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-getTimestamp-bytes32-)
-   [getOperationState(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-getOperationState-bytes32-)
-   [getMinDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-getMinDelay--)
-   [hashOperation(target, value, data, predecessor, salt)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-hashOperation-address-uint256-bytes-bytes32-bytes32-)
-   [hashOperationBatch(targets, values, payloads, predecessor, salt)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-hashOperationBatch-address---uint256---bytes---bytes32-bytes32-)
-   [schedule(target, value, data, predecessor, salt, delay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-schedule-address-uint256-bytes-bytes32-bytes32-uint256-)
-   [scheduleBatch(targets, values, payloads, predecessor, salt, delay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-scheduleBatch-address---uint256---bytes---bytes32-bytes32-uint256-)
-   [cancel(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-cancel-bytes32-)
-   [execute(target, value, payload, predecessor, salt)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-execute-address-uint256-bytes-bytes32-bytes32-)
-   [executeBatch(targets, values, payloads, predecessor, salt)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-executeBatch-address---uint256---bytes---bytes32-bytes32-)
-   [\_execute(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-_execute-address-uint256-bytes-)
-   [updateDelay(newDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-updateDelay-uint256-)
-   [\_encodeStateBitmap(operationState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-_encodeStateBitmap-enum-TimelockController-OperationState-)
-   [PROPOSER\_ROLE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-PROPOSER_ROLE-bytes32)
-   [EXECUTOR\_ROLE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-EXECUTOR_ROLE-bytes32)
-   [CANCELLER\_ROLE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CANCELLER_ROLE-bytes32)

ERC1155Holder

-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#ERC1155Holder-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#ERC1155Holder-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)

ERC721Holder

-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#ERC721Holder-onERC721Received-address-address-uint256-bytes-)

AccessControl

-   [hasRole(role, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-hasRole-bytes32-address-)
-   [\_checkRole(role)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-_checkRole-bytes32-)
-   [\_checkRole(role, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-_checkRole-bytes32-address-)
-   [getRoleAdmin(role)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-getRoleAdmin-bytes32-)
-   [grantRole(role, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-grantRole-bytes32-address-)
-   [revokeRole(role, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-revokeRole-bytes32-address-)
-   [renounceRole(role, callerConfirmation)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-renounceRole-bytes32-address-)
-   [\_setRoleAdmin(role, adminRole)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-_setRoleAdmin-bytes32-bytes32-)
-   [\_grantRole(role, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-_grantRole-bytes32-address-)
-   [\_revokeRole(role, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-_revokeRole-bytes32-address-)
-   [DEFAULT\_ADMIN\_ROLE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#AccessControl-DEFAULT_ADMIN_ROLE-bytes32)

### Events

-   [CallScheduled(id, index, target, value, data, predecessor, delay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallScheduled-bytes32-uint256-address-uint256-bytes-bytes32-uint256-)
-   [CallExecuted(id, index, target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallExecuted-bytes32-uint256-address-uint256-bytes-)
-   [CallSalt(id, salt)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallSalt-bytes32-bytes32-)
-   [Cancelled(id)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-Cancelled-bytes32-)
-   [MinDelayChange(oldDuration, newDuration)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-MinDelayChange-uint256-uint256-)

IAccessControl

-   [RoleAdminChanged(role, previousAdminRole, newAdminRole)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IAccessControl-RoleAdminChanged-bytes32-bytes32-bytes32-)
-   [RoleGranted(role, account, sender)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IAccessControl-RoleGranted-bytes32-address-address-)
-   [RoleRevoked(role, account, sender)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IAccessControl-RoleRevoked-bytes32-address-address-)

### Errors

-   [TimelockInvalidOperationLength(targets, payloads, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockInvalidOperationLength-uint256-uint256-uint256-)
-   [TimelockInsufficientDelay(delay, minDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockInsufficientDelay-uint256-uint256-)
-   [TimelockUnexpectedOperationState(operationId, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockUnexpectedOperationState-bytes32-bytes32-)
-   [TimelockUnexecutedPredecessor(predecessorId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockUnexecutedPredecessor-bytes32-)
-   [TimelockUnauthorizedCaller(caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockUnauthorizedCaller-address-)

IAccessControl

-   [AccessControlUnauthorizedAccount(account, neededRole)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IAccessControl-AccessControlUnauthorizedAccount-address-bytes32-)
-   [AccessControlBadConfirmation()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IAccessControl-AccessControlBadConfirmation--)

onlyRoleOrOpenRole(bytes32 role)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-onlyRoleOrOpenRole-bytes32-)

Modifier to make a function callable only by a certain role. In addition to checking the sender's role, `address(0)` 's role is also considered. Granting a role to `address(0)` is equivalent to enabling this role for everyone.

constructor(uint256 minDelay, address\[\] proposers, address\[\] executors, address admin)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-constructor-uint256-address---address---address-)

Initializes the contract with the following parameters:

-   `minDelay`: initial minimum delay in seconds for operations
-   `proposers`: accounts to be granted proposer and canceller roles
-   `executors`: accounts to be granted executor role
-   `admin`: optional account to be granted admin role; disable with zero address

The optional admin can aid with initial configuration of roles after deployment without being subject to delay, but this role should be subsequently renounced in favor of administration through timelocked proposals. Previous versions of this contract would assign this admin to the deployer automatically and should be renounced as well.

receive()

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-receive--)

Contract might receive/hold ETH as part of the maintenance process.

supportsInterface(bytes4 interfaceId) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-supportsInterface-bytes4-)

Returns true if this contract implements the interface defined by `interfaceId`. See the corresponding [ERC section](https://eips.ethereum.org/EIPS/eip-165#how-interfaces-are-identified) to learn more about how these ids are created.

This function call must use less than 30 000 gas.

isOperation(bytes32 id) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperation-bytes32-)

Returns whether an id corresponds to a registered operation. This includes both Waiting, Ready, and Done operations.

isOperationPending(bytes32 id) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationPending-bytes32-)

Returns whether an operation is pending or not. Note that a "pending" operation may also be "ready".

isOperationReady(bytes32 id) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationReady-bytes32-)

Returns whether an operation is ready for execution. Note that a "ready" operation is also "pending".

isOperationDone(bytes32 id) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-isOperationDone-bytes32-)

Returns whether an operation is done or not.

getTimestamp(bytes32 id) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-getTimestamp-bytes32-)

Returns the timestamp at which an operation becomes ready (0 for unset operations, 1 for done operations).

getOperationState(bytes32 id) → enum TimelockController.OperationState

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-getOperationState-bytes32-)

Returns operation state.

getMinDelay() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-getMinDelay--)

Returns the minimum delay in seconds for an operation to become valid.

This value can be changed by executing an operation that calls `updateDelay`.

hashOperation(address target, uint256 value, bytes data, bytes32 predecessor, bytes32 salt) → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-hashOperation-address-uint256-bytes-bytes32-bytes32-)

Returns the identifier of an operation containing a single transaction.

hashOperationBatch(address\[\] targets, uint256\[\] values, bytes\[\] payloads, bytes32 predecessor, bytes32 salt) → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-hashOperationBatch-address---uint256---bytes---bytes32-bytes32-)

Returns the identifier of an operation containing a batch of transactions.

schedule(address target, uint256 value, bytes data, bytes32 predecessor, bytes32 salt, uint256 delay)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-schedule-address-uint256-bytes-bytes32-bytes32-uint256-)

Schedule an operation containing a single transaction.

Emits [`TimelockController.CallSalt`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallSalt-bytes32-bytes32-) if salt is nonzero, and [`TimelockController.CallScheduled`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallScheduled-bytes32-uint256-address-uint256-bytes-bytes32-uint256-).

Requirements:

-   the caller must have the 'proposer' role.

scheduleBatch(address\[\] targets, uint256\[\] values, bytes\[\] payloads, bytes32 predecessor, bytes32 salt, uint256 delay)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-scheduleBatch-address---uint256---bytes---bytes32-bytes32-uint256-)

Schedule an operation containing a batch of transactions.

Emits [`TimelockController.CallSalt`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallSalt-bytes32-bytes32-) if salt is nonzero, and one [`TimelockController.CallScheduled`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallScheduled-bytes32-uint256-address-uint256-bytes-bytes32-uint256-) event per transaction in the batch.

Requirements:

-   the caller must have the 'proposer' role.

cancel(bytes32 id)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-cancel-bytes32-)

Cancel an operation.

Requirements:

-   the caller must have the 'canceller' role.

execute(address target, uint256 value, bytes payload, bytes32 predecessor, bytes32 salt)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-execute-address-uint256-bytes-bytes32-bytes32-)

Execute a ready operation containing a single transaction.

Emits a [`TimelockController.CallExecuted`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallExecuted-bytes32-uint256-address-uint256-bytes-) event.

Requirements:

-   the caller must have the 'executor' role.

executeBatch(address\[\] targets, uint256\[\] values, bytes\[\] payloads, bytes32 predecessor, bytes32 salt)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-executeBatch-address---uint256---bytes---bytes32-bytes32-)

Execute a ready operation containing a batch of transactions.

Emits one [`TimelockController.CallExecuted`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallExecuted-bytes32-uint256-address-uint256-bytes-) event per transaction in the batch.

Requirements:

-   the caller must have the 'executor' role.

\_execute(address target, uint256 value, bytes data)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-_execute-address-uint256-bytes-)

Execute an operation's call.

updateDelay(uint256 newDelay)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-updateDelay-uint256-)

Changes the minimum timelock duration for future operations.

Emits a [`TimelockController.MinDelayChange`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-MinDelayChange-uint256-uint256-) event.

Requirements:

-   the caller must be the timelock itself. This can only be achieved by scheduling and later executing an operation where the timelock is the target and the data is the ABI-encoded call to this function.

\_encodeStateBitmap(enum TimelockController.OperationState operationState) → bytes32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-_encodeStateBitmap-enum-TimelockController-OperationState-)

Encodes a `OperationState` into a `bytes32` representation where each bit enabled corresponds to the underlying position in the `OperationState` enum. For example:

0x000...1000 ^^^^^^----- ... ^---- Done ^--- Ready ^-- Waiting ^- Unset

PROPOSER\_ROLE() → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-PROPOSER_ROLE-bytes32)

EXECUTOR\_ROLE() → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-EXECUTOR_ROLE-bytes32)

CANCELLER\_ROLE() → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CANCELLER_ROLE-bytes32)

CallScheduled(bytes32 indexed id, uint256 indexed index, address target, uint256 value, bytes data, bytes32 predecessor, uint256 delay)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallScheduled-bytes32-uint256-address-uint256-bytes-bytes32-uint256-)

Emitted when a call is scheduled as part of operation `id`.

CallExecuted(bytes32 indexed id, uint256 indexed index, address target, uint256 value, bytes data)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallExecuted-bytes32-uint256-address-uint256-bytes-)

Emitted when a call is performed as part of operation `id`.

CallSalt(bytes32 indexed id, bytes32 salt)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-CallSalt-bytes32-bytes32-)

Emitted when new proposal is scheduled with non-zero salt.

Cancelled(bytes32 indexed id)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-Cancelled-bytes32-)

Emitted when operation `id` is cancelled.

MinDelayChange(uint256 oldDuration, uint256 newDuration)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-MinDelayChange-uint256-uint256-)

Emitted when the minimum delay for future operations is modified.

TimelockInvalidOperationLength(uint256 targets, uint256 payloads, uint256 values)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockInvalidOperationLength-uint256-uint256-uint256-)

Mismatch between the parameters length for an operation call.

TimelockInsufficientDelay(uint256 delay, uint256 minDelay)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockInsufficientDelay-uint256-uint256-)

The schedule operation doesn't meet the minimum delay.

TimelockUnexpectedOperationState(bytes32 operationId, bytes32 expectedStates)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockUnexpectedOperationState-bytes32-bytes32-)

The current state of an operation is not as required. The `expectedStates` is a bitmap with the bits enabled for each OperationState enum position counting from right to left.

See [`Governor._encodeStateBitmap`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-).

TimelockUnexecutedPredecessor(bytes32 predecessorId)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockUnexecutedPredecessor-bytes32-)

The predecessor to an operation not yet done.

TimelockUnauthorizedCaller(address caller)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController-TimelockUnauthorizedCaller-address-)

The caller account is not authorized.

## [`GovernorCountingFractional`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorcountingfractional)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorCountingFractional.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorCountingFractional.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) for fractional voting.

Similar to [`GovernorCountingSimple`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple), this contract is a votes counting module for [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) that supports 3 options: Against, For, Abstain. Additionally, it includes a fourth option: Fractional, which allows voters to split their voting power amongst the other 3 options.

Votes cast with the Fractional support must be accompanied by a `params` argument that is three packed `uint128` values representing the weight the delegate assigns to Against, For, and Abstain respectively. For those votes cast for the other 3 options, the `params` argument must be empty.

This is mostly useful when the delegate is a contract that implements its own rules for voting. These delegate-contracts can cast fractional votes according to the preferences of multiple entities delegating their voting power.

Some example use cases include:

-   Voting from tokens that are held by a DeFi pool
-   Voting from an L2 with tokens held by a bridge
-   Voting privately from a shielded pool using zero knowledge proofs.

Based on ScopeLift's [`GovernorCountingFractional`](https://github.com/ScopeLift/flexible-voting/blob/e5de2efd1368387b840931f19f3c184c85842761/src/GovernorCountingFractional.sol)

*Available since v5.1.*

### Functions

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-hasVoted-uint256-address-)
-   [usedVotes(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-usedVotes-uint256-address-)
-   [proposalVotes(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-proposalVotes-uint256-)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-_voteSucceeded-uint256-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-_countVote-uint256-address-uint8-uint256-bytes-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

-   [GovernorExceedRemainingWeight(voter, usedVotes, remainingWeight)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-GovernorExceedRemainingWeight-address-uint256-uint256-)

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

COUNTING\_MODE() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-COUNTING_MODE--)

A description of the possible `support` values for [`Governor.castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-) and the way these votes are counted, meant to be consumed by UIs to show correct vote options and interpret the results. The string is a URL-encoded sequence of key-value pairs that each describe one aspect, for example `support=bravo&quorum=for,abstain`.

There are 2 standard keys: `support` and `quorum`.

-   `support=bravo` refers to the vote options 0 = Against, 1 = For, 2 = Abstain, as in `GovernorBravo`.
-   `quorum=bravo` means that only For votes are counted towards quorum.
-   `quorum=for,abstain` means that both For and Abstain votes are counted towards quorum.

If a counting module makes use of encoded `params`, it should include this under a `params` key with a unique name that describes the behavior. For example:

-   `params=fractional` might refer to a scheme where votes are divided fractionally between for/against/abstain.
-   `params=erc721` might refer to a scheme where specific NFTs are delegated to vote.

The string can be decoded by the standard [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) JavaScript class.

hasVoted(uint256 proposalId, address account) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-hasVoted-uint256-address-)

Returns whether `account` has cast a vote on `proposalId`.

usedVotes(uint256 proposalId, address account) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-usedVotes-uint256-address-)

Get the number of votes already cast by `account` for a proposal with `proposalId`. Useful for integrations that allow delegates to cast rolling, partial votes.

proposalVotes(uint256 proposalId) → uint256 againstVotes, uint256 forVotes, uint256 abstainVotes

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-proposalVotes-uint256-)

Get current distribution of votes for a given proposal.

\_quorumReached(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-_quorumReached-uint256-)

Amount of votes already cast passes the threshold limit.

\_voteSucceeded(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-_voteSucceeded-uint256-)

See [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-). In this module, forVotes must be > againstVotes.

\_countVote(uint256 proposalId, address account, uint8 support, uint256 totalWeight, bytes params) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-_countVote-uint256-address-uint8-uint256-bytes-)

See [`Governor._countVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-). Function that records the delegate's votes.

Executing this function consumes (part of) the delegate's weight on the proposal. This weight can be distributed amongst the 3 options (Against, For, Abstain) by specifying a fractional `support`.

This counting module supports two vote casting modes: nominal and fractional.

-   Nominal: A nominal vote is cast by setting `support` to one of the 3 bravo options (Against, For, Abstain).
-   Fractional: A fractional vote is cast by setting `support` to `type(uint8).max` (255).

Casting a nominal vote requires `params` to be empty and consumes the delegate's full remaining weight on the proposal for the specified `support` option. This is similar to the [`GovernorCountingSimple`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple) module and follows the `VoteType` enum from Governor Bravo. As a consequence, no vote weight remains unspent so no further voting is possible (for this `proposalId` and this `account`).

Casting a fractional vote consumes a fraction of the delegate's remaining weight on the proposal according to the weights the delegate assigns to each support option (Against, For, Abstain respectively). The sum total of the three decoded vote weights *must* be less than or equal to the delegate's remaining weight on the proposal (i.e. their checkpointed total weight minus votes already cast on the proposal). This format can be produced using:

`abi.encodePacked(uint128(againstVotes), uint128(forVotes), uint128(abstainVotes))`

Consider that fractional voting restricts the number of casted votes (in each category) to 128 bits. Depending on how many decimals the underlying token has, a single voter may require to split their vote into multiple vote operations. For precision higher than ~30 decimals, large token holders may require a potentially large number of calls to cast all their votes. The voter has the possibility to cast all the remaining votes in a single operation using the traditional "bravo" vote.

GovernorExceedRemainingWeight(address voter, uint256 usedVotes, uint256 remainingWeight)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-GovernorExceedRemainingWeight-address-uint256-uint256-)

A fractional vote params uses more votes than are available for that user.

## [`GovernorCountingOverridable`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorcountingoverridable)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorCountingOverridable.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorCountingOverridable.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) which enables delegators to override the vote of their delegates. This module requires a token that inherits [`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended).

### Functions

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-hasVoted-uint256-address-)
-   [hasVotedOverride(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-hasVotedOverride-uint256-address-)
-   [proposalVotes(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-proposalVotes-uint256-)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_voteSucceeded-uint256-)
-   [\_countVote(proposalId, account, support, totalWeight, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_countOverride(proposalId, account, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_countOverride-uint256-address-uint8-)
-   [\_castOverride(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_castOverride-uint256-address-uint8-string-)
-   [castOverrideVote(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-castOverrideVote-uint256-uint8-string-)
-   [castOverrideVoteBySig(proposalId, support, voter, reason, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-castOverrideVoteBySig-uint256-uint8-address-string-bytes-)
-   [OVERRIDE\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-OVERRIDE_BALLOT_TYPEHASH-bytes32)

GovernorVotes

-   [token()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-token--)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-CLOCK_MODE--)
-   [\_getVotes(account, timepoint, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-_getVotes-address-uint256-bytes-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [VoteReduced(delegate, proposalId, support, weight)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-VoteReduced-address-uint256-uint8-uint256-)
-   [OverrideVoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-OverrideVoteCast-address-uint256-uint8-uint256-string-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

-   [GovernorAlreadyOverriddenVote(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-GovernorAlreadyOverriddenVote-address-)

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

COUNTING\_MODE() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-COUNTING_MODE--)

A description of the possible `support` values for [`Governor.castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-) and the way these votes are counted, meant to be consumed by UIs to show correct vote options and interpret the results. The string is a URL-encoded sequence of key-value pairs that each describe one aspect, for example `support=bravo&quorum=for,abstain`.

There are 2 standard keys: `support` and `quorum`.

-   `support=bravo` refers to the vote options 0 = Against, 1 = For, 2 = Abstain, as in `GovernorBravo`.
-   `quorum=bravo` means that only For votes are counted towards quorum.
-   `quorum=for,abstain` means that both For and Abstain votes are counted towards quorum.

If a counting module makes use of encoded `params`, it should include this under a `params` key with a unique name that describes the behavior. For example:

-   `params=fractional` might refer to a scheme where votes are divided fractionally between for/against/abstain.
-   `params=erc721` might refer to a scheme where specific NFTs are delegated to vote.

The string can be decoded by the standard [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) JavaScript class.

hasVoted(uint256 proposalId, address account) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-hasVoted-uint256-address-)

See [`IGovernor.hasVoted`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-).

Calling [`Governor.castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-) (or similar) casts a vote using the voting power that is delegated to the voter. Conversely, calling [`GovernorCountingOverridable.castOverrideVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-castOverrideVote-uint256-uint8-string-) (or similar) uses the voting power of the account itself, from its asset balances. Casting an "override vote" does not count as voting and won't be reflected by this getter. Consider using [`GovernorCountingOverridable.hasVotedOverride`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-hasVotedOverride-uint256-address-) to check if an account has casted an "override vote" for a given proposal id.

hasVotedOverride(uint256 proposalId, address account) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-hasVotedOverride-uint256-address-)

Check if an `account` has overridden their delegate for a proposal.

proposalVotes(uint256 proposalId) → uint256 againstVotes, uint256 forVotes, uint256 abstainVotes

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-proposalVotes-uint256-)

Accessor to the internal vote counts.

\_quorumReached(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_quorumReached-uint256-)

Amount of votes already cast passes the threshold limit.

\_voteSucceeded(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_voteSucceeded-uint256-)

See [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-). In this module, the forVotes must be strictly over the againstVotes.

\_countVote(uint256 proposalId, address account, uint8 support, uint256 totalWeight, bytes) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_countVote-uint256-address-uint8-uint256-bytes-)

See [`Governor._countVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-). In this module, the support follows the `VoteType` enum (from Governor Bravo).

called by [`Governor._castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-) which emits the [`IGovernor.VoteCast`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-) (or [`IGovernor.VoteCastWithParams`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)) event.

\_countOverride(uint256 proposalId, address account, uint8 support) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_countOverride-uint256-address-uint8-)

Variant of [`Governor._countVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-) that deals with vote overrides.

See [`IGovernor.hasVoted`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-) for more details about the difference between [`Governor.castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-) and [`GovernorCountingOverridable.castOverrideVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-castOverrideVote-uint256-uint8-string-).

\_castOverride(uint256 proposalId, address account, uint8 support, string reason) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-_castOverride-uint256-address-uint8-string-)

Variant of [`Governor._castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-) that deals with vote overrides. Returns the overridden weight.

castOverrideVote(uint256 proposalId, uint8 support, string reason) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-castOverrideVote-uint256-uint8-string-)

Public function for casting an override vote. Returns the overridden weight.

castOverrideVoteBySig(uint256 proposalId, uint8 support, address voter, string reason, bytes signature) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-castOverrideVoteBySig-uint256-uint8-address-string-bytes-)

Public function for casting an override vote using a voter's signature. Returns the overridden weight.

OVERRIDE\_BALLOT\_TYPEHASH() → bytes32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-OVERRIDE_BALLOT_TYPEHASH-bytes32)

VoteReduced(address indexed delegate, uint256 proposalId, uint8 support, uint256 weight)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-VoteReduced-address-uint256-uint8-uint256-)

The votes casted by `delegate` were reduced by `weight` after an override vote was casted by the original token holder

OverrideVoteCast(address indexed voter, uint256 proposalId, uint8 support, uint256 weight, string reason)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-OverrideVoteCast-address-uint256-uint8-uint256-string-)

A delegated vote on `proposalId` was overridden by `weight`

GovernorAlreadyOverriddenVote(address account)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingOverridable-GovernorAlreadyOverriddenVote-address-)

## [`GovernorCountingSimple`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorcountingsimple)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorCountingSimple.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) for simple, 3 options, vote counting.

### Functions

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-hasVoted-uint256-address-)
-   [proposalVotes(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-proposalVotes-uint256-)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-_voteSucceeded-uint256-)
-   [\_countVote(proposalId, account, support, totalWeight, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-_countVote-uint256-address-uint8-uint256-bytes-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

COUNTING\_MODE() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-COUNTING_MODE--)

A description of the possible `support` values for [`Governor.castVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-) and the way these votes are counted, meant to be consumed by UIs to show correct vote options and interpret the results. The string is a URL-encoded sequence of key-value pairs that each describe one aspect, for example `support=bravo&quorum=for,abstain`.

There are 2 standard keys: `support` and `quorum`.

-   `support=bravo` refers to the vote options 0 = Against, 1 = For, 2 = Abstain, as in `GovernorBravo`.
-   `quorum=bravo` means that only For votes are counted towards quorum.
-   `quorum=for,abstain` means that both For and Abstain votes are counted towards quorum.

If a counting module makes use of encoded `params`, it should include this under a `params` key with a unique name that describes the behavior. For example:

-   `params=fractional` might refer to a scheme where votes are divided fractionally between for/against/abstain.
-   `params=erc721` might refer to a scheme where specific NFTs are delegated to vote.

The string can be decoded by the standard [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) JavaScript class.

hasVoted(uint256 proposalId, address account) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-hasVoted-uint256-address-)

Returns whether `account` has cast a vote on `proposalId`.

proposalVotes(uint256 proposalId) → uint256 againstVotes, uint256 forVotes, uint256 abstainVotes

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-proposalVotes-uint256-)

Accessor to the internal vote counts.

\_quorumReached(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-_quorumReached-uint256-)

Amount of votes already cast passes the threshold limit.

\_voteSucceeded(uint256 proposalId) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-_voteSucceeded-uint256-)

See [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-). In this module, the forVotes must be strictly over the againstVotes.

\_countVote(uint256 proposalId, address account, uint8 support, uint256 totalWeight, bytes) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple-_countVote-uint256-address-uint8-uint256-bytes-)

See [`Governor._countVote`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-). In this module, the support follows the `VoteType` enum (from Governor Bravo).

## [`GovernorNoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governornonceskeyed)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorNoncesKeyed.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorNoncesKeyed.sol";
```

An extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) that extends existing nonce management to use [`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed), where the key is the low-order 192 bits of the `proposalId`. This is useful for voting by signature while maintaining separate sequences of nonces for each proposal.

Traditional (un-keyed) nonces are still supported and can continue to be used as if this extension was not present.

### Functions

-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed-_useCheckedNonce-address-uint256-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)

NoncesKeyed

-   [nonces(owner, key)](https://docs.openzeppelin.com/contracts/5.x/api/governance#NoncesKeyed-nonces-address-uint192-)
-   [\_useNonce(owner, key)](https://docs.openzeppelin.com/contracts/5.x/api/governance#NoncesKeyed-_useNonce-address-uint192-)
-   [\_useCheckedNonce(owner, key, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#NoncesKeyed-_useCheckedNonce-address-uint192-uint64-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

\_useCheckedNonce(address owner, uint256 nonce)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed-_useCheckedNonce-address-uint256-)

\_validateVoteSig(uint256 proposalId, uint8 support, address voter, bytes signature) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed-_validateVoteSig-uint256-uint8-address-bytes-)

Check the signature against keyed nonce and falls back to the traditional nonce.

This function won't call `super._validateVoteSig` if the keyed nonce is valid. Side effects may be skipped depending on the linearization of the function.

\_validateExtendedVoteSig(uint256 proposalId, uint8 support, address voter, string reason, bytes params, bytes signature) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorNoncesKeyed-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)

Check the signature against keyed nonce and falls back to the traditional nonce.

This function won't call `super._validateExtendedVoteSig` if the keyed nonce is valid. Side effects may be skipped depending on the linearization of the function.

## [`GovernorPreventLateQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorpreventlatequorum)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorPreventLateQuorum.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorPreventLateQuorum.sol";
```

A module that ensures there is a minimum voting period after quorum is reached. This prevents a large voter from swaying a vote and triggering quorum at the last minute, by ensuring there is always time for other voters to react and try to oppose the decision.

If a vote causes quorum to be reached, the proposal's voting period may be extended so that it does not end before at least a specified time has passed (the "vote extension" parameter). This parameter can be set through a governance proposal.

### Functions

-   [constructor(initialVoteExtension)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-constructor-uint48-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-proposalDeadline-uint256-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-_tallyUpdated-uint256-)
-   [lateQuorumVoteExtension()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-lateQuorumVoteExtension--)
-   [setLateQuorumVoteExtension(newVoteExtension)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-setLateQuorumVoteExtension-uint48-)
-   [\_setLateQuorumVoteExtension(newVoteExtension)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-_setLateQuorumVoteExtension-uint48-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [ProposalExtended(proposalId, extendedDeadline)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-ProposalExtended-uint256-uint64-)
-   [LateQuorumVoteExtensionSet(oldVoteExtension, newVoteExtension)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-LateQuorumVoteExtensionSet-uint64-uint64-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(uint48 initialVoteExtension)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-constructor-uint48-)

Initializes the vote extension parameter: the time in either number of blocks or seconds (depending on the governor clock mode) that is required to pass since the moment a proposal reaches quorum until its voting period ends. If necessary the voting period will be extended beyond the one set during proposal creation.

proposalDeadline(uint256 proposalId) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-proposalDeadline-uint256-)

Returns the proposal deadline, which may have been extended beyond that set at proposal creation, if the proposal reached quorum late in the voting period. See [`Governor.proposalDeadline`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-).

\_tallyUpdated(uint256 proposalId)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-_tallyUpdated-uint256-)

Vote tally updated and detects if it caused quorum to be reached, potentially extending the voting period.

May emit a [`GovernorPreventLateQuorum.ProposalExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-ProposalExtended-uint256-uint64-) event.

lateQuorumVoteExtension() → uint48

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-lateQuorumVoteExtension--)

Returns the current value of the vote extension parameter: the number of blocks that are required to pass from the time a proposal reaches quorum until its voting period ends.

setLateQuorumVoteExtension(uint48 newVoteExtension)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-setLateQuorumVoteExtension-uint48-)

Changes the [`GovernorPreventLateQuorum.lateQuorumVoteExtension`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-lateQuorumVoteExtension--). This operation can only be performed by the governance executor, generally through a governance proposal.

Emits a [`GovernorPreventLateQuorum.LateQuorumVoteExtensionSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-LateQuorumVoteExtensionSet-uint64-uint64-) event.

\_setLateQuorumVoteExtension(uint48 newVoteExtension)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-_setLateQuorumVoteExtension-uint48-)

Changes the [`GovernorPreventLateQuorum.lateQuorumVoteExtension`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-lateQuorumVoteExtension--). This is an internal function that can be exposed in a public function like [`GovernorPreventLateQuorum.setLateQuorumVoteExtension`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-setLateQuorumVoteExtension-uint48-) if another access control mechanism is needed.

Emits a [`GovernorPreventLateQuorum.LateQuorumVoteExtensionSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-LateQuorumVoteExtensionSet-uint64-uint64-) event.

ProposalExtended(uint256 indexed proposalId, uint64 extendedDeadline)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-ProposalExtended-uint256-uint64-)

Emitted when a proposal deadline is pushed back due to reaching quorum late in its voting period.

LateQuorumVoteExtensionSet(uint64 oldVoteExtension, uint64 newVoteExtension)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-LateQuorumVoteExtensionSet-uint64-uint64-)

Emitted when the [`GovernorPreventLateQuorum.lateQuorumVoteExtension`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorPreventLateQuorum-lateQuorumVoteExtension--) parameter is changed.

## [`GovernorProposalGuardian`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorproposalguardian)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorProposalGuardian.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorProposalGuardian.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) which adds a proposal guardian that can cancel proposals at any stage in the proposal's lifecycle.

if the proposal guardian is not configured, then proposers take this role for their proposals.

### Functions

-   [proposalGuardian()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-proposalGuardian--)
-   [setProposalGuardian(newProposalGuardian)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-setProposalGuardian-address-)
-   [\_setProposalGuardian(newProposalGuardian)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-_setProposalGuardian-address-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-_validateCancel-uint256-address-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [ProposalGuardianSet(oldProposalGuardian, newProposalGuardian)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-ProposalGuardianSet-address-address-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

proposalGuardian() → address

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-proposalGuardian--)

Getter that returns the address of the proposal guardian.

setProposalGuardian(address newProposalGuardian)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-setProposalGuardian-address-)

Update the proposal guardian's address. This operation can only be performed through a governance proposal.

Emits a [`GovernorProposalGuardian.ProposalGuardianSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-ProposalGuardianSet-address-address-) event.

\_setProposalGuardian(address newProposalGuardian)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-_setProposalGuardian-address-)

Internal setter for the proposal guardian.

Emits a [`GovernorProposalGuardian.ProposalGuardianSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-ProposalGuardianSet-address-address-) event.

\_validateCancel(uint256 proposalId, address caller) → bool

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-_validateCancel-uint256-address-)

Override [`Governor._validateCancel`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-) to implement the extended cancellation logic.

-   The [`GovernorProposalGuardian.proposalGuardian`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-proposalGuardian--) can cancel any proposal at any point.
-   If no proposal guardian is set, the [`IGovernor.proposalProposer`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-proposalProposer-uint256-) can cancel their proposals at any point.
-   In any case, permissions defined in [`Governor._validateCancel`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-) (or another override) remains valid.

ProposalGuardianSet(address oldProposalGuardian, address newProposalGuardian)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorProposalGuardian-ProposalGuardianSet-address-address-)

## [`GovernorSequentialProposalId`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorsequentialproposalid)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorSequentialProposalId.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorSequentialProposalId.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) that changes the numbering of proposal ids from the default hash-based approach to sequential ids.

### Functions

-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-getProposalId-address---uint256---bytes---bytes32-)
-   [latestProposalId()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-latestProposalId--)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-_propose-address---uint256---bytes---string-address-)
-   [\_initializeLatestProposalId(newLatestProposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-_initializeLatestProposalId-uint256-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

-   [GovernorAlreadyInitializedLatestProposalId()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-GovernorAlreadyInitializedLatestProposalId--)

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

getProposalId(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-getProposalId-address---uint256---bytes---bytes32-)

latestProposalId() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-latestProposalId--)

Returns the latest proposal id. A return value of 0 means no proposals have been created yet.

\_propose(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, string description, address proposer) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-_propose-address---uint256---bytes---string-address-)

See `IGovernor-_propose`. Hook into the proposing mechanism to increment proposal count.

\_initializeLatestProposalId(uint256 newLatestProposalId)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-_initializeLatestProposalId-uint256-)

Internal function to set the [`GovernorSequentialProposalId.latestProposalId`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-latestProposalId--). This function is helpful when transitioning from another governance system. The next proposal id will be `newLatestProposalId` + 1.

May only call this function if the current value of [`GovernorSequentialProposalId.latestProposalId`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-latestProposalId--) is 0.

GovernorAlreadyInitializedLatestProposalId()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-GovernorAlreadyInitializedLatestProposalId--)

The [`GovernorSequentialProposalId.latestProposalId`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSequentialProposalId-latestProposalId--) may only be initialized if it hasn't been set yet (through initialization or the creation of a proposal).

## [`GovernorSettings`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorsettings)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorSettings.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) for settings updatable through governance.

### Functions

-   [constructor(initialVotingDelay, initialVotingPeriod, initialProposalThreshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-constructor-uint48-uint32-uint256-)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-votingPeriod--)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-proposalThreshold--)
-   [setVotingDelay(newVotingDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-setVotingDelay-uint48-)
-   [setVotingPeriod(newVotingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-setVotingPeriod-uint32-)
-   [setProposalThreshold(newProposalThreshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-setProposalThreshold-uint256-)
-   [\_setVotingDelay(newVotingDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-_setVotingDelay-uint48-)
-   [\_setVotingPeriod(newVotingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-_setVotingPeriod-uint32-)
-   [\_setProposalThreshold(newProposalThreshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-_setProposalThreshold-uint256-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [VotingDelaySet(oldVotingDelay, newVotingDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingDelaySet-uint256-uint256-)
-   [VotingPeriodSet(oldVotingPeriod, newVotingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingPeriodSet-uint256-uint256-)
-   [ProposalThresholdSet(oldProposalThreshold, newProposalThreshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-ProposalThresholdSet-uint256-uint256-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(uint48 initialVotingDelay, uint32 initialVotingPeriod, uint256 initialProposalThreshold)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-constructor-uint48-uint32-uint256-)

Initialize the governance parameters.

votingDelay() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-votingDelay--)

votingPeriod() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-votingPeriod--)

proposalThreshold() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-proposalThreshold--)

The number of votes required in order for a voter to become a proposer.

setVotingDelay(uint48 newVotingDelay)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-setVotingDelay-uint48-)

Update the voting delay. This operation can only be performed through a governance proposal.

Emits a [`GovernorSettings.VotingDelaySet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingDelaySet-uint256-uint256-) event.

setVotingPeriod(uint32 newVotingPeriod)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-setVotingPeriod-uint32-)

Update the voting period. This operation can only be performed through a governance proposal.

Emits a [`GovernorSettings.VotingPeriodSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingPeriodSet-uint256-uint256-) event.

setProposalThreshold(uint256 newProposalThreshold)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-setProposalThreshold-uint256-)

Update the proposal threshold. This operation can only be performed through a governance proposal.

Emits a [`GovernorSettings.ProposalThresholdSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-ProposalThresholdSet-uint256-uint256-) event.

\_setVotingDelay(uint48 newVotingDelay)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-_setVotingDelay-uint48-)

Internal setter for the voting delay.

Emits a [`GovernorSettings.VotingDelaySet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingDelaySet-uint256-uint256-) event.

\_setVotingPeriod(uint32 newVotingPeriod)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-_setVotingPeriod-uint32-)

Internal setter for the voting period.

Emits a [`GovernorSettings.VotingPeriodSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingPeriodSet-uint256-uint256-) event.

\_setProposalThreshold(uint256 newProposalThreshold)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-_setProposalThreshold-uint256-)

Internal setter for the proposal threshold.

Emits a [`GovernorSettings.ProposalThresholdSet`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-ProposalThresholdSet-uint256-uint256-) event.

VotingDelaySet(uint256 oldVotingDelay, uint256 newVotingDelay)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingDelaySet-uint256-uint256-)

VotingPeriodSet(uint256 oldVotingPeriod, uint256 newVotingPeriod)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-VotingPeriodSet-uint256-uint256-)

ProposalThresholdSet(uint256 oldProposalThreshold, uint256 newProposalThreshold)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSettings-ProposalThresholdSet-uint256-uint256-)

## [`GovernorStorage`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorstorage)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorStorage.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorStorage.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) that implements storage of proposal details. This module also provides primitives for the enumerability of proposals.

Use cases for this module include:

-   UIs that explore the proposal state without relying on event indexing.
-   Using only the proposalId as an argument in the [`Governor.queue`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-) and [`Governor.execute`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-) functions for L2 chains where storage is cheap compared to calldata.

### Functions

-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-_propose-address---uint256---bytes---string-address-)
-   [queue(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-queue-uint256-)
-   [execute(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-execute-uint256-)
-   [cancel(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-cancel-uint256-)
-   [proposalCount()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-proposalCount--)
-   [proposalDetails(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-proposalDetails-uint256-)
-   [proposalDetailsAt(index)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-proposalDetailsAt-uint256-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

\_propose(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, string description, address proposer) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-_propose-address---uint256---bytes---string-address-)

Hook into the proposing mechanism

queue(uint256 proposalId)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-queue-uint256-)

Version of [`IGovernor.queue`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-queue-address---uint256---bytes---bytes32-) with only `proposalId` as an argument.

execute(uint256 proposalId)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-execute-uint256-)

Version of [`IGovernor.execute`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-execute-address---uint256---bytes---bytes32-) with only `proposalId` as an argument.

cancel(uint256 proposalId)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-cancel-uint256-)

ProposalId version of [`IGovernor.cancel`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-cancel-address---uint256---bytes---bytes32-).

proposalCount() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-proposalCount--)

Returns the number of stored proposals.

proposalDetails(uint256 proposalId) → address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-proposalDetails-uint256-)

Returns the details of a proposalId. Reverts if `proposalId` is not a known proposal.

proposalDetailsAt(uint256 index) → uint256 proposalId, address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorStorage-proposalDetailsAt-uint256-)

Returns the details (including the proposalId) of a proposal given its sequential index.

## [`GovernorSuperQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorsuperquorum)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorSuperQuorum.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorSuperQuorum.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) with a super quorum. Proposals that meet the super quorum (and have a majority of for votes) advance to the `Succeeded` state before the proposal deadline. Counting modules that want to use this extension must implement [`GovernorCountingFractional.proposalVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingFractional-proposalVotes-uint256-).

### Functions

-   [superQuorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-superQuorum-uint256-)
-   [proposalVotes(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-proposalVotes-uint256-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-state-uint256-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

superQuorum(uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-superQuorum-uint256-)

Minimum number of cast votes required for a proposal to reach super quorum. Only FOR votes are counted towards the super quorum. Once the super quorum is reached, an active proposal can proceed to the next state without waiting for the proposal deadline.

The `timepoint` parameter corresponds to the snapshot used for counting the vote. This enables scaling of the quorum depending on values such as the `totalSupply` of a token at this timepoint (see [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes)).

Make sure the value specified for the super quorum is greater than [`Governor.quorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-), otherwise, it may be possible to pass a proposal with less votes than the default quorum.

proposalVotes(uint256 proposalId) → uint256 againstVotes, uint256 forVotes, uint256 abstainVotes

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-proposalVotes-uint256-)

Accessor to the internal vote counts. This must be implemented by the counting module. Counting modules that don't implement this function are incompatible with this module

state(uint256 proposalId) → enum IGovernor.ProposalState

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-state-uint256-)

Overridden version of the [`Governor.state`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-) function that checks if the proposal has reached the super quorum.

If the proposal reaches super quorum but [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-) returns false, eg, assuming the super quorum has been set low enough that both FOR and AGAINST votes have exceeded it and AGAINST votes exceed FOR votes, the proposal continues to be active until [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-) returns true or the proposal deadline is reached. This means that with a low super quorum it is also possible that a vote can succeed prematurely before enough AGAINST voters have a chance to vote. Hence, it is recommended to set a high enough super quorum to avoid these types of scenarios.

## [`GovernorTimelockAccess`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governortimelockaccess)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorTimelockAccess.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockAccess.sol";
```

This module connects a [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) instance to an [`AccessManager`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager) instance, allowing the governor to make calls that are delay-restricted by the manager using the normal [`Governor.queue`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-) workflow. An optional base delay is applied to operations that are not delayed externally by the manager. Execution of a proposal will be delayed as much as necessary to meet the required delays of all of its operations.

This extension allows the governor to hold and use its own assets and permissions, unlike [`GovernorTimelockControl`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl) and [`GovernorTimelockCompound`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound), where the timelock is a separate contract that must be the one to hold assets and permissions. Operations that are delay-restricted by the manager, however, will be executed through the [`AccessManager.execute`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager-execute-address-bytes-) function.

#### [Security Considerations](https://docs.openzeppelin.com/contracts/5.x/api/governance#security-considerations)

Some operations may be cancelable in the `AccessManager` by the admin or a set of guardians, depending on the restricted function being invoked. Since proposals are atomic, the cancellation by a guardian of a single operation in a proposal will cause all of the proposal to become unable to execute. Consider proposing cancellable operations separately.

By default, function calls will be routed through the associated `AccessManager` whenever it claims the target function to be restricted by it. However, admins may configure the manager to make that claim for functions that a governor would want to call directly (e.g., token transfers) in an attempt to deny it access to those functions. To mitigate this attack vector, the governor is able to ignore the restrictions claimed by the `AccessManager` using [`GovernorTimelockAccess.setAccessManagerIgnored`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setAccessManagerIgnored-address-bytes4---bool-). While permanent denial of service is mitigated, temporary DoS may still be technically possible. All of the governor's own functions (e.g., [`GovernorTimelockAccess.setBaseDelaySeconds`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setBaseDelaySeconds-uint32-)) ignore the `AccessManager` by default.

`AccessManager` does not support scheduling more than one operation with the same target and calldata at the same time. See [`AccessManager.schedule`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager-schedule-address-bytes-uint48-) for a workaround.

### Functions

-   [constructor(manager, initialBaseDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-constructor-address-uint32-)
-   [accessManager()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-accessManager--)
-   [baseDelaySeconds()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-baseDelaySeconds--)
-   [setBaseDelaySeconds(newBaseDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setBaseDelaySeconds-uint32-)
-   [\_setBaseDelaySeconds(newBaseDelay)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_setBaseDelaySeconds-uint32-)
-   [isAccessManagerIgnored(target, selector)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-isAccessManagerIgnored-address-bytes4-)
-   [setAccessManagerIgnored(target, selectors, ignored)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setAccessManagerIgnored-address-bytes4---bool-)
-   [\_setAccessManagerIgnored(target, selector, ignored)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_setAccessManagerIgnored-address-bytes4-bool-)
-   [proposalExecutionPlan(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-proposalExecutionPlan-uint256-)
-   [proposalNeedsQueuing(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-proposalNeedsQueuing-uint256-)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-propose-address---uint256---bytes---string-)
-   [\_queueOperations(proposalId, targets, , calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [\_executeOperations(proposalId, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_cancel-address---uint256---bytes---bytes32-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [BaseDelaySet(oldBaseDelaySeconds, newBaseDelaySeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-BaseDelaySet-uint32-uint32-)
-   [AccessManagerIgnoredSet(target, selector, ignored)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-AccessManagerIgnoredSet-address-bytes4-bool-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

-   [GovernorUnmetDelay(proposalId, neededTimestamp)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-GovernorUnmetDelay-uint256-uint256-)
-   [GovernorMismatchedNonce(proposalId, expectedNonce, actualNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-GovernorMismatchedNonce-uint256-uint256-uint256-)
-   [GovernorLockedIgnore()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-GovernorLockedIgnore--)

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(address manager, uint32 initialBaseDelay)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-constructor-address-uint32-)

Initialize the governor with an [`AccessManager`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager) and initial base delay.

accessManager() → contract IAccessManager

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-accessManager--)

Returns the [`AccessManager`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager) instance associated to this governor.

baseDelaySeconds() → uint32

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-baseDelaySeconds--)

Base delay that will be applied to all function calls. Some may be further delayed by their associated `AccessManager` authority; in this case the final delay will be the maximum of the base delay and the one demanded by the authority.

Execution delays are processed by the `AccessManager` contracts, and according to that contract are expressed in seconds. Therefore, the base delay is also in seconds, regardless of the governor's clock mode.

setBaseDelaySeconds(uint32 newBaseDelay)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setBaseDelaySeconds-uint32-)

Change the value of [`GovernorTimelockAccess.baseDelaySeconds`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-baseDelaySeconds--). This operation can only be invoked through a governance proposal.

\_setBaseDelaySeconds(uint32 newBaseDelay)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_setBaseDelaySeconds-uint32-)

Change the value of [`GovernorTimelockAccess.baseDelaySeconds`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-baseDelaySeconds--). Internal function without access control.

isAccessManagerIgnored(address target, bytes4 selector) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-isAccessManagerIgnored-address-bytes4-)

Check if restrictions from the associated [`AccessManager`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager) are ignored for a target function. Returns true when the target function will be invoked directly regardless of `AccessManager` settings for the function. See [`GovernorTimelockAccess.setAccessManagerIgnored`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setAccessManagerIgnored-address-bytes4---bool-) and Security Considerations above.

setAccessManagerIgnored(address target, bytes4\[\] selectors, bool ignored)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setAccessManagerIgnored-address-bytes4---bool-)

Configure whether restrictions from the associated [`AccessManager`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager) are ignored for a target function. See Security Considerations above.

\_setAccessManagerIgnored(address target, bytes4 selector, bool ignored)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_setAccessManagerIgnored-address-bytes4-bool-)

Internal version of [`GovernorTimelockAccess.setAccessManagerIgnored`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-setAccessManagerIgnored-address-bytes4---bool-) without access restriction.

proposalExecutionPlan(uint256 proposalId) → uint32 delay, bool\[\] indirect, bool\[\] withDelay

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-proposalExecutionPlan-uint256-)

Public accessor to check the execution plan, including the number of seconds that the proposal will be delayed since queuing, an array indicating which of the proposal actions will be executed indirectly through the associated [`AccessManager`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager), and another indicating which will be scheduled in [`Governor.queue`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-). Note that those that must be scheduled are cancellable by `AccessManager` guardians.

proposalNeedsQueuing(uint256 proposalId) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-proposalNeedsQueuing-uint256-)

propose(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, string description) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-propose-address---uint256---bytes---string-)

\_queueOperations(uint256 proposalId, address\[\] targets, uint256\[\], bytes\[\] calldatas, bytes32) → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_queueOperations-uint256-address---uint256---bytes---bytes32-)

Mechanism to queue a proposal, potentially scheduling some of its operations in the AccessManager.

The execution delay is chosen based on the delay information retrieved in [`Governor.propose`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-). This value may be off if the delay was updated since proposal creation. In this case, the proposal needs to be recreated.

\_executeOperations(uint256 proposalId, address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_executeOperations-uint256-address---uint256---bytes---bytes32-)

Mechanism to execute a proposal, potentially going through [`AccessManager.execute`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager-execute-address-bytes-) for delayed operations.

\_cancel(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-_cancel-address---uint256---bytes---bytes32-)

Internal cancel mechanism with minimal restrictions. A proposal can be cancelled in any state other than Canceled, Expired, or Executed. Once cancelled a proposal can't be re-submitted.

Emits a [`IGovernor.ProposalCanceled`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-) event.

BaseDelaySet(uint32 oldBaseDelaySeconds, uint32 newBaseDelaySeconds)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-BaseDelaySet-uint32-uint32-)

AccessManagerIgnoredSet(address target, bytes4 selector, bool ignored)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-AccessManagerIgnoredSet-address-bytes4-bool-)

GovernorUnmetDelay(uint256 proposalId, uint256 neededTimestamp)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-GovernorUnmetDelay-uint256-uint256-)

GovernorMismatchedNonce(uint256 proposalId, uint256 expectedNonce, uint256 actualNonce)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-GovernorMismatchedNonce-uint256-uint256-uint256-)

GovernorLockedIgnore()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockAccess-GovernorLockedIgnore--)

## [`GovernorTimelockCompound`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governortimelockcompound)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorTimelockCompound.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockCompound.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) that binds the execution process to a Compound Timelock. This adds a delay, enforced by the external timelock to all successful proposals (in addition to the voting duration). The [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) needs to be the admin of the timelock for any operation to be performed. A public, unrestricted, [`GovernorTimelockCompound.__acceptAdmin`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-__acceptAdmin--) is available to accept ownership of the timelock.

Using this model means the proposal will be operated by the [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController) and not by the [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor). Thus, the assets and permissions must be attached to the [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController). Any asset sent to the [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) will be inaccessible from a proposal, unless executed via [`Governor.relay`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-).

### Functions

-   [constructor(timelockAddress)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-constructor-contract-ICompoundTimelock-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-state-uint256-)
-   [timelock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-timelock--)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-proposalNeedsQueuing-uint256-)
-   [\_queueOperations(proposalId, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [\_executeOperations(proposalId, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_cancel-address---uint256---bytes---bytes32-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_executor--)
-   [\_\_acceptAdmin()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-__acceptAdmin--)
-   [updateTimelock(newTimelock)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-updateTimelock-contract-ICompoundTimelock-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [TimelockChange(oldTimelock, newTimelock)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-TimelockChange-address-address-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(contract ICompoundTimelock timelockAddress)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-constructor-contract-ICompoundTimelock-)

Set the timelock.

state(uint256 proposalId) → enum IGovernor.ProposalState

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-state-uint256-)

Overridden version of the [`Governor.state`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-) function with added support for the `Expired` state.

timelock() → address

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-timelock--)

Public accessor to check the address of the timelock

proposalNeedsQueuing(uint256) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-proposalNeedsQueuing-uint256-)

\_queueOperations(uint256 proposalId, address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32) → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_queueOperations-uint256-address---uint256---bytes---bytes32-)

Function to queue a proposal to the timelock.

\_executeOperations(uint256 proposalId, address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_executeOperations-uint256-address---uint256---bytes---bytes32-)

Overridden version of the [`Governor._executeOperations`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-) function that run the already queued proposal through the timelock.

\_cancel(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_cancel-address---uint256---bytes---bytes32-)

Overridden version of the [`Governor._cancel`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-) function to cancel the timelocked proposal if it has already been queued.

\_executor() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-_executor--)

Address through which the governor executes action. In this case, the timelock.

\_\_acceptAdmin()

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-__acceptAdmin--)

Accept admin right over the timelock.

updateTimelock(contract ICompoundTimelock newTimelock)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-updateTimelock-contract-ICompoundTimelock-)

Public endpoint to update the underlying timelock instance. Restricted to the timelock itself, so updates must be proposed, scheduled, and executed through governance proposals.

For security reasons, the timelock must be handed over to another admin before setting up a new one. The two operations (hand over the timelock) and do the update can be batched in a single proposal.

Note that if the timelock admin has been handed over in a previous operation, we refuse updates made through the timelock if admin of the timelock has already been accepted and the operation is executed outside the scope of governance.

It is not recommended to change the timelock while there are other queued governance proposals.

TimelockChange(address oldTimelock, address newTimelock)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockCompound-TimelockChange-address-address-)

Emitted when the timelock controller used for proposal execution is modified.

## [`GovernorTimelockControl`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governortimelockcontrol)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorTimelockControl.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) that binds the execution process to an instance of [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController). This adds a delay, enforced by the [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController) to all successful proposals (in addition to the voting duration). The [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) needs the proposer (and ideally the executor and canceller) roles for the [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) to work properly.

Using this model means the proposal will be operated by the [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController) and not by the [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor). Thus, the assets and permissions must be attached to the [`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController). Any asset sent to the [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) will be inaccessible from a proposal, unless executed via [`Governor.relay`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-).

Setting up the TimelockController to have additional proposers or cancelers besides the governor is very risky, as it grants them the ability to: 1) execute operations as the timelock, and thus possibly performing operations or accessing funds that are expected to only be accessible through a vote, and 2) block governance proposals that have been approved by the voters, effectively executing a Denial of Service attack.

### Functions

-   [constructor(timelockAddress)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-constructor-contract-TimelockController-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-state-uint256-)
-   [timelock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-timelock--)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-proposalNeedsQueuing-uint256-)
-   [\_queueOperations(proposalId, targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [\_executeOperations(proposalId, targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_cancel-address---uint256---bytes---bytes32-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_executor--)
-   [updateTimelock(newTimelock)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-updateTimelock-contract-TimelockController-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_getVotes(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_getVotes-address-uint256-bytes-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [TimelockChange(oldTimelock, newTimelock)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-TimelockChange-address-address-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(contract TimelockController timelockAddress)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-constructor-contract-TimelockController-)

Set the timelock.

state(uint256 proposalId) → enum IGovernor.ProposalState

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-state-uint256-)

Overridden version of the [`Governor.state`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-) function that considers the status reported by the timelock.

timelock() → address

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-timelock--)

Public accessor to check the address of the timelock

proposalNeedsQueuing(uint256) → bool

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-proposalNeedsQueuing-uint256-)

\_queueOperations(uint256 proposalId, address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_queueOperations-uint256-address---uint256---bytes---bytes32-)

Function to queue a proposal to the timelock.

\_executeOperations(uint256 proposalId, address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_executeOperations-uint256-address---uint256---bytes---bytes32-)

Overridden version of the [`Governor._executeOperations`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-) function that runs the already queued proposal through the timelock.

\_cancel(address\[\] targets, uint256\[\] values, bytes\[\] calldatas, bytes32 descriptionHash) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_cancel-address---uint256---bytes---bytes32-)

Overridden version of the [`Governor._cancel`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-) function to cancel the timelocked proposal if it has already been queued.

\_executor() → address

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-_executor--)

Address through which the governor executes action. In this case, the timelock.

updateTimelock(contract TimelockController newTimelock)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-updateTimelock-contract-TimelockController-)

Public endpoint to update the underlying timelock instance. Restricted to the timelock itself, so updates must be proposed, scheduled, and executed through governance proposals.

It is not recommended to change the timelock while there are other queued governance proposals.

TimelockChange(address oldTimelock, address newTimelock)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorTimelockControl-TimelockChange-address-address-)

Emitted when the timelock controller used for proposal execution is modified.

## [`GovernorVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorvotes)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorVotes.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) for voting weight extraction from an [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes) token, or since v4.5 an [`ERC721Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Votes) token.

### Functions

-   [constructor(tokenAddress)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-constructor-contract-IVotes-)
-   [token()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-token--)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-CLOCK_MODE--)
-   [\_getVotes(account, timepoint, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-_getVotes-address-uint256-bytes-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-quorum-uint256-)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(contract IVotes tokenAddress)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-constructor-contract-IVotes-)

token() → contract IERC5805

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-token--)

The token that voting power is sourced from.

clock() → uint48

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-clock--)

Clock (as specified in ERC-6372) is set to match the token's clock. Fallback to block numbers if the token does not implement ERC-6372.

CLOCK\_MODE() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-CLOCK_MODE--)

Machine-readable description of the clock as specified in ERC-6372.

\_getVotes(address account, uint256 timepoint, bytes) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-_getVotes-address-uint256-bytes-)

## [`GovernorVotesQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorvotesquorumfraction)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorVotesQuorumFraction.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";
```

Extension of [`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor) for voting weight extraction from an [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes) token and a quorum expressed as a fraction of the total supply.

### Functions

-   [constructor(quorumNumeratorValue)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-constructor-uint256-)
-   [quorumNumerator()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumNumerator--)
-   [quorumNumerator(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumNumerator-uint256-)
-   [quorumDenominator()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumDenominator--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorum-uint256-)
-   [updateQuorumNumerator(newQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-updateQuorumNumerator-uint256-)
-   [\_updateQuorumNumerator(newQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-_updateQuorumNumerator-uint256-)
-   [\_optimisticUpperLookupRecent(ckpts, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-_optimisticUpperLookupRecent-struct-Checkpoints-Trace208-uint256-)

GovernorVotes

-   [token()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-token--)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-CLOCK_MODE--)
-   [\_getVotes(account, timepoint, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-_getVotes-address-uint256-bytes-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [QuorumNumeratorUpdated(oldQuorumNumerator, newQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-QuorumNumeratorUpdated-uint256-uint256-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

-   [GovernorInvalidQuorumFraction(quorumNumerator, quorumDenominator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-GovernorInvalidQuorumFraction-uint256-uint256-)

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(uint256 quorumNumeratorValue)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-constructor-uint256-)

Initialize quorum as a fraction of the token's total supply.

The fraction is specified as `numerator / denominator`. By default the denominator is 100, so quorum is specified as a percent: a numerator of 10 corresponds to quorum being 10% of total supply. The denominator can be customized by overriding [`GovernorVotesQuorumFraction.quorumDenominator`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumDenominator--).

quorumNumerator() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumNumerator--)

Returns the current quorum numerator. See [`GovernorVotesQuorumFraction.quorumDenominator`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumDenominator--).

quorumNumerator(uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumNumerator-uint256-)

Returns the quorum numerator at a specific timepoint. See [`GovernorVotesQuorumFraction.quorumDenominator`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumDenominator--).

quorumDenominator() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumDenominator--)

Returns the quorum denominator. Defaults to 100, but may be overridden.

quorum(uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorum-uint256-)

Returns the quorum for a timepoint, in terms of number of votes: `supply * numerator / denominator`.

updateQuorumNumerator(uint256 newQuorumNumerator)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-updateQuorumNumerator-uint256-)

Changes the quorum numerator.

Emits a [`GovernorVotesQuorumFraction.QuorumNumeratorUpdated`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-QuorumNumeratorUpdated-uint256-uint256-) event.

Requirements:

-   Must be called through a governance proposal.
-   New numerator must be smaller or equal to the denominator.

\_updateQuorumNumerator(uint256 newQuorumNumerator)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-_updateQuorumNumerator-uint256-)

Changes the quorum numerator.

Emits a [`GovernorVotesQuorumFraction.QuorumNumeratorUpdated`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-QuorumNumeratorUpdated-uint256-uint256-) event.

Requirements:

-   New numerator must be smaller or equal to the denominator.

\_optimisticUpperLookupRecent(struct Checkpoints.Trace208 ckpts, uint256 timepoint) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-_optimisticUpperLookupRecent-struct-Checkpoints-Trace208-uint256-)

Returns the numerator at a specific timepoint.

QuorumNumeratorUpdated(uint256 oldQuorumNumerator, uint256 newQuorumNumerator)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-QuorumNumeratorUpdated-uint256-uint256-)

GovernorInvalidQuorumFraction(uint256 quorumNumerator, uint256 quorumDenominator)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-GovernorInvalidQuorumFraction-uint256-uint256-)

The quorum set is not a valid fraction.

## [`GovernorVotesSuperQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorvotessuperquorumfraction)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/extensions/GovernorVotesSuperQuorumFraction.sol)

```
import "@openzeppelin/contracts/governance/extensions/GovernorVotesSuperQuorumFraction.sol";
```

Extension of [`GovernorVotesQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction) with a super quorum expressed as a fraction of the total supply. Proposals that meet the super quorum (and have a majority of for votes) advance to the `Succeeded` state before the proposal deadline.

### Functions

-   [constructor(superQuorumNumeratorValue)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-constructor-uint256-)
-   [superQuorumNumerator()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-superQuorumNumerator--)
-   [superQuorumNumerator(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-superQuorumNumerator-uint256-)
-   [superQuorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-superQuorum-uint256-)
-   [updateSuperQuorumNumerator(newSuperQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-updateSuperQuorumNumerator-uint256-)
-   [\_updateSuperQuorumNumerator(newSuperQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-_updateSuperQuorumNumerator-uint256-)
-   [\_updateQuorumNumerator(newQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-_updateQuorumNumerator-uint256-)
-   [state(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-state-uint256-)

GovernorSuperQuorum

-   [proposalVotes(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-proposalVotes-uint256-)

GovernorVotesQuorumFraction

-   [quorumNumerator()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumNumerator--)
-   [quorumNumerator(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumNumerator-uint256-)
-   [quorumDenominator()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorumDenominator--)
-   [quorum(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-quorum-uint256-)
-   [updateQuorumNumerator(newQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-updateQuorumNumerator-uint256-)
-   [\_optimisticUpperLookupRecent(ckpts, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-_optimisticUpperLookupRecent-struct-Checkpoints-Trace208-uint256-)

GovernorVotes

-   [token()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-token--)
-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-CLOCK_MODE--)
-   [\_getVotes(account, timepoint, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotes-_getVotes-address-uint256-bytes-)

Governor

-   [receive()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-receive--)
-   [supportsInterface(interfaceId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-supportsInterface-bytes4-)
-   [name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-name--)
-   [version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-version--)
-   [hashProposal(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-hashProposal-address---uint256---bytes---bytes32-)
-   [getProposalId(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getProposalId-address---uint256---bytes---bytes32-)
-   [proposalThreshold()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)
-   [proposalSnapshot(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-)
-   [proposalDeadline(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalDeadline-uint256-)
-   [proposalProposer(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalProposer-uint256-)
-   [proposalEta(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalEta-uint256-)
-   [proposalNeedsQueuing()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalNeedsQueuing-uint256-)
-   [\_checkGovernance()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_checkGovernance--)
-   [\_quorumReached(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_quorumReached-uint256-)
-   [\_voteSucceeded(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-)
-   [\_countVote(proposalId, account, support, totalWeight, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_countVote-uint256-address-uint8-uint256-bytes-)
-   [\_tallyUpdated(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_tallyUpdated-uint256-)
-   [\_defaultParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_defaultParams--)
-   [propose(targets, values, calldatas, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-propose-address---uint256---bytes---string-)
-   [\_propose(targets, values, calldatas, description, proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_propose-address---uint256---bytes---string-address-)
-   [queue(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-queue-address---uint256---bytes---bytes32-)
-   [\_queueOperations(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_queueOperations-uint256-address---uint256---bytes---bytes32-)
-   [execute(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-execute-address---uint256---bytes---bytes32-)
-   [\_executeOperations(, targets, values, calldatas, )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executeOperations-uint256-address---uint256---bytes---bytes32-)
-   [cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-)
-   [\_cancel(targets, values, calldatas, descriptionHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_cancel-address---uint256---bytes---bytes32-)
-   [getVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotes-address-uint256-)
-   [getVotesWithParams(account, timepoint, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-getVotesWithParams-address-uint256-bytes-)
-   [castVote(proposalId, support)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVote-uint256-uint8-)
-   [castVoteWithReason(proposalId, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReason-uint256-uint8-string-)
-   [castVoteWithReasonAndParams(proposalId, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParams-uint256-uint8-string-bytes-)
-   [castVoteBySig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteBySig-uint256-uint8-address-bytes-)
-   [castVoteWithReasonAndParamsBySig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-castVoteWithReasonAndParamsBySig-uint256-uint8-address-string-bytes-bytes-)
-   [\_validateVoteSig(proposalId, support, voter, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateVoteSig-uint256-uint8-address-bytes-)
-   [\_validateExtendedVoteSig(proposalId, support, voter, reason, params, signature)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateExtendedVoteSig-uint256-uint8-address-string-bytes-bytes-)
-   [\_castVote(proposalId, account, support, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-)
-   [\_castVote(proposalId, account, support, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_castVote-uint256-address-uint8-string-bytes-)
-   [relay(target, value, data)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-relay-address-uint256-bytes-)
-   [\_executor()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_executor--)
-   [onERC721Received(, , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC721Received-address-address-uint256-bytes-)
-   [onERC1155Received(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155Received-address-address-uint256-uint256-bytes-)
-   [onERC1155BatchReceived(, , , , )](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-onERC1155BatchReceived-address-address-uint256---uint256---bytes-)
-   [\_encodeStateBitmap(proposalState)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_encodeStateBitmap-enum-IGovernor-ProposalState-)
-   [\_validateStateBitmap(proposalId, allowedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateStateBitmap-uint256-bytes32-)
-   [\_isValidDescriptionForProposer(proposer, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_isValidDescriptionForProposer-address-string-)
-   [\_validateCancel(proposalId, caller)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_validateCancel-uint256-address-)
-   [votingDelay()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)
-   [votingPeriod()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)
-   [BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-BALLOT_TYPEHASH-bytes32)
-   [EXTENDED\_BALLOT\_TYPEHASH()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-EXTENDED_BALLOT_TYPEHASH-bytes32)

IGovernor

-   [COUNTING\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-COUNTING_MODE--)
-   [hasVoted(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-hasVoted-uint256-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

-   [SuperQuorumNumeratorUpdated(oldSuperQuorumNumerator, newSuperQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-SuperQuorumNumeratorUpdated-uint256-uint256-)

GovernorVotesQuorumFraction

-   [QuorumNumeratorUpdated(oldQuorumNumerator, newQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-QuorumNumeratorUpdated-uint256-uint256-)

IGovernor

-   [ProposalCreated(proposalId, proposer, targets, values, signatures, calldatas, voteStart, voteEnd, description)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCreated-uint256-address-address---uint256---string---bytes---uint256-uint256-string-)
-   [ProposalQueued(proposalId, etaSeconds)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalQueued-uint256-uint256-)
-   [ProposalExecuted(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalExecuted-uint256-)
-   [ProposalCanceled(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-ProposalCanceled-uint256-)
-   [VoteCast(voter, proposalId, support, weight, reason)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCast-address-uint256-uint8-uint256-string-)
-   [VoteCastWithParams(voter, proposalId, support, weight, reason, params)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-VoteCastWithParams-address-uint256-uint8-uint256-string-bytes-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

-   [GovernorInvalidSuperQuorumFraction(superQuorumNumerator, denominator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-GovernorInvalidSuperQuorumFraction-uint256-uint256-)
-   [GovernorInvalidSuperQuorumTooSmall(superQuorumNumerator, quorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-GovernorInvalidSuperQuorumTooSmall-uint256-uint256-)
-   [GovernorInvalidQuorumTooLarge(quorumNumerator, superQuorumNumerator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-GovernorInvalidQuorumTooLarge-uint256-uint256-)

GovernorVotesQuorumFraction

-   [GovernorInvalidQuorumFraction(quorumNumerator, quorumDenominator)](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-GovernorInvalidQuorumFraction-uint256-uint256-)

IGovernor

-   [GovernorInvalidProposalLength(targets, calldatas, values)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidProposalLength-uint256-uint256-uint256-)
-   [GovernorAlreadyCastVote(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyCastVote-address-)
-   [GovernorDisabledDeposit()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorDisabledDeposit--)
-   [GovernorOnlyExecutor(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorOnlyExecutor-address-)
-   [GovernorNonexistentProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNonexistentProposal-uint256-)
-   [GovernorUnexpectedProposalState(proposalId, current, expectedStates)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnexpectedProposalState-uint256-enum-IGovernor-ProposalState-bytes32-)
-   [GovernorInvalidVotingPeriod(votingPeriod)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVotingPeriod-uint256-)
-   [GovernorInsufficientProposerVotes(proposer, votes, threshold)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInsufficientProposerVotes-address-uint256-uint256-)
-   [GovernorRestrictedProposer(proposer)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorRestrictedProposer-address-)
-   [GovernorInvalidVoteType()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteType--)
-   [GovernorInvalidVoteParams()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidVoteParams--)
-   [GovernorQueueNotImplemented()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorQueueNotImplemented--)
-   [GovernorNotQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorNotQueuedProposal-uint256-)
-   [GovernorAlreadyQueuedProposal(proposalId)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorAlreadyQueuedProposal-uint256-)
-   [GovernorInvalidSignature(voter)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorInvalidSignature-address-)
-   [GovernorUnableToCancel(proposalId, account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IGovernor-GovernorUnableToCancel-uint256-address-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

constructor(uint256 superQuorumNumeratorValue)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-constructor-uint256-)

Initialize super quorum as a fraction of the token's total supply.

The super quorum is specified as a fraction of the token's total supply and has to be greater than the quorum.

superQuorumNumerator() → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-superQuorumNumerator--)

Returns the current super quorum numerator.

superQuorumNumerator(uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-superQuorumNumerator-uint256-)

Returns the super quorum numerator at a specific `timepoint`.

superQuorum(uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-superQuorum-uint256-)

Returns the super quorum for a `timepoint`, in terms of number of votes: `supply * numerator / denominator`. See [`GovernorSuperQuorum.superQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum-superQuorum-uint256-) for more details.

updateSuperQuorumNumerator(uint256 newSuperQuorumNumerator)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-updateSuperQuorumNumerator-uint256-)

Changes the super quorum numerator.

Emits a [`GovernorVotesSuperQuorumFraction.SuperQuorumNumeratorUpdated`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-SuperQuorumNumeratorUpdated-uint256-uint256-) event.

Requirements:

-   Must be called through a governance proposal.
-   New super quorum numerator must be smaller or equal to the denominator.
-   New super quorum numerator must be greater than or equal to the quorum numerator.

\_updateSuperQuorumNumerator(uint256 newSuperQuorumNumerator)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-_updateSuperQuorumNumerator-uint256-)

Changes the super quorum numerator.

Emits a [`GovernorVotesSuperQuorumFraction.SuperQuorumNumeratorUpdated`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-SuperQuorumNumeratorUpdated-uint256-uint256-) event.

Requirements:

-   New super quorum numerator must be smaller or equal to the denominator.
-   New super quorum numerator must be greater than or equal to the quorum numerator.

\_updateQuorumNumerator(uint256 newQuorumNumerator)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-_updateQuorumNumerator-uint256-)

Overrides [`GovernorVotesQuorumFraction._updateQuorumNumerator`](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction-_updateQuorumNumerator-uint256-) to ensure the super quorum numerator is greater than or equal to the quorum numerator.

state(uint256 proposalId) → enum IGovernor.ProposalState

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-state-uint256-)

Overridden version of the [`Governor.state`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-state-uint256-) function that checks if the proposal has reached the super quorum.

If the proposal reaches super quorum but [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-) returns false, eg, assuming the super quorum has been set low enough that both FOR and AGAINST votes have exceeded it and AGAINST votes exceed FOR votes, the proposal continues to be active until [`Governor._voteSucceeded`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-_voteSucceeded-uint256-) returns true or the proposal deadline is reached. This means that with a low super quorum it is also possible that a vote can succeed prematurely before enough AGAINST voters have a chance to vote. Hence, it is recommended to set a high enough super quorum to avoid these types of scenarios.

SuperQuorumNumeratorUpdated(uint256 oldSuperQuorumNumerator, uint256 newSuperQuorumNumerator)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-SuperQuorumNumeratorUpdated-uint256-uint256-)

GovernorInvalidSuperQuorumFraction(uint256 superQuorumNumerator, uint256 denominator)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-GovernorInvalidSuperQuorumFraction-uint256-uint256-)

The super quorum set is not valid as it exceeds the quorum denominator.

GovernorInvalidSuperQuorumTooSmall(uint256 superQuorumNumerator, uint256 quorumNumerator)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-GovernorInvalidSuperQuorumTooSmall-uint256-uint256-)

The super quorum set is not valid as it is smaller or equal to the quorum.

GovernorInvalidQuorumTooLarge(uint256 quorumNumerator, uint256 superQuorumNumerator)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesSuperQuorumFraction-GovernorInvalidQuorumTooLarge-uint256-uint256-)

The quorum set is not valid as it exceeds the super quorum.

## [`IVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#ivotes)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/utils/IVotes.sol)

```
import "@openzeppelin/contracts/governance/utils/IVotes.sol";
```

Common interface for [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes), [`ERC721Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Votes), and other [`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes)\-enabled contracts.

### Functions

-   [getVotes(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-getVotes-address-)
-   [getPastVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-getPastVotes-address-uint256-)
-   [getPastTotalSupply(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-getPastTotalSupply-uint256-)
-   [delegates(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-delegates-address-)
-   [delegate(delegatee)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-delegate-address-)
-   [delegateBySig(delegatee, nonce, expiry, v, r, s)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-delegateBySig-address-uint256-uint256-uint8-bytes32-bytes32-)

### Events

-   [DelegateChanged(delegator, fromDelegate, toDelegate)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateChanged-address-address-address-)
-   [DelegateVotesChanged(delegate, previousVotes, newVotes)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateVotesChanged-address-uint256-uint256-)

### Errors

-   [VotesExpiredSignature(expiry)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-VotesExpiredSignature-uint256-)

getVotes(address account) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-getVotes-address-)

Returns the current amount of votes that `account` has.

getPastVotes(address account, uint256 timepoint) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-getPastVotes-address-uint256-)

Returns the amount of votes that `account` had at a specific moment in the past. If the `clock()` is configured to use block numbers, this will return the value at the end of the corresponding block.

getPastTotalSupply(uint256 timepoint) → uint256

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-getPastTotalSupply-uint256-)

Returns the total supply of votes available at a specific moment in the past. If the `clock()` is configured to use block numbers, this will return the value at the end of the corresponding block.

This value is the sum of all available votes, which is not necessarily the sum of all delegated votes. Votes that have not been delegated are still part of total supply, even though they would not participate in a vote.

delegates(address account) → address

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-delegates-address-)

Returns the delegate that `account` has chosen.

delegate(address delegatee)

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-delegate-address-)

Delegates votes from the sender to `delegatee`.

delegateBySig(address delegatee, uint256 nonce, uint256 expiry, uint8 v, bytes32 r, bytes32 s)

external

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-delegateBySig-address-uint256-uint256-uint8-bytes32-bytes32-)

Delegates votes from signer to `delegatee`.

DelegateChanged(address indexed delegator, address indexed fromDelegate, address indexed toDelegate)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateChanged-address-address-address-)

Emitted when an account changes their delegate.

DelegateVotesChanged(address indexed delegate, uint256 previousVotes, uint256 newVotes)

event

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateVotesChanged-address-uint256-uint256-)

Emitted when a token transfer or delegate change results in changes to a delegate's number of voting units.

VotesExpiredSignature(uint256 expiry)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-VotesExpiredSignature-uint256-)

The signature used has expired.

## [`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#votes)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/utils/Votes.sol)

```
import "@openzeppelin/contracts/governance/utils/Votes.sol";
```

This is a base abstract contract that tracks voting units, which are a measure of voting power that can be transferred, and provides a system of vote delegation, where an account can delegate its voting units to a sort of "representative" that will pool delegated voting units from different accounts and can then use it to vote in decisions. In fact, voting units *must* be delegated in order to count as actual votes, and an account has to delegate those votes to itself if it wishes to participate in decisions and does not have a trusted representative.

This contract is often combined with a token contract such that voting units correspond to token units. For an example, see [`ERC721Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Votes).

The full history of delegate votes is tracked on-chain so that governance protocols can consider votes as distributed at a particular block number to protect against flash loans and double voting. The opt-in delegate system makes the cost of this history tracking optional.

When using this module the derived contract must implement [`Votes._getVotingUnits`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getVotingUnits-address-) (for example, make it return [`ERC721.balanceOf`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721-balanceOf-address-)), and can use [`Votes._transferVotingUnits`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_transferVotingUnits-address-address-uint256-) to track a change in the distribution of those units (in the previous example, it would be included in [`ERC721._update`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721-_update-address-uint256-address-)).

### Functions

-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-CLOCK_MODE--)
-   [\_validateTimepoint(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_validateTimepoint-uint256-)
-   [getVotes(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getVotes-address-)
-   [getPastVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getPastVotes-address-uint256-)
-   [getPastTotalSupply(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getPastTotalSupply-uint256-)
-   [\_getTotalSupply()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getTotalSupply--)
-   [delegates(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegates-address-)
-   [delegate(delegatee)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegate-address-)
-   [delegateBySig(delegatee, nonce, expiry, v, r, s)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegateBySig-address-uint256-uint256-uint8-bytes32-bytes32-)
-   [\_delegate(account, delegatee)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_delegate-address-address-)
-   [\_transferVotingUnits(from, to, amount)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_transferVotingUnits-address-address-uint256-)
-   [\_moveDelegateVotes(from, to, amount)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_moveDelegateVotes-address-address-uint256-)
-   [\_numCheckpoints(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_numCheckpoints-address-)
-   [\_checkpoints(account, pos)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_checkpoints-address-uint32-)
-   [\_getVotingUnits()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getVotingUnits-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IVotes

-   [DelegateChanged(delegator, fromDelegate, toDelegate)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateChanged-address-address-address-)
-   [DelegateVotesChanged(delegate, previousVotes, newVotes)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateVotesChanged-address-uint256-uint256-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

-   [ERC6372InconsistentClock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-ERC6372InconsistentClock--)
-   [ERC5805FutureLookup(timepoint, clock)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-ERC5805FutureLookup-uint256-uint48-)

IVotes

-   [VotesExpiredSignature(expiry)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-VotesExpiredSignature-uint256-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

clock() → uint48

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-clock--)

Clock used for flagging checkpoints. Can be overridden to implement timestamp based checkpoints (and voting), in which case [`Governor.CLOCK_MODE`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-CLOCK_MODE--) should be overridden as well to match.

CLOCK\_MODE() → string

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-CLOCK_MODE--)

Machine-readable description of the clock as specified in ERC-6372.

\_validateTimepoint(uint256 timepoint) → uint48

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_validateTimepoint-uint256-)

Validate that a timepoint is in the past, and return it as a uint48.

getVotes(address account) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getVotes-address-)

Returns the current amount of votes that `account` has.

getPastVotes(address account, uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getPastVotes-address-uint256-)

Returns the amount of votes that `account` had at a specific moment in the past. If the `clock()` is configured to use block numbers, this will return the value at the end of the corresponding block.

Requirements:

-   `timepoint` must be in the past. If operating using block numbers, the block must be already mined.

getPastTotalSupply(uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getPastTotalSupply-uint256-)

Returns the total supply of votes available at a specific moment in the past. If the `clock()` is configured to use block numbers, this will return the value at the end of the corresponding block.

This value is the sum of all available votes, which is not necessarily the sum of all delegated votes. Votes that have not been delegated are still part of total supply, even though they would not participate in a vote.

Requirements:

-   `timepoint` must be in the past. If operating using block numbers, the block must be already mined.

\_getTotalSupply() → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getTotalSupply--)

Returns the current total supply of votes.

delegates(address account) → address

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegates-address-)

Returns the delegate that `account` has chosen.

delegate(address delegatee)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegate-address-)

Delegates votes from the sender to `delegatee`.

delegateBySig(address delegatee, uint256 nonce, uint256 expiry, uint8 v, bytes32 r, bytes32 s)

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegateBySig-address-uint256-uint256-uint8-bytes32-bytes32-)

Delegates votes from signer to `delegatee`.

\_delegate(address account, address delegatee)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_delegate-address-address-)

Delegate all of `account`'s voting units to `delegatee`.

Emits events [`IVotes.DelegateChanged`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateChanged-address-address-address-) and [`IVotes.DelegateVotesChanged`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateVotesChanged-address-uint256-uint256-).

\_transferVotingUnits(address from, address to, uint256 amount)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_transferVotingUnits-address-address-uint256-)

Transfers, mints, or burns voting units. To register a mint, `from` should be zero. To register a burn, `to` should be zero. Total supply of voting units will be adjusted with mints and burns.

\_moveDelegateVotes(address from, address to, uint256 amount)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_moveDelegateVotes-address-address-uint256-)

Moves delegated votes from one delegate to another.

\_numCheckpoints(address account) → uint32

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_numCheckpoints-address-)

Get number of checkpoints for `account`.

\_checkpoints(address account, uint32 pos) → struct Checkpoints.Checkpoint208

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_checkpoints-address-uint32-)

Get the `pos`\-th checkpoint for `account`.

\_getVotingUnits(address) → uint256

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getVotingUnits-address-)

Must return the voting units held by an account.

ERC6372InconsistentClock()

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-ERC6372InconsistentClock--)

The clock was incorrectly modified.

ERC5805FutureLookup(uint256 timepoint, uint48 clock)

error

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-ERC5805FutureLookup-uint256-uint48-)

Lookup to future votes is not available.

## [`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#votesextended)

[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.6.1/contracts/governance/utils/VotesExtended.sol)

```
import "@openzeppelin/contracts/governance/utils/VotesExtended.sol";
```

Extension of [`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes) that adds checkpoints for delegations and balances.

While this contract extends [`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes), valid uses of [`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes) may not be compatible with [`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended) without additional considerations. This implementation of [`Votes._transferVotingUnits`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_transferVotingUnits-address-address-uint256-) must run AFTER the voting weight movement is registered, such that it is reflected on [`Votes._getVotingUnits`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getVotingUnits-address-).

Said differently, [`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended) MUST be integrated in a way that calls [`Votes._transferVotingUnits`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_transferVotingUnits-address-address-uint256-) AFTER the asset transfer is registered and balances are updated:

```
contract VotingToken is Token, VotesExtended {
  function transfer(address from, address to, uint256 tokenId) public override {
    super.transfer(from, to, tokenId); // <- Perform the transfer first ...
    _transferVotingUnits(from, to, 1); // <- ... then call _transferVotingUnits.
  }

  function _getVotingUnits(address account) internal view override returns (uint256) {
     return balanceOf(account);
  }
}
```

[`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes) and [`ERC721Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Votes) follow this pattern and are thus safe to use with [`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended).

### Functions

-   [getPastDelegate(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-getPastDelegate-address-uint256-)
-   [getPastBalanceOf(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-getPastBalanceOf-address-uint256-)
-   [\_delegate(account, delegatee)](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-_delegate-address-address-)
-   [\_transferVotingUnits(from, to, amount)](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-_transferVotingUnits-address-address-uint256-)

Votes

-   [clock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-clock--)
-   [CLOCK\_MODE()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-CLOCK_MODE--)
-   [\_validateTimepoint(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_validateTimepoint-uint256-)
-   [getVotes(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getVotes-address-)
-   [getPastVotes(account, timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getPastVotes-address-uint256-)
-   [getPastTotalSupply(timepoint)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-getPastTotalSupply-uint256-)
-   [\_getTotalSupply()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getTotalSupply--)
-   [delegates(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegates-address-)
-   [delegate(delegatee)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegate-address-)
-   [delegateBySig(delegatee, nonce, expiry, v, r, s)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegateBySig-address-uint256-uint256-uint8-bytes32-bytes32-)
-   [\_moveDelegateVotes(from, to, amount)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_moveDelegateVotes-address-address-uint256-)
-   [\_numCheckpoints(account)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_numCheckpoints-address-)
-   [\_checkpoints(account, pos)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_checkpoints-address-uint32-)
-   [\_getVotingUnits()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-_getVotingUnits-address-)

Nonces

-   [nonces(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-nonces-address-)
-   [\_useNonce(owner)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useNonce-address-)
-   [\_useCheckedNonce(owner, nonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-_useCheckedNonce-address-uint256-)

EIP712

-   [\_domainSeparatorV4()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_domainSeparatorV4--)
-   [\_hashTypedDataV4(structHash)](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_hashTypedDataV4-bytes32-)
-   [eip712Domain()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-eip712Domain--)
-   [\_EIP712Name()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Name--)
-   [\_EIP712Version()](https://docs.openzeppelin.com/contracts/5.x/api/governance#EIP712-_EIP712Version--)

### Events

IVotes

-   [DelegateChanged(delegator, fromDelegate, toDelegate)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateChanged-address-address-address-)
-   [DelegateVotesChanged(delegate, previousVotes, newVotes)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateVotesChanged-address-uint256-uint256-)

IERC5267

-   [EIP712DomainChanged()](https://docs.openzeppelin.com/contracts/5.x/api/governance#IERC5267-EIP712DomainChanged--)

### Errors

Votes

-   [ERC6372InconsistentClock()](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-ERC6372InconsistentClock--)
-   [ERC5805FutureLookup(timepoint, clock)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-ERC5805FutureLookup-uint256-uint48-)

IVotes

-   [VotesExpiredSignature(expiry)](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-VotesExpiredSignature-uint256-)

Nonces

-   [InvalidAccountNonce(account, currentNonce)](https://docs.openzeppelin.com/contracts/5.x/api/governance#Nonces-InvalidAccountNonce-address-uint256-)

getPastDelegate(address account, uint256 timepoint) → address

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-getPastDelegate-address-uint256-)

Returns the delegate of an `account` at a specific moment in the past. If the `clock()` is configured to use block numbers, this will return the value at the end of the corresponding block.

Requirements:

-   `timepoint` must be in the past. If operating using block numbers, the block must be already mined.

getPastBalanceOf(address account, uint256 timepoint) → uint256

public

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-getPastBalanceOf-address-uint256-)

Returns the `balanceOf` of an `account` at a specific moment in the past. If the `clock()` is configured to use block numbers, this will return the value at the end of the corresponding block.

Requirements:

-   `timepoint` must be in the past. If operating using block numbers, the block must be already mined.

\_delegate(address account, address delegatee)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-_delegate-address-address-)

Delegate all of `account`'s voting units to `delegatee`.

Emits events [`IVotes.DelegateChanged`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateChanged-address-address-address-) and [`IVotes.DelegateVotesChanged`](https://docs.openzeppelin.com/contracts/5.x/api/governance#IVotes-DelegateVotesChanged-address-uint256-uint256-).

\_transferVotingUnits(address from, address to, uint256 amount)

internal

[#](https://docs.openzeppelin.com/contracts/5.x/api/governance#VotesExtended-_transferVotingUnits-address-address-uint256-)

Transfers, mints, or burns voting units. To register a mint, `from` should be zero. To register a burn, `to` should be zero. Total supply of voting units will be adjusted with mints and burns.

[

Finance

Previous Page

](https://docs.openzeppelin.com/contracts/5.x/api/finance)[

Interfaces

Next Page

](https://docs.openzeppelin.com/contracts/5.x/api/interfaces)

### On this page

[Governor](https://docs.openzeppelin.com/contracts/5.x/api/governance#governor)[Core](https://docs.openzeppelin.com/contracts/5.x/api/governance#core)[Modules](https://docs.openzeppelin.com/contracts/5.x/api/governance#modules)[Extensions](https://docs.openzeppelin.com/contracts/5.x/api/governance#extensions)[Utils](https://docs.openzeppelin.com/contracts/5.x/api/governance#utils)[Timelock](https://docs.openzeppelin.com/contracts/5.x/api/governance#timelock)[Terminology](https://docs.openzeppelin.com/contracts/5.x/api/governance#terminology)[Operation structure](https://docs.openzeppelin.com/contracts/5.x/api/governance#operation-structure)[Operation lifecycle](https://docs.openzeppelin.com/contracts/5.x/api/governance#operation-lifecycle)[Roles](https://docs.openzeppelin.com/contracts/5.x/api/governance#roles)[Admin](https://docs.openzeppelin.com/contracts/5.x/api/governance#admin)[Proposer](https://docs.openzeppelin.com/contracts/5.x/api/governance#proposer)[Executor](https://docs.openzeppelin.com/contracts/5.x/api/governance#executor)[`Governor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governor-1)[`IGovernor`](https://docs.openzeppelin.com/contracts/5.x/api/governance#igovernor)[`TimelockController`](https://docs.openzeppelin.com/contracts/5.x/api/governance#timelockcontroller)[`GovernorCountingFractional`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorcountingfractional)[`GovernorCountingOverridable`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorcountingoverridable)[`GovernorCountingSimple`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorcountingsimple)[`GovernorNoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governornonceskeyed)[`GovernorPreventLateQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorpreventlatequorum)[`GovernorProposalGuardian`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorproposalguardian)[`GovernorSequentialProposalId`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorsequentialproposalid)[`GovernorSettings`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorsettings)[`GovernorStorage`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorstorage)[`GovernorSuperQuorum`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorsuperquorum)[`GovernorTimelockAccess`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governortimelockaccess)[Security Considerations](https://docs.openzeppelin.com/contracts/5.x/api/governance#security-considerations)[`GovernorTimelockCompound`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governortimelockcompound)[`GovernorTimelockControl`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governortimelockcontrol)[`GovernorVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorvotes)[`GovernorVotesQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorvotesquorumfraction)[`GovernorVotesSuperQuorumFraction`](https://docs.openzeppelin.com/contracts/5.x/api/governance#governorvotessuperquorumfraction)[`IVotes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#ivotes)[`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#votes)[`VotesExtended`](https://docs.openzeppelin.com/contracts/5.x/api/governance#votesextended)
