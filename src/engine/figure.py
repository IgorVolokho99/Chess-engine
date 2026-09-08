"""Модуль, содержащий реализацию шахматных фигур."""

from typing import TYPE_CHECKING

from src.engine.coord import Coord, CoordCastling, CoordWithTransform
from src.engine.enums import Color, FigureType

if TYPE_CHECKING:
    from src.engine.fen_state import FenState

from_char_to_figure = {
    "K": FigureType.king,
    "k": FigureType.king,
    "Q": FigureType.queen,
    "q": FigureType.queen,
    "R": FigureType.rook,
    "r": FigureType.rook,
    "B": FigureType.bishop,
    "b": FigureType.bishop,
    "N": FigureType.knight,
    "n": FigureType.knight,
    "P": FigureType.pawn,
    "p": FigureType.pawn,
}
BOARD_SIZE = 8
WHITE_PAWN_START_RANK = BOARD_SIZE - 2
BLACK_PAWN_START_RANK = 1
WHITE_PROMOTION_RANK = 0
BLACK_PROMOTION_RANK = BOARD_SIZE - 1


class Figure:
    """Реализация шахматной фигуры."""

    def __init__(self, char: str, coord: Coord) -> None:
        """Initialize a figure from its FEN character and board coordinate."""
        self.type_of_figure = from_char_to_figure[char]
        self.char = char
        self.color = Color.white if char.isupper() else Color.black
        self.coord = coord
        self.possible_moves = []

    def generate_move(
        self,
        board: list[list],
        coord_of_king: Coord,
        fen_state: FenState,
    ) -> None:
        """Populate the legal moves available to this figure."""
        my_case = self.color == Color.white
        match self.type_of_figure:
            case FigureType.rook:
                # DOWN
                for changed_y in range(self.coord.y + 1, BOARD_SIZE):
                    cell = board[changed_y][self.coord.x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[changed_y][self.coord.x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(changed_y, self.coord.x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[changed_y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[changed_y][self.coord.x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(changed_y, self.coord.x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[changed_y][self.coord.x] = cell

                # UP
                for changed_y in range(self.coord.y - 1, -1, -1):
                    cell = board[changed_y][self.coord.x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[changed_y][self.coord.x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(changed_y, self.coord.x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[changed_y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[changed_y][self.coord.x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(changed_y, self.coord.x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[changed_y][self.coord.x] = cell

                # RIGHT
                for changed_x in range(self.coord.x + 1, BOARD_SIZE):
                    cell = board[self.coord.y][changed_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[self.coord.y][changed_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(self.coord.y, changed_x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[self.coord.y][changed_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[self.coord.y][changed_x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(self.coord.y, changed_x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[self.coord.y][changed_x] = cell

                # LEFT
                for changed_x in range(self.coord.x - 1, -1, -1):
                    cell = board[self.coord.y][changed_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[self.coord.y][changed_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(self.coord.y, changed_x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[self.coord.y][changed_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[self.coord.y][changed_x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(self.coord.y, changed_x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[self.coord.y][changed_x] = cell

            case FigureType.bishop:
                start_y = self.coord.y + 1
                start_x = self.coord.x + 1
                while start_y < BOARD_SIZE and start_x < BOARD_SIZE:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y += 1
                    start_x += 1

                start_y = self.coord.y + 1
                start_x = self.coord.x - 1
                while start_y < BOARD_SIZE and start_x >= 0:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y += 1
                    start_x -= 1

                start_y = self.coord.y - 1
                start_x = self.coord.x + 1
                while start_y >= 0 and start_x < BOARD_SIZE:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y -= 1
                    start_x += 1

                start_y = self.coord.y - 1
                start_x = self.coord.x - 1
                while start_y >= 0 and start_x >= 0:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y -= 1
                    start_x -= 1

            case FigureType.queen:
                # DOWN
                for changed_y in range(self.coord.y + 1, BOARD_SIZE):
                    cell = board[changed_y][self.coord.x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[changed_y][self.coord.x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(changed_y, self.coord.x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[changed_y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[changed_y][self.coord.x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(changed_y, self.coord.x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[changed_y][self.coord.x] = cell

                # UP
                for changed_y in range(self.coord.y - 1, -1, -1):
                    cell = board[changed_y][self.coord.x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[changed_y][self.coord.x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(changed_y, self.coord.x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[changed_y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[changed_y][self.coord.x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(changed_y, self.coord.x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[changed_y][self.coord.x] = cell

                # RIGHT
                for changed_x in range(self.coord.x + 1, BOARD_SIZE):
                    cell = board[self.coord.y][changed_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[self.coord.y][changed_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(self.coord.y, changed_x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[self.coord.y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[self.coord.y][changed_x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(self.coord.y, changed_x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[self.coord.y][changed_x] = cell

                # LEFT
                for changed_x in range(self.coord.x - 1, -1, -1):
                    cell = board[self.coord.y][changed_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[self.coord.y][changed_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(
                                    Coord(self.coord.y, changed_x),
                                )

                            board[self.coord.y][self.coord.x] = self.char
                            board[self.coord.y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[self.coord.y][changed_x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(self.coord.y, changed_x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[self.coord.y][changed_x] = cell

                start_y = self.coord.y + 1
                start_x = self.coord.x + 1
                while start_y < BOARD_SIZE and start_x < BOARD_SIZE:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y += 1
                    start_x += 1

                start_y = self.coord.y + 1
                start_x = self.coord.x - 1
                while start_y < BOARD_SIZE and start_x >= 0:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y += 1
                    start_x -= 1

                start_y = self.coord.y - 1
                start_x = self.coord.x + 1
                while start_y >= 0 and start_x < BOARD_SIZE:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y -= 1
                    start_x += 1

                start_y = self.coord.y - 1
                start_x = self.coord.x - 1
                while start_y >= 0 and start_x >= 0:
                    cell = board[start_y][start_x]
                    if cell != "-":
                        if cell.isupper() == my_case:
                            break
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = "-"
                            board[start_y][start_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(start_y, start_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[start_y][start_x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = "-"
                        board[start_y][start_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(start_y, start_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[start_y][start_x] = cell
                    start_y -= 1
                    start_x -= 1

            case FigureType.knight:
                knight_y, knight_x = self.coord.y + 2, self.coord.x + 1
                if knight_y < BOARD_SIZE and knight_x < BOARD_SIZE:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

                knight_y, knight_x = self.coord.y + 1, self.coord.x + 2
                if knight_y < BOARD_SIZE and knight_x < BOARD_SIZE:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

                knight_y, knight_x = self.coord.y + 1, self.coord.x - 2
                if knight_y < BOARD_SIZE and knight_x >= 0:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

                knight_y, knight_x = self.coord.y - 1, self.coord.x + 2
                if knight_y >= 0 and knight_x < BOARD_SIZE:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

                knight_y, knight_x = self.coord.y - 1, self.coord.x - 2
                if knight_y >= 0 and knight_x >= 0:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

                knight_y, knight_x = self.coord.y + 2, self.coord.x - 1
                if knight_y < BOARD_SIZE and knight_x >= 0:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

                knight_y, knight_x = self.coord.y - 2, self.coord.x + 1
                if knight_y >= 0 and knight_x < BOARD_SIZE:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

                knight_y, knight_x = self.coord.y - 2, self.coord.x - 1
                if knight_y >= 0 and knight_x >= 0:
                    cell = board[knight_y][knight_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[knight_y][knight_x] = self.char

                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(knight_y, knight_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[knight_y][knight_x] = cell

            case FigureType.pawn:
                if self.color is Color.white:
                    # left up
                    move_y, move_x = self.coord.y - 1, self.coord.x - 1
                    if 0 <= move_y < BOARD_SIZE and 0 <= move_x < BOARD_SIZE:
                        cell = board[move_y][move_x]
                        if cell.isupper() != self.char.isupper() and cell != "-":
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                if move_y == WHITE_PROMOTION_RANK:
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "Q"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "R"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "B"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "N"),
                                    )
                                else:
                                    self.possible_moves.append(Coord(move_y, move_x))
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                        elif (
                            fen_state.en_passant_cell
                            and Coord(move_y, move_x) == fen_state.en_passant_cell
                        ):
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(fen_state.en_passant_cell)
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                    # right up
                    move_y, move_x = self.coord.y - 1, self.coord.x + 1
                    if 0 <= move_y < BOARD_SIZE and 0 <= move_x < BOARD_SIZE:
                        cell = board[move_y][move_x]
                        if cell.isupper() != self.char.isupper() and cell != "-":
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                if move_y == WHITE_PROMOTION_RANK:
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "Q"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "R"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "B"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "N"),
                                    )
                                else:
                                    self.possible_moves.append(Coord(move_y, move_x))
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                        elif (
                            fen_state.en_passant_cell
                            and Coord(move_y, move_x) == fen_state.en_passant_cell
                        ):
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(fen_state.en_passant_cell)
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                    move_y, move_x = self.coord.y - 1, self.coord.x
                    if 0 <= move_y < BOARD_SIZE and 0 <= move_x < BOARD_SIZE:
                        cell = board[move_y][move_x]
                        if cell == "-":
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                if move_y == WHITE_PROMOTION_RANK:
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "Q"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "R"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "B"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "N"),
                                    )
                                else:
                                    self.possible_moves.append(Coord(move_y, move_x))
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                            if self.coord.y == WHITE_PAWN_START_RANK:
                                move_y, move_x = self.coord.y - 2, self.coord.x
                                if cell == "-":
                                    board[self.coord.y][self.coord.x] = "-"
                                    board[move_y][move_x] = self.char
                                    if not self.check_to_king(
                                        board,
                                        coord_of_king,
                                        self.color,
                                    ):
                                        self.possible_moves.append(
                                            Coord(move_y, move_x),
                                        )
                                    board[self.coord.y][self.coord.x] = self.char
                                    board[move_y][move_x] = cell
                else:
                    # left down
                    move_y, move_x = self.coord.y + 1, self.coord.x - 1
                    if 0 <= move_y < BOARD_SIZE and 0 <= move_x < BOARD_SIZE:
                        cell = board[move_y][move_x]
                        if cell.isupper() != self.char.isupper() and cell != "-":
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                if move_y == BLACK_PROMOTION_RANK:
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "Q"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "R"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "B"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "N"),
                                    )
                                else:
                                    self.possible_moves.append(Coord(move_y, move_x))
                            elif (
                                fen_state.en_passant_cell
                                and Coord(move_y, move_x) == fen_state.en_passant_cell
                            ):
                                board[self.coord.y][self.coord.x] = "-"
                                board[move_y][move_x] = self.char
                                if not self.check_to_king(
                                    board,
                                    coord_of_king,
                                    self.color,
                                ):
                                    self.possible_moves.append(
                                        fen_state.en_passant_cell,
                                    )
                                board[self.coord.y][self.coord.x] = self.char
                                board[move_y][move_x] = cell
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                    # right down
                    move_y, move_x = self.coord.y + 1, self.coord.x + 1
                    if 0 <= move_y < BOARD_SIZE and 0 <= move_x < BOARD_SIZE:
                        cell = board[move_y][move_x]
                        if cell.isupper() != self.char.isupper() and cell != "-":
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                if move_y == BLACK_PROMOTION_RANK:
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "Q"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "R"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "B"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "N"),
                                    )
                                else:
                                    self.possible_moves.append(Coord(move_y, move_x))
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                        elif (
                            fen_state.en_passant_cell
                            and Coord(move_y, move_x) == fen_state.en_passant_cell
                        ):
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(fen_state.en_passant_cell)
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                    move_y, move_x = self.coord.y + 1, self.coord.x
                    if 0 <= move_y < BOARD_SIZE and 0 <= move_x < BOARD_SIZE:
                        cell = board[move_y][move_x]
                        if cell == "-":
                            board[self.coord.y][self.coord.x] = "-"
                            board[move_y][move_x] = self.char
                            if not self.check_to_king(board, coord_of_king, self.color):
                                if move_y == BLACK_PROMOTION_RANK:
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "Q"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "R"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "B"),
                                    )
                                    self.possible_moves.append(
                                        CoordWithTransform(move_y, move_x, "N"),
                                    )
                                else:
                                    self.possible_moves.append(Coord(move_y, move_x))
                            board[self.coord.y][self.coord.x] = self.char
                            board[move_y][move_x] = cell
                            if self.coord.y == BLACK_PAWN_START_RANK:
                                move_y, move_x = self.coord.y - 2, self.coord.x
                                if cell == "-":
                                    board[self.coord.y][self.coord.x] = "-"
                                    board[move_y][move_x] = self.char
                                    if not self.check_to_king(
                                        board,
                                        coord_of_king,
                                        self.color,
                                    ):
                                        if move_y == BLACK_PROMOTION_RANK:
                                            self.possible_moves.append(
                                                CoordWithTransform(move_y, move_x, "Q"),
                                            )
                                            self.possible_moves.append(
                                                CoordWithTransform(move_y, move_x, "R"),
                                            )
                                            self.possible_moves.append(
                                                CoordWithTransform(move_y, move_x, "B"),
                                            )
                                            self.possible_moves.append(
                                                CoordWithTransform(move_y, move_x, "N"),
                                            )
                                        else:
                                            self.possible_moves.append(
                                                Coord(move_y, move_x),
                                            )
                                    board[self.coord.y][self.coord.x] = self.char
                                    board[move_y][move_x] = cell
            case FigureType.king:
                # KING PART
                king_y, king_x = self.coord.y + 1, self.coord.x + 1
                if king_y < BOARD_SIZE and king_x < BOARD_SIZE:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                king_y, king_x = self.coord.y - 1, self.coord.x + 1
                if king_y >= 0 and king_x < BOARD_SIZE:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                king_y, king_x = self.coord.y + 1, self.coord.x - 1
                if king_y < BOARD_SIZE and king_x >= 0:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                king_y, king_x = self.coord.y - 1, self.coord.x - 1
                if king_y >= 0 and king_x >= 0:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                king_y, king_x = self.coord.y, self.coord.x - 1
                if king_x >= 0:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                king_y, king_x = self.coord.y, self.coord.x + 1
                if king_x < BOARD_SIZE:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                king_y, king_x = self.coord.y - 1, self.coord.x
                if king_y >= 0:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                king_y, king_x = self.coord.y + 1, self.coord.x
                if king_y < BOARD_SIZE:
                    cell = board[king_y][king_x]
                    if (
                        cell.isupper() != board[self.coord.y][self.coord.x].isupper()
                        or cell.upper() == "-"
                    ):
                        board[self.coord.y][self.coord.x] = "-"
                        board[king_y][king_x] = self.char

                        if not self.check_to_king(
                            board,
                            Coord(king_y, king_x),
                            self.color,
                        ):
                            self.possible_moves.append(Coord(king_y, king_x))

                        board[self.coord.y][self.coord.x] = self.char
                        board[king_y][king_x] = cell

                if self.char.isupper():
                    if fen_state.white_long_castling and not self.check_to_king(
                        board,
                        coord_of_king,
                        self.color,
                    ):
                        left_1 = board[7][3]
                        left_2 = board[7][2]
                        left_3 = board[7][1]
                        if left_1 == "-" and left_2 == "-" and left_3 == "-":
                            king_y, king_x = 7, 3
                            board[self.coord.y][self.coord.x] = "-"
                            board[king_y][king_x] = self.char
                            if not self.check_to_king(
                                board,
                                Coord(king_y, king_x),
                                self.color,
                            ):
                                board[self.coord.y][self.coord.x] = self.char
                                board[king_y][king_x] = "-"
                                king_y, king_x = 7, 2
                                board[self.coord.y][self.coord.x] = "-"
                                board[king_y][king_x] = self.char
                                if not self.check_to_king(
                                    board,
                                    Coord(king_y, king_x),
                                    self.color,
                                ):
                                    board[self.coord.y][self.coord.x] = self.char
                                    board[king_y][king_x] = "-"
                                    king_y, king_x = 7, 1
                                    board[self.coord.y][self.coord.x] = "-"
                                    board[king_y][king_x] = self.char
                                    if not self.check_to_king(
                                        board,
                                        Coord(king_y, king_x),
                                        self.color,
                                    ):
                                        self.possible_moves.append(
                                            CoordCastling(king_y, king_x, "Q"),
                                        )
                                    board[self.coord.y][self.coord.x] = self.char
                                    board[king_y][king_x] = "-"
                    if fen_state.white_short_castling and not self.check_to_king(
                        board,
                        coord_of_king,
                        self.color,
                    ):
                        right_1 = board[7][5]
                        right_2 = board[7][6]
                        if right_1 == "-" and right_2 == "-":
                            king_y, king_x = 7, 5
                            board[self.coord.y][self.coord.x] = "-"
                            board[king_y][king_x] = self.char
                            if not self.check_to_king(
                                board,
                                Coord(king_y, king_x),
                                self.color,
                            ):
                                board[self.coord.y][self.coord.x] = self.char
                                board[king_y][king_x] = "-"
                                king_y, king_x = 7, 6
                                board[self.coord.y][self.coord.x] = "-"
                                board[king_y][king_x] = self.char
                                if not self.check_to_king(
                                    board,
                                    Coord(king_y, king_x),
                                    self.color,
                                ):
                                    self.possible_moves.append(
                                        CoordCastling(king_y, king_x, "K"),
                                    )
                                board[self.coord.y][self.coord.x] = self.char
                                board[king_y][king_x] = "-"
                else:
                    if fen_state.black_long_castling and not self.check_to_king(
                        board,
                        coord_of_king,
                        self.color,
                    ):
                        left_1 = board[0][3]
                        left_2 = board[0][2]
                        left_3 = board[0][1]
                        if left_1 == "-" and left_2 == "-" and left_3 == "-":
                            king_y, king_x = 0, 3
                            board[self.coord.y][self.coord.x] = "-"
                            board[king_y][king_x] = self.char
                            if not self.check_to_king(
                                board,
                                Coord(king_y, king_x),
                                self.color,
                            ):
                                board[self.coord.y][self.coord.x] = self.char
                                board[king_y][king_x] = "-"
                                king_y, king_x = 0, 2
                                board[self.coord.y][self.coord.x] = "-"
                                board[king_y][king_x] = self.char
                                if not self.check_to_king(
                                    board,
                                    Coord(king_y, king_x),
                                    self.color,
                                ):
                                    board[self.coord.y][self.coord.x] = self.char
                                    board[king_y][king_x] = "-"
                                    king_y, king_x = 0, 1
                                    board[self.coord.y][self.coord.x] = "-"
                                    board[king_y][king_x] = self.char
                                    if not self.check_to_king(
                                        board,
                                        Coord(king_y, king_x),
                                        self.color,
                                    ):
                                        self.possible_moves.append(
                                            CoordCastling(king_y, king_x, "q"),
                                        )
                                    board[self.coord.y][self.coord.x] = self.char
                                    board[king_y][king_x] = "-"
                    if fen_state.black_short_castling and not self.check_to_king(
                        board,
                        coord_of_king,
                        self.color,
                    ):
                        right_1 = board[0][5]
                        right_2 = board[0][6]
                        if right_1 == "-" and right_2 == "-":
                            king_y, king_x = 0, 5
                            board[self.coord.y][self.coord.x] = "-"
                            board[king_y][king_x] = self.char
                            if not self.check_to_king(
                                board,
                                Coord(king_y, king_x),
                                self.color,
                            ):
                                board[self.coord.y][self.coord.x] = self.char
                                board[king_y][king_x] = "-"
                                king_y, king_x = 7, 6
                                board[self.coord.y][self.coord.x] = "-"
                                board[king_y][king_x] = self.char
                                if not self.check_to_king(
                                    board,
                                    Coord(king_y, king_x),
                                    self.color,
                                ):
                                    self.possible_moves.append(
                                        CoordCastling(king_y, king_x, "k"),
                                    )
                            board[self.coord.y][self.coord.x] = self.char
                            board[king_y][king_x] = "-"

    @staticmethod
    def check_to_king(board: list[list], coord_of_king: Coord, color: Color) -> bool:
        """Return whether moving to a square would leave the king in check."""
        my_case = color is Color.white

        # ROOK
        for changed_y in range(coord_of_king.y + 1, BOARD_SIZE):
            cell = board[changed_y][coord_of_king.x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "R" or cell.upper() == "Q":
                    return True
                break

        for changed_y in range(coord_of_king.y - 1, -1, -1):
            cell = board[changed_y][coord_of_king.x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "R" or cell.upper() == "Q":
                    return True
                break

        for changed_x in range(coord_of_king.x + 1, BOARD_SIZE):
            cell = board[coord_of_king.y][changed_x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "R" or cell.upper() == "Q":
                    return True
                break

        for changed_x in range(coord_of_king.x - 1, -1, -1):
            cell = board[coord_of_king.y][changed_x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "R" or cell.upper() == "Q":
                    return True
                break

        # BISHOP
        start_y = coord_of_king.y + 1
        start_x = coord_of_king.x + 1
        while start_y < BOARD_SIZE and start_x < BOARD_SIZE:
            cell = board[start_y][start_x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "B" or cell.upper() == "Q":
                    return True
                break
            start_y += 1
            start_x += 1

        start_y = coord_of_king.y + 1
        start_x = coord_of_king.x - 1
        while start_y < BOARD_SIZE and start_x >= 0:
            cell = board[start_y][start_x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "B" or cell.upper() == "Q":
                    return True
                break
            start_y += 1
            start_x -= 1

        start_y = coord_of_king.y - 1
        start_x = coord_of_king.x + 1
        while start_y >= 0 and start_x < BOARD_SIZE:
            cell = board[start_y][start_x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "B" or cell.upper() == "Q":
                    return True
                break
            start_y -= 1
            start_x += 1

        start_y = coord_of_king.y - 1
        start_x = coord_of_king.x - 1
        while start_y >= 0 and start_x >= 0:
            cell = board[start_y][start_x]
            if cell != "-":
                if cell.isupper() == my_case:
                    break
                if cell.upper() == "B" or cell.upper() == "Q":
                    return True
                break
            start_y -= 1
            start_x -= 1

        # KNIGHT Part
        knight_y, knight_x = coord_of_king.y + 2, coord_of_king.x + 1
        if knight_y < BOARD_SIZE and knight_x < BOARD_SIZE:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        knight_y, knight_x = coord_of_king.y + 1, coord_of_king.x + 2
        if knight_y < BOARD_SIZE and knight_x < BOARD_SIZE:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        knight_y, knight_x = coord_of_king.y + 1, coord_of_king.x - 2
        if knight_y < BOARD_SIZE and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        knight_y, knight_x = coord_of_king.y - 1, coord_of_king.x + 2
        if knight_y >= 0 and knight_x < BOARD_SIZE:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        knight_y, knight_x = coord_of_king.y - 1, coord_of_king.x - 2
        if knight_y >= 0 and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        knight_y, knight_x = coord_of_king.y + 2, coord_of_king.x - 1
        if knight_y < BOARD_SIZE and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        knight_y, knight_x = coord_of_king.y - 2, coord_of_king.x + 1
        if knight_y >= 0 and knight_x < BOARD_SIZE:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        knight_y, knight_x = coord_of_king.y - 2, coord_of_king.x - 1
        if knight_y >= 0 and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "N"
            ):
                return True

        # PAWN part
        if my_case:
            pawn_y = coord_of_king.y - 1
            pawn_x = coord_of_king.x - 1
            if (
                pawn_y >= 0
                and pawn_x >= 0
                and board[pawn_y][pawn_x].isupper() != my_case
                and board[pawn_y][pawn_x].isupper() == "P"
            ):
                return True
            pawn_x = coord_of_king.x + 1
            if (
                pawn_y >= 0
                and pawn_x < BOARD_SIZE
                and board[pawn_y][pawn_x].isupper() != my_case
                and board[pawn_y][pawn_x].isupper() == "P"
            ):
                return True
        else:
            pawn_y = coord_of_king.y + 1
            pawn_x = coord_of_king.x - 1
            if (
                pawn_y < BOARD_SIZE
                and pawn_x >= 0
                and board[pawn_y][pawn_x].isupper() != my_case
                and board[pawn_y][pawn_x].isupper() == "P"
            ):
                return True
            pawn_x = coord_of_king.x + 1
            if (
                pawn_y < BOARD_SIZE
                and pawn_x < BOARD_SIZE
                and board[pawn_y][pawn_x].isupper() != my_case
                and board[pawn_y][pawn_x].isupper() == "P"
            ):
                return True

        # KING PART
        king_y, king_x = coord_of_king.y + 1, coord_of_king.x + 1
        if king_y < BOARD_SIZE and king_x < BOARD_SIZE:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        king_y, king_x = coord_of_king.y + 1, coord_of_king.x - 1
        if king_y < BOARD_SIZE and king_x < BOARD_SIZE:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        king_y, king_x = coord_of_king.y + 1, coord_of_king.x
        if king_y < BOARD_SIZE and king_x >= 0:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        king_y, king_x = coord_of_king.y - 1, coord_of_king.x + 1
        if king_y >= 0 and king_x < BOARD_SIZE:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        king_y, king_x = coord_of_king.y - 1, coord_of_king.x - 1
        if king_y >= 0 and king_x >= 0:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        king_y, king_x = coord_of_king.y - 1, coord_of_king.x
        if king_y < BOARD_SIZE and king_x >= 0:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        king_y, king_x = coord_of_king.y, coord_of_king.x + 1
        if king_y >= 0 and king_x < BOARD_SIZE:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        king_y, king_x = coord_of_king.y, coord_of_king.x - 1
        if king_y >= 0 and king_x >= 0:
            cell = board[king_y][king_x]
            if (
                cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper()
                and cell.upper() == "K"
            ):
                return True

        return False

    def __repr__(self) -> str:
        """Return the FEN symbol for this figure."""
        return str(self.type_of_figure.value)
