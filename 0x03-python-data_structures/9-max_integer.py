#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == [] or my_list is None:
        return None
    else:
        highest = my_list[0]
        for i in my_list:
            if i > highest:
                highest = i
    return highest
