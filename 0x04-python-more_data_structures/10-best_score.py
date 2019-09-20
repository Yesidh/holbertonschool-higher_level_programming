#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a_dictionary = sorted(a_dictionary)
    max_score = 0
    for i in a_dictionary:
        max_score = i
    return max_score
