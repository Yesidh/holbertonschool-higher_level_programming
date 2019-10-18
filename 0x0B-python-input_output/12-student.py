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

        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dic[key] = value
        return dic
