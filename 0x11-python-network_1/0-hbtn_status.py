#!/usr/bin/python3
# Write a Python script that fetches https://intranet.hbtn.io/status
#    You must use the package urllib
#    You are not allowed to import any packages other than urllib
#    The body of the response must be displayed like the following example
#     You must use a with statement

import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()

print('Body response:')
print('\t- type:', type(the_page))
print('\t- content:', the_page)
print('\t- utf8 content:', the_page.decode('utf8'))
