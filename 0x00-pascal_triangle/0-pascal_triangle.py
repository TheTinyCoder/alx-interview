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
    lists = [[1]]
    for i in range(n - 1):
        a_list, next_list = lists[i], [1]
        for i in range(len(a_list)):
            j = a_list[i + 1] if (i + 1 < len(a_list)) else 0
            next_list.append(a_list[i] + j)
        lists.append(next_list)
    return lists
