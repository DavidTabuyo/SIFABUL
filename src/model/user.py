class User:
    def __init__(self, user_id: str, nombre: str, salt: bytes, hash: bytes):
        self.user_id = user_id
        self.nombre = nombre
        self.salt = salt
        self.hash = hash
        
    def check_password(self, password):
        ...