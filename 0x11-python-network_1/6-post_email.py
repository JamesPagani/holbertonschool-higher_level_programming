#!/usr/bin/python3
"""6. POST an email #1.

Make a POST request to an URL, sending an email address as data.
Return the body of the HTTP response.
"""


import requests
from sys import argv


if __name__ == "__main__":
    response = requests.post(argv[1], data = {"email":argv[2]})

    print(response.text)

