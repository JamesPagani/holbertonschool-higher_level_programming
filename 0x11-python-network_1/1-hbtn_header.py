#!/usr/bin/python3
"""Response header value #0.

Make a GET request to an user specified URL.
Return the value of the header 'X-Request-Id'.
"""


import sys
import urllib.request


with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.info()

print(headers["X-Request-Id"])
