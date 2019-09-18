#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        if len(my_list) == 0:
                return None
        new_string = []
        for i in my_list:
                if i % 2 == 0:
                        new_string.append(True)
                else:
                        new_string.append(False)
        return new_string
