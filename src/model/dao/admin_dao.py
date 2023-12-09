import sqlite3
from model.notification import Notification
from model.worker import Worker


class AdminDao:
    @staticmethod
    def get_notifications(admin_id: str) -> list[Notification]:
        # return a list with the sent notificatios
        ...

    @staticmethod
    def get_workers(admin_id: str) -> list[Worker]:
        # return a list with the workers
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                 SELECT workers.worker_id, users.name
                 FROM workers
                 JOIN users ON users.user_id = workers.worker_id
                 WHERE workers.admin_id = ?
             ''', (admin_id,))
            return [Worker(*worker) for worker in cursor.fetchall()]
