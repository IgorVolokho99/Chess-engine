import datetime


class Move:
    def __init__(
            self,
            id: int,
            user_id: int,
            game_id: int,
            move_number: int,
            played_at: datetime.datetime,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.game_id = game_id
        self.move_number = move_number
        self.played_at = played_at
