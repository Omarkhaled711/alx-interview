#!/usr/bin/python3
"""
solving Making Change problem module
"""


def calculate_change(coins, total, dp, coin_num):
    """
    using memoization to calculate the fewest number of coins
    """
    if total == 0:
        return 0

    if total < 0 or coin_num >= len(coins):
        return 2e9

    if dp[total] == -1:
        dp[total] = 2e9
    take_coin = calculate_change(
        coins, total - coins[coin_num], dp, coin_num) + 1
    no_coin = calculate_change(
        coins, total, dp, coin_num + 1) + 1
    dp[total] = min(take_coin, no_coin, dp[total])
    return dp[total]


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
    """
    if (total <= 0):
        return 0

    dp = [-1]*(total + 1)
    calculate_change(coins, total, dp, 0)
    if (dp[total] >= 2e9):
        return -1
    return dp[total]
