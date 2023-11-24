import sqlite3
import os


try:
    os.remove('db/db.sqlite')
except:
    pass


with sqlite3.connect('db/db.sqlite') as connection:
    cursor = connection.cursor()


    with open('db/_setup.sql', 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)


    connection.commit()
