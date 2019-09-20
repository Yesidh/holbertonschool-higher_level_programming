#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = my_list[:]
        for i in range(new_list.count(search)):
            a = new_list.index(search)
            new_list.remove(search)
            new_list.insert(a, replace)
        return new_list
