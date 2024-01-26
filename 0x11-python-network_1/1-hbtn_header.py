#!/usr/bin/python3
"""Let the  script that takes in auest-Id
variable found in the header ofthe response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
