#!/usr/bin/python3
for i in range(0, 99):
    if i != 98:
        print("{:d}{:d}".format(i // 10, i % 10), end=", ")
    else:
        print("{:d}{:d}".format(i // 10, i % 10))
