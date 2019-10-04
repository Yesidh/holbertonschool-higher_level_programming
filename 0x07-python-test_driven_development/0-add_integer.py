#!/usr/bin/python3
"""
****************************
Calculation module
****************************
"""
def add_integer(a, b=98):
    """ Addition Function"""

    if  not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
