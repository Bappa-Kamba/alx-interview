#!/usr/bin/python3
""" UTF-8 Validation Module"""
from typing import List


def validUTF8(data: List) -> bool:
    """
        Function that determines if a given data set represents
        a valid UTF-8 encoding.

        Args:
            data: list of integers representing the UTF string.

        Returns:
            `True` if the data is a valid string, `False otherwise.
    """
    if not data:
        return False

    num_count = 0
    for num in data:
        bin_repr = format(num, '08b')

        if num_count == 0:
            if bin_repr[0] == '0':
                continue
            elif bin_repr[:3] == '110':
                num_count = 2  # a 2-byte character

            elif bin_repr[:4] == '1110':
                num_count = 3  # a 3-byte character

            elif bin_repr[:5] == '11110':
                num_count = 4  # a 4-byte character

        else:
            if bin_repr[:2] != '10':

                return False
            num_count = 0

    return num_count == 0
