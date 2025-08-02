import pytest

from src.coord import Coord
from src.enums import Color
from src.position import Position


class TestPosition:
    @pytest.mark.parametrize(
        "fen",
        [
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        ]
    )
    def test_generate_board_from_starting_position(self, fen: str) -> None:
        pos = Position(fen)
        assert pos._board[0] == list("rnbqkbnr")
        assert pos._board[1] == list("pppppppp")
        assert pos._board[2] == list("-" * 8)
        assert pos._board[6] == list("PPPPPPPP")
        assert pos._board[7] == list("RNBQKBNR")

        assert pos._fen_state.board_part == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    @pytest.mark.parametrize(
        "fen, expected, comment",
        [
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", [True, True, True, True], "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Qkq - 0 1", [False, True, True, True], "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1", [True, False, True, True], "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQq - 0 1", [True, True, False, True], "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQk - 0 1", [True, True, True, False], "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kk - 0 1", [True, False, True, False], "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Qq - 0 1", [False, True, False, True], "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1", [False, False, False, False], "Test_1"),
        ]
    )
    def test_castling(self, fen: str, expected: list, comment: str) -> None:
        pos = Position(fen)

        assert pos._fen_state.white_short_castling == expected[0], comment + " 1 assert"
        assert pos._fen_state.white_long_castling == expected[1], comment + " 2 assert"
        assert pos._fen_state.black_short_castling == expected[2], comment + " 3 assert"
        assert pos._fen_state.black_long_castling == expected[3], comment + " 4 assert"

    @pytest.mark.parametrize(
        "fen, expected_color, comment",
        [
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", Color.white, "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1", Color.black, "Test_2"),
        ]
    )
    def test_color(self, fen: str, expected_color: Color, comment) -> None:
        pos = Position(fen)
        assert pos._fen_state.active_color == expected_color, comment

    @pytest.mark.parametrize(
        "fen, expected_coord, comment",
        [
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", None, "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq e3 0 1", Coord(4, 5), "Test_2"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq b5 0 1", Coord(1, 3), "Test_3"),
        ]
    )
    def test_el_passant_cell(self, fen: str, expected_coord: Coord, comment: str) -> None:
        pos = Position(fen)
        assert pos._fen_state.en_passant_cell == expected_coord, comment

    @pytest.mark.parametrize(
        "fen, expected_count, comment",
        [
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 0, "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 5 1", 5, "Test_2"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 17 1", 17, "Test_3")
        ]
    )
    def test_move_without_pawn(self, fen: str, expected_count: int, comment: str) -> None:
        pos = Position(fen)
        assert pos._fen_state.moves_without_pawn == expected_count, comment

    @pytest.mark.parametrize(
        "fen, expected_count, comment",
        [
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 1, "Test_1"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 5 17", 17, "Test_2"),
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 17 112", 112, "Test_3")
        ]
    )
    def test_move_clock(self, fen: str, expected_count: int, comment: str) -> None:
        pos = Position(fen)
        assert pos._fen_state.move_clock == expected_count, comment

    @pytest.mark.parametrize(
        "fen, expected_white_coord, expected_black_coord, comment",
        [
            ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", Coord(4, 7), Coord(4, 0), "Test_1"),
            ("8/8/4k3/8/8/2K5/8/8 w - - 0 1", Coord(2, 5), Coord(4, 2), "Test_1"),
        ]
    )
    def test_coordinates_of_kings(self, fen: str, expected_white_coord: Coord, expected_black_coord: Coord,
                                  comment: str) -> None:
        pos = Position(fen)
        assert pos._coord_of_white_king == expected_white_coord, comment + " 1 assert"
        assert pos._coord_of_black_king == expected_black_coord, comment + " 2 assert"
