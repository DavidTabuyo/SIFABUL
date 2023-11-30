from model.user import User


class Responsable(User):
    def __init__(self, user_id: str, nombre: str, salt: bytes, hash: bytes):
        super().__init__(user_id, nombre, salt, hash)
    

    @staticmethod
    def from_id(responsable_id) -> 'Responsable':
        ...
    

    @staticmethod
    def is_responsable(user_id: str) -> bool:
        ...