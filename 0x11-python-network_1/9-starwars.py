#!/usr/bin/python3
# Python script that takes in a string and sends a search request to the
#  Star Wars API Use the Star Wars API search people endpoint
#    Use the string argument as the search value of the request
#    The body response must be JSON and converted to a Python dictionary.
#    Display: Number of results: <count>
#    Display the name of each result (see example below)
#    You must use the packages requests and sys
#    You are not allowed to import packages other than requests and sys
#    You don’t need to check arguments passed to the script (number or type)
#    You don’t need to manage the pagination

import requests
import sys

if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    search = sys.argv[1]
    r = requests.get(url, params={'search': search})
    print("Number of results:", r.json().get('count'))
    for i in r.json().get('results'):
        print(i.get('name'))
