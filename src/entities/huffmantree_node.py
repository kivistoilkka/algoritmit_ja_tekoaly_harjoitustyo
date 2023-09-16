class HuffmanTreeNode:
    def __init__(self, frequency: int, symbol: str, left_child=None, right_child=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left_child = left_child
        self.right_child = right_child
        self.huffman_code = ''

    def __lt__(self, node) -> bool:
        return self.frequency < node.frequency

    def __str__(self) -> str:
        return f"{self.symbol}: {self.huffman_code}"
