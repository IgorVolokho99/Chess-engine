from pprint import pprint

import pytest

from src.engine.enums import Color
from src.engine.figure import Figure
from src.engine.position import Position


class TestFigure:

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/4k3/8/8/2K3r1/8/8 w - - 0 1", "Test_1"),
            ("8/2r5/4k3/8/8/2K5/8/8 w - - 0 1", "Test_2"),
            ("8/8/4k3/8/8/r1K5/8/8 w - - 0 1", "Test_3"),
            ("8/8/4k3/8/8/2K5/8/2r5 w - - 0 1", "Test_4"),
            ("r7/8/4k3/8/8/8/8/K7 w - - 0 1", "Test_5"),
            ("r7/8/4k3/8/8/8/8/K7 w - - 0 1", "Test_6"),
            ("8/8/4k3/8/8/5rK1/8/8 w - - 0 1", "Test_7"),
            ("8/8/4k3/1rrr4/1rKr4/1rrr4/8/8 w - - 0 1", "Test_8"),
        ]
    )
    def test_check_to_white_king_rook_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/4k3/8/2K5/8/r7/8 w - - 0 1", "Test_1"),
            ("8/8/4k3/8/2K5/2R5/r1r5/8 w - - 0 1", "Test_2"),
            ("2r5/2n5/4k3/8/2K5/2R5/r1r5/8 w - - 0 1", "Test_3"),
        ]
    )
    def test_check_to_white_king_rook_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/4K3/8/8/2k3R1/8/8 w - - 0 1", "Test_1"),
            ("8/2R5/4K3/8/8/2k5/8/8 w - - 0 1", "Test_2"),
            ("8/8/4K3/8/8/R1k5/8/8 w - - 0 1", "Test_3"),
            ("8/8/4K3/8/8/2k5/8/2R5 w - - 0 1", "Test_4"),
            ("R7/8/4K3/8/8/8/8/k7 w - - 0 1", "Test_5"),
            ("R7/8/4K3/8/8/8/8/k7 w - - 0 1", "Test_6"),
            ("8/8/4K3/8/8/5Rk1/8/8 w - - 0 1", "Test_7"),
            ("8/8/4K3/1RRR4/1RkR4/1RRR4/8/8 w - - 0 1", "Test_8"),
        ]
    )
    def test_check_to_black_king_rook_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black), comment

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/4K3/8/2k5/8/R7/8 w - - 0 1", "Test_1"),
            ("8/8/4K3/8/2k5/2r5/R1R5/8 w - - 0 1", "Test_2"),
            ("2R5/2N5/4K3/8/2k5/2r5/R1R5/8 w - - 0 1", "Test_3"),
        ]
    )
    def test_check_to_black_king_rook_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/5k2/8/2K5/8/4b3/8 w - - 0 1", "Test_1"),
            ("8/2k5/8/5b2/6K1/8/8/8 w - - 0 1", "Test_2"),
            ("1k3K2/8/7b/8/8/b7/8/8 w - - 0 1", "Test_3"),
            ("1k6/8/8/2b1b3/3K4/2b1b3/8/8 w - - 0 1", "Test_4"),
        ]
    )
    def test_check_to_white_king_bishop_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/5K2/8/2k5/8/4B3/8 w - - 0 1", "Test_1"),
            ("8/2K5/8/5B2/6k1/8/8/8 w - - 0 1", "Test_2"),
            ("1K3k2/8/7B/8/8/b7/8/8 w - - 0 1", "Test_3"),
            ("1K6/8/8/2B1B3/3k4/2B1B3/8/8 w - - 0 1", "Test_4"),
        ]
    )
    def test_check_to_black_king_bishop_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("1k6/8/8/8/3K4/8/2B5/8 w - - 0 1", "Test_1"),
            ("1k6/8/8/3B4/3K4/3B4/2B5/8 w - - 0 1", "Test_2"),
            ("1k6/8/8/6K1/8/4B3/8/2b5 w - - 0 1", "Test_3"),
            ("1k1b4/4p3/8/6K1/8/4B3/8/2b5 w - - 0 1", "Test_4"),
        ]
    )
    def test_check_to_white_king_bishop_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("1K6/8/8/8/3k4/8/2b5/8 w - - 0 1", "Test_1"),
            ("1K6/8/8/3b4/3k4/3b4/2b5/8 w - - 0 1", "Test_2"),
            ("1K6/8/8/6k1/8/4b3/8/2B5 w - - 0 1", "Test_3"),
            ("1K1B4/4P3/8/6k1/8/4b3/8/2B5 w - - 0 1", "Test_4"),
        ]
    )
    def test_check_to_black_king_bishop_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    # KNIGHT
    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("1k6/8/4n3/8/3K4/8/8/8 w - - 0 1", "Test_1"),
            ("1k6/8/8/8/3K4/1n6/8/8 w - - 0 1", "Test_2"),
            ("1k6/8/8/8/8/6n1/5n2/7K w - - 0 1", "Test_3"),
            ("KP6/PPn5/8/6k1/8/8/5n2/8 w - - 0 1", "Test_4"),
            ("1P6/PPn5/8/6k1/8/8/2n5/K7 w - - 0 1", "Test_5"),
            ("1P6/PPn5/8/6k1/8/8/2n5/K7 w - - 0 1", "Test_5"),

        ]
    )
    def test_check_to_white_king_knight_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/8/6k1/2n5/1n1n4/n1K1n3/1n1n4 w - - 0 1", "Test_1"),

        ]
    )
    def test_check_to_white_king_knight_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/2k5/8/1N1N4/8/8/7K w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_black_king_knight_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("2N5/1N1N4/N1k1N3/1N1N4/2N5/8/8/7K w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_black_king_knight_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    # QUEEN
    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/1k4q1/8/8/3K4/8/8/8 w - - 0 1", "Test_1"),
            ("8/1k6/8/8/8/8/8/q6K w - - 0 1", "Test_2"),
        ]
    )
    def test_check_to_white_king_queen_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/1k6/8/6q1/8/5K2/1q6/8 w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_white_king_queen_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/1k6/8/6K1/8/8/1Q6/8 w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_black_king_queen_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/1k6/8/6K1/8/2Q5/8/8 w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_black_king_queen_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/5k2/3p4/2K5/8/8/8 w - - 0 1", "Test_1"),
            ("8/8/5k2/1p6/2K5/8/8/8 w - - 0 1", "Test_2"),
        ]
    )
    def test_check_to_white_king_pawn_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/5K2/8/2k5/3P4/8/8 w - - 0 1", "Test_1"),
            ("8/8/5K2/8/2k5/1P6/8/8 w - - 0 1", "Test_2"),
        ]
    )
    def test_check_to_black_king_pawn_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/8/3k4/2K5/8/8/8 w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_white_king_king_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/8/3k4/8/8/2K5/8 w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_white_king_king_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_white_king, Color.white)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/8/3k4/2K5/8/8/8 w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_black_king_king_with_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/8/3k4/8/8/2K5/8 w - - 0 1", "Test_1"),
        ]
    )
    def test_check_to_black_king_king_without_check(self, fen: str, comment: str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)
