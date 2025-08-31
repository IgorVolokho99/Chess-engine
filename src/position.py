"""Модуль, который содержит реализацию шахматной позиции."""
from src.coord import Coord
from src.enums import Color, FigureType
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
            figure.generate_move(self._board, coord_of_king)

    def show_board(self) -> None:
        for line in self._board:
            for cell in line:
                print(cell, end=' ')
            print()

    def show_moves(self) -> None:
        # figures = self._white_figures if self._fen_state.active_color == 'w' else self._black_figures
        # opposite_figures = self._white_figures if self._fen_state.active_color == 'b' else self._black_figures
        #
        # for y, line in enumerate(self._board):
        #     for x, cell in enumerate(line):
        #         if cell == '-':
        #             maybe_attack = Coord(y, x)
        #             for figure in figures:
        #                 if maybe_attack in figure.possible_moves:
        #                     print('*', end=' ')
        #                     break
        #             else:
        #                 print(cell, end=' ')
        #         else:
        #             maybe_attack = Coord(y, x)
        #             for figure in figures:
        #                 if maybe_attack in figure.possible_moves:
        #                     print('!', end=' ')
        #                     break
        #             else:
        #                 print(cell, end=' ')
        #     print()
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
    import time

    start_time = time.time()
    # position = Position("2q5/8/5k2/2R5/8/8/8/2K5 w - - 0 1") # Rook
    # position = Position("3k4/8/7q/8/5B2/8/7K/8 w - - 0 1")  # Bishop
    # position = Position("3k4/8/8/8/5Q2/8/7K/8 w - - 0 1")  # Queen
    # position = Position("3k4/8/8/4q3/5N2/8/7K/8 w - - 0 1")  # Knight
    for i in range(1000):
        position = Position("rnbqkbnr/1p1p1ppp/2p1p3/p3Q2R/1P1P4/r7/P1P1PPPP/RNBQKBNR w KQkq - 0 1")  # Knight
        Figure.check_to_king(position._board, position._coord_of_white_king, Color.white)
        # position.show_board()
        # position.show_moves()
    # for figure in position._white_figures:
    #     print(figure.possible_moves)
    end_time = time.time()
    print(end_time - start_time)
