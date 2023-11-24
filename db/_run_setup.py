import sqlite3
import os


try:
    os.remove('db/db.sqlite')
except:
    pass


connection = sqlite3.connect('db/db.sqlite')
cursor = connection.cursor()


with open('db/_setup.sql', 'r') as file:
    sql_script = file.read()

cursor.executescript(sql_script)


connection.commit()
connection.close()
