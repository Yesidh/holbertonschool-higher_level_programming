#!/usr/bin/python3
# list 10 commits (from the most recent to oldest) of the repository
# “rails” by the user “rails”

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url)
    try:
        for i in range(0, 10):
            a = r.json()[i].get('sha')
            b = r.json()[i].get('commit').get('author').get('name')
            print("{}: {}".format(a, b))
    except IndexError:
        pass
