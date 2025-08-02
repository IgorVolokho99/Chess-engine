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
        self.color = Color.white if char.isupper() else Color.black
        self.coord = coord
        self.possible_moves = None

    @staticmethod
    def check_to_king(board: list[list], coord_of_king: Coord, color: Color) -> bool:
        if color == Color.white:
            my_case = True
        else:
            my_case = False

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

        # start_y = coord_of_king.y + 1
        # start_x = coord_of_king.x + 1
        # while start_y < 8 and start_x < 8:
        #     cell = board[start_y][start_x]
        #     if cell != '-':
        #         if cell.isupper() == my_case:
        #             break
        #         else:
        #             if cell.upper() == 'R' or cell.upper() == 'Q':
        #                 return True
        #             break
        #     start_y += 1
        #     start_x += 1
        #
        # start_y = coord_of_king.y + 1
        # start_x = coord_of_king.x - 1
        # while start_y < 8 and start_x >= 0:
        #     cell = board[start_y][start_x]
        #     if cell != '-':
        #         if cell.isupper() == my_case:
        #             break
        #         else:
        #             if cell.upper() == 'R' or cell.upper() == 'Q':
        #                 return True
        #             break
        #     start_y += 1
        #     start_x -= 1
        #
        # start_y = coord_of_king.y - 1
        # start_x = coord_of_king.x + 1
        # while start_y >= 0 and start_x < 8:
        #     cell = board[start_y][start_x]
        #     if cell != '-':
        #         if cell.isupper() == my_case:
        #             break
        #         else:
        #             if cell.upper() == 'R' or cell.upper() == 'Q':
        #                 return True
        #             break
        #     start_y -= 1
        #     start_x += 1
        #
        # start_y = coord_of_king.y - 1
        # start_x = coord_of_king.x - 1
        # while start_y >= 0 and start_x >= 0:
        #     cell = board[start_y][start_x]
        #     if cell != '-':
        #         if cell.isupper() == my_case:
        #             break
        #         else:
        #             if cell.upper() == 'R' or cell.upper() == 'Q':
        #                 return True
        #             break
        #     start_y -= 1
        #     start_x -= 1

        return False
