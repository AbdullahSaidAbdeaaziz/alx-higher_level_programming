"""a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Return Area of square'''
        return self.__size ** 2

    def __str__(self):
        '''Return Square representation'''
        return f'[Square] {self.__size}/{self.__size}'

    def __repr__(self):
        '''Return Square representation'''
        return f'[Square] {self.__size}/{self.__size}'
