#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d}".format(number), end=" ")
if number < 0:
    print("is {:d}".format(number % -10), end=" ")
    if (number % -10) == 0:
        print("and is zero")
    elif (number % -10) < 6:
        print("and is less than 6 and not 0")
    else:
        print("and is greater than 5")
else:
    print("is {:d}".format(number % 10), end=" ")
    if (number % 10) == 0:
        print("and is zero")
    elif (number % 10) < 6:
        print("and is less than 6 and not 0")
    else:
        print("and is greater than 5")
