#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    sum = 0
    for i in range(1, argc):
        sum = sum + int(argv[i])
    print(sum)
