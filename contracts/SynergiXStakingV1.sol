// SPDX-License-Identifier: MIT
pragma solidity =0.8.38;

import {IERC20} from "@openzeppelin/contracts-v5/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts-v5/token/ERC20/utils/SafeERC20.sol";
import {ReentrancyGuard} from "@openzeppelin/contracts-v5/utils/ReentrancyGuard.sol";
import {Math} from "@openzeppelin/contracts-v5/utils/math/Math.sol";

/// @title SynergiXStakingV1
/// @notice Immutable-terms staking with escrowed principal and fully reserved fixed rewards.
/// @dev Deploy one version with explicitly approved immutable parameters. This contract has no
///      daily reward records, mint path, upgrade path, administrator, or withdrawal-to-admin path.
contract SynergiXStakingV1 is ReentrancyGuard {
    using SafeERC20 for IERC20;

    /// @notice Basis-point denominator used by the fixed simple reward formula.
    uint256 public constant BPS_DENOMINATOR = 10_000;
    /// @notice Fixed year length in seconds used by the simple reward formula.
    uint256 public constant SECONDS_PER_YEAR = 365 days;

    /// @notice ERC20 asset escrowed as principal and used to pay prefunded rewards.
    IERC20 public immutable stakingToken;
    /// @notice Simple annual reward rate in basis points, fixed for this deployed version.
    uint64 public immutable annualRateBps;
    /// @notice Minimum stake amount in token base units.
    uint128 public immutable minStakeAmount;
    /// @notice Maximum stake amount in token base units.
    uint128 public immutable maxStakeAmount;
    /// @notice Minimum position duration in seconds.
    uint64 public immutable minDurationSeconds;
    /// @notice Maximum position duration in seconds.
    uint64 public immutable maxDurationSeconds;

    /// @notice Next position identifier. IDs start at one.
    uint256 public nextPositionId = 1;
    /// @notice Total principal owed to all open positions.
    uint256 public totalPrincipalLiability;
    /// @notice Rewards reserved for all open positions.
    uint256 public totalReservedRewardLiability;
    /// @notice Funded rewards not yet committed to a position.
    uint256 public availableRewardReserve;

    /// @notice Position terms are set once at entry; claim flags change at settlement.
    struct Position {
        /// @notice Account that deposited principal and receives settlement.
        address beneficiary;
        /// @notice Escrowed principal in token base units.
        uint256 principal;
        /// @notice Reward amount reserved at position creation.
        uint256 fixedReward;
        /// @notice Inclusive withdrawal timestamp in Unix seconds.
        uint64 maturityTimestamp;
        /// @notice Whether principal has been returned to the beneficiary.
        bool principalWithdrawn;
        /// @notice Whether the fixed reward has been paid to the beneficiary.
        bool rewardClaimed;
    }

    /// @notice Positions indexed by their unique identifier.
    mapping(uint256 positionId => Position position) public positions;

    /// @notice Emitted when tokens are accepted into the uncommitted reward reserve.
    event RewardsFunded(address indexed funder, uint256 amount);
    /// @notice Emitted when principal and a fixed reward are committed to a position.
    event PositionCreated(
        uint256 indexed positionId,
        address indexed beneficiary,
        uint256 principal,
        uint256 fixedReward,
        uint64 maturityTimestamp
    );
    /// @notice Emitted when matured principal is returned to its beneficiary.
    event PrincipalWithdrawn(
        uint256 indexed positionId,
        address indexed beneficiary,
        address indexed caller,
        uint256 principal
    );
    /// @notice Emitted when a matured fixed reward is paid to its beneficiary.
    event RewardClaimed(
        uint256 indexed positionId,
        address indexed beneficiary,
        address indexed caller,
        uint256 reward
    );

    error ZeroAddress();
    error InvalidParameters();
    error AmountOutOfRange();
    error DurationOutOfRange();
    error InsufficientRewardReserve();
    error PositionNotFound();
    error PositionNotMatured();
    error PrincipalAlreadyWithdrawn();
    error RewardAlreadyClaimed();
    error NotBeneficiary();
    error UnsupportedTokenBehavior();
    error TimestampOutOfRange();

    /// @param token ERC20 token used for principal and reward settlement.
    /// @param rewardRateBps Immutable simple annual rate in basis points; set from approved terms.
    /// @param minimumStake Minimum principal in token base units; no decimal assumption is made.
    /// @param maximumStake Maximum principal in token base units.
    /// @param minimumDuration Minimum position duration in elapsed seconds.
    /// @param maximumDuration Maximum position duration in elapsed seconds.
    constructor(
        IERC20 token,
        uint64 rewardRateBps,
        uint128 minimumStake,
        uint128 maximumStake,
        uint64 minimumDuration,
        uint64 maximumDuration
    ) {
        if (address(token) == address(0)) revert ZeroAddress();
        if (address(token).code.length == 0) revert UnsupportedTokenBehavior();
        if (
            minimumStake == 0 || maximumStake < minimumStake ||
            minimumDuration == 0 || maximumDuration < minimumDuration
        ) revert InvalidParameters();

        stakingToken = token;
        annualRateBps = rewardRateBps;
        minStakeAmount = minimumStake;
        maxStakeAmount = maximumStake;
        minDurationSeconds = minimumDuration;
        maxDurationSeconds = maximumDuration;
    }

    /// @notice Adds exactly `amount` tokens to the uncommitted reward reserve.
    /// @dev Fee-on-transfer and rebasing behavior is unsupported. No caller can withdraw reserves.
    /// @param amount Amount of reward tokens to fund.
    function fundRewards(uint256 amount) external nonReentrant {
        if (amount == 0) revert AmountOutOfRange();

        uint256 balanceBefore = stakingToken.balanceOf(address(this));
        availableRewardReserve += amount;
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        uint256 balanceAfter = stakingToken.balanceOf(address(this));
        if (balanceAfter < balanceBefore || balanceAfter - balanceBefore != amount) {
            revert UnsupportedTokenBehavior();
        }

        emit RewardsFunded(msg.sender, amount);
    }

    /// @notice Opens a position with entry-fixed, simple interest and escrowed principal.
    /// @dev The full reward is reserved atomically before the position is accepted. Reward is
    ///      floor(principal * annualRateBps * duration / (10_000 * 365 days)).
    /// @param amount Principal amount in token base units.
    /// @param durationSeconds Fixed duration in elapsed seconds.
    /// @return positionId Identifier of the created position.
    function stake(uint256 amount, uint64 durationSeconds)
        external
        nonReentrant
        returns (uint256 positionId)
    {
        if (amount < minStakeAmount || amount > maxStakeAmount) revert AmountOutOfRange();
        if (durationSeconds < minDurationSeconds || durationSeconds > maxDurationSeconds) {
            revert DurationOutOfRange();
        }

        uint256 maturity = block.timestamp + durationSeconds;
        if (maturity > type(uint64).max) revert TimestampOutOfRange();
        uint256 reward = Math.mulDiv(
            amount,
            uint256(annualRateBps) * durationSeconds,
            BPS_DENOMINATOR * SECONDS_PER_YEAR
        );
        if (reward > availableRewardReserve) revert InsufficientRewardReserve();

        positionId = nextPositionId++;
        positions[positionId] = Position({
            beneficiary: msg.sender,
            principal: amount,
            fixedReward: reward,
            maturityTimestamp: uint64(maturity),
            principalWithdrawn: false,
            rewardClaimed: false
        });
        totalPrincipalLiability += amount;
        availableRewardReserve -= reward;
        totalReservedRewardLiability += reward;

        uint256 balanceBefore = stakingToken.balanceOf(address(this));
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        uint256 balanceAfter = stakingToken.balanceOf(address(this));
        if (balanceAfter < balanceBefore || balanceAfter - balanceBefore != amount) {
            revert UnsupportedTokenBehavior();
        }

        emit PositionCreated(positionId, msg.sender, amount, reward, uint64(maturity));
    }

    /// @notice Returns a matured position's principal independently of its reward claim.
    /// @dev Effects precede the token transfer. Exact recipient delivery is required.
    /// @param positionId Identifier of the position whose principal to return.
    function withdrawPrincipal(uint256 positionId) external nonReentrant {
        Position storage position = positions[positionId];
        if (position.beneficiary == address(0)) revert PositionNotFound();
        if (position.principalWithdrawn) revert PrincipalAlreadyWithdrawn();
        if (msg.sender != position.beneficiary) revert NotBeneficiary();
        if (block.timestamp < position.maturityTimestamp) revert PositionNotMatured();

        address beneficiary = position.beneficiary;
        uint256 principal = position.principal;
        uint256 contractBalanceBefore = stakingToken.balanceOf(address(this));
        uint256 recipientBalanceBefore = stakingToken.balanceOf(beneficiary);

        position.principalWithdrawn = true;
        totalPrincipalLiability -= principal;

        stakingToken.safeTransfer(beneficiary, principal);
        uint256 contractBalanceAfter = stakingToken.balanceOf(address(this));
        uint256 recipientBalanceAfter = stakingToken.balanceOf(beneficiary);
        if (
            contractBalanceAfter > contractBalanceBefore ||
            contractBalanceBefore - contractBalanceAfter != principal ||
            recipientBalanceAfter < recipientBalanceBefore ||
            recipientBalanceAfter - recipientBalanceBefore != principal
        ) revert UnsupportedTokenBehavior();

        emit PrincipalWithdrawn(positionId, beneficiary, msg.sender, principal);
    }

    /// @notice Claims a matured position's fixed reward independently of principal return.
    /// @dev A failed reward transfer reverts only this claim and leaves principal withdrawable.
    /// @param positionId Identifier of the position whose reward to claim.
    function claimReward(uint256 positionId) external nonReentrant {
        Position storage position = positions[positionId];
        if (position.beneficiary == address(0)) revert PositionNotFound();
        if (position.rewardClaimed) revert RewardAlreadyClaimed();
        if (msg.sender != position.beneficiary) revert NotBeneficiary();
        if (block.timestamp < position.maturityTimestamp) revert PositionNotMatured();

        address beneficiary = position.beneficiary;
        uint256 reward = position.fixedReward;
        position.rewardClaimed = true;
        totalReservedRewardLiability -= reward;

        if (reward > 0) {
            uint256 contractBalanceBefore = stakingToken.balanceOf(address(this));
            uint256 recipientBalanceBefore = stakingToken.balanceOf(beneficiary);

            stakingToken.safeTransfer(beneficiary, reward);
            uint256 contractBalanceAfter = stakingToken.balanceOf(address(this));
            uint256 recipientBalanceAfter = stakingToken.balanceOf(beneficiary);
            if (
                contractBalanceAfter > contractBalanceBefore ||
                contractBalanceBefore - contractBalanceAfter != reward ||
                recipientBalanceAfter < recipientBalanceBefore ||
                recipientBalanceAfter - recipientBalanceBefore != reward
            ) revert UnsupportedTokenBehavior();
        }

        emit RewardClaimed(positionId, beneficiary, msg.sender, reward);
    }
}
