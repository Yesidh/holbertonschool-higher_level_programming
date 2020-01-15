#!/usr/bin/python3
# list 10 commits (from the most recent to oldest) of the repository
# “rails” by the user “rails”

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1],
                                                              sys.argv[2])
    r = requests.get(url)
    for i in range(0, 10):
        print(r.json()[i].get('sha') + ': ', end="")
        print(r.json()[i].get('commit').get('author').get('name'))
