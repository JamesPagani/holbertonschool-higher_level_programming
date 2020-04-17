#!/usr/bin/python3
"""Response header value #1.

Make a GET request to an user specified URL.
Return the value of the header 'X-Request-Id'.
"""


import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])

    print(response.headers.get("X-Request-Id"))
