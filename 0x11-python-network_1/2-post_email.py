#!/usr/bin/python3
"""POST an email #0.

Send a post request to an URL along with an email address.
"""


from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode("ascii")

    with request.urlopen(argv[1], data) as response:
        body = response.read()

    print(body.decode())
