from sudoku.puzzle import Puzzle
from sudoku.block_position import BlockPosition
from sudoku.block import Block


def main():
    # Create a default puzzle
    default_puzzle = Puzzle([
                [0, 0, 0, 2, 9, 0, 4, 5, 0],
                [0, 5, 0, 3, 4, 0, 0, 0, 2],
                [6, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 9, 0, 0, 0, 6, 7],
                [0, 0, 7, 6, 8, 1, 0, 2, 9],
                [8, 0, 6, 5, 0, 0, 1, 0, 0],
                [7, 0, 0, 1, 2, 9, 0, 8, 0],
                [0, 0, 3, 0, 0, 0, 0, 1, 4],
                [0, 0, 0, 0, 0, 3, 7, 0, 0]
            ])
    
    # Print the default puzzle
    print(default_puzzle)
    print("")

    blocka = default_puzzle.get_block(BlockPosition.TOP_LEFT)
    print(blocka)

    print("")

    blockb = Block([[0, 0, 0], [2, 9, 0], [4, 5, 0]])
    print(blockb)
    print(blocka == blockb)

if __name__ == "__main__":
    main()