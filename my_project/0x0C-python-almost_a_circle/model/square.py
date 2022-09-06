#!/usr/bin/python3
"""contains class Square that
    inherits from class Rectangle"""

from model.rectangle import Rectangle


class Square(Rectangle):
    #size = Rectangle.width
    def __init__(self, size, x=0, y=0, id=None):
        size = Rectangle.width
        self.size = size


        Rectangle.__init__(id, width, height, x, y) 
        #self.size = 2(Rectangle.width + Rectangle.height)

    #def __str__(self):
        #while size:
            #super().__class__.__name__ = self.__class__.__name__
        #return __str__()
