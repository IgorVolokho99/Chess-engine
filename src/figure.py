"""Модуль, который содержит реализацию фигуры со всем её содержимым."""

from src.coord import Coord
from src.enums import FigureType, Color


class Figure:
    """Реализация шахматной фигуры."""

    def __init__(self, type_of_figure: FigureType, color: Color, coord: Coord, possible_moves: list[Coord]) -> None:
        self.type_of_figure = type_of_figure
        self.color = color
        self.coord = coord
        self.possible_moves = possible_moves
