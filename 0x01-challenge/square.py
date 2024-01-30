#!/usr/bin/python3

class square():

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
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
