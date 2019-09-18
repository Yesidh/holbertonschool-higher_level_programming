#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        if not tuple_a:
                return tuple_b
        elif not tuple_b:
                return tuple_a
        tuple_ab = (sum(i) for i in zip(tuple_a, tuple_b))
        return tuple(tuple_ab)
