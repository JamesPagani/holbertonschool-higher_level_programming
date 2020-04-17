#!/usr/bin/python3
"""What's my status? #1.

Make a request to Holberton's platform using the 'requests' library.
"""


import requests


response =  requests.get("")

print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
