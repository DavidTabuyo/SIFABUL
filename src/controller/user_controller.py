import bcrypt
from model.dao.user_dao import UserDao
from model.week import Week


class UserController:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id

    def get_weeks(self, worker_id: str, n: int) -> list[Week]:
        weeks = UserDao.get_weeks(worker_id)
        return [[None] * n + weeks][-n::]
    
    def change_password(self, old_password:str,new_password:str):
        ...
