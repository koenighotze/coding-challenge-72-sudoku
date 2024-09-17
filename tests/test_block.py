# -*- coding: utf-8 -*-
import pytest
from sudoku.block import Block


class TestBlock:
    def test_equals_false(self):
        a_block = Block([[1, 2, 9], [0, 0, 0], [0, 0, 3]])

        assert a_block != Block([[1, 2, 9], [0, 0, 0], [0, 0, 4]])

    def test_equals_true(self):
        a_block = Block([[1, 2, 9], [0, 0, 0], [0, 0, 3]])

        # pylint: disable=comparison-with-itself
        assert a_block == a_block  # noqa: R0124

        assert a_block == Block([[1, 2, 9], [0, 0, 0], [0, 0, 3]])


if __name__ == '__main__':
    pytest.main()
