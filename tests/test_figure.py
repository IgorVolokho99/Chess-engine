import pytest

from src.enums import Color
from src.figure import Figure
from src.position import Position


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
    def test_check_to_white_king_rook_with_check(self, fen: str, comment:str) -> None:
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
    def test_check_to_white_king_rook_without_check(self, fen: str, comment:str) -> None:
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
    def test_check_to_black_king_rook_with_check(self, fen: str, comment:str) -> None:
        pos = Position(fen)
        assert Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)

    @pytest.mark.parametrize(
        "fen, comment",
        [
            ("8/8/4K3/8/2k5/8/R7/8 w - - 0 1", "Test_1"),
            ("8/8/4K3/8/2k5/2r5/R1R5/8 w - - 0 1", "Test_2"),
            ("2R5/2N5/4K3/8/2k5/2r5/R1R5/8 w - - 0 1", "Test_3"),
        ]
    )
    def test_check_to_black_king_rook_without_check(self, fen: str, comment:str) -> None:
        pos = Position(fen)
        assert not Figure.check_to_king(pos._board, pos._coord_of_black_king, Color.black)