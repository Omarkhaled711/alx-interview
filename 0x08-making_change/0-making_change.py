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

    if dp[total] != -1:
        return dp[total]

    result = 2e9

    for i in range(coin_num):
        if (coins[i] <= total):
            take_coin = calculate_change(coins, total-coins[i], dp, coin_num)

            if take_coin != 2e9 and result > take_coin + 1:
                result = take_coin + 1
    dp[total] = result
    return result


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
    """
    if (total <= 0):
        return 0

    dp = [-1]*(total + 1)
    result = calculate_change(coins, total, dp, len(coins))
    if result == 2e9:
        return -1
    return result
