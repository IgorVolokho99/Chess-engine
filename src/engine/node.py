from src.engine.enums import Color
from src.engine.position import Position


class Node:
    def __init__(self, position: Position):
        self.position = position
        self.children = []


class ChessEngine:
    def __init__(self, node: Node):
        self.root = node

    def generate_tree(self, node: Node, depth: int, amount_of_moves: int) -> bool:
        if depth == 0:
            return node.position.is_win()
        depth -= 1

        active_figures = node.position._white_figures if node.position._fen_state.active_color is Color.white else node.position._black_figures

        children = []
        next_color = Color.white if node.position._fen_state.active_color is Color.black else Color.black
        current_color = node.position._fen_state.active_color
        for figure in active_figures:
            for move in figure.possible_moves:
                old_figure = node.position._board[move.y][move.x]
                node.position._board[move.y][move.x] = figure.char
                node.position._board[figure.coord.y][figure.coord.x] = '-'
                node.position._fen_state.active_color = next_color
                # Обработать изменение полей
                new_fen = node.position.generate_fen_from_board()
                node.position._fen_state.active_color = current_color
                node.position._board[figure.coord.y][figure.coord.x] = figure.char
                node.position._board[move.y][move.x] = old_figure
                children.append(Position(new_fen))

        amount_of_moves += 1

        if amount_of_moves % 2 == 1:
            return any(self.generate_tree(Node(child), depth, amount_of_moves) for child in children)
        else:
            return all(self.generate_tree(Node(child), depth, amount_of_moves) for child in children)


def main():
    position = Position("1k6/8/1KR5/8/8/8/8/8 w - - 0 1")
    node = Node(position)
    chess_engine = ChessEngine(node)
    if chess_engine.generate_tree(node, 3, 0):
        print("Есть победа.")
    else:
        print("Нет победы.")


if __name__ == "__main__":
    main()
