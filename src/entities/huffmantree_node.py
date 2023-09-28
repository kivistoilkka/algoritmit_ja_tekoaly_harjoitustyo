class HuffmanTreeNode:

    def __init__(self, frequency: int, symbol: bytes, left_child=None, right_child=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left_child = left_child
        self.right_child = right_child

    def __lt__(self, node) -> bool:
        return self.frequency < node.frequency

    def __str__(self) -> str:
        return f"{self.symbol}: {self.frequency}"

    def __repr__(self) -> str:
        return f"{self.symbol}: {self.frequency}"

    def is_leaf(self) -> bool:
        return self.left_child is None and self.right_child is None
