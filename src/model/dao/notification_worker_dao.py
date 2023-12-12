import sqlite3


class NotificationWorkerdao:
    
    @staticmethod
    def update_notifications_status(worker_id: str, notificationID:str, monday:str,total:int):
        connection = sqlite3.connect('db/db.sqlite')
        connection.execute('''
            INSERT OR REPLACE INTO weeks (worker_id, monday, total) VALUES
                (?, ?, ?);
        ''', (worker_id, monday, total))
        connection.commit()
        connection.close()