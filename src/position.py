"""Модуль, который содержит реализацию шахматной позиции."""
from src.fen_state import FenState


class Position:
    """Реализация шахматной позиции."""

    def __init__(self, fen: str) -> None:
        """Иницилизирует позицию принимая на вход fen-параметр.

        Args:
            fen: Строка, представляющая из себя нотацию Форсайта — Эдвардса.
        """
        self._fen = fen
        self._board = [['-'] * 8 for _ in range(8)]
        self._fet_state = FenState(fen)
        self._white_figures = None
        self._black_figures = None
        self._white_coords = None
        self._black_coords = None
        self.generate_board_from_fen()

    def generate_board_from_fen(self) -> None:
        board_parts = self._fen.split(' ')[0].split('/')
        for i, part in enumerate(board_parts):
            j = 0
            for cell in part:
                if cell.isdigit():
                    j += int(cell)
                else:
                    self._board[i][j] = cell
                    j += 1

    def generate_fen_from_board(self) -> None:
        pass

    def generate_moves(self) -> None:
        pass


if __name__ == "__main__":
    pos = Position("rnbq1bnr/pppkpppp/8/3p4/4P3/5N2/PPPP1PPP/RNBQKB1R w KQ - 2 3")
    for partt in pos._board:
        print(partt)
