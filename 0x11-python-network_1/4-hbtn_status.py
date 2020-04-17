#!/usr/bin/python3
"""What's my status? #1.

Make a request to Holberton's platform using the 'requests' library.
"""


import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
