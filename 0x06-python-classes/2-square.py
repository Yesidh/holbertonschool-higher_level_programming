#!/usr/bin/python3
class Square:
    def __init__(self, __size=0):
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
