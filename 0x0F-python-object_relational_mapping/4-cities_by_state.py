#!/usr/bin/python3
"""
===========================================================
script that lists all cities from the database hbtn_0e_4_usa
============================================================
"""

import MySQLdb
import sys


def states():
    """states to import"""

    connect_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = connect_db.cursor()
    que = "SELECT cities.id, cities.name, states.name FROM cities INNER\
           JOIN states ON cities.state_id = states.id;"
    cur.execute(que)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connect_db.close()
if __name__ == "__main__":
    states()
