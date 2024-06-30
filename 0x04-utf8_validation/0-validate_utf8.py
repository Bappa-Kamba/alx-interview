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
    num_count = 0  # number of continuation bytes expected
    for num in data:
        bin_repr = format(num, '08b')
        print(bin_repr)

        if num_count == 0:
            if bin_repr[0] == '0':
                continue
            elif bin_repr[:3] == '110':
                num_count = 1  # expecting 1 continuation byte
            elif bin_repr[:4] == '1110':
                num_count = 2  # expecting 2 continuation bytes
            elif bin_repr[:5] == '11110':
                num_count = 3  # expecting 3 continuation bytes
            else:
                return False

        else:
            if bin_repr[:2] != '10':
                return False
            num_count -= 1

    return num_count == 0
