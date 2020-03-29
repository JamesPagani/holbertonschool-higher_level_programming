#!/usr/bin/python3
"""Select States, specific state (SQL INJECTION SAFE)

Using MySQLdb and some user input, make a query to the database.
This specific code should be resistant to an SQL Injection attack.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]
    db_table = argv[4]

    hbtn_db = MySQLdb.connect(host="localhost", user=sql_user,
                              passwd=sql_pass, db=sql_db, port=3306)
    db_cursor = hbtn_db.cursor()
    db_cursor.execute("""SELECT * FROM states
    WHERE BINARY states.name = %s ORDER BY id ASC;""", (db_table,))

    for i in db_cursor.fetchall():
        print(i)
