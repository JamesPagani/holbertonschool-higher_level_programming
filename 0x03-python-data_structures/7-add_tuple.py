#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_a = tuple_a[:2] + (0, 0)
    t_b = tuple_b[:2] + (0, 0)
    return t_a[0] + t_b[0], t_a[1] + t_b[1]
