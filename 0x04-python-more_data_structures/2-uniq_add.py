#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    value = 0
    for j in new_list:
        value += j
    return value
