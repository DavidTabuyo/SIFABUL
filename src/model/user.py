import sqlite3
from model.semana import Semana


class User:
    def __init__(self, user_id: str, nombre: str, salt: bytes, hash: bytes):
        self.user_id = user_id
        self.nombre = nombre
        self.salt = salt
        self.hash = hash

    def get_semanas(self, becario_id: str) -> list[Semana]:
        connection = sqlite3.connect('db/db.sqlite')
        semanas = connection.execute('''
            SELECT becario_id, lunes, total_semana
            FROM semanas
            WHERE becario_id = ?
            ORDER BY lunes
        ''', (becario_id,)).fetchall()
        connection.close()

        return [Semana(*semana) for semana in semanas]

    @staticmethod
    def is_becario(user_id: str) -> bool:
        '''
        Verifica si un usuario es un becario.

        Args:
            user_id (str): El ID del usuario que se va a verificar.

        Returns:
            bool: True si el usuario es becario, False en caso contrario.
        '''
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM becarios WHERE becario_id = ?
            ''', (user_id,))
            return bool(cursor.fetchone())

    @staticmethod
    def is_responsable(user_id: str) -> bool:
        '''
        Verifica si un usuario es un responsable.

        Args:
            user_id (str): El ID del usuario que se va a verificar.

        Returns:
            bool: True si el usuario es responsable, False en caso contrario.
        '''
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM responsables WHERE responsable_id = ?
            ''', (user_id,))
            return bool(cursor.fetchone())
