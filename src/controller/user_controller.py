import bcrypt
from model.dao.user_dao import User_dao
from model.week import Week


class User_controller:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id

    def check_password(self, password: str) -> bool:
        return self.user.hash == bcrypt.hashpw(password.encode('utf-8'), self.user.salt)

    def get_weeks(self, worker_id: str, n: int) -> list[Week]:
        semanas = User_dao.get_weeks(worker_id)
        return [[None] * n + semanas][-n::]
