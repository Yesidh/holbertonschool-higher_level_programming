#!/usr/bin/python3
'''
=============================
Module with the class Base
=============================
'''

import json
import os
import csv
import turtle


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
            list_objs = []
        full_list_json = list()
        for fulano in list_objs:
            full_list_json.append(fulano.to_dictionary())

        empty_list_json = Base.to_json_string(full_list_json)
        with open(cls.__name__+'.json', 'w') as f:
            f.write(empty_list_json)

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

        if cls.__name__ == 'Rectangle':
            instance_class = cls(10, 2, 3)
        if cls.__name__ == 'Square':
            instance_class = cls(10, 15)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save in CSV file'''

        if cls.__name__ == 'Rectangle':
            _file = 'Rectangle.csv'
            headers = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            _file = 'Square.csv'
            headers = ['id', 'size', 'x', 'y']
        with open(_file, 'w') as fil:
            csv_writer = csv.DictWriter(fil, fieldnames=headers)
            csv_writer.writeheader()
            for row in list_objs:
                dict_row = row.to_dictionary()
                csv_writer.writerow(dict_row)

    @classmethod
    def load_from_file_csv(cls):
        '''deserializes from csv'''

        if cls.__name__ == 'Rectangle':
            _file = 'Rectangle.csv'
        elif cls.__name__ == 'Square':
            _file = 'Square.csv'
        list_csv = []
        dict_csv = {}
        with open(_file) as f:
            dic_reader = csv.DictReader(f)
            for row in dic_reader:
                for key, value in row.items():
                    dict_csv[key] = int(value)
                list_csv.append(cls.create(**dict_csv))
            return list_csv

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''open a window and draws all the Rectangles and Squares'''

        yesid = turtle.Screen()
        yesid.bgcolor("orange")
        yesid.title("Task21")
        yesid2 = turtle.Turtle()

        for rectangle in list_rectangles:
            yesid2.up()
            yesid2.goto(rectangle.x, rectangle.y)
            yesid2.color("Royal Blue")
            yesid2.down()
            for slic in range(2):
                yesid2.forward(rectangle.width)
                yesid2.left(90)
                yesid2.forward(rectangle.height)
                yesid2.left(90)

        for square in list_squares:
            yesid2.up()
            yesid2.goto(square.x, square.y)
            yesid2.color("Red")
            yesid2.down()
            for slic in range(4):
                yesid2.forward(square.width)
                yesid2.left(90)
                yesid2.forward(square.width)
        turtle.done()
