#!/usr/bin/python3
'''
=============================
Module with the class Base
=============================
'''


class Base:
    '''starting with class Base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init method for the clase Base'''

        if id :
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
