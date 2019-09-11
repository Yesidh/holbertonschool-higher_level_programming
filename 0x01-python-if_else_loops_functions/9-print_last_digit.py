#!/usr/bin/python3
def print_last_digit(number):
    a = abs(number) % 10
    print("{}".format(a), end="")
    return(a)
