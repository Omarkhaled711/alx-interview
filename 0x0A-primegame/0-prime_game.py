#!/usr/bin/python3
"""
This moduel solves a prime game problem,
using sieve
"""


def Sieve(n):
    """
    find prime numbers between 1, n inclusive
    """
    p = 2
    prime = [True for i in range(n+1)]
    prime_nums = n - 1
    while (p * p <= n):

        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = False
                prime_nums -= 1

        p += 1
    return prime_nums


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that number and
    its multiples from the set. The player that cannot make a move
    loses the game.
    """
    maria = 0
    ben = 0
    for i in range(x):
        prime_nums = Sieve(nums[i])
        if prime_nums % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria == ben:
        return None
    elif maria > ben:
        return "Maria"
    else:
        return "Ben"
