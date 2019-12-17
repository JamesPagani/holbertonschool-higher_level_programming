#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    your_list = my_list.copy()
    if idx < 0 or idx + 1 > len(your_list):
        return your_list
    else:
        your_list[idx] = element
        return your_list
