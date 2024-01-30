#!/usr/bin/python3
"""
let sends a request to the URL and displays X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
