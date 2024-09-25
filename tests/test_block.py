# -*- coding: utf-8 -*-
import pytest
from sudoku.block import Block


class TestBlock:
    def test_equals_false(self) -> None:
        a_block = Block([[1, 2, 9], [0, 0, 0], [0, 0, 3]])

        assert a_block != Block([[1, 2, 9], [0, 0, 0], [0, 0, 4]])

    def test_equals_true(self) -> None:
        a_block = Block([[1, 2, 9], [0, 0, 0], [0, 0, 3]])

        # pylint: disable=comparison-with-itself
        assert a_block == a_block  # noqa: R0124

        assert a_block == Block([[1, 2, 9], [0, 0, 0], [0, 0, 3]])

    @pytest.mark.parametrize(
        "block, is_solved",
        [
            ([[1, 2, 9], [0, 0, 0], [0, 0, 3]], False),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], True),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], False),
            ([[9, 9, 9], [0, 0, 0], [0, 0, 0]], False),
            ([[9, 8, 7], [1, 2, 3], [4, 6, 5]], True),
        ],
    )
    def test_solved(self, block: list[list[int]], is_solved: bool) -> None:
        assert Block(block).is_solved() == is_solved


if __name__ == "__main__":
    pytest.main()
