"""Модуль, который содержит реализацию фигуры со всем её содержимым."""

from src.coord import Coord
from src.enums import FigureType, Color

from_char_to_figure = {
    'K': FigureType.king,
    'k': FigureType.king,
    'Q': FigureType.queen,
    'q': FigureType.queen,
    'R': FigureType.rook,
    'r': FigureType.rook,
    'B': FigureType.bishop,
    'b': FigureType.bishop,
    'N': FigureType.knight,
    'n': FigureType.knight,
    'P': FigureType.pawn,
    'p': FigureType.pawn,
}


class Figure:
    """Реализация шахматной фигуры."""

    def __init__(self, char: str, coord: Coord) -> None:
        self.type_of_figure = from_char_to_figure[char]
        self.char = char
        self.color = Color.white if char.isupper() else Color.black
        self.coord = coord
        self.possible_moves = []

    def generate_move(self, board: list[list], coord_of_king: Coord) -> None:
        if self.color == Color.white:
            my_case = True
        else:
            my_case = False
        match self.type_of_figure:
            case FigureType.rook:
                # DOWN
                for changed_y in range(self.coord.y + 1, 8):
                    cell = board[changed_y][self.coord.x]
                    if cell != '-':
                        if cell.isupper() == my_case:
                            break
                        elif cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = '-'
                            board[changed_y][self.coord.x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(changed_y, self.coord.x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[changed_y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = '-'
                        board[changed_y][self.coord.x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(changed_y, self.coord.x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[changed_y][self.coord.x] = cell
                # UP
                for changed_y in range(self.coord.y - 1, -1, -1):
                    cell = board[changed_y][self.coord.x]
                    if cell != '-':
                        if cell.isupper() == my_case:
                            break
                        elif cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = '-'
                            board[changed_y][self.coord.x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(changed_y, self.coord.x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[changed_y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = '-'
                        board[changed_y][self.coord.x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(changed_y, self.coord.x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[changed_y][self.coord.x] = cell

                # RIGHT
                for changed_x in range(self.coord.x + 1, 8):
                    cell = board[self.coord.y][changed_x]
                    if cell != '-':
                        if cell.isupper() == my_case:
                            break
                        elif cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = '-'
                            board[self.coord.y][changed_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(self.coord.y, changed_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[self.coord.y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = '-'
                        board[self.coord.y][changed_x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(self.coord.y, changed_x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[self.coord.y][changed_x] = cell

                # LEFT
                for changed_x in range(self.coord.x - 1, -1, -1):
                    cell = board[self.coord.y][changed_x]
                    if cell != '-':
                        if cell.isupper() == my_case:
                            break
                        elif cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = '-'
                            board[self.coord.y][changed_x] = self.char

                            if not self.check_to_king(board, coord_of_king, self.color):
                                self.possible_moves.append(Coord(self.coord.y, changed_x))

                            board[self.coord.y][self.coord.x] = self.char
                            board[self.coord.y][self.coord.x] = cell
                            break
                    else:
                        board[self.coord.y][self.coord.x] = '-'
                        board[self.coord.y][changed_x] = self.char
                        if not self.check_to_king(board, coord_of_king, self.color):
                            self.possible_moves.append(Coord(self.coord.y, changed_x))
                        board[self.coord.y][self.coord.x] = self.char
                        board[self.coord.y][changed_x] = cell

            case FigureType.bishop:
                pass
            case FigureType.queen:
                pass
            case FigureType.knight:
                pass
            case FigureType.pawn:
                pass
            case FigureType.king:
                pass

    @staticmethod
    def check_to_king(board: list[list], coord_of_king: Coord, color: Color) -> bool:
        if color == Color.white:
            my_case = True
        else:
            my_case = False

        # ROOK
        for changed_y in range(coord_of_king.y + 1, 8):
            cell = board[changed_y][coord_of_king.x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'R' or cell.upper() == 'Q':
                        return True
                    break

        for changed_y in range(coord_of_king.y - 1, -1, -1):
            cell = board[changed_y][coord_of_king.x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'R' or cell.upper() == 'Q':
                        return True
                    break

        for changed_x in range(coord_of_king.x + 1, 8):
            cell = board[coord_of_king.y][changed_x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'R' or cell.upper() == 'Q':
                        return True
                    break

        for changed_x in range(coord_of_king.x - 1, -1, -1):
            cell = board[coord_of_king.y][changed_x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'R' or cell.upper() == 'Q':
                        return True
                    break

        # BISHOP
        start_y = coord_of_king.y + 1
        start_x = coord_of_king.x + 1
        while start_y < 8 and start_x < 8:
            cell = board[start_y][start_x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'B' or cell.upper() == 'Q':
                        return True
                    break
            start_y += 1
            start_x += 1

        start_y = coord_of_king.y + 1
        start_x = coord_of_king.x - 1
        while start_y < 8 and start_x >= 0:
            cell = board[start_y][start_x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'B' or cell.upper() == 'Q':
                        return True
                    break
            start_y += 1
            start_x -= 1

        start_y = coord_of_king.y - 1
        start_x = coord_of_king.x + 1
        while start_y >= 0 and start_x < 8:
            cell = board[start_y][start_x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'B' or cell.upper() == 'Q':
                        return True
                    break
            start_y -= 1
            start_x += 1

        start_y = coord_of_king.y - 1
        start_x = coord_of_king.x - 1
        while start_y >= 0 and start_x >= 0:
            cell = board[start_y][start_x]
            if cell != '-':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'B' or cell.upper() == 'Q':
                        return True
                    break
            start_y -= 1
            start_x -= 1

        # KNIGHT Part
        knight_y, knight_x = coord_of_king.y + 2, coord_of_king.x + 1
        if knight_y < 8 and knight_x < 8:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        knight_y, knight_x = coord_of_king.y + 1, coord_of_king.x + 2
        if knight_y < 8 and knight_x < 8:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        knight_y, knight_x = coord_of_king.y + 1, coord_of_king.x - 2
        if knight_y < 8 and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        knight_y, knight_x = coord_of_king.y - 1, coord_of_king.x + 2
        if knight_y >= 0 and knight_x < 8:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        knight_y, knight_x = coord_of_king.y - 1, coord_of_king.x - 2
        if knight_y >= 0 and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        knight_y, knight_x = coord_of_king.y + 2, coord_of_king.x - 1
        if knight_y < 8 and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        knight_y, knight_x = coord_of_king.y - 2, coord_of_king.x + 1
        if knight_y >= 0 and knight_x < 8:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        knight_y, knight_x = coord_of_king.y - 2, coord_of_king.x - 1
        if knight_y >= 0 and knight_x >= 0:
            cell = board[knight_y][knight_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'N':
                return True

        # PAWN part
        if my_case:
            pawn_y = coord_of_king.y - 1
            pawn_x = coord_of_king.x - 1
            if pawn_y >= 0 and pawn_x >= 0 and board[pawn_y][pawn_x].isupper() != my_case and \
                    board[pawn_y][pawn_x].isupper() == 'P':
                return True
            pawn_x = coord_of_king.x + 1
            if pawn_y >= 0 and pawn_x <= 8 and board[pawn_y][pawn_x].isupper() != my_case and \
                    board[pawn_y][pawn_x].isupper() == 'P':
                return True
        else:
            pawn_y = coord_of_king.y + 1
            pawn_x = coord_of_king.x - 1
            if pawn_y < 8 and pawn_x >= 0 and board[pawn_y][pawn_x].isupper() != my_case and \
                    board[pawn_y][pawn_x].isupper() == 'P':
                return True
            pawn_x = coord_of_king.x + 1
            if pawn_y < 8 and pawn_x <= 8 and board[pawn_y][pawn_x].isupper() != my_case and \
                    board[pawn_y][pawn_x].isupper() == 'P':
                return True

        # KING PART
        king_y, king_x = coord_of_king.y + 1, coord_of_king.x + 1
        if king_y < 8 and king_x < 8:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        king_y, king_x = coord_of_king.y + 1, coord_of_king.x + 1
        if king_y < 8 and king_x < 8:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        king_y, king_x = coord_of_king.y + 1, coord_of_king.x - 1
        if king_y < 8 and king_x >= 0:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        king_y, king_x = coord_of_king.y - 1, coord_of_king.x + 1
        if king_y >= 0 and king_x < 8:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        king_y, king_x = coord_of_king.y - 1, coord_of_king.x - 1
        if king_y >= 0 and king_x >= 0:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        king_y, king_x = coord_of_king.y + 1, coord_of_king.x - 1
        if king_y < 8 and king_x >= 0:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        king_y, king_x = coord_of_king.y - 1, coord_of_king.x + 1
        if king_y >= 0 and king_x < 8:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        king_y, king_x = coord_of_king.y - 1, coord_of_king.x - 1
        if king_y >= 0 and king_x >= 0:
            cell = board[king_y][king_x]
            if cell.isupper() != board[coord_of_king.y][coord_of_king.x].isupper() and cell.upper() == 'K':
                return True

        return False
