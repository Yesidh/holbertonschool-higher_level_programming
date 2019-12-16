#!/usr/bin/python3
"""
==================================================================
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa using arguments from the script:
 should take 3 arguments: mysql username, mysql password and
 database name
==================================================================
"""

import MySQLdb
import sys


# db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
# the way obove is how to connect a database using MySQLdb in this case we need
# to add the conection port

def _States():
    """states to import"""

    connect_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3],
                                 port=3306)

    cur = connect_db.cursor()  # cur is a method to retrieve data from database
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()  # close all cursors
    connect_db.close()  # close database

if __name__ == "__main__":
    _States()
