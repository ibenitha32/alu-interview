#!/usr/bin/python3
"""Given a list of non-negative integers
representing the heights of walls with unit width 1
as if viewing the cross-section of a relief map
calculate how many square units of water will be retained after it rains.
"""


def rain(walls):
    """Calculating the square units of retained water"""
    if not walls:
        return 0

    n = len(walls)
    left = [0] * n
    right = [0] * n

    left[0] = walls[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], walls[i])

    right[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], walls[i])

    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - walls[i]

    return water
