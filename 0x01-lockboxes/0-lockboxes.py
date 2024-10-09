#!/usr/bin/python3
"""
Optimized solution to the lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether all boxes can be unlocked.
    Each box contains keys to other boxes.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    seen_boxes = {0}  # Set of unlocked boxes, starting with the first box
    unseen_boxes = set(boxes[0])  # Keys available from the first box

    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if boxIdx < 0 or boxIdx >= n or boxIdx in seen_boxes:
            continue  # Skip invalid or already seen boxes
        seen_boxes.add(boxIdx)
        unseen_boxes.update(boxes[boxIdx])  # Add new keys from the current box

    return len(seen_boxes) == n

