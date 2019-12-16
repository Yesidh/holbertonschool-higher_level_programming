#!/usr/bin/python3
"""
==============================================================
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
should take 4 arguments: mysql username, mysql password,
database name and state name searched
==============================================================
"""


import MySQLdb
import sys


def _States():
    """states to import"""

    connect_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = connect_db.cursor()  # cur is a method to retrieve data from database
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id;"
                .format(sys.argv[4]))
    rows = cur.fetchall()  # save the query in the rowsvariablelikecurespecifi
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()  # close all cursors
    connect_db.close()  # close databases
if __name__ == "__main__":
    _States()
