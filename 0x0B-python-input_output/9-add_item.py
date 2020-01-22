#!/usr/bin/python3
"""Load, add, save.
Script that loads a Python list, appends elements to it (given as the script's
arguments) and saves it. The list is saved (and must be loaded) in a JSON file.
"""


from sys import argv
import json
json_save = __import__("7-save_to_json_file").save_to_json_file
json_load = __import__("8-load_from_json_file").load_from_json_file


try:
    my_list = json_load("add_item.json")
    my_list += argv[1:]
    json_save(my_list, "add_item.json")
except FileNotFoundError:
    my_list = []
    my_list += argv[1:]
    json_save(my_list, "add_item.json")
