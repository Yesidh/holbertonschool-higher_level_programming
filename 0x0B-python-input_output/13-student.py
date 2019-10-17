#!/usr/bin/python3
"""
===============================
module with the class Student
===============================
"""


class Student:
    """class with methods to_json for retrieves dictionary"""

    def __init__(self, first_name, last_name, age):
        """method for initialized all atributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method for retrieve a dictionary representation for a
        student instance"""

        if type(attrs) is str or type(attrs) is list:
            return attrs
        return self.__dict__
