#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """the Square.

        Args:
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            q = 0
            for arg in args:
                if q == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif q == 1:
                    self.size = arg
                elif q == 2:
                    self.x = arg
                elif q == 3:
                    self.y = arg
                q += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
