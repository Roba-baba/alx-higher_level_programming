#!/usr/bin/python3
"""Defines a class called rectangl"""


class Rectangle:
    """Representation of rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle.
        Args:
            width(int type): is the width of the rectangle
            height(int type): is the height of the rectangle.
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer type")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
