#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    x = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        x = False
        return x
