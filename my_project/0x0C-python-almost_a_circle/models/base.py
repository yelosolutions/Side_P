#!/usr/bin/python3


class Base():
    """the base class to inherit from
        arguments: no arguments

        returns: string
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1

            self.id = Base.__nb_objects
