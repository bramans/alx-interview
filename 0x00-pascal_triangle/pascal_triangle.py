#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def generate_pascal_triangle(rows):
    """returns a list of lists of numbers
    representing the Pascal's triangle"""
    if rows <= 0:
        return []

    triangle = []

    for row in range(rows):
        triangle.append([])
        triangle[row].append(1)

        for col in range(1, row):
            left = triangle[row-1][col-1]
            right = triangle[row-1][col]
            triangle[row].append(left + right)

        if rows != 0 and row != 0:
            triangle[row].append(1)

    return triangle
