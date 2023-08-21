#!/usr/bin/python3
"""
Making change
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Function that determines fewest number of coins
    needed to meet a given amount of total

    Args: coins(int) - amount in different denominations
          total(int) - amount in coins needed

    Returns: Fewest number of coins needed
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
