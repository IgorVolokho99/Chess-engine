from enum import Enum


class GameStatus(str, Enum):
    ACTIVE = "ACTIVE"
    FINISHED = "FINISHED"
    ABANDONED = "ABANDONED"

