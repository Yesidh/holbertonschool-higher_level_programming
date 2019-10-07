<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: Python - Exceptions:                                               
- What's the difference between errors and exceptions                           
- What are exceptions and how to use them                                       
- When do we need to use exceptions                                             
- How to correctly handle an axception                                          
- What's the purpose of catching exceptions                                     
- How to raise a builtion exception                                             
- When do we need to implement a clean-up action after an exception             
## Examples                                                                     

## Prerequisites
8 lecture hours about exceptions.                                               
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
|    **0-safe_print_list.py**    | Function that prints x elements of a list, x represents the number of elements to print, x can be bigger than the length of my_List, hava to use try: / except:, not allowed to import any module, not allowed to use len()|
|    **1-safe_print_integer.py** | Function that prints an integer with "{:d}".format() returns True if value has been corectly printed(it means the value is an integer) otherside return False, have to use try: / except:. not allowed to import any module and use typy()|
|**2-safe_print_list_integers.py**| Function that prints the first x elements of a list and only integers. x represents the number of elements to access in my_list, x can be bigger than the length of my_list-if it's the case, an axception will occur, return the real number of integers printed, have to use try: / except: not allowed to import any module and use len()
|**3-safe_print_division.py**| Function that divides 2 integers and prints the result, the result of the divition should print on the finally: section preceded by Inside result:, returns the value of the division otherwise: None. use try: / except: / finally. Not allowed to import any module|
|  **4-list_division.py**| Function that divides element by element 2 lists. list_length can be bigger than the length of both lists, return a new list with all divisions, if 2 elements can't be divided the division result should be equal to 0. If a element is not integer or float print wrong type, if divition can't be done /0 print division by 0. if my_list1 or my_list2 is too short print out of range. Have to use try: / except: / finally:. Not allowed to import any module|
|  **5-raise_exception.py**| Function that raises a type exception|
| **6-raise_exception_msg.py**| Function that raises a name exception with a message. Not allowed to import any module|
| **100-safe_print_integer_err.py**| Function that prints an integer. Return True if value has been correctly printed(it menas the value is an integer). Otherwise returns False and prints stderr the error precede by Exception: Have to use try: / except:. Not allowed to use type()|
|  **101-safe_function.py**| Function that executes a function safely. you can asume fct will be always a pointer to a function. returns the result of the function. Otherwise return None if something happens during the function and prints in stderr the error precede by Exception:. Have to use try: / except:|
|  **102-magic_calculation.py**| Bytecode|