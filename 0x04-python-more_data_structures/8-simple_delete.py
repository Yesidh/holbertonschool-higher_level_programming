#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        for i in a_dictionary:
            if i == key:
                del a_dictionary[i]
                return a_dictionary
    return a_dictionary
