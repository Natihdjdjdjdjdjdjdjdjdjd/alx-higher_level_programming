#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str, optional): name of the file.
    Returns: int char nub byte wriiten
    """
    with open(filename, mode='w', encoding="UTF-8") as f:
        """This method returns written to a file."""
        return f.write(text)
