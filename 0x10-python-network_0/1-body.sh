#!/bin/bash
# Send a GET request and displays the body of the response if its status code is 200 (OK)
curl -sLf -X GET "$1"
