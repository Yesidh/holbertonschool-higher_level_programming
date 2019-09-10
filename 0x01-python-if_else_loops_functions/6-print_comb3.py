#!/usr/bin/python3
a = 0
b = 0
while a < 10:
    while b < 10:
        if a < b:
            if a + b < 17:
                print("{}{}, ".format(a, b), end="")
            elif a + b == 17:
                print("{}{}".format(a, b))
        b += 1
    b = 0
    a += 1
