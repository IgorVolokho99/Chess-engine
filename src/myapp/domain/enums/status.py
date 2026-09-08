"""Provide application functionality."""

from enum import StrEnum


class GameStatus(StrEnum):
    """Represent a domain component."""

    ACTIVE = "ACTIVE"
    FINISHED = "FINISHED"
    ABANDONED = "ABANDONED"
