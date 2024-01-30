#!/usr/bin/python3
"""class of square"""


class square():
    """
    a square class with two attributes:
        width
        height
    has methods for calculating area and
    perimeter
    """
    width = 0
    height = 0

    def __init__(self, x):
        # for key, value in kwargs.items():
        #     setattr(self, key, value)
        self.width = x
        self.height = x

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """returns the measurements of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """
    instantiates the class and prevents
    execution incase the module is imported
    """

    s = square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
