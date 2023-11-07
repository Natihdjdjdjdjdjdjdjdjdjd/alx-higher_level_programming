#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""
class Student:
    """
        A the function class students that defines a student by:
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Retrieves a dictionary representation
            Returns: dictionatie reperesent
        """
        return self.__dict__
