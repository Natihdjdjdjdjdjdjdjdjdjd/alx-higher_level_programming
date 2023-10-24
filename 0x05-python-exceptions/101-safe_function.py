#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        value = fct(*args)
    except Exception as e:
        value = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return value
