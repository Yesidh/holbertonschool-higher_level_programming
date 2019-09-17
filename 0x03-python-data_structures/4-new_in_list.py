#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        if len(my_list) > idx and idx > 0:
                new_list = my_list.copy()
                new_list[idx] = element
                return new_list
        else:
                return my_list
