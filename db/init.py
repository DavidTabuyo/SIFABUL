import sqlite3
import os
import bcrypt


os.remove('db/db.sqlite')

with open('db/init.sql', 'r') as file:
    sql_script = file.read()
    
connection = sqlite3.connect('db/db.sqlite')
connection.executescript(sql_script)
connection.commit()
connection.close()



# --------------- temp inserts ---------------
connection = sqlite3.connect('db/db.sqlite')

sales = [bcrypt.gensalt() for _ in range(5)]
connection.execute('''
    INSERT INTO users (user_id, name, salt, hash) VALUES
        ('ogingd00', 'Demi', ?, ?),
        ('vtunog00', 'Victor', ?, ?),
        ('dmartm14', 'Dario', ?, ?),
        ('dtabum00', 'David', ?, ?),
        ('emcuef', 'Eva Cuervo', ?, ?);
''', (sales[0], bcrypt.hashpw('hola'.encode('utf-8'), sales[0]),
      sales[1], bcrypt.hashpw('hola'.encode('utf-8'), sales[1]),
      sales[2], bcrypt.hashpw('hola'.encode('utf-8'), sales[2]),
      sales[3], bcrypt.hashpw('hola'.encode('utf-8'), sales[3]),
      sales[4], bcrypt.hashpw('hola'.encode('utf-8'), sales[4])))


with open('db/temp_inserts.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

connection.executescript(sql_script)


connection.commit()
connection.close()
