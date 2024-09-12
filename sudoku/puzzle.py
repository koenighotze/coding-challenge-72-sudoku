from .block import Block 

class Puzzle:
    def __init__(self, puzzle) -> None:
        if not isinstance(puzzle, list) or len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
            raise ValueError("Puzzle must be a list with 9 rows and 9 columns")
        self.puzzle = puzzle

    @staticmethod
    def empty_puzzle():
        return Puzzle([[0] * 9 for _ in range(9)])

    def get_value_at(self, row: int, col: int) -> int:
        return self.puzzle[row][col]
    
    def get_block(self, position):
        row, col = position.value
        block = []
        for i in range(row, row + 3):
            block.append(self.puzzle[i][col:col + 3])
        return Block(block)
    
    def __str__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.puzzle)

