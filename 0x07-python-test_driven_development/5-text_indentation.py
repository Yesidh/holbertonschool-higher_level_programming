#!/usr/bin/python3
"""
======================================
Module for text_indentatiion() function
=======================================
"""


def text_indentation(text):
    """function for indentation a string"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while len(text) > i:
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}".format(text[i]))
            print("")
            i += 1
            if text[i] == ' ':
                i += 1
        print("{}".format(text[i]), end="")
        i += 1
