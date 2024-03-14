#!/usr/bin/python3
"""
This moduel solves a prime game problem,
using sieve
"""


def Sieve(n, prime):
    """
    find prime numbers between 1, n inclusive
    """
    p = 2
    while (p * p <= n):

        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = 0

        p += 1


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that number and
    its multiples from the set. The player that cannot make a move
    loses the game.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    maria = 0
    ben = 0
    prime = [1 for i in range(sorted(nums)[-1]+1)]
    Sieve(sorted(nums)[-1], prime)
    for num in nums:
        prime_nums = sum(prime[2: num + 1])
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
