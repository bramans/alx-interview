#!/usr/bin/python3
"""
Pascal Triangle Interview Challenge
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        # Start with a new row
        triangle.append([1])  # First element is always 1

        # For each element in the row (except the first and last),
        # calculate the value from the previous row
        for col in range(1, row):
            left = triangle[row-1][col-1]
            right = triangle[row-1][col]
            triangle[row].append(left + right)

        # Last element of the row is also 1, for rows > 0
        if row > 0:
            triangle[row].append(1)

    return triangle

