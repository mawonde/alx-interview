#!/usr/bin/python3


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
