from werkzeug.security import generate_password_hash

from src.myapp.application.ports.password_hasher import PasswordHasher


class WerkzeugPasswordHasher(PasswordHasher):
    def hash(self, raw_password: str) -> str:
        return generate_password_hash(raw_password)
