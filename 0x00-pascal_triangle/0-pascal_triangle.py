#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Computes the Pascal’s triangle of n
    Args:
        n (integer)
    Returns: a list of lists of integers
    """
    if (n <= 0):
        return []
    a_list = [[1]]
    for x in range(0, n - 1):
        inner_list = [1]
        for y in range(1, len(a_list[x])):
            inner_list.append(a_list[x][y] + a_list[x][y - 1])
        inner_list.append(1)
        a_list.append(inner_list)
    return a_list
