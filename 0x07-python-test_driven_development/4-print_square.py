#!/usr/bin/python3
"""
===============================
Module for print_square function
===============================
"""


def print_square(size):
    """Function that prints a square with "#" character with
    hight and width like "size" argument"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    else:
        for i in range(0, size):
            print("#" * size)
