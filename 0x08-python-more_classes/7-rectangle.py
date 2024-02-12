#!/usr/bin/python3

'''Rectangle class'''


class Rectangle:
    '''Initialize Width & Height of Rectangle'''
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        '''Initialize instance attribute
        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle
        '''
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

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

    def area(self):
        '''Area for rectangle = width x height'''
        return self.width * self.height

    def perimeter(self):
        '''perimeter of rectangle = 2 x (width + height)'''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        w = f'{self.print_symbol}' * self.width
        rect = f'{w}\n'*self.height
        rect = rect[:-1]
        return rect

    def __repr__(self):
        '''Return new representation for rectangle'''
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        '''after destory instance'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
