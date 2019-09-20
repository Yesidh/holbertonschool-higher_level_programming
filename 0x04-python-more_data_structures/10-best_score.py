#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    max_score = list(sorted(a_dictionary))[-1:]
    return max_score
