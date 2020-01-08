#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    your_list = []
    for i in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            your_list.append(quotient)
    return your_list
