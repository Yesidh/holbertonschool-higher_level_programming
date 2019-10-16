<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: Python - Inheritance                                               
- What is a superclass, baseclass or parentclass                                
- What is a subclass                                                            
- How to list all attributes and methods of a class or instance                 
- When can an instance have new attributes                                      
- How to inherit class from another                                             
- How to define a class with multiple base classes                              
- What is the default class every class inherit from                            
- How to override a method or attribute inherited from the base class           
- Which attributes or methods are available by heritage to subclasses           
- What is the purpose of inheritance                                            
- What are, when and how to use isinstance, issubclass, type and super built-in functions
## Examples                                                                     
Create a class method for validate an integer into the class BaseGeometry        
```
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```
The output                                                                      
```
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```
check the code in the file 7-base_geometry.py
## Prerequisites
8 lecture hours about  Inheritance                                              
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
|**0-lookup.py**| function that returns the list of available attributes and methods of an object:
|**1-my_list.py, tests/1-my_list.txt**| Write a class MyList that inherits from list
|**2-is_same_class.py**| Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
|**3-is_kind_of_class.py**| unction that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
|**4-inherits_from.py**| function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise Fals
|**5-base_geometry.py**| Write an empty class BaseGeometry.
|**6-base_geometry.py**| Public instance method: def area(self): that raises an Exception with the message area() is not implemented into the class BaseGeometry
|**7-base_geometry.py, tests/7-base_geometry.txt**| adding Public instance method: def integer_validator(self, name, value): that validates value: you can assume name is always a string if value is not an integer: raise a TypeError exception, with the message <name> must be an integer if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0. Into the class BaseGeometry
|**8-rectangle.py**| rite a class Rectangle that inherits from BaseGeometry Instantiation with width and height: def __init__(self, width, height): width and height must be private. No getter or setter width and height must be positive integers, validated by integer_validator
|**9-rectangle.py**| adding the area() method must be implemented print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height> to the class Rectangle
|**10-square.py**| Write a class Square that inherits from Rectangle Instantiation with size: def __init__(self, size) size must be private. No getter or setter size must be a positive integer, validated by integer_validator the area() method must be implemented
|**11-saquare.py**| adding print() should print, and str() should return, the square description: [Square] <width>/<height> to the class square
|**100-my_int.py**| Write a class MyInt that inherits from int: MyInt is a rebel. MyInt has == and != operators inverted