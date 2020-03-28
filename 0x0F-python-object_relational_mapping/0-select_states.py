#!/usr/bin/pyhton3
"""Select States
Using MySQLdb, make a query to the database.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    hbtn_db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    hbtn_db.query("""SELECT * FROM states ORDER BY id ASC;""")
    table = dbtn_db.store_result()

    for i in table.fetch_row(maxrows=0):
        print(i)
