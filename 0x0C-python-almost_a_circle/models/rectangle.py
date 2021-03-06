#!/usr/bin/python3
"""Rectangle class.

A basic rectangle with a width, hieght and offset coordinates.

It is capable of displaying its area, printing a rectangle made of hash (#)
symbols and can update its values if needed to.
"""


from models.base import Base


class Rectangle(Base):
    """A basic rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """An informal string representation of this Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def to_dictionary(self):
        """Return a dictionary representation of a rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter."""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter."""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate the area of this rectangle."""
        return self.width * self.height

    def display(self):
        """Draw a square with the hash (#) symbol."""
        for v_space in range(self.y):
            print()
        for i in range(self.height):
            for h_space in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the id, width, height, x and y placement of the rectangle."""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
