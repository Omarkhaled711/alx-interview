#!/usr/bin/python3

def Sieve(n, prime):
    """
    find prime numbers between 1, n inclusive
    """
    p = 2
    while (p * p <= n):

        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1


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
        prime = [True for _ in range(nums[i]+1)]
        Sieve(nums[i], prime)
        if len(prime) % 2 == 0:
            ben += 1
        else:
            maria += 1
        prime.clear()
    if maria == ben:
        return None
    elif maria > ben:
        return "Maria"
    else:
        return "Ben"
