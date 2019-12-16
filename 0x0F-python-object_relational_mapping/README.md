<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: Python - Object-relational mapping                                 
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
## Examples                                                                     
## Prerequisites
- Object-relational mappers
- mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
- MySQLdb tutorial
- SQLAlchemy tutorial
- SQLAlchemy
- mysqlclient/MySQLdb
- Introduction to SQLAlchemy
- Flask SQLAlchemy
- 10 common stumbling blocks for SQLAlchemy newbies
- Python SQLAlchemy Cheatsheet
- SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
## Installing
For installing MySQLdb 
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
```
```
$ pythone
>>> import MySQLdb
>>> MySQLdb.__version__
'1.3.10'
```

## Built With

All the code was write under ubuntu 14.04 using MySQL 5.7.8                                

## Contributing

-- Yesid Gutierrez - Holberton Student                                          

## Versioning
for my learning in Holberton School

## Authors

---Yesid Gutierrez  944@holbertonshcool.com                                    
                                                                               
## Files

|             File               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-select_states.py**| script that lists all states from the database hbtn_0e_0_usa|
|**1-filter_states.py**|  script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa|
|**2-my_filter_states.py**|  script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument|
|**3-my_safe_filter_states.py**| SQL injection|
|**4-cities_by_state.py**| script that lists all cities from the database hbtn_0e_4_usa|
|**5-filter_cities.py**| script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa|
|**model_state.py**| first state model|
|**7-model_state_fetch_all.py**| script that lists all State objects from the database hbtn_0e_6_usa|
|**8-model_state_fetch_first.py**| script that prints the first State object from the database hbtn_0e_6_usa|
|**9-model_state_filter_a.py**| script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa|
|**10-model_state_my_get.py**| script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa|
|**11-model_state_insert.py**| script that adds the State object “Louisiana” to the database hbtn_0e_6_usa|
|**12-model_state_update_id_2.py**| script that changes the name of a State object from the database hbtn_0e_6_usa|
|**13-model_state_delete_a.py**|script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa| 
|**model_city.py,14-model_city_fetch_by_state.py**| Python file similar to model_state.py named model_city.py that contains the class definition of a City|
