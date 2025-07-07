"""Модуль, который содержит необходимые перечисления для игры."""

from enum import Enum, StrEnum


class Color(Enum):
    """Перечисление, для реализации цвета фигуры."""
    black = StrEnum
    white = StrEnum


class FigureType(Enum):
    """Перечисление, для реализации типа фигуры."""
    king = StrEnum
    queen = StrEnum
    rook = StrEnum
    bishop = StrEnum
    Knight = StrEnum
    Pawn = StrEnum
