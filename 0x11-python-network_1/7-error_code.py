#!/usr/bin/python3
"""Error code #1.
Send a GET request to an user-specified URL.
Return the body of the response or the status code on HTTP error.
"""


import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
