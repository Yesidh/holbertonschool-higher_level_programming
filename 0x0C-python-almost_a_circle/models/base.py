#!/usr/bin/python3
'''
=============================
Module with the class Base
=============================
'''

import json
import os


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
                empty_lis_json = cls.to_json_string(empty_lis)
                f.write(empty_list_json)
        else:
            full_list_json = list()
            with open(cls.__name__ + '.json', 'w') as f:
                for fulano in list_objs:
                    full_list_json.append(fulano.to_dictionary())
                f.write(cls.to_json_string(full_list_json))

    @staticmethod
    def from_json_string(json_string):
        '''return the list of the JSON string representation'''

        if json_string is None or len(json_string) == 0:
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''method that returns an instance with all attributes already set'''

        instance_class = cls(10, 7, 8, 2)
        instance_class.update(**dictionary)
        return instance_class

    @classmethod
    def load_from_file(cls):
        '''return a list of instances'''

        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json') as _file:
                to_json = _file.read()
            dict_list = Base.from_json_string(to_json)
            obj_list = list()
            for sutanito in dict_list:
                obj_list.append(cls.create(**sutanito))
            return obj_list
