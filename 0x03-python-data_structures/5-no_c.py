#!/usr/bin/python3
def no_c(my_string):
        if my_string is not None:
                my_string = [i for i in my_string if i != 'c' and i != 'C']
                for i in my_string:
                        if i != 'c' and i != 'C':
                                my_string = i
                return my_string
