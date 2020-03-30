#!/usr/bin/python3
"""Select citites

Using MySQLdb and some user input, make a query to the database.
SQL Injection safe and uses data from two tables (cities and states).
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]

    hbtn_db = MySQLdb.connect(host="localhost", user=sql_user,
                              passwd=sql_pass, db=sql_db, port=3306)
    db_cursor = hbtn_db.cursor()
    db_cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;""")

    for i in db_cursor.fetchall():
        print(i)
