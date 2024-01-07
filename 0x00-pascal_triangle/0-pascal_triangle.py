#!/usr/bin/python3
"""
This module contains 2 functions, they are responsible for
creating the pascal's triangle
"""


def calculate_row(row_n, prev_list):
    """
    Forming each row in the pascal's triangle
    """
    row_list = [1]
    for i in range(1, row_n):
        if i == row_n - 1:
            row_list.append(1)
        else:
            row_list.append(prev_list[i] + prev_list[i - 1])
    return row_list


def pascal_triangle(n):
    """
    Forming the pascal's triangle, from the 1st row, to the nth row
    """
    if (n <= 0):
        return []
    pasc_list = [[1]]
    prev_list = [1]
    for i in range(2, n + 1):
        prev_list = calculate_row(i, prev_list)
        pasc_list.append(prev_list)
    return pasc_list
