#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    """Appends a string.
    Args:
        filename (str, optional): name of the file.

    Returns:
        int: number of characters appended to file.
    """
    with open(filename, 'a', encoding="utf-8") as f:

        return f.write(text)
