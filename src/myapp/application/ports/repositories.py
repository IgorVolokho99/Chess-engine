"""Provide application functionality."""

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from src.myapp.domain.entities.user import User


class UserRepository(Protocol):
    """Define persistence operations for users."""

    def add(self, user: User) -> None:
        """Persist a new user."""
        ...

    def is_exist_user_name(self, user_name: str) -> bool:
        """Return whether a username is already in use."""
        ...

    def save_user(self, user: User) -> None:
        """Persist updates to a user."""
        ...

    def get_by_user_name(self, user_name: str) -> User:
        """Return a user by username."""
        ...

    def get_by_id(self, user_id: int) -> User | None:
        """Return a user by identifier, when present."""
        ...
