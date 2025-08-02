"""Модуль, который содержит реализацию шахматной позиции."""
from src.coord import Coord
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
        self._fen_state = FenState(fen)
        self.generate_board_from_fen()
        self.fill_figures_and_coords()

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
        pass


if __name__ == "__main__":
    import time
    start_time = time.time()
    position = Position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    # print(position._white_coords)
    # print(position._black_coords)
    end_time = time.time()
    print(end_time - start_time)
