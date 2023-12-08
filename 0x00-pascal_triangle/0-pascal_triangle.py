#!/usr/bin/env python3

"""Returns Pascal's triangle as a list of 
lists of integers for the given number of rows."""

from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Returns:
    List[List[int]]: Pascal's triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
