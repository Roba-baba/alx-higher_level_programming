#!/usr/bin/python3
"""defines a rectangle class"""

class Rectangle:
    """
    Defines a rectangle with a given width and height.
        number_of_instances (int):
        keeps track of instances created.
        width (int): width of rectangle.
        height (int): height of rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance
           width (int): width of the rectangle.
           height (int): height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Deletes a Rectangle then prints a message.
        """
        Rectangle.number_of_instances -= 1
        print("Good bye rectangle...")

    def __str__(self):
        """
        Returns a string that represents rectangle using '#'.

        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for i in range(self.height)])

    def __repr__(self):
        """
        Returns a string when creating a new instance
    
            str: string representation of the
            rectangle to recreate a new instance.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """
        Getter method for width.
        int: width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.
        value (int): value to set as width.

        TypeError: if value is not an integer.
       ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): value to set as height.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value   
    def area(self):  
        """
        Calculates the area of the rectangle.

        Returns:
            int: area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
