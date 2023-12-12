import sqlite3
from model.user import User


class UserDao:
    @staticmethod
    def is_worker(user_id: str) -> bool:
        connection = sqlite3.connect('db/db.sqlite')
        worker = connection.execute('''
            SELECT worker_id
            FROM workers
            WHERE worker_id = ?
        ''', (user_id,)).fetchone()
        connection.close()
        return worker != None

    @staticmethod
    def is_admin(user_id: str) -> bool:
        connection = sqlite3.connect('db/db.sqlite')
        admin = connection.execute('''
            SELECT admin_id
            FROM admins
            WHERE admin_id = ?
        ''', (user_id,)).fetchone()
        connection.close()
        return admin != None
        
    @staticmethod
    def get_user(user_id: str) -> User:
        connection = sqlite3.connect('db/db.sqlite')
        user = connection.execute('''
            SELECT user_id, name, salt, hash
            FROM users
            WHERE user_id = ?
        ''', (user_id,)).fetchone()
        connection.close()
        return User(*user) if user else None
        
