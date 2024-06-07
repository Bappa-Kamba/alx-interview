#!/usr/bin/env python3
"""Lockboxes module"""
from collections import deque


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened"""
    opened_boxes = set()
    keys = deque()

    # Start with the first box
    keys.extend(boxes[0])
    opened_boxes.add(0)

    while keys:
        key = keys.popleft()

        # Only process this key if it is a valid box and hasn't been opened yet
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == len(boxes)
