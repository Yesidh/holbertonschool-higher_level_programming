<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: Python - Input/Output                                              
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
## Examples                                                                     
Create a function that returns a list of lists of integers representing the Pascal’s triangle of n:
                                                                                
```
print_triangle(pascal_triangle(5))
```
the output:
```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
see the file 14-pascal_triangle.py
## Prerequisites
8 lecture hours about Input/Output and JSON                                     
## Installing

for have the code in your local machine you only need download the code files and put it into a directory.
## Built With

All the code was write under ubuntu 14.04 using the compiler version            
python 3.4 and pep8                                                             

## Contributing

-- Yesid Gutierrez - Holberton Student                                          

## Versioning
for my learning in Holberton School

## Authors

---Yesid Gutierrez  944@holbertonshcool.com                                    
                                                                               
## Files

|             File               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-read_file.py**| function that reads a text file (UTF8) and prints it to stdout|
|**1-number_of_lines.py**| function that returns the number of lines of a text file|
|**2-read_lines.py**| function that reads n lines of a text file (UTF8) and prints it to stdout|
|**3-write_file.py**| function that writes a string to a text file (UTF8) and returns the number of characters written|
|**4-append_write.py**| function that appends a string at the end of a text file (UTF8) and returns the number of characters added|
|**5-to_json_string.py**| function that returns the JSON representation of an object (string)|
|**6-from_json_string.py**| function that returns an object (Python data structure) represented by a JSON string|
|**7-save_to_json_file.py**|  function that writes an Object to a text file, using a JSON representation|
|**8-load_from_json_file.py**| function that creates an Object from a “JSON file”|
|**9-add_item.py**|  script that adds all arguments to a Python list, and then save them to a file|
|**10-class_to_json.py**| function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object|
|**11-student.py**| Write a class Student that defines a student by: Public instance attributes: first_name last_name age Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age): Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)|
|**12-student.py**| adding the method into the class Studen: Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py): If attrs is a list of strings, only attribute names contained in this list must be retrieved. Otherwise, all attributes must be retrieved|
|**13-student.py**| adding public method: Public method def reload_from_json(self, json): that replaces all attributes of the Student instance: You can assume json will always be a dictionary A dictionary key will be the public attribute name A dictionary value will be the value of the public attribute into the class Student|
|**14-pascal_triangle.py**| Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n: Returns an empty list if n <= 0|