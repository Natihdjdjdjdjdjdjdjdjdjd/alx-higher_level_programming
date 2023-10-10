#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    product = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            product.append(True)
        else:
            product.append(False)

    return (product)
