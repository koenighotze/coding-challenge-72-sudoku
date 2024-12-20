# -*- coding: utf-8 -*-

import pytest

from sudoku.block import Block
from sudoku.block_position import BlockPosition
from sudoku.puzzle import Puzzle


class TestPuzzle:
    test_puzzle_configuration = [
        [0, 0, 0, 2, 9, 0, 4, 5, 0],
        [0, 5, 0, 3, 4, 0, 0, 0, 2],
        [6, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 9, 0, 0, 0, 6, 7],
        [0, 0, 7, 6, 8, 1, 0, 2, 9],
        [8, 0, 6, 5, 0, 0, 1, 0, 0],
        [7, 0, 0, 1, 2, 9, 0, 8, 0],
        [0, 0, 3, 0, 0, 0, 0, 1, 4],
        [0, 0, 0, 0, 0, 3, 7, 0, 0],
    ]

    def test_the_constructor_empty_field(self) -> None:
        p = Puzzle.empty_puzzle()

        value = p.get_value_at(row=1, col=2)

        assert value == 0

    def test_empty_puzzle_returns_a_puzzle_filled_with_zeros(self) -> None:
        p = Puzzle.empty_puzzle()

        assert len(p.puzzle) == 9
        for row in p.puzzle:
            assert len(row) == 9
            for value in row:
                assert value == 0

    def test_the_puzzle_must_have_9_rows(self) -> None:
        with pytest.raises(ValueError):
            Puzzle([[]] * 8)

    def test_the_puzzle_must_have_9_columns(self) -> None:
        with pytest.raises(ValueError):
            Puzzle([[0]] * 8)

    @pytest.mark.parametrize(
        "expected, row, col",
        [
            (6, 1, 2),
            (3, 3, 5),
        ],
    )
    def test_the_constructor_with_puzzle(self, expected: int, row: int, col: int) -> None:
        p = Puzzle(
            [
                [1, 2, 3, 0, 0, 0, 0, 0, 0],
                [4, 5, 6, 0, 0, 0, 0, 0, 0],
                [7, 8, 9, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 3, 0, 0, 0],
                [0, 0, 0, 4, 5, 6, 0, 0, 0],
                [0, 0, 0, 7, 8, 9, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

        assert expected == p.get_value_at(row=row, col=col)

    @pytest.mark.parametrize(
        "expected, position",
        [
            ([[0, 0, 0], [0, 5, 0], [6, 0, 0]], BlockPosition.TOP_LEFT),
            ([[1, 2, 9], [0, 0, 0], [0, 0, 3]], BlockPosition.BOTTOM_CENTER),
            ([[9, 0, 0], [6, 8, 1], [5, 0, 0]], BlockPosition.MIDDLE_CENTER),
        ],
    )
    def test_getting_a_block(self, expected: list[list[int]], position: BlockPosition) -> None:
        p = Puzzle(self.test_puzzle_configuration)

        assert p.get_block(position) == Block(expected)


if __name__ == "__main__":
    pytest.main()
