"""Модуль, который содержит реализацию шахматной позиции."""
from src.coord import Coord
from src.enums import Color
from src.fen_state import FenState
from src.figure import Figure


class Position:
    """Реализация шахматной позиции."""

    def __init__(self, fen: str) -> None:
        """Иницилизирует позицию принимая на вход fen-параметр.

        Args:
            fen: Строка, представляющая из себя нотацию Форсайта — Эдвардса.
        """
        self._fen = fen
        self._board = [['-'] * 8 for _ in range(8)]
        self._white_figures = []
        self._black_figures = []
        self._white_coords = []
        self._black_coords = []
        self._coord_of_white_king = None
        self._coord_of_black_king = None
        self._fen_state = FenState(fen)
        self.generate_board_from_fen()
        self.fill_figures_and_coords()
        self.generate_moves()

    def generate_board_from_fen(self) -> None:
        board_parts = self._fen_state.board_part.split('/')
        for i, part in enumerate(board_parts):
            j = 0
            for cell in part:
                if cell.isdigit():
                    j += int(cell)
                else:
                    self._board[i][j] = cell
                    j += 1

    def fill_figures_and_coords(self) -> None:
        board_parts = self._fen_state.board_part.split('/')
        for i, part in enumerate(board_parts):
            j = 0
            for cell in part:
                if cell.isdigit():
                    j += int(cell)
                else:
                    if cell == 'K':
                        self._coord_of_white_king = Coord(j, i)
                    elif cell == 'k':
                        self._coord_of_black_king = Coord(j, i)
                    self._add_figure(cell, j, i)
                    self._board[i][j] = cell
                    j += 1

    def _add_figure(self, char: str, x: int, y: int) -> None:
        coord = Coord(x, y)
        figure = Figure(char, coord)
        if char.isupper():
            self._white_figures.append(figure)
            self._white_coords.append(coord)
        else:
            self._black_figures.append(figure)
            self._black_coords.append(coord)

    def generate_fen_from_board(self) -> None:
        pass

    def generate_moves(self) -> None:
        active_figures = self._white_figures if self._fen_state.active_color == Color.white else self._black_figures
        coord_of_king = self._coord_of_white_king if self._fen_state.active_color == Color.white else self._coord_of_black_king
        for figure in active_figures:
            figure.generate_move(self._board, coord_of_king)


if __name__ == "__main__":
    import time

    start_time = time.time()
    position = Position("1k1b4/4p3/8/6K1/8/4B3/8/2b5 w - - 0 1")
    Figure.check_to_king(position._board, position._coord_of_white_king, Color.white)
    end_time = time.time()
    print(end_time - start_time)
