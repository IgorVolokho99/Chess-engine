from enum import Enum


class GameResult(str, Enum):
    WHITE_WIN = "WHITE_WIN"
    BLACK_WIN = "BLACK_WIN"
    DRAW = "DRAW"
    UNKNOWN = "UNKNOWN"
