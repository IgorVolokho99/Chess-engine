"""Provide application functionality."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import datetime

    from src.myapp.domain.enums.game_result import GameResult
    from src.myapp.domain.enums.status import GameStatus


class Game:
    """Represent a domain component."""

    def __init__(
        self,
        entity_id: int,
        user_id: int,
        status: GameStatus,
        result: GameResult,
        fen_start: str,
        fen_current: str,
        created_at: datetime.datetime,
        finished_at: datetime.datetime,
    ) -> None:
        """Initialize the instance."""
        self.id = entity_id
        self.user_id = user_id
        self.status = status
        self.result = result
        self.fen_start = fen_start
        self.fen_current = fen_current
        self.created_at = created_at
        self.finished_at = finished_at
