import sqlite3
from model.week import Week
from model.user import User


class UserDao:
    @staticmethod
    def is_worker(user_id: str) -> bool:
        return True

    @staticmethod
    def is_admin(user_id: str) -> bool:
        ...
        
    @staticmethod
    def get_user(user_id: str) -> User:
        connection = sqlite3.connect('db/db.sqlite')
        user = connection.execute('''
            SELECT users.user_id, users.name, users.salt, users.hash
            FROM users
            JOIN workers on users.user_id = workers.worker_id
            WHERE user_id = ?
        ''', (user_id,)).fetchone()
        connection.close()
        return User(*user) if user else None
        
    @staticmethod
    def get_weeks(worker_id: str) -> list[Week]:
        ...
