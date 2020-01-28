#!/usr/bin/python3
"""Square class.
A rectangle whose width and height are the same size, also known as a square.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A basic square.."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Informal string representation of a square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    @property
    def size(self):
        """Size (width and height) getter."""
        return self.width

    @size.setter
    def size(self, size):
        """Size (width and height) setter."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the id, size, x and y offsets of a square."""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
