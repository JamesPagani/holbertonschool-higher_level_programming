#!/bin/bash
# Send a DELETE request to an user specified URL and return the response's body
curl -s -X DELETE "$1"
