#!/bin/bash
# Get the size (in bytes) of an HTTP response made to localhost on port 5000
curl -s "$1" | wc -c
