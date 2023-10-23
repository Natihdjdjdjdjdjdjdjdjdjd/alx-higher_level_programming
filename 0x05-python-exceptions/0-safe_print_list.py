#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    back = 0
    try:
        while back is not x:
            print(my_list[back], end='')
            back += 1
    except IndexError:
        None
    print()
    return back
