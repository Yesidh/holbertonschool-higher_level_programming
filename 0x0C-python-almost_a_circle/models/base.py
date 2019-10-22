#!/usr/bin/python3

import json

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

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Dictionaries to JSON string'''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''JSON string to file'''

        if list_objs is None:
            empty_lis = []
            with open(cls.__name__ + '.json', 'w') as f:
                empty_lis_json = Base.to_json_string(empty_lis)
                f.write(empty_list_json)
        else:
            full_list_json = list()
            with open(cls.__name__ + '.json', 'w') as f:
                for fulano in list_objs:
                    full_list_json.append(fulano.to_dictionary())
                f.write(Base.to_json_string(full_list_json))
