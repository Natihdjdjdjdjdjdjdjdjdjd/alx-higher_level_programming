#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    start = 0
    j = 0
    str_list = []
    for j in range(list_length):
        try:
            r = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            str_list.append(r)
    return str_list
