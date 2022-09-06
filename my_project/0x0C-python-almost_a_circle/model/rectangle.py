#!/usr/bin/python3
"""contains class Rectangle"""
from model.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        rectangle = (self.x * "\n")
        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
                __class__.__name__, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0: 
            args_list = ['id', 'width', 'height', 'x','y']
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
