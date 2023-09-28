from collections import Counter
from heapq import heappush, heappop, heapify

from entities.huffmantree_node import HuffmanTreeNode


class HuffmanCoder:
    """Class handling Huffman coding
    """

    def __init__(self) -> None:
        pass

    def encode(self, input: bytes) -> tuple[bytes, bytes]:
        """Method for encoding input bytes with Huffman coding

        Args:
            input_string (bytes): Text to be encoded as bytes

        Returns:
            tuple[bytes, bytes]: Tuple where first value is encoded data and second is encoded Huffman tree
        """

        symbols_and_frequencies = self.calculate_frequencies(input)
        tree = self.create_huffman_tree(symbols_and_frequencies)
        table = self.create_huffman_table(tree)
        print(table)
        encoded_data = self.huffman_encode_data(input, table)
        encoded_tree = self.encode_huffman_tree(tree)
        return (encoded_data, encoded_tree)

    def decode(self, encoded_data: bytes, encoded_tree: bytes) -> bytes:
        """Method for decoding Huffman coded data using given encoded Huffman tree

        Args:
            encoded_data (bytes): Data to be encoded
            encoded_tree (bytes): Encoded Huffman tree that was used for encoding of data

        Returns:
            str: Decoded text in bytes
        """

        tree = self.decode_huffman_tree(encoded_tree)
        print()
        return self.huffman_decode_data(encoded_data, tree)

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
            table[node.symbol] = code
            return
        self.add_node_to_table(node.left_child, table, code + '0')
        self.add_node_to_table(node.right_child, table, code + '1')

    def huffman_encode_data(self, data: bytes, table: dict) -> bytes:
        encoded_data = b''
        for symbol in data:
            encoded_symbol = int(table[symbol], 2).to_bytes(1, byteorder='big', signed=False) #TODO: Word size is now magic number (1)
            encoded_data = encoded_data + encoded_symbol
        return encoded_data

    def encode_huffman_tree(self, root_node: HuffmanTreeNode) -> bytes:
        encoded_tree = self.add_node_to_encoded_tree(root_node)
        print('encoded tree: ', end='')
        print(encoded_tree)
        return bin(int(encoded_tree, 2))

    def add_node_to_encoded_tree(self, node: HuffmanTreeNode, encoded_tree: str = '') -> str:
        if node is None:
            return
        if node.is_leaf():
            return encoded_tree + '1'
        encoded_tree = encoded_tree + '0'
        encoded_tree = self.add_node_to_encoded_tree(
            node.left_child, encoded_tree)
        encoded_tree = self.add_node_to_encoded_tree(
            node.right_child, encoded_tree)
        return encoded_tree

    def decode_huffman_tree(self, encoded_tree: bytes) -> HuffmanTreeNode:
        print('Tree to decode:')
        print(encoded_tree)
        print()
        huffman_tree_root_and_remaining_code = self.add_node_to_decoded_tree(
            encoded_tree[2:])
        return huffman_tree_root_and_remaining_code[0]

    def add_node_to_decoded_tree(self, code: bytes):
        print(code)
        byte = code[0]
        #code = code[1:]
        if byte == '1':
            print('adding')
            char = code[0:8]
            code = code[1:]
            return (HuffmanTreeNode(1, int(char, 2).to_bytes(1, byteorder='big', signed=False)), code) #TODO: Word size is now magic number (1)
        print('going left')
        left_child, code = self.add_node_to_decoded_tree(code)
        print('going right')
        right_child, code = self.add_node_to_decoded_tree(code)
        return (HuffmanTreeNode(0, '#', left_child, right_child), code)

    def huffman_decode_data(self, encoded_data: bytes, tree: HuffmanTreeNode) -> bytes:
        decoded_data = b''
        i = 0
        node = tree
        for i in range(0, len(encoded_data)):
            print('next byte:', end='')
            print(encoded_data[i])
            if encoded_data[i] == 0 and node.left_child:
                node = node.left_child
            elif node.right_child:
                node = node.right_child
            if node.is_leaf():
                print('symbol:', end='')
                print(node.symbol)
                decoded_data = decoded_data + bytes(node.symbol)
                node = tree
        return decoded_data


if __name__ == "__main__":
    coder = HuffmanCoder()

    test_string = 'How to code this string with Huffman coding?'
    data = test_string.encode()
    encoded = coder.encode(data)
    print('Encoded data:')
    for byte in encoded[0]:
        print(format(byte, 'b'), end=' ')
    print('\n')

    print('Encoded tree:')
    for byte in encoded[1]:
        print(byte, end='')
    print('\n')

    decoded_data = coder.decode(encoded[0], encoded[1])
    print()
    print(decoded_data)

    int('0',2)

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
