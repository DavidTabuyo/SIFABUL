from model.week import Week
from model.user import User


class UserDao:
    @staticmethod
    def is_worker(user_id: str) -> bool:
        return True

    @staticmethod
    def is_admin(user_id: str) -> bool:
        ...
        
    @staticmethod
    def get_user(user_id: str) -> User:
        ...

    @staticmethod
    def get_weeks(worker_id: str) -> list[Week]:
        ...
