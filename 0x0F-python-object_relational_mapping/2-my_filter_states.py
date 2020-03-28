#!/usr/bin/python3
"""Select States, specific state.

Using MySQLdb and some user input, make a query to the database.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    hbtn_db = MySQLdb.connect(host="localhost", user=argv[1],
                              passwd=argv[2], db=argv[3], port=3306)
    hbtn_db.query("""SELECT * FROM states
    WHERE states.name = '{}' ORDER BY id ASC;""".format(argv[4]))
    table = hbtn_db.store_result()

    for i in table.fetch_row(maxrows=0):
        print(i)
