#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canOpenAll(lockboxes):
    '''Checks if all the lockboxes in a list of boxes containing keys
    (indices) to other lockboxes can be unlocked, starting with the
    first one unlocked.
    '''
    total_boxes = len(lockboxes)
    unlocked_boxes = set([0])  # Track which boxes are unlocked
    available_keys = set(lockboxes[0]).difference(set([0]))  # Keys from the first box

    while available_keys:
        current_key = available_keys.pop()
        if current_key < 0 or current_key >= total_boxes or current_key in unlocked_boxes:
            continue  # Skip invalid or already unlocked boxes
        unlocked_boxes.add(current_key)
        available_keys.update(lockboxes[current_key])  # Add new keys from the current box
    
    return len(unlocked_boxes) == total_boxes  # Return True if all boxes are unlocked
