#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {
        "email": email
    }
    query_string = urllib.parse.urlencode(param)
    data = query_string.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:

        text_resp = response.read().decode("utf-8")
        print(text_resp)
