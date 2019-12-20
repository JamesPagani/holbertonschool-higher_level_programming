#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        your_list = my_list[:]
        for i in range(len(your_list)):
            if your_list[i] == search:
                your_list[i] = replace
        return your_list
