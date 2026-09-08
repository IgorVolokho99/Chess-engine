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
        self._board = [["-"] * 8 for _ in range(8)]
        self._white_figures = []
        self._black_figures = []
        self._white_coords = []
        self._black_coords = []
        self._coord_of_white_king = None
        self._coord_of_black_king = None
        self._fen_state = None
        self._initialize()

    def _initialize(self) -> None:
        self._fen_state = FenState(self._fen)
        self.fill_board()
        self.fill_figures_and_coords()
        self.generate_moves()

    @property
    def board(self) -> list[list[str]]:
        """Return the mutable board representation."""
        return self._board

    @property
    def fen_state(self) -> FenState:
        """Return the parsed state of the current FEN position."""
        return self._fen_state

    @property
    def white_figures(self) -> list[Figure]:
        """Return the white figures in this position."""
        return self._white_figures

    @property
    def black_figures(self) -> list[Figure]:
        """Return the black figures in this position."""
        return self._black_figures

    def fill_board(self) -> None:
        """Populate the board from the piece-placement part of the FEN."""
        board_parts = self._fen_state.board_part.split("/")
        for i, part in enumerate(board_parts):
            j = 0
            for cell in part:
                if cell.isdigit():
                    j += int(cell)
                else:
                    self._board[i][j] = cell
                    j += 1

    def fill_figures_and_coords(self) -> None:
        """Create figure objects and cache the king coordinates."""
        board_parts = self._fen_state.board_part.split("/")
        for i, part in enumerate(board_parts):
            j = 0
            for cell in part:
                if cell.isdigit():
                    j += int(cell)
                else:
                    if cell == "K":
                        self._coord_of_white_king = Coord(i, j)
                    elif cell == "k":
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

    def generate_fen_from_board(self) -> str:
        """Build a FEN string from the current board and state."""
        fen = ""
        for line in self._board:
            s = ""
            counter = 0
            for cell in line:
                if cell == "-":
                    counter += 1
                else:
                    if counter != 0:
                        s += str(counter)
                    s += cell
                    counter = 0
            if counter != 0:
                s += str(counter)

            fen += s + "/"
        fen = fen[:-1]

        if self._fen_state.active_color is Color.white:
            fen += " w "
        else:
            fen += " b "

        if self._fen_state.white_short_castling:
            fen += "K"
        if self._fen_state.white_long_castling:
            fen += "Q"
        if self._fen_state.black_short_castling:
            fen += "k"
        if self._fen_state.black_long_castling:
            fen += "q"

        if fen[-1] == " ":
            fen += "- "

        if self._fen_state.en_passant_cell is not None:
            fen += self._fen_state.el_passant_cell.chess_string_visualization()
        else:
            fen += "- "

        fen += str(self._fen_state.moves_without_pawn) + " "
        fen += str(self._fen_state.move_clock)

        return fen

    def generate_moves(self) -> None:
        """Generate legal moves for every figure in the active position."""
        active_figures = (
            self._white_figures
            if self._fen_state.active_color == Color.white
            else self._black_figures
        )
        coord_of_king = (
            self._coord_of_white_king
            if self._fen_state.active_color == Color.white
            else self._coord_of_black_king
        )
        for figure in active_figures:
            figure.generate_move(self._board, coord_of_king, self._fen_state)

    def show_board(self) -> None:
        """Perform this operation."""
        for line in self._board:
            for _cell in line:
                pass

    def show_moves(self) -> None:
        """Perform this operation."""
        figures = (
            self._white_figures
            if self._fen_state.active_color is Color.white
            else self._black_figures
        )

        for y, line in enumerate(self._board):
            for x, cell in enumerate(line):
                if cell == "-":
                    maybe_attack = Coord(y, x)
                    counter = 0
                    for figure in figures:
                        if maybe_attack in figure.possible_moves:
                            counter += 1
                        if counter != 0:
                            break
                    else:
                        pass
                else:
                    maybe_attack = Coord(y, x)
                    for figure in figures:
                        if maybe_attack in figure.possible_moves:
                            break
                    else:
                        pass

    def make_move(self, figure: Figure, move_from: Coord, move_to: Coord) -> None:
        """Perform this operation."""
        if move_to is Coord:
            self._board[move_to.y][move_to.x] = self._board[move_from.y][move_from.x]
            figure.coord = move_to
        else:
            pass

    def is_win(self) -> True:
        """Perform this operation."""
        active_figures = (
            self._white_figures
            if self._fen_state.active_color is Color.white
            else self._black_figures
        )

        return all(not figure.possible_moves for figure in active_figures)


if __name__ == "__main__":
    position = Position("rnbqkbnr/pppppppp/8/8/8/BN3NBQ/PPPPPPPP/R3K2R w KQkq - 0 1")
    position.show_moves()
