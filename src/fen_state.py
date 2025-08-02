"""Модуль, который содержит реализацию и хранения параметров fen-нотации."""
from src.coord import Coord
from src.enums import Color

from_letter_to_digit = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


class FenState:
    """Реализация fen-параметров."""

    def __init__(self, fen: str) -> None:
        """Инициализирует поля объектами None."""
        self.board_part = None
        self.active_color = None
        self.white_long_castling = False
        self.white_short_castling = False
        self.black_long_castling = False
        self.black_short_castling = False
        self.en_passant_cell = None
        self.moves_without_pawn = None
        self.move_clock = None

        self.parse_fen(fen)

    def parse_fen(self, fen: str) -> None:
        fen_parts = fen.split(' ')

        self.board_part = fen_parts[0]

        if fen_parts[1] == 'w':
            self.active_color = Color.white
        else:
            self.active_color = Color.black

        if 'K' in fen_parts[2]:
            self.white_short_castling = True
        if 'Q' in fen_parts[2]:
            self.white_long_castling = True
        if 'k' in fen_parts[2]:
            self.black_short_castling = True
        if 'q' in fen_parts[2]:
            self.black_long_castling = True

        if fen_parts[3] != '-':
            letter = fen_parts[3][0]
            digit = fen_parts[3][1]
            coord_x = from_letter_to_digit[letter]
            coord_y = 8 - int(digit)
            self.en_passant_cell = Coord(coord_x, coord_y)

        if fen_parts[4] == '-':
            self.moves_without_pawn = 0
        else:
            self.moves_without_pawn = int(fen_parts[4])

        self.move_clock = int(fen_parts[5])
