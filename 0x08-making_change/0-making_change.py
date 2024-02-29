#!/usr/bin/python3

"""
solving Making Change problem module
"""

import sys


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
    """
    if (total <= 0):
        return 0
    if coins is None or not coins:
        return -1
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            take_coin = dp[i - coin]
            if take_coin != sys.maxsize and take_coin + 1 < dp[i]:
                dp[i] = take_coin + 1
    if dp[total] == sys.maxsize:
        return -1
    return dp[total]
