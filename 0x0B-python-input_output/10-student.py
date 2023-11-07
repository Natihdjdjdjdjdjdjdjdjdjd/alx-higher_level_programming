#!/usr/bin/python3
"""
    Module for class Student
"""


class Student:
    """
        A students that defines a student by:
        Attributes:
            first_name :student name.
            last_name : sudent last name
            age (int): student age.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:
            res = {i: self.__dict__[i] for i in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
