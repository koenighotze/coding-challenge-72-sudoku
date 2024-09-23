class Block:
    def __init__(self, block):
        self.block = block

    def is_solved(self):
        target = [i for i in range(1, 10)]
        flattened = [element for row in self.block for element in row]

        return len([missing for missing in target if missing not in flattened]) == 0

    def __eq__(self, other):
        if not isinstance(other, Block):
            return False
        return self.block == other.block

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.block)
