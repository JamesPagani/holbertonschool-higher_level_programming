#!/usr/bin/python3
"""Compare rectangles (Rectangle v8).
Create a rectangle that contains the following attributes:
    FIELDS:
        number_of_instances (integer, public)
        print_symbol (anything, public)
        width (integer, private).
        height (integer, private).
    METHODS:
        area (width * height, instance).
        preimeter (2 * (width + height), instance).
        bigger_or_equal (rect_1, rect_2, static).
"""


class Rectangle:
    """Basic rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initiate a basic rectangle."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Current instance saying Good Bye."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Informal representation of this rectangle."""
        for row in range(self.height):
            for spot in range(self.width):
                self.__figure += str(self.print_symbol)
            if row + 1 != self.height:
                self.__figure += "\n"
        return self.__figure

    def __repr__(self):
        """Formal representation of this square."""
        return "Rectangle ({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare rectangles by area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @property
    def width(self):
        """Retrieve this rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set this rectangle's width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve this rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set this rectangle'sa height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of this rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of this rectangle."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)
