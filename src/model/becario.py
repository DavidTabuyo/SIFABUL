from model.user import User


class Becario(User):
    def __init__(self, user_id: str, nombre: str, salt: bytes, hash: bytes, responsable_id: str):
        self.user_id = user_id
        self.nombre = nombre
        self.salt = salt
        self.hash = hash
        self.responsable_id = responsable_id
        
        
    @staticmethod
    def from_id(becario_id) -> 'Becario':
        ...
        
        
    @staticmethod
    def is_becario(user_id: str) -> bool:
        ...