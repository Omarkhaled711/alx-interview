#!/usr/bin/python3

"""
problem statment:
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other
boxes.

Write a method that determines if all the boxes can be opened.

    - Prototype: def canUnlockAll(boxes)
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False

"""


def canUnlockAll(boxes):
    """
    parameters: boxes list
    Return: True if all boxes can be opened, else return False
    """
    keys = boxes[0].copy()
    keys_num = len(keys)
    i = 0
    while i < keys_num:
        keys.extend(boxes[keys[i]])
        boxes[keys[i]] = []
        keys_num = len(keys)
        i += 1
    keys.append(0)
    keys_unique = set(keys)
    return len(keys_unique) == len(boxes)
