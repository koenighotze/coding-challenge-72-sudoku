from sudoku.block import Block
from sudoku.block_position import BlockPosition


class Puzzle:
    def __init__(self, puzzle: list[list[int]]) -> None:
        if len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
            raise ValueError("Puzzle must be a list with 9 rows and 9 columns")
        self.puzzle = puzzle

    @staticmethod
    def empty_puzzle() -> "Puzzle":
        return Puzzle([[0] * 9 for _ in range(9)])

    def get_value_at(self, row: int, col: int) -> int:
        return self.puzzle[row][col]

    def get_block(self, position: BlockPosition) -> Block:
        row, col = position.value
        block: list[list[int]] = []
        for i in range(row, row + 3):
            block.append(self.puzzle[i][col : col + 3])
        return Block(block)

    def is_solved(self) -> bool:
        return False

    def __str__(self) -> str:
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.puzzle)
