#!/usr/bin/python3

def print_last_digit(number):
    """print the number in last digit then return."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
