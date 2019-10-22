#!/usr/bin/python3
'''
============================================================
Module with the class Rectangle that inherit from class Base
============================================================
'''

from models.base import Base


class Rectangle(Base):
    '''Rectangle class that inherits form Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''method that initialize the class and the parent class'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter method for width'''

        return self.__width

    @width.setter
    def width(self, width):
        '''setter method for the attribute width'''

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''getter method for the attribute height'''

        return self.__height

    @height.setter
    def height(self, height):
        '''setter method for the attribute height'''

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        '''getter method for the attribute x'''

        return self.__x

    @x.setter
    def x(self, x):
        '''setter method for the attribute x'''

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''getter method for the attribute'''

        return self.__y

    @y.setter
    def y(self, y):
        '''setter method for the attribute y'''

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        '''method for calculate rectangle area'''

        return self.width * self.height

    def display(self):
        '''method that print the rectangle with the character #'''

        [print() for space in range(self.y)]
        [print(" " * self.x + "#" * self.width)
         for line in range(self.height)]

    def __str__(self):
        '''define the __str__ method'''

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        '''Updating the class Rectangle with arguments'''

        index = 0
        if len(args) > 0 and args:
            for i in args:
                if index == 0:
                    self.id = i
                elif index == 1:
                    self.width = i
                elif index == 2:
                    self.height = i
                elif index == 3:
                    self.x = i
                elif index == 4:
                    self.y = i
                index += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''Method for create a dictionary for the class Rectangle'''

        dic_rectangle = dict(id=self.id, width=self.width, height=self.height,
                             x=self.x, y=self.y)
        return dic_rectangle
