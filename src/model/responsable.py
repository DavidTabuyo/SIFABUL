import sqlite3
from model.user import User


class Responsable(User):
    def __init__(self, user_id: str, nombre: str, salt: bytes, hash: bytes):
        super().__init__(user_id, nombre, salt, hash)
    

    @staticmethod
    def from_id(responsable_id: str) -> 'Responsable':
        """
        Crea una instancia de la clase Responsable utilizando el ID del responsable.

        Args:
            responsable_id (str): ID del responsable.

        Returns:
            Responsable: Instancia de la clase Responsable.
        """
        connection = sqlite3.connect('db/db.sqlite')
        responsable = connection.execute('''
            SELECT user_id, nombre, salt, hash
            FROM users
            WHERE user_id = ?
        ''', (responsable_id,)).fetchone()
        connection.close()
        
        return Responsable(*responsable)