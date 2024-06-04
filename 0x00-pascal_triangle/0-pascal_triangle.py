#!/usr/bin/python3
""" 0-pascal_triangle"""
# def pascal_triangle(n):
#     triangle = [[1]]
#     temp_row = []
#     for i in range(1, n):
#         row = [1]
#         for j in range(1, i):
#             if len(temp_row) == 1:
#                 break
#             row.append(temp_row[j - 1] + temp_row[j])
#         row.append(1)
#         temp_row = row
#         triangle.append(row)

#     return triangle


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    triangle = [[1]]
    temp_row = []
    if n <= 0:
        return []
    for i in range(1, n):
        row = [1] + [temp_row[j - 1] + temp_row[j] for j in range(1, i) if len(temp_row) > 1] + [1]
        temp_row = row
        triangle.append(row)

    return triangle
