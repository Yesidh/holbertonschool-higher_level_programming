#!/usr/bin/python3
# Python script that takes your Github credentials (username and password)
#  and uses the Github API to display your id
#      You must use Basic Authentication to access to your information
#      The first argument will be your username
#      The second argument will be your password
#      You must use the package requests and sys
#      You are not allowed to import packages other than requests and sys
#      You don’t need to check arguments passed to the script (number or type)

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
