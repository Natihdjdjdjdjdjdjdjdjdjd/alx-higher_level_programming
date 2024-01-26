#!/usr/bin/python3
"""let  fetches data to  https://alx-intranet.hbtn.io/status
"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html_body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html_body)))
    print("\t- content: {}".format(html_body))
    print("\t- utf8 content: {}".format(html_body.decode('utf-8')))
