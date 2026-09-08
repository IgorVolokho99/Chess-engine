"""Provide application functionality."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import datetime


class User:
    """Represent a domain component."""

    def __init__(
        self,
        user_name: str,
        email: str,
        password_hash: str,
        entity_id: int | None = None,
        created_at: datetime.datetime | None = None,
    ) -> None:
        """Initialize the instance."""
        self.id = entity_id
        self.user_name = user_name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
