// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IStakingReentryTarget {
    function stakeStart(uint256 stakeValue, uint256 stakeDays, address staker) external returns (uint256);
}

/// @dev Test fixture for checking the staking contract's transferFrom callback guard.
contract ReentrantERC20Mock {
    string public constant name = "Reentrant Test Token";
    string public constant symbol = "RTT";
    uint8 public constant decimals = 18;

    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    IStakingReentryTarget public staking;
    bool public reentryRejected;
    bool public returnFalseFrom;
    uint256 public transferFeeBps;

    function setStaking(address stakingAddress) external {
        staking = IStakingReentryTarget(stakingAddress);
    }

    function setTransferFeeBps(uint256 feeBps) external {
        require(feeBps <= 10_000, "Fee exceeds 100 percent.");
        transferFeeBps = feeBps;
    }

    function setReturnFalseFrom(bool shouldReturnFalse) external {
        returnFalseFrom = shouldReturnFalse;
    }

    function mint(address account, uint256 amount) external {
        totalSupply += amount;
        balanceOf[account] += amount;
    }

    function burn(uint256 amount) external {
        balanceOf[msg.sender] -= amount;
        totalSupply -= amount;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        return true;
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        try staking.stakeStart(amount, 1, from) {
            reentryRejected = false;
        } catch {
            reentryRejected = true;
        }

        if (returnFalseFrom) {
            return false;
        }

        allowance[from][msg.sender] -= amount;
        balanceOf[from] -= amount;
        uint256 fee = (amount * transferFeeBps) / 10_000;
        balanceOf[to] += amount - fee;
        totalSupply -= fee;
        return true;
    }
}
