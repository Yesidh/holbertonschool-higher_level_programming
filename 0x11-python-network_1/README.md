<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: Python - Network #1                                           
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service
## Examples                                                                
## Prerequisites                                                           
- Quickstart with Requests package
- Requests package
## Installing

## Built With

All the code was write under ubuntu 14.04                                       

## Contributing

-- Yesid Gutierrez - Holberton Student                                          

## Versioning
for my learning in Holberton School

## Authors

---Yesid Gutierrez  944@holbertonshcool.com                                    
                                                                               
## Files

|             File               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-hbtn_status.py**|Python script that fetches https://intranet.hbtn.io/status|
|**1-hbtn_header.py**|Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.|
|**2-post_email.py**|Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)|
|**3-error_code.py**|Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)|
|**4-hbtn_status.py**|Python script that fetches https://intranet.hbtn.io/status, You must use the package requests, You are not allow to import packages other than requests, The body of the response must be display like the following example (tabulation before -)|
|**5-hbtn_header.py*|Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header You must use the packages requests and sys, You are not allow to import other packages than requests and sys, The value of this variable is different for each request, You don’t need to check script arguments (number and type)|
|**6-post_email.py**|Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response. The email must be sent in the variable email, You must use the packages requests and sys, You are not allowed to import packages other than requests and sys, You don’t need to error check arguments passed to the script (number or type)|
|**7-error_code.py**|Python script that takes in a URL, sends a request to the URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code, You must use the packages requests and sys, You are not allowed to import packages other than requests and sys, You don’t need to check arguments passed to the script (number or type)|
|**8-json_api.py**|Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. The letter must be sent in the variable q, If no argument is given, set q="" If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name> Otherwise: Display Not a valid JSON is the JSON is invalid Display No result is the JSON is empty You must use the package requests and sys You are not allowed to import packages other than requests and sys|
|**9-starwars.py**|Python script that takes in a string and sends a search request to the Star Wars API. Use the Star Wars API search people endpoint, Use the string argument as the search value of the request, The body response must be JSON and converted to a Python dictionary. Display: Number of results: <count>, Display the name of each result (see example below), You must use the packages requests and sys, You are not allowed to import packages other than requests and sys, You don’t need to check arguments passed to the script (number or type), You don’t need to manage the pagination|
|**10-my_github.py**|Python script that takes your Github credentials (username and password) and uses the Github API to display your id, You must use Basic Authentication to access to your information, The first argument will be your username, The second argument will be your password, You must use the package requests and sys, You are not allowed to import packages other than requests and sys, You don’t need to check arguments passed to the script (number or type)|