#!/bin/bash
# Get the size (in bytes) of an HTTP response made to localhost on port 5000
curl -sI 0:5000 | grep "Content-Length" | cut -d " " -f 2

