#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            if j < x:
               print("{}".format(i), end="")
               j += 1
    except IndexError:
        print("That index doesn't exist")
    print("")
    return j
