#!/usr/bin/python3

"""
N-queen problem module
"""
import sys


def check_valid(possible, square):
    """
    check if a queen can be placed in this square
    """
    for sq in possible:
        if sq[1] == square[1]:
            return False
        if (sq[0] + sq[1]) == (square[0] + square[1]):
            return False
        if (sq[1] - sq[0]) == (square[1] - square[0]):
            return False
    possible.append(square)
    return True


def back_track(possible, N, row):
    """
    Placing the queens in non-attacking squares using
    backtracking
    """
    if (row == N):
        print(possible)
        return
    for i in range(N):
        if (check_valid(possible, [row, i])):
            back_track(possible, N, row + 1)
            possible.pop()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    N = sys.argv[1]
    try:
        N = int(N)
        if (N < 4):
            print('N must be at least 4')
            exit(1)
        possible = []
        for i in range(N):
            possible.append([0, i])
            back_track(possible, N, 1)
            possible.pop()
    except ValueError:
        print('N must be a number')
        exit(1)
