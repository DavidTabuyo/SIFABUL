class User:
    def __init__(self, user_id: str, name: str, salt: bytes, hash: bytes):
        self.user_id = user_id
        self.name = name
        self.salt = salt
        self.hash = hash
