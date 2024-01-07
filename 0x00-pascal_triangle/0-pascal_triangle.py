#!/usr/bin/python3

def calculate_row(row_n, prev_list):
    row_list = [1]
    for i in range(1, row_n):
        if i == row_n - 1:
            row_list.append(1)
        else:
            row_list.append(prev_list[i] + prev_list[i - 1])
    return row_list


def pascal_triangle(n):
    if (n <= 0):
        return []
    pasc_list = [[1]]
    prev_list = [1]
    for i in range(2, n + 1):
        prev_list = calculate_row(i, prev_list)
        pasc_list.append(prev_list)
    return pasc_list
