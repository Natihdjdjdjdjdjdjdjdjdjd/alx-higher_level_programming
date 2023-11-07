#!/usr/bin/python3
""" the function  that loads, adds and saves arguments to a Python list"""
from sys import argv
import json
import os.path


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_file(json_list, 'add_item.json')
