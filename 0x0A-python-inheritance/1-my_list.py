#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""

    def print_sorted(self):
        """Methot that sorted a list"""

        new_list = self[:]
        print(sorted(new_list))
