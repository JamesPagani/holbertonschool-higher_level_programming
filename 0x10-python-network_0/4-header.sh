#!/bin/bash
# Send a GET request, along with a custom header variable, to an user-specified URL and displays the response's body
curl -s -H "X-HolbertonSchool-User-Id":98 "$1"
