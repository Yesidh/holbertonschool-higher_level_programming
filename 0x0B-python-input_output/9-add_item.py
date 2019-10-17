#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


list1 = []

try:
    list1 = list(load_from_json_file("add_item.json"))

except:
    len(list1) == 0

for arg in range(1, len(argv)):
    list1.append(argv[arg])

save_to_json_file(list1, "add_item.json")
