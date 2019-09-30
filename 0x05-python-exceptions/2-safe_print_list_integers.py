#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in my_list:
        try:
            if abs(i) / 2 >= 0 and j < x:
                print("{:d}".format(i), end="")
                j += 1
        except(IndexError, TypeError, ValueError):
            pass
    print("")
    return j
