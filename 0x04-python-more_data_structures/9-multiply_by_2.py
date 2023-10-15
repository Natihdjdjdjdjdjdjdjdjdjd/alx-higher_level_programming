#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_2 = {}
    for x in a_dictionary:
        mul_2[x] = a_dictionary[x] * 2
    return mul_2
