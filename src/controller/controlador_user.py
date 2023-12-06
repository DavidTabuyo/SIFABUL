import bcrypt
from model.week import Week
from model.user import User


class ControladorUser:
    def __init__(self, user: User) -> None:
        self.user = user

    def check_password(self, password: str) -> bool:
        return self.user.hash == bcrypt.hashpw(password.encode('utf-8'), self.user.salt)

    def get_semanas(self, becario_id: str, n: int) -> list[Semana]:
        semanas = self.user.get_semanas(becario_id)
        return [[None] * n + semanas][-n::]
