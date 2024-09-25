class Block:
    def __init__(self, block: list[list[int]]) -> None:
        self.block = block

    def is_solved(self) -> bool:
        target: set[int] = set(range(1, 10))
        flattened = {element for row in self.block for element in row}

        return len(target - flattened) == 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Block):
            return False
        return self.block == other.block

    def __str__(self) -> str:
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.block)
