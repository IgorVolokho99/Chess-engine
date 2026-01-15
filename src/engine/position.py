"""Модуль, который содержит реализацию шахматной позиции."""
from src.engine.coord import Coord
from src.engine.enums import Color
from src.engine.fen_state import FenState
from src.engine.figure import Figure


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
        self._fen_state = None
        self._initialize()

    def _initialize(self) -> None:
        self.fill_board()
        self.fill_figures_and_coords()
        self._fen_state = FenState(self._fen)
        self.generate_moves()

    def fill_board(self) -> None:
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
                        self._coord_of_white_king = Coord(i, j)
                    elif cell == 'k':
                        self._coord_of_black_king = Coord(i, j)
                    self._add_figure(cell, i, j)
                    self._board[i][j] = cell
                    j += 1

    def _add_figure(self, char: str, y: int, x: int) -> None:
        coord = Coord(y, x)
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
            figure.generate_move(self._board, coord_of_king, self._fen_state.en_passant_cell)

    def show_board(self) -> None:
        for line in self._board:
            for cell in line:
                print(cell, end=' ')
            print()

    def show_moves(self) -> None:
        figures = self._white_figures if self._fen_state.active_color is Color.white else self._black_figures

        for y, line in enumerate(self._board):
            for x, cell in enumerate(line):
                if cell == '-':
                    maybe_attack = Coord(y, x)
                    counter = 0
                    for figure in figures:
                        if maybe_attack in figure.possible_moves:
                            counter += 1
                        if counter != 0:
                            print(counter, end=' ')
                            break
                    else:
                        print(cell, end=' ')
                else:
                    maybe_attack = Coord(y, x)
                    for figure in figures:
                        if maybe_attack in figure.possible_moves:
                            print('!', end=' ')
                            break
                    else:
                        print(cell, end=' ')
            print()


if __name__ == "__main__":
    position = Position("1k6/8/8/3pP3/8/8/8/1K6 w - d6 0 1")
    position.show_moves()
