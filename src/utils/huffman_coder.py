from collections import Counter
from heapq import heappush, heappop, heapify

from bitstring import Bits, BitArray, ConstBitStream

from config import ENCODING


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


class HuffmanCoder:
    """Class handling Huffman coding
    """

    def __init__(self) -> None:
        pass

    def encode(self, input_string: str) -> BitArray:
        """Method for encoding input bytes with Huffman coding

        Args:
            input_string (str): Text to be encoded

        Returns:
            BitArray: BitArray of combined encoded Huffman tree and encoded data
        """

        input_bytes = input_string.encode(encoding=ENCODING)
        symbols_and_frequencies = Counter(input_bytes)
        tree = self.create_huffman_tree(symbols_and_frequencies)
        table = self.create_huffman_table(tree)
        encoded_data = self.huffman_encode_data(input_bytes, table)
        encoded_tree = self.encode_huffman_tree(tree)
        return encoded_tree + encoded_data

    def decode(self, encoded_bytes: BitArray) -> bytes:
        """Method for decoding Huffman coded data using given encoded Huffman tree

        Args:
            encoded_bytes (bytes): Encoded Huffman tree that was used for
                                   encoding of data followed by encoded data.

        Returns:
            str: Decoded text in bytes
        """

        encoded_stream = ConstBitStream(encoded_bytes)
        tree = self.decode_huffman_tree(encoded_stream)
        return self.huffman_decode_data(encoded_stream, tree)

    def create_huffman_tree(self, symbols_and_frequencies: dict[bytes, int]) -> HuffmanTreeNode:
        nodes = []
        for symbol, freq in symbols_and_frequencies.items():
            nodes.append(HuffmanTreeNode(freq, symbol))
        heapify(nodes)

        while len(nodes) > 1:
            left = heappop(nodes)
            right = heappop(nodes)

            new_node = HuffmanTreeNode(
                left.frequency+right.frequency,
                left.symbol+right.symbol,
                left,
                right
            )
            heappush(nodes, new_node)

        return heappop(nodes)

    def create_huffman_table(self, root_node: HuffmanTreeNode) -> dict[int, Bits]:
        huffman_table = {}
        self.add_node_to_table(root_node, huffman_table)
        return huffman_table

    def add_node_to_table(self, node: HuffmanTreeNode, table: dict, code: str = ''):
        if node is None:
            return
        if node.is_leaf():
            table[node.symbol] = Bits(bin=code)
            return
        self.add_node_to_table(node.left_child, table, code + '0')
        self.add_node_to_table(node.right_child, table, code + '1')

    def huffman_encode_data(self, data: bytes, table: dict) -> BitArray:
        encoded_data = BitArray()
        for symbol in data:
            encoded_symbol = table[symbol]
            encoded_data.append(encoded_symbol)
        return encoded_data

    def encode_huffman_tree(self, root_node: HuffmanTreeNode) -> BitArray:
        tree = BitArray()
        encoded_tree = self.add_node_to_encoded_tree(root_node, tree)
        return encoded_tree

    def add_node_to_encoded_tree(self, node: HuffmanTreeNode, encoded_tree: BitArray) -> BitArray:
        if node is None:
            return
        if node.is_leaf():
            encoded_tree.append(bin(1))
            return encoded_tree.append(node.symbol.to_bytes(1))
        encoded_tree.append(bin(0))
        self.add_node_to_encoded_tree(
            node.left_child, encoded_tree)
        self.add_node_to_encoded_tree(
            node.right_child, encoded_tree)
        return encoded_tree

    def decode_huffman_tree(self, encoded_tree: ConstBitStream) -> HuffmanTreeNode:
        huffman_tree_root = self.add_node_to_decoded_tree(encoded_tree)
        return huffman_tree_root

    def add_node_to_decoded_tree(self, code: ConstBitStream):
        bit = code.read(1)
        if bit == bin(1):
            char = code.read(8)
            return HuffmanTreeNode(1, char.bytes)
        left_child = self.add_node_to_decoded_tree(code)
        right_child = self.add_node_to_decoded_tree(code)
        return HuffmanTreeNode(0, '#', left_child, right_child)

    def huffman_decode_data(self, encoded_data: ConstBitStream, tree: HuffmanTreeNode) -> bytes:
        decoded_data = b''
        node = tree
        while True:
            current_bit = encoded_data.read(1)
            if current_bit == bin(0) and node.left_child:
                node = node.left_child
            elif node.right_child:
                node = node.right_child
            if node.is_leaf():
                decoded_data += node.symbol
                node = tree
            if encoded_data.pos == len(encoded_data):
                break
        return decoded_data
