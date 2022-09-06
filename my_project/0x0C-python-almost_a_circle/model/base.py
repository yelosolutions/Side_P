#!/usr/bin/python3
"""Contains class Base"""

class Base():
    """base class for all other classes to inherit from"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1

            self.id = Base.__nb_objects
