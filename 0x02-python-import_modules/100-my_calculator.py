#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    a = int(len(argv))
    b = int(argv[1])
    c = int(argv[3])
    if a > 4:
        print("usage: {} {} {} {}".format(argv[0], argv[1], argv[2], argv[3]))
        exit(1)
    elif argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(b, c, int(add(b, c))))
        exit(0)
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(b, c, int(sub(b, c))))
        exit(0)
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(b, c, int(mul(b, c))))
        exit(0)
    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(b, c, int(div(b, c))))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
