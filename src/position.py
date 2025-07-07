"""Модуль, который содержит реализацию шахматной позиции."""


class Position:
    """Реализация шахматной позиции."""

    def __init__(self, fen: str) -> None:
        """Иницилизирует позицию принимая на вход fen-параметр.

        Args:
            fen: Строка, представляющая из себя нотацию Форсайта — Эдвардса.
        """
        self._fen = fen
        self._board = None
        self._white_figures = None
        self._black_figures = None
        self._white_coords = None
        self._black_coords = None

    def generate_board_from_fen(self) -> None:
        pass

    def generate_fen_from_board(self) -> None:
        pass

    def generate_moves(self) -> None:
        pass
