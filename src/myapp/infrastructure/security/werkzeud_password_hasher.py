from werkzeug.security import generate_password_hash, check_password_hash

from src.myapp.application.ports.password_hasher import PasswordHasher


class WerkzeugPasswordHasher(PasswordHasher):
    def hash(self, raw_password: str) -> str:
        return generate_password_hash(raw_password)

    def verify(self, raw_password: str, password_hash: str) -> bool:
        return check_password_hash(password_hash, raw_password)
