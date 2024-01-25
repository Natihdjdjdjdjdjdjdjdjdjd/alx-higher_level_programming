#!/usr/bin/python3
#finds a peak in a list of integers


def find_peak(list_of_integers):

    val_list = list_of_integers
    # if there is no list of integers return None
    if val_list == []:
        return None
    length = len(val_list)

    begin, end = 0, length - 1
    while begin < end:
        mid = begin + (end - begin) // 2
        if val_list[mid] > val_list[mid - 1] and val_list[mid] > val_list[mid + 1]:
            return val_list[mid]
        if val_list[mid - 1] > val_list[mid + 1]:
            end = mid
        else:
            begin = mid + 1
    return val_list[begin]
