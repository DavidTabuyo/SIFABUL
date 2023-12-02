import sqlite3
import bcrypt
import requests
import arrow
from model.semana import Semana
from model.user import User


class ControladorUser:
    def __init__(self, user: User) -> None:
        self.user = user

    def check_password(self, password: str) -> bool:
        return self.user.hash == bcrypt.hashpw(password.encode('utf-8'), self.user.salt)

    def get_semanas(self, becario_id: str, n: int) -> list[Semana]:
        semanas = self.user.get_semanas(becario_id)
        return [[None] * n + semanas][-n::]


# class __Controlador:
#     def __init__(self, user_id: str):
#         self._user_id = user_id

#     def get_resumen_semanas(self, becario_id: str) -> list[int]:
#         '''
#         Devuelve una lista con las horas que el becario ha estado fichado en cada semana
#         en n semanas
#         '''
#         with sqlite3.connect('db/db.sqlite') as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT total_semana
#                 FROM semanas
#                 WHERE becario_id = ?
#                 ORDER BY lunes
#                 LIMIT 10
#             ''', (self._user_id,))
#             return [segundos // 3600 for (segundos,) in cursor.fetchall()]
