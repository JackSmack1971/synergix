# Economic-security decision checks

Load only the checks needed for the active branch, keeping concrete source/code references for findings.

## 1. Identity, mint semantics, effective cap

- Resolve chain ID, contract address, token decimals, block height and archive state; proxy address vs implementation; governance or beacon/diamond facets; source verification hash; prior upgrade events.
- Enumerate every mint path, including role-gated internal calls, vesting minters, bridges, reward controllers, inflation rebases, upgrades, timelock operations and cross-chain inbound messages. Compute reachable mint bound by authority and time, not by advertised `maxSupply` variable alone.
- Distinguish mint-at-genesis unlocked allocations from deferred minting. A vested pre-minted token release increases float but does not increase total supply. Burns lower outstanding supply only where tokens really are destroyed; transfers to dead-looking addresses may not. Consider cap refill when burned tokens make headroom.
- Examine external bridges for locked canonical collateral vs separately minted representations; whether representations are circulating on multiple chains; replay limits, mint authentication, finality, escrow backing and supply proofs. If unverifiable, explicitly limit analysis to the resolved chain.

## 2. Distribution and vesting

- Reconcile allocations to full genesis or total allocation budget; mark unscheduled/unallocated reserve. Document cliff convention and final unlock date, revocability, beneficiary-change authority, claim permission, early termination or acceleration, unvested collateral, staking boosts, and whether an admin can move reserved tokens before release.
- Model month 0..36 minimum; if vesting ends after 36, disclose tail. Identify month-by-month unlocks relative to previous float and multiple coincident cliffs. Avoid claiming team/investor ownership from allocation schedules; wallet current share requires a holder snapshot and holder entity clustering assumptions.
- Heuristics requiring scrutiny, not categorical breaches: combined insider allocation around or above 20% without robust vesting; cliff less than 12 months for core teams; highly concentrated TGE float; short cliffs with minimal sinks; milestone/price vesting games and oracle manipulation. No fixed cliff length is mandatory or universally "standard".

## 3. Utility, value, and incentive loop

- Map payable actions -> received asset -> contract accounting -> distribution -> token impact -> authority that can redirect/disable the flow. Is the token **necessary** for core usage, an optional payment substitute, a discount instrument or just a governance claim?
- Model recurring rewards from external revenue separately from newly minted emissions, token transfers from treasury and recycling of existing liquidity; avoid equating staking APY with economic yield. Compute `NetIssuance = mints - burns` separately from net *circulating* unlocks.
- Stress incentives under near-zero product usage and migration: what funds validators/LPs/stakers when fees are negligible? Are liquidity incentives just timed subsidies? Is revenue contract-captured, manually discretionary, or easily redirected by privileged parameter updates? Verify fee splits and no alternate paths that evade fee payment.
- Pure calendar *vesting* is not by itself an economic defect. Scheduled *emissions* without a funded value loop can be unsustainable, but can sometimes fund explicit bootstrapping; judge by bounded budget, utility, duration, measurable results and scenario outcomes.

## 4. Governance capture and privilege graph

- Trace all roles, owner/admin ability to grant/revoke, multisig threshold + signer independence, delay changes, guardian/veto bypass, arbitrary calls, upgrade rights, pause/blacklist/confiscate paths, veto/emergency/executor roles, cancellation, delegation and proposal validation.
- Estimate quorum/threshold *using actual voting weight at relevant snapshot*, including delegation, token lending, flash loans, voting snapshots, temporary votes and holdings across treasuries. Time locks constrain execution latency but do not cure captured voting or instantly executable emergency roles.
- If governance is token-weighted, test if a coordinated entity can acquire or delegate enough votes to meet proposal threshold/quorum, pass snapshot checks and execute arbitrary tokenomics changes. Treat attack loans and market availability as conditional, not established facts.
- For contract-change recommendations consider capped supply, signed mint budget, segmented roles, least privilege, delayed parameter increases, independent cancellation and time-delay minimums, and revocation/renunciation only if recovery impact is acceptable.

## 5. Contract-to-economics testing

- Test proposed invariants: no increase past cap; entire vesting sum accounted; precise cliff boundary (`month 0, cliff, cliff+1, final`); no early claim/revocation unless intended; role grant or upgrade path cannot circumvent budget; unauthorized mint/fee diversion reverts; timelock and governance quorum settings are effective; bridge mint backed by locked supply.
- When editing code, honor existing repository architecture, dependencies and `AGENTS.md`; benchmark existing behavior before changes. Prefer isolated read-only call simulations, local fork or unit tests; do not use live contracts to "test" an exploit.
- A well-known library (e.g. OpenZeppelin ERC20Capped/VestingWallet/Governor/TimelockController) is a candidate design primitive, not a proof that the deployed custom integration is safe. Check effective version, inheritance hooks, initializers, privilege chains and implementation code.

## 6. Regulatory flagging (not legal assessment)

- Note issuer/operator promises, profit expectations from others' efforts, enforceable dividends/revenue claims, redemption/repurchase mechanisms, sale and distribution context, market-making, control and governance representations, geography and users. Classify as **counsel-review flags** only.
- U.S. interpretation changed in March 2026; distinguish asset characterization from transactions/offers involving it. Consult regulator-issued contemporaneous sources for the jurisdiction and date. A proposed rule is not final law.

## Pointers to primary technical and regulatory references (verify versions when used)

- OpenZeppelin ERC20 modules, including `ERC20Capped`, `ERC20Pausable`, `ERC20Votes`: https://docs.openzeppelin.com/contracts/5.x/api/token/erc20
- OpenZeppelin governance and timelock: https://docs.openzeppelin.com/contracts/5.x/governance
- OpenZeppelin vesting wallet and vesting caveats: https://docs.openzeppelin.com/contracts/5.x/api/finance
- SEC March 17, 2026 interpretation (effective March 23, 2026): https://www.sec.gov/rules-regulations/2026/03/s7-2026-09
- SEC explanatory guidance, April 22, 2026: https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/transactions-involving-crypto-assets
