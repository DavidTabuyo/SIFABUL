import sqlite3
from model.admin import Admin
from model.notification import Notification
from model.worker import Worker


class AdminDao:
    @staticmethod
    def get_admin(admin_id: str) -> Admin:
        connection = sqlite3.connect('db/db.sqlite')
        admin = connection.execute('''
            SELECT user_id, name, salt, hash
            FROM users
            WHERE user_id = ?
        ''', (admin_id,)).fetchone()
        connection.close()
        return Admin(*admin) if admin else None
    
    @staticmethod
    def get_notifications(admin_id: str) -> list[Notification]:
        # return a list with the sent notificatios
        ...

    @staticmethod
    def get_workers(admin_id: str) -> list[Worker]:
        # return a list with the workers
        connection = sqlite3.connect('db/db.sqlite')
        workers = connection.execute('''
            SELECT users.user_id, users.name, users.salt, users.hash workers.admin_id
            FROM users
            JOIN workers on users.user_id = workers.worker_id
            WHERE user_id = ?
        ''', (admin_id,)).fetchall()
        connection.close()
        return [Admin(*worker) for worker in workers]