#!/usr/bin/python3

'''More upgrade for class square'''


class Square:
    "Hi I'm upgrade square"
    def __init__(self, size=0) -> None:
        '''Initialize square with size also with default value.

        Args:
            size (int): size of square
        '''
        self.__size = size

    @property
    def size(self):
        '''get size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set value to size of square'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return area of square'''
        return self.__size ** 2

    def my_print(self):
        '''print shape of square'''
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#"*self.__size)
