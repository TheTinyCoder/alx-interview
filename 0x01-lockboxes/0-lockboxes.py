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
    keys = list(set(boxes[0]))
    locked_boxes = []
    for box in range(1, len(boxes)):
        if (len(keys) == len(boxes)):
            return True
        if box not in keys:
            locked_boxes.append(box)
        else:
            keys = list(set(keys + boxes[box]))
            for key in locked_boxes:
                if key in keys:
                    locked_boxes.remove(key)
                    keys = list(set(keys + boxes[key]))
    return len(locked_boxes) == 0
