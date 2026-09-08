"""Password hashing service interface."""

from typing import Protocol


class PasswordHasher(Protocol):
    """Define password hashing operations."""

    def hash(self, raw_password: str) -> str:
        """Return a secure hash for a raw password."""
        ...

    def verify(self, raw_password: str, password_hash: str) -> bool:
        """Return whether a raw password matches a stored hash."""
        ...
