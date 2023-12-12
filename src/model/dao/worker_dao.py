import sqlite3
from model.check import Check
from model.notification import Notification
from model.notification_worker import NotificationWorker
from model.week import Week
from model.worker import Worker


class WorkerDao:
    @staticmethod
    def get_worker(worker_id: str) -> Worker:
        connection = sqlite3.connect('db/db.sqlite')
        worker = connection.execute('''
            SELECT users.user_id, users.name, users.salt, users.hash, workers.admin_id
            FROM users
            JOIN workers on users.user_id = workers.worker_id
            WHERE user_id = ?
        ''', (worker_id,)).fetchone()
        connection.close()
        return Worker(*worker) if worker else None

    @staticmethod
    def get_notifications(worker_id: str) -> list[NotificationWorker]:
        connection = sqlite3.connect('db/db.sqlite')
        notifications = connection.execute('''
            SELECT notifications.title, notifications.description, notifications.datetime, workers_notifications.seen
            FROM notifications
            JOIN workers_notifications on notifications.notification_id = workers_notifications.notification_id
            WHERE workers_notifications.worker_id = ?
            ORDER BY notifications.datetime DESC
        ''', (worker_id,)).fetchall()
        connection.close()
        return [NotificationWorker(*notification) for notification in notifications]

    @staticmethod
    def get_today_checks(worker_id: str, date: str) -> list[Check]:
        connection = sqlite3.connect('db/db.sqlite')
        today_checks = connection.execute('''
            SELECT worker_id, date, time, is_entry
            FROM checks
            WHERE worker_id = ? and date = ?
            ORDER BY time 
        ''', (worker_id, date)).fetchall()
        connection.close()
        return [Check(*check) for check in today_checks]

    @staticmethod
    def get_last_today_check(worker_id: str, date: str) -> Check:
        connection = sqlite3.connect('db/db.sqlite')
        last_check = connection.execute('''
            SELECT worker_id, date, time, is_entry
            FROM checks
            WHERE worker_id = ? and date = ?
            ORDER BY time DESC
        ''', (worker_id, date)).fetchone()
        connection.close()
        return Check(*last_check) if last_check else None

    @staticmethod
    def get_week(worker_id: str, monday: str) -> Week:
        connection = sqlite3.connect('db/db.sqlite')
        week = connection.execute('''
            SELECT worker_id, monday, total
            FROM weeks
            WHERE worker_id = ? and monday = ?
        ''', (worker_id, monday)).fetchone()
        connection.close()
        return Week(*week) if week else None

    @staticmethod
    def add_new_check(worker_id: str, date: str, time: str, is_entry: bool):
        connection = sqlite3.connect('db/db.sqlite')
        connection.execute('''
            INSERT INTO checks (worker_id, date, time, is_entry) VALUES
                (?, ?, ?, ?);
        ''', (worker_id, date, time, is_entry))
        connection.commit()
        connection.close()

    @staticmethod
    def udpate_or_create_week(worker_id: str, monday: str, total: int):
        connection = sqlite3.connect('db/db.sqlite')
        connection.execute('''
            INSERT OR REPLACE INTO weeks (worker_id, monday, total) VALUES
                (?, ?, ?);
        ''', (worker_id, monday, total))
        connection.commit()
        connection.close()
