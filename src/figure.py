"""Модуль, который содержит реализацию фигуры со всем её содержимым."""

from src.coord import Coord
from src.enums import FigureType, Color

from_char_to_figure = {
    'K': FigureType.king,
    'k': FigureType.king,
    'Q': FigureType.queen,
    'q': FigureType.queen,
    'R': FigureType.rook,
    'r': FigureType.rook,
    'B': FigureType.bishop,
    'b': FigureType.bishop,
    'N': FigureType.knight,
    'n': FigureType.knight,
    'P': FigureType.pawn,
    'p': FigureType.pawn,
}


class Figure:
    """Реализация шахматной фигуры."""

    def __init__(self, char: str, coord: Coord) -> None:
        self.type_of_figure = from_char_to_figure[char]
        self.color = Color.white if char.isupper() else Color.black
        self.coord = coord
        self.possible_moves = None
