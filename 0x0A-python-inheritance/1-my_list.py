#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new_list = self[:]
        print(sorted(new_list))
