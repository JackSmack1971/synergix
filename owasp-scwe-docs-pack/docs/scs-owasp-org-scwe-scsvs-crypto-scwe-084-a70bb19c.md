---
title: "SCWE-084: Insecure Use of blockhash"
source_url: "https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:34.676Z"
---
*Last updated: August 19, 2026*


# SCWE-084: Insecure Use of blockhash

Stable Version v1.0

This content is in the **version-(v1.0)** and still under active development, so it is subject to change any time (e.g. structure, IDs, content, URLs, etc.).

[Send Feedback](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/discussions/categories/scwe-scstg-v2-beta-feedback)

## Relationships[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#relationships "Permanent link")

-   CWE-20: Improper Input Validation
    [https://cwe.mitre.org/data/definitions/20.html](https://cwe.mitre.org/data/definitions/20.html)

## Description[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#description "Permanent link")

The `blockhash` function is often misused to generate randomness in smart contracts. However, `blockhash` is publicly available and can be influenced by validators (or miners on PoW chains), making it an unreliable and insecure source of randomness.

Attackers can manipulate `blockhash` by controlling which transactions are included in a block, reordering transactions, or discarding unfavorable blocks. This can lead to predictable random outcomes, allowing malicious actors to exploit lotteries, gaming, and other randomness-dependent mechanisms.

**Attack Scenarios** - Lottery Manipulation: A validator (or miner on PoW) can withhold or reorder transactions to ensure a favorable `blockhash` that lets them win. - Game Exploitation: If a game outcome depends on `blockhash`, an attacker can predict future results and place bets accordingly.

## Remediation[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#remediation "Permanent link")

Do not rely on `blockhash` for generating randomness. Use more secure and unpredictable sources of randomness, such as using Chainlink VRF or other trusted oracles.

### Vulnerable Contract Example[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#vulnerable-contract-example "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-1)// Vulnerable contract using blockhash for randomness [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-2)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-3)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-4)contract InsecureRandomness {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-5)    function getRandomNumber(uint256 _blockNumber) public view returns (uint256) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-6)        return uint256(blockhash(_blockNumber)); // Predictable randomness    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-7)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-0-8)}`

**Why is this insecure?** - Validators (or miners on PoW) control block production — they can reorder or discard blocks to manipulate `blockhash`. - Predictability - Attackers can call this function for past block numbers, making randomness guessable.

### Fixed Contract Example- Secure Random Number Generation Using Chainlink VRF[¶](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#fixed-contract-example-secure-random-number-generation-using-chainlink-vrf "Permanent link")

`[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-1)pragma solidity ^0.8.0; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-2)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-3)import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol"; // Note: Chainlink VRF V1 is deprecated; use VRF V2 (VRFConsumerBaseV2) in production [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-4)[](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-5)contract SecureLottery is VRFConsumerBase {     [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-6)    address[] public players;    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-7)    bytes32 internal keyHash;    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-8)    uint256 internal fee;    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-9)    uint256 public randomResult; [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-10)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-11)    constructor()        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-12)        VRFConsumerBase(            [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-13)            0x514910771AF9Ca656af840dff83E8264EcF986CA, // Chainlink VRF Coordinator            [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-14)            0x514910771AF9Ca656af840dff83E8264EcF986CA // LINK Token address        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-15)        )    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-16)    {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-17)        keyHash = 0x6c3699283bda56ad74f6b855546325b68d482e983852a617d11109b44b8aab01;        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-18)        fee = 0.1 * 10**18; // 0.1 LINK (varies by network)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-19)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-20)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-21)    function enter() public payable {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-22)        require(msg.value > 0.1 ether, "Minimum ETH required");        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-23)        players.push(msg.sender);    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-24)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-25)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-26)    function requestRandomWinner() public returns (bytes32 requestId) {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-27)        require(players.length > 0, "No players joined");        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-28)        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK");        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-29)        return requestRandomness(keyHash, fee);    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-30)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-31)    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-32)    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-33)        uint256 index = randomness % players.length;        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-34)        (bool ok, ) = payable(players[index]).call{value: address(this).balance}("");        [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-35)        require(ok, "Transfer failed");    [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-36)    } [](https://scs.owasp.org/SCWE/SCSVS-CRYPTO/SCWE-084/#__codelineno-1-37)}`

**Why is this secure?** - Uses `Chainlink VRF` (Verifiable Random Function), which provides unpredictable, tamper-proof randomness. - Validators (or miners on PoW) cannot manipulate the randomness as it is derived from a verifiable external source. - Players cannot predict the outcome before participating.
