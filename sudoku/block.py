class Block:
    def __init__(self, block):
        self.block = block

    def __eq__(self, other):
        if not isinstance(other, Block):
            return False
        return self.block == other.block

    def __str__(self):
        return "\n".join(' '.join(str(cell) for cell in row) for row in self.block)