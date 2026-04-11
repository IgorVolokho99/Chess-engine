import datetime

from src.domain.enums.game_result import Result
from src.domain.enums.status import Status


class Game:
    def __init__(
            self,
            id: int,
            user_id: int,
            status: Status,
            result: Result,
            fen_start: str,
            fen_current: str,
            created_at: datetime.datetime,
            finished_at: datetime.datetime,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.status = status
        self.result = result
        self.fen_start = fen_start
        self.fen_current = fen_current
        self.created_at = created_at
        self.finished_at = finished_at
