#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = int(len(sys.argv))
    if a == 1:
        print("0 arguments.")
    elif a > 1:
        print("{:d} arguments:".format(a - 1))
        i = 1
        while i < a:
            print("{:d}: {}".format(i, sys.argv[i]))
            i += 1
