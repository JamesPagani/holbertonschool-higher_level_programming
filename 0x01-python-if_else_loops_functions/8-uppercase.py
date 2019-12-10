#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) >= 97 and ord(w) <= 122:
            ch = ord(w) - 32
        else:
            ch = ord(w)
        print("{:c}".format(ch), end="")
    print("")
