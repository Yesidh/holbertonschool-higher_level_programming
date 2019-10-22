#!/usr/bin/python3
from models.rectangle import Rectangle
'''
===========================================================
Module with the class Square that inherinten from Rectangle
Rectangle inheriten form Base
===========================================================
'''


class Square(Rectangle):
    '''class Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''__init__ method using superclass width and height must be
        replaced by size'''

        self.size = size
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        '''overwriten the __str__ method that inherint from Rectangle'''

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)
