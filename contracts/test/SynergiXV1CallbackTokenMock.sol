// SPDX-License-Identifier: MIT
pragma solidity =0.8.38;

/// @dev Test-only ERC20 double for adversarial V1 deposit behavior.
contract SynergiXV1CallbackTokenMock {
    string public constant name = "V1 Callback Token";
    string public constant symbol = "V1CB";
    uint8 public constant decimals = 18;

    /// @notice Total token supply in this test fixture.
    uint256 public totalSupply;
    /// @notice Token balances in this test fixture.
    mapping(address account => uint256 balance) public balanceOf;
    /// @notice Token allowances in this test fixture.
    mapping(address account => mapping(address spender => uint256 amount)) public allowance;

    /// @notice Target called during the next transferFrom operation when configured.
    address public callbackTarget;
    /// @notice Calldata sent to the configured transferFrom callback target.
    bytes public callbackData;
    /// @notice Whether a callback has been attempted.
    bool public callbackAttempted;
    /// @notice Whether the most recent callback succeeded.
    bool public callbackSucceeded;
    /// @notice Whether transferFrom is configured to return false.
    bool public returnFalseFrom;
    /// @notice Fee deducted from transfers in basis points.
    uint16 public transferFeeBps;
    /// @notice Whether this fixture returns empty data from token transfers.
    bool public returnNoData;
    /// @notice Whether this fixture rejects token transfers while paused.
    bool public transfersPaused;

    /// @notice Mints tokens for test setup.
    /// @param account Account receiving tokens.
    /// @param amount Amount to mint.
    function mint(address account, uint256 amount) external {
        totalSupply += amount;
        balanceOf[account] += amount;
    }

    /// @notice Sets an allowance for test transfers.
    /// @param spender Account allowed to transfer tokens.
    /// @param amount Maximum transfer amount.
    /// @return success Whether the allowance was set.
    function approve(address spender, uint256 amount) external returns (bool success) {
        allowance[msg.sender][spender] = amount;
        return true;
    }

    /// @notice Configures an arbitrary callback during transferFrom.
    /// @param target Callback contract.
    /// @param data Calldata sent to the callback contract.
    function configureCallback(address target, bytes calldata data) external {
        callbackTarget = target;
        callbackData = data;
        callbackAttempted = false;
        callbackSucceeded = false;
    }

    /// @notice Configures false-return and fee-on-transfer test behavior.
    /// @param shouldReturnFalse Whether transferFrom returns false.
    /// @param feeBps Fee deducted from transfers in basis points.
    function configureTransferBehavior(bool shouldReturnFalse, uint16 feeBps) external {
        require(feeBps <= 10_000, "fee too large");
        returnFalseFrom = shouldReturnFalse;
        transferFeeBps = feeBps;
    }

    /// @notice Configures empty return data to model nonstandard ERC20 tokens.
    /// @param shouldReturnNoData Whether transfer and transferFrom return no data.
    function configureNoReturn(bool shouldReturnNoData) external {
        returnNoData = shouldReturnNoData;
    }

    /// @notice Pauses or resumes test token transfers.
    /// @param isPaused Whether transfers are paused.
    function setTransfersPaused(bool isPaused) external {
        transfersPaused = isPaused;
    }

    /// @notice Transfers tokens in the test fixture.
    /// @param to Recipient account.
    /// @param amount Amount to transfer.
    /// @return success Whether the transfer succeeded.
    function transfer(address to, uint256 amount) external returns (bool success) {
        _runCallback();
        _transfer(msg.sender, to, amount);
        if (returnNoData) assembly { return(0, 0) }
        return true;
    }

    /// @notice Transfers tokens and optionally attempts a callback or returns false.
    /// @param from Source account.
    /// @param to Recipient account.
    /// @param amount Amount to transfer.
    /// @return success Whether the transfer succeeded.
    function transferFrom(address from, address to, uint256 amount) external returns (bool success) {
        if (returnFalseFrom) return false;
        _runCallback();

        uint256 permitted = allowance[from][msg.sender];
        require(permitted >= amount, "insufficient allowance");
        if (permitted != type(uint256).max) allowance[from][msg.sender] = permitted - amount;
        _transfer(from, to, amount);
        if (returnNoData) assembly { return(0, 0) }
        return true;
    }

    function _runCallback() private {
        if (callbackTarget != address(0)) {
            callbackAttempted = true;
            (callbackSucceeded,) = callbackTarget.call(callbackData);
        }
    }

    function _transfer(address from, address to, uint256 amount) private {
        require(!transfersPaused, "transfers paused");
        require(to != address(0), "zero receiver");
        require(balanceOf[from] >= amount, "insufficient balance");
        balanceOf[from] -= amount;
        uint256 fee = (amount * transferFeeBps) / 10_000;
        balanceOf[to] += amount - fee;
        totalSupply -= fee;
    }
}
