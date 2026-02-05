from copy import deepcopy

from src.engine.enums import Color
from src.engine.position import Position


class Node:
    def __init__(self, position: Position):
        self.position = position
        self.children = []


class ChessEngine:
    def __init__(self, node: Node):
        self.root = node

    def generate_tree(self, node: Node, depth: int) -> bool:
        if depth == 0:
            return node.position.is_win()
        depth -= 1

        active_figures = node.position._white_figures if node.position._fen_state.active_color is Color.white else node.position._black_figures

        for figure in active_figures:
            for move in figure.possible_moves:
                old_figure = node.position._board[move.y][move.x]
                node.position._board[move.y][move.x] = figure.char
                node.position._board[move.y][move.x] = '-'
                # Обработать изменение полей
                new_fen = node.position.generate_fen_from_board()
                node.position._board[move.y][move.x] = figure.char
                node.position._board[move.y][move.x] = old_figure

                new_position = Position(new_fen)

                # Сделать ход на доске.
                # Вызывать метод get_fen_from_board()
                # Сгенерировать производную доску по новому фену.
                # Вернуть ход на доске.


def get_win(position: Position):
    node = Node(position)
    chess_engine = ChessEngine(node)


def main():
    position = Position("1k6/8/1KR5/8/8/8/8/8 w - - 0 1")
    if get_win(position):
        print("Есть победа.")
    else:
        print("Нет победы.")


if __name__ == "__main__":
    main()
