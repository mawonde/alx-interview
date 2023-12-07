#!/usr/bin/python3
"""
Determine if all locked boxes can be opened.

Args:
- boxes (list): List of lists, each representing a locked box with keys.

Returns:
- bool: True if all boxes can be opened, False otherwise.
"""


def canUnlockAll(boxes):
    """
    A method that determines if all
    the boxes can be opened
    """
    num_keys = [0]
    num_boxes = len(boxes)

    for keys in num_keys:
        for box in boxes[keys]:
            if box < num_boxes and box not in num_keys:
                num_keys.append(box)
    if len(num_keys) == num_boxes:
        return True
    return False
