#!/usr/bin/python3

"""
problem statement:
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    The method calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if (n <= 1):
        return 0
    curr = 2
    inc = 1
    operations = 2
    while (curr != n):
        if (n % curr == 0):
            operations += 1
            inc = curr
        if (curr > (n / 2) and inc == 1):
            return n
        operations += 1
        curr += inc
    return operations
