#!/usr/bin/python3
"""
===========================================================
SQL injection
============================================================
"""

import MySQLdb
import sys


def states():
    """states to import"""

    connect_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = connect_db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connect_db.close()

if __name__ == "__main__":
    states()
