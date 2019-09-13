#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    a = int(len(argv))
    if a > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    b = int(argv[1])
    c = int(argv[3])
    elif argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(b, c, int(add(b, c))))
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(b, c, int(sub(b, c))))
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(b, c, int(mul(b, c))))
    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(b, c, int(div(b, c))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
