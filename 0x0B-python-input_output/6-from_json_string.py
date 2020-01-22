#!/usr/bin/python3
"""From JSON string to Object.
Function that returns a Python object represented by a JSON string.
"""

import json
def from_json_string(my_str):
    """Return a Python object from my_str, a JSON string."""
    return json.loads(my_str)
