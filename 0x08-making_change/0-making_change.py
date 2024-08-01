#!/usr/bin/python3
""" Making Change Module """


def makeChange(coins, total):
    """
        Determine the fewest number of coins needed to meet a given total

        Args:
            coins - list of coins possessed
            total - total coins to make up

        Returns:
            0 if total is <= 0, -1 if total cannot be met or fewest number
            of coins needed to amke total
    """
    if total < 0:
        return -1

    # Create a DP array with a large initial value
    dp = [total + 1] * (total + 1)
    # Base case: to make 0 total, 0 coins are required
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        # Update dp array for each total from coin to the target total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still the large initial value, return -1
    # Otherwise, return dp[total] as the minimum number of coins needed
    return dp[total] if dp[total] != total + 1 else -1
