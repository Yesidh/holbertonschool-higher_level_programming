#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        if len(my_list) > search:
            new_list = my_list[:]
            a = new_list.index(search)
            new_list.remove(search)
            new_list.insert(a, replace)
            return new_list
