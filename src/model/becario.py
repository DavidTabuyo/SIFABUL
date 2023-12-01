import sqlite3
from model.user import User


class Becario(User):
    def __init__(self, user_id: str, nombre: str, salt: bytes, hash: bytes, responsable_id: str):
        self.user_id = user_id
        self.nombre = nombre
        self.salt = salt
        self.hash = hash
        self.responsable_id = responsable_id
        
        
    @staticmethod
    def from_id(becario_id: str) -> 'Becario':
        """
        Crea una instancia de la clase Becario utilizando el ID del becario.

        Args:
            becario_id (str): ID del becario.

        Returns:
            Becario: Instancia de la clase Becario.
        """
        connection = sqlite3.connect('db/db.sqlite')
        becario = connection.execute('''
            SELECT users.user_id, users.nombre, users.salt, users.hash, becarios.responsable_id
            FROM users
            JOIN becarios ON users.user_id = becarios.becario_id
            WHERE user_id = ?
        ''', (becario_id,)).fetchone()
        connection.close()
        
        return Becario(*becario)