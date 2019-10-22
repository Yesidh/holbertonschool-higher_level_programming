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

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''overwriten the __str__ method that inherint from Rectangle'''

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        '''getter method for size'''

        return self.width

    @size.setter
    def size(self, value):
        '''setter method for size'''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Method for update all attributes in the class Square'''

        if len(args) > 0 and args:
            index = 0
            for i in args:
                if index == 0:
                    self.id = i
                elif index == 1:
                    self.size = i
                elif index == 2:
                    self.x = i
                elif index == 3:
                    self.y = i
                index += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
