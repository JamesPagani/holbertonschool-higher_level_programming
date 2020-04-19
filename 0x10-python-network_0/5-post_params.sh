#!/bin/bash
# Use cURL to send a POST request, along with an email address and a subject, to an user specified URL
curl -s -X POST -d "email=hr%40holbertonschool%2Ecom&subject=I+will+always+be+here+for+PLD" "$1"
