#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and
#     displays the body of the response.
#  If the HTTP status code is greater than or equal to 400, print:
#      Error code: followed by the value of the HTTP status code
#      You must use the packages requests and sys
#      You are not allowed to import packages other than requests and sys
#      You don’t need to check arguments passed to the script (number or type)

import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":

    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except HTTPError as e:
        print('Error code:', e.response.status_code)
