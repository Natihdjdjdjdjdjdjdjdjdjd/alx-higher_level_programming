#!/usr/bin/python3
"""
the func of 0-read_file module
"""


def read_file(filename=""):
    """
    read_file - read the text(UTF8) and prints it to stdout
    Args:
        filename: the value of name 
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
