import sqlite3


class DBConnecionService:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('db/db.sqlite')
        
    def close(self):
        self.connection.close()
    
    def querry(self, querry: str):
        self.connection.execute(querry).fetchall()


conn = DBConnecionService()
a = conn.querry('''
    CREATE TABLE yyy (
        user_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        salt BLOB NOT NULL,
        hash BLOB NOT NULL
    );            
''')
print(a)