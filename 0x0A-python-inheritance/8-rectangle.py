#!/usr/bin/python3
"""
===================================
module with class BaseGeometry
===================================
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """method for calculated area"""
        raise Exception("area () is not implemented")

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greatter than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
