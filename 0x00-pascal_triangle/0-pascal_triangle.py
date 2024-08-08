#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row.

    Args:
      n: The number of rows in the Pascal's triangle.

    Returns:
      A list of lists representing Pascal's triangle, where each inner list
      represents a row.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
