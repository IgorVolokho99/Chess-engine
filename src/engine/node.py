"""Search-tree nodes and a simple chess-engine traversal."""

import time

from src.engine.enums import Color
from src.engine.position import Position


class Node:
    """A node holding a chess position in the search tree."""

    def __init__(self, position: Position) -> None:
        """Initialize a node for a position."""
        self.position = position
        self.children = []


class ChessEngine:
    """Generate and evaluate a tree of legal chess positions."""

    def __init__(self, node: Node) -> None:
        """Initialize the engine with its root node."""
        self.root = node

    def generate_tree(self, node: Node, depth: int, amount_of_moves: int) -> bool:
        """Evaluate the game tree below a node to the requested depth."""
        if depth == 0:
            return node.position.is_win()
        depth -= 1

        active_figures = (
            node.position.white_figures
            if node.position.fen_state.active_color is Color.white
            else node.position.black_figures
        )

        children = []
        next_color = (
            Color.white
            if node.position.fen_state.active_color is Color.black
            else Color.black
        )
        current_color = node.position.fen_state.active_color
        for figure in active_figures:
            for move in figure.possible_moves:
                old_figure = node.position.board[move.y][move.x]
                node.position.board[move.y][move.x] = figure.char
                node.position.board[figure.coord.y][figure.coord.x] = "-"
                node.position.fen_state.active_color = next_color
                # Обработать изменение полей
                new_fen = node.position.generate_fen_from_board()
                node.position.fen_state.active_color = current_color
                node.position.board[figure.coord.y][figure.coord.x] = figure.char
                node.position.board[move.y][move.x] = old_figure
                children.append(Position(new_fen))

        amount_of_moves += 1

        if amount_of_moves % 2 == 1:
            return any(
                self.generate_tree(Node(child), depth, amount_of_moves)
                for child in children
            )
        return all(
            self.generate_tree(Node(child), depth, amount_of_moves)
            for child in children
        )


def main() -> None:
    """Run a small search-tree demonstration."""
    position = Position("2k5/8/3KR3/8/8/8/8/8 w - - 0 1")
    node = Node(position)
    time.perf_counter()
    chess_engine = ChessEngine(node)
    if chess_engine.generate_tree(node, 7, 0):
        pass
    else:
        pass


if __name__ == "__main__":
    main()
