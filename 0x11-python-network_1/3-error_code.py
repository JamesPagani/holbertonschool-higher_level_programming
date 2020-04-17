#!/usr/bin/python3
"""Error code #0.

Send a request to an user-specified URL and show the body of the response.
Can handle HTTP errors.
"""


from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read()

        print(body.decode("utf_8"))

    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
