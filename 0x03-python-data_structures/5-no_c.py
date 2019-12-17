#!/usr/bin/python3
def no_c(my_string):
    out = ""
    for c in my_string:
        if c == "c" or c == "C":
            continue
        else:
            out = out + c
    return out
