#!/usr/bin/python3
""" let define Square that create class"""


class Square:
    """ the class Square """

    def __init__(self, size=0):
        """intialize the square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """returns the area.

        Returns:
            ares.
        """
        return self.__size**2
