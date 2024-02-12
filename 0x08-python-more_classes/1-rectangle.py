#!/usr/bin/python3

'''Rectangle class'''


class Rectangle:
    '''Initialize Width & Height of Rectangle'''
    def __init__(self, width=0, height=0):
        '''Initialize instance attribute
        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle
        '''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''return width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        set value to width
        Args:
        value (int): value to set to width

        Raises:
        TypeError: if value not integer
        ValueError: if value less than 0

        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''return height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        set value to height
        Args:
        value (int): value to set to height

        Raises:
        TypeError: if value not integer
        ValueError: if value less than 0

        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
