#!/usr/bin/python3
"""
Solution for determining if all lockboxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines whether all lockboxes can be unlocked given a list where each
    box contains keys to other boxes.
    - The first box is always unlocked.
    - A box can only be unlocked if you have its corresponding key.
    """
    if not isinstance(boxes, list):
        return False
    elif len(boxes) == 0:
        return False

    for key in range(1, len(boxes) - 1):
        box_is_unlocked = False
        for idx in range(len(boxes)):
            box_is_unlocked = key in boxes[idx] and key != idx
            if box_is_unlocked:
                break
        if not box_is_unlocked:
            return box_is_unlocked
    return True
