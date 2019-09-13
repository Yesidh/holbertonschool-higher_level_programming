#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    from pdb import set_trace
    set_trace()
    a = int(len(sys.argv))
    operators = "+-\*"
    b = int(sys.argv[1])
    c = int(sys.argv[3])
    if a > 4:
        print("usage: {} {} {} {}".format(sys.argv[0], sys.argv[1],\
                                          sys.argv[2], sys.argv[3]))
        exit(1)
    for idx, val in enumerate(operators):
        if val == sys.argv[2]:
            if idx == 0:
                print("{:d} + {:d} = {:d}".format(b, c, int(add(a, b))))
                exit(0)
            if idx == 1:
                print("{:d} - {:d} = {:d}".format(b, c, int(sub(a, b))))
                exit(0)
            if idx == 2:
                print("{:d} * {:d} = {:d}".format(b, c, mul(mul(a, b))))
                exit(0)
