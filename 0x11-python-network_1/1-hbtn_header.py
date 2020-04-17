#!/usr/bin/python3
"""Response header value #0.

Make a GET request to an user specified URL.
Return the value of the header 'X-Request-Id'.
"""


import sys
import urllib.request


http_request = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(http_request) as response:
    headers = response.info()

print(headers["X-Request-Id"])
