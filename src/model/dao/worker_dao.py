import sqlite3
from model.check import Check
from model.notification import Notification
from model.notification_worker import NotificationWorker
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
        return Worker(*worker)

    @staticmethod
    def get_notifications(worker_id: str) -> list[NotificationWorker]:
        connection = sqlite3.connect('db/db.sqlite')
        notifications = connection.execute('''
            SELECT notifications.title, notifications.description, notifications.datetime, workers_notifications.seen
            FROM notifications
            JOIN workers_notifications on notifications.notifications_id = workers_notifications.notification_id
            WHERE notifications_workers.worker_id = ?
            ORDER BY notifications.datetime DESC
        ''', (worker_id,)).fetchone()
        connection.close()
        return [NotificationWorker(*notification) for notification in notifications]

    @staticmethod
    def get_today_checks(worker_id: str, date: str) -> list[Check]:
        connection = sqlite3.connect('db/db.sqlite')
        today_checks = connection.execute('''
            SELECT worker_id, date, time, is_entry
            FROM checks
            WHERE worker_id = ? and date = ?
            ORDER BY time DESC
        ''', (worker_id, date)).fetchall()
        connection.close()
        return [Check(*check) for check in today_checks]

    @staticmethod
    def add_new_check(worker_ID: str, check: Check):
        ...
