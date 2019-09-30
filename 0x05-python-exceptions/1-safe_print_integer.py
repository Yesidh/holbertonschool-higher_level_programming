#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if abs(value) / 2 >= 0:
            print("{:d}".format(value))
            return True
    except (TypeError, ValueError):
            return False
