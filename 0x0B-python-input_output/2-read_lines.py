#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file and prints it to stdout"""

    lines = 0
    with open(filename) as f:
        for lin in f:
            lines += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= lines:
            print(f.read(), end="")
        else:
            for i in range(0, nb_lines):
                print(f.readline(), end="")
