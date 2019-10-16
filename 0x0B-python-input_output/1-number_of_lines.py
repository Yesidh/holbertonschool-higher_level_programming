#!/usr/bin/python3
def number_of_lines(filename=""):
    """function that reads a text and return number of lines"""

    lines = 0
    with open(filename) as f:
        for lin in f:
            lines += 1
        return (lines)
