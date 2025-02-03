#!/usr/bin/python3

"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the inner boxes inside 'boxes' can be opened
    Args:
        boxes (list of lists)
    Returns: True or False
    """
    keys = sum(boxes, [])
    unique_keys = sorted(set(sum(boxes, [])))
    for i in range(1, len(boxes)):
        if (len([j for j in boxes[i - 1]
                 if j in range(1, len(boxes))]) == len(boxes) - 1):
            return True
        alt_keys = sorted(set(sum(boxes[0:i] + boxes[i + 1:], [])))
        if i not in unique_keys:
            return False
        if i not in alt_keys:
            return False
    return True
