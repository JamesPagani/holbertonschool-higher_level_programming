#!/usr/bin/python3
class Square:
    """Defines a Square with a size attribute"""
    def __init__(self, size=0):
            """Initializes the class with an positive integer size"""
            if isinstance(size, int) is False:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
