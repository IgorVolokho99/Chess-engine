"""Provide application functionality."""

from werkzeug.security import check_password_hash, generate_password_hash

from src.myapp.application.ports.password_hasher import PasswordHasher


class WerkzeugPasswordHasher(PasswordHasher):
    """Represent a domain component."""

    def hash(self, raw_password: str) -> str:
        """Perform this operation."""
        return generate_password_hash(raw_password)

    def verify(self, raw_password: str, password_hash: str) -> bool:
        """Perform this operation."""
        return check_password_hash(password_hash, raw_password)
