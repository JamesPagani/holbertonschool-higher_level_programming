#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list != [] or my_list is not None:
        if idx < 0 or idx + 1 > len(my_list):
            return my_list
        else:
            del my_list[idx]
            return my_list