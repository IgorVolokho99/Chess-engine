"""Модуль, который содержит необходимые перечисления для игры."""

from enum import Enum


class Color(Enum):
    """Перечисление, для реализации цвета фигуры."""
    black = "black"
    white = "white"


class FigureType(Enum):
    """Перечисление, для реализации типа фигуры."""
    king = "king"
    queen = "queen"
    rook = "rook"
    bishop = "bishop"
    knight = "knight"
    pawn = "pawn"

