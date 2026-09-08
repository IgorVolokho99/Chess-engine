"""Provide application functionality."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import datetime


class Move:
    """Represent a domain component."""

    def __init__(
        self,
        entity_id: int,
        user_id: int,
        game_id: int,
        move_number: int,
        played_at: datetime.datetime,
    ) -> None:
        """Initialize the instance."""
        self.id = entity_id
        self.user_id = user_id
        self.game_id = game_id
        self.move_number = move_number
        self.played_at = played_at
