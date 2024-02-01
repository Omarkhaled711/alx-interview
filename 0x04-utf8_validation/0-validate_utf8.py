#!/usr/bin/python3

"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False

    The data will be represented by a list of integers
    """
    cont = 0
    i = 0
    while i < len(data):
        if data[i] >> 5 == 0b110:
            cont = 1
        elif data[i] >> 4 == 0b1110:
            cont = 2
        elif data[i] >> 3 == 0b11110:
            cont = 3
        elif data[i] >> 7 != 0:
            return False
        i += 1
        while cont != 0:
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
            cont -= 1
            i += 1
    return True
