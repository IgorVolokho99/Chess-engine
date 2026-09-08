"""Provide application functionality."""

from enum import StrEnum


class GameResult(StrEnum):
    """Represent a domain component."""

    WHITE_WIN = "WHITE_WIN"
    BLACK_WIN = "BLACK_WIN"
    DRAW = "DRAW"
    UNKNOWN = "UNKNOWN"
