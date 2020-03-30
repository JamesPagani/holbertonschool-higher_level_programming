#!/usr/bin/python3
"""Filter citites

Using MySQLdb and some user input, make a query to the database.
SQL Injection safe; Prints only the cities found in the asked state.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]
    db_city = argv[4]
    cities = []

    hbtn_db = MySQLdb.connect(host="localhost", user=sql_user,
                              passwd=sql_pass, db=sql_db, port=3306)
    db_cursor = hbtn_db.cursor()
    db_cursor.execute("""SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s
    ORDER BY cities.id ASC;""", (argv[4],))

    q_result = db_cursor.fetchall()
    for i in range(len(q_result)):
        cities.append(q_result[i][0])

    print(*cities, sep=", ")
