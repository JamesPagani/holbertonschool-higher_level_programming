#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list != [] or my_list is not None:
        num_list = []
        result = 0
        for n in my_list:
            if n not in num_list:
                result += n
                num_list.append(n)
        return result
