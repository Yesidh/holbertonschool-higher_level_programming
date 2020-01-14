#!/usr/bin/python3
# Python script that takes in a letter and sends a POST request to
#   http://0.0.0.0:5000/search_user with the letter as a parameter.
# The letter must be sent in the variable q
# If no argument is given, set q=""
# If the response body is properly JSON formatted and not empty, display
#     the id and name like this: [<id>] <name>
#  Otherwise:
#     Display Not a valid JSON is the JSON is invalid
#     Display No result is the JSON is empty
# You must use the package requests and sys
# You are not allowed to import packages other than requests and sys

import requests
import sys

if __name__ == "__main__":
    payload = {}
    if (len(sys.argv) > 1):
        payload['q'] = sys.argv[1]
    else:
        payload['q'] = ""
    url = "http://0.0.0.0:5000/search_user"
    try:
        r = requests.post(url, data=payload)
        if (len(eval(r.text)) == 0):
            print('No result')
        if (len(eval(r.text)) > 0):
            print('[{}] {}'.format(eval(r.text)['id'], eval(r.text)['name']))
    except Exception as e:
        print("Not a valid JSON")
