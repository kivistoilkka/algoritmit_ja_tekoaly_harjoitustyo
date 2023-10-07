from collections import Counter
from heapq import heappush, heappop, heapify

from bitstring import Bits, BitArray, ConstBitStream

from ..entities.huffmantree_node import HuffmanTreeNode


class HuffmanCoder:
    """Class handling Huffman coding
    """

    def __init__(self) -> None:
        pass

    def encode(self, input_string: str) -> tuple[BitArray, BitArray]:
        """Method for encoding input bytes with Huffman coding

        Args:
            input_string (str): Text to be encoded

        Returns:
            tuple[BitArray, BitArray]: Tuple where first value is encoded Huffman tree and second is encoded data
        """

        input = input_string.encode(encoding='ISO8859-1')
        symbols_and_frequencies = self.calculate_frequencies(input)
        tree = self.create_huffman_tree(symbols_and_frequencies)
        table = self.create_huffman_table(tree)
        print(table)
        encoded_data = self.huffman_encode_data(input, table)
        encoded_tree = self.encode_huffman_tree(tree)
        return (encoded_tree, encoded_data)

    def decode(self, encoded_tree: bytes, encoded_data: bytes) -> bytes:
        """Method for decoding Huffman coded data using given encoded Huffman tree

        Args:
            encoded_tree (bytes): Encoded Huffman tree that was used for encoding of data
            encoded_data (bytes): Data to be encoded

        Returns:
            str: Decoded text in bytes
        """

        tree_bits = ConstBitStream(encoded_tree)
        data_bits = ConstBitStream(encoded_data)
        tree = self.decode_huffman_tree(tree_bits)
        return self.huffman_decode_data(data_bits, tree)

    def calculate_frequencies(self, input: bytes) -> dict:
        output = Counter(input)
        return output

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

    def create_huffman_table(self, root_node: HuffmanTreeNode) -> dict:
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
        print('Tree to decode:')
        print(encoded_tree.bin)
        print()
        huffman_tree_root = self.add_node_to_decoded_tree(encoded_tree)
        return huffman_tree_root

    def add_node_to_decoded_tree(self, code: ConstBitStream):
        bit = code.read(1)
        if bit == bin(1):
            #print('adding')
            char = code.read(8)
            #print('char:', int.from_bytes(char.tobytes()))
            return HuffmanTreeNode(1, char.bytes)
        #print('going left')
        left_child = self.add_node_to_decoded_tree(code)
        #print('going right')
        right_child = self.add_node_to_decoded_tree(code)
        return HuffmanTreeNode(0, '#', left_child, right_child)

    def huffman_decode_data(self, encoded_data: ConstBitStream, tree: HuffmanTreeNode) -> bytes:
        decoded_data = b''
        #i = 0
        node = tree
        # for i in range(0, len(encoded_data)):
        #     print('next byte:', end='')
        #     print(encoded_data.peek(1))
        #     if encoded_data[i] == 0 and node.left_child:
        #         node = node.left_child
        #     elif node.right_child:
        #         node = node.right_child
        #     if node.is_leaf():
        #         print('symbol:', end='')
        #         print(node.symbol)
        #         decoded_data = decoded_data + bytes(node.symbol)
        #         node = tree
        while True:
            current_bit = encoded_data.read(1)
            print('current bit:', current_bit)
            if current_bit == bin(0) and node.left_child:
                node = node.left_child
            elif node.right_child:
                node = node.right_child
            if node.is_leaf():
                print('symbol:', node.symbol)
                decoded_data += node.symbol
                node = tree
            if encoded_data.pos == len(encoded_data):
                break
        return decoded_data


if __name__ == "__main__":
    coder = HuffmanCoder()

    test_string = 'How to code this string with Huffman coding?'
    print(BitArray(test_string.encode(encoding='ISO8859-1')).bin)
    encoded = coder.encode(test_string)

    print()
    print('Encoded tree:')
    print(encoded[0].bin)

    print()
    print('Encoded data:')
    print(encoded[1].bin)

    print()
    print('Combined:')
    print((encoded[0]+ encoded[1]).bin)

    print()
    decoded_data = coder.decode(encoded[0], encoded[1])
    print()
    print(decoded_data)

    # test_string = 'How to code this string with Huffman coding?'

    # data = test_string.encode()
    # print(data)
    # for byte in data:
    #     print(byte, end=' ')
    # print('\n')

    # data2 = bytes(test_string, 'utf-8')
    # print(data2)
    # for byte in data2:
    #     print(byte, end=' ')
    # print('\n')



    # test_string = 'How to code this string with Huffman coding?'
    # print(test_string.encode())
    # result = coder.calculate_frequencies(test_string)
    # print(result)

    # keko = []
    # heappush(keko,5)
    # heappush(keko,3)
    # heappush(keko,8)
    # heappush(keko,7)
    # print(keko[0]) # 3
    # heappop(keko)
    # print(keko[0]) # 5
    # print(type(keko))
    # print(keko)

    # symbols_and_frequencies = {
    #     'H': 2,
    #     'o': 4,
    #     'w': 2,
    #     't': 4,
    #     'n': 3
    # }
    # print(symbols_and_frequencies)
    # print('')

    # # print(list(symbols_and_frequencies.values()))
    # # items = []
    # # for symbol, freq in symbols_and_frequencies.items():
    # #     items.append((freq, symbol))
    # # print(items)
    # # heapify(items)
    # # print(items)
    # # while items:
    # #     print(heappop(items))

    # tree_root = coder.create_huffman_tree(symbols_and_frequencies)
    # print(tree_root)
    # dictionary = coder.create_huffman_table(tree_root)
    # print(dictionary)

    # print()
    # # TiRa-kurssimonisteen esimerkki
    # # test_freqs = {
    # #     '1': 1,
    # #     '3': 3,
    # #     '5_1': 5,
    # #     '4': 4,
    # #     '5_2': 5,
    # #     '8_1': 8,
    # #     '9': 9,
    # #     '7': 7,
    # #     '8_2': 8,
    # #     '5_3': 5
    # # }
    # test_freqs = {
    #     'a': 1,
    #     'b': 3,
    #     'c': 5,
    #     'd': 4,
    #     'e': 5,
    #     'f': 8,
    #     'g': 9,
    #     'h': 7,
    #     'i': 8,
    #     'j': 5
    # }
    # tree_root = coder.create_huffman_tree(test_freqs)
    # print(tree_root)
    # dictionary = coder.create_huffman_table(tree_root)
    # print(dictionary)

    # print()
    # test_freqs = {
    #     'A': 6,
    #     'B': 1,
    #     'C': 6,
    #     'D': 2,
    #     'E': 5
    # }
    # tree_root = coder.create_huffman_tree(test_freqs)
    # print(tree_root)
    # dictionary = coder.create_huffman_table(tree_root)
    # print(dictionary)
