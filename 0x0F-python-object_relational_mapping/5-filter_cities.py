#!/usr/bin/python3
"""
===============================================================
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
===============================================================
"""

import MySQLdb
import sys


def states():
    """states to import"""

    connect_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3305)

    cur = connect_db.cursor()
    query1 = "SELECT cities.name FROM cities INNER JOIN states ON\
    states.id = cities.state_id WHERE states.name = %s"
    cur.execute(query1, (sys.argv[4], ))
    val = cur.fetchall()
    _list = []
    for row in val:
        _list.append(row[0])
    print(', '.join(_list))
    cur.close()
    connect_db.close()
if __name__ == "__main__":
    states()
