import sqlite3


class Checkdao:
    
    @staticmethod
    def add_new_check(worker_id: str, date: str, time: str, is_entry: bool):
        connection = sqlite3.connect('db/db.sqlite')
        connection.execute('''
            INSERT INTO checks (worker_id, date, time, is_entry) VALUES
                (?, ?, ?, ?);
        ''', (worker_id, date, time, is_entry))
        connection.commit()
        connection.close()