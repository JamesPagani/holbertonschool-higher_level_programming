#!/bin/bash
# Shows the accepted HTTP methods an user-specified server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
