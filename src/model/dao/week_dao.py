import sqlite3

from model.week import Week

class Weekdao:
    @staticmethod
    def get_weeks(worker_id: str) -> list[Week]:
        ...

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
    def update_or_create_week(worker_id: str, monday: str, total: int):
        connection = sqlite3.connect('db/db.sqlite')
        connection.execute('''
            INSERT OR REPLACE INTO weeks (worker_id, monday, total) VALUES
                (?, ?, ?);
        ''', (worker_id, monday, total))
        connection.commit()
        connection.close()