# -*- coding: utf-8 -*-


from .context import sudoku


import unittest


class PuzzleTestSuite(unittest.TestCase):
    test_puzzle_configuration = [
                [0, 0, 0, 2, 9, 0, 4, 5, 0],
                [0, 5, 0, 3, 4, 0, 0, 0, 2],
                [6, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 9, 0, 0, 0, 6, 7],
                [0, 0, 7, 6, 8, 1, 0, 2, 9],
                [8, 0, 6, 5, 0, 0, 1, 0, 0],
                [7, 0, 0, 1, 2, 9, 0, 8, 0],
                [0, 0, 3, 0, 0, 0, 0, 1, 4],
                [0, 0, 0, 0, 0, 3, 7, 0, 0]
            ]

    def test_the_constructor_empty_field(self):
        p = sudoku.Puzzle.empty_puzzle()

        value = p.get_value_at(row = 1, col = 2)

        assert value == 0

    def test_empty_puzzle_returns_a_puzzle_filled_with_zeros(self):
        p = sudoku.Puzzle.empty_puzzle()

        assert len(p.puzzle) == 9
        for row in p.puzzle:
            assert len(row) == 9
            for value in row:
                assert value == 0

    def test_the_puzzle_must_have_9_rows(self):
        with self.assertRaises(ValueError):
            sudoku.Puzzle([[]] * 8)

    def test_the_puzzle_must_have_9_columns(self):
        with self.assertRaises(ValueError):
            sudoku.Puzzle([[0]] * 8)

    def test_the_constructor_with_puzzle(self):
        p = sudoku.Puzzle(
            [
                [1, 2, 3, 0, 0, 0, 0, 0, 0],
                [4, 5, 6, 0, 0, 0, 0, 0, 0],
                [7, 8, 9, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 2, 3, 0, 0, 0],
                [0, 0, 0, 4, 5, 6, 0, 0, 0],
                [0, 0, 0, 7, 8, 9, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        )
        
        assert 6 == p.get_value_at(row = 1, col = 2)
        assert 3 == p.get_value_at(row = 3, col = 5)

    def test_getting_a_block(self):
        p = sudoku.Puzzle(self.test_puzzle_configuration)

        assert p.get_block(sudoku.BlockPosition.TOP_LEFT) == sudoku.Block([[0, 0, 0], [0, 5, 0], [6, 0, 0]])
        assert p.get_block(sudoku.BlockPosition.BOTTOM_CENTER) == sudoku.Block([[1, 2, 9], [0, 0, 0], [0, 0, 3]])
        assert p.get_block(sudoku.BlockPosition.MIDDLE_CENTER) == sudoku.Block([[9, 0, 0], [6, 8, 1], [5, 0, 0]])
 
if __name__ == '__main__':
    unittest.main()
