#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dictionary = a_dictionary.copy()
        for i in a_dictionary:
            new_dictionary[i] *= 2
        return new_dictionary
