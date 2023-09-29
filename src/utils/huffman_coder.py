from collections import Counter
from heapq import heappush, heappop, heapify

from entities.huffmantree_node import HuffmanTreeNode


class HuffmanCoder:
    def __init__(self) -> None:
        pass

    def encode(self, input_string: str) -> tuple[str, str]:
        symbols_and_frequencies = self.calculate_frequencies(input_string)
        tree = self.create_huffman_tree(symbols_and_frequencies)
        table = self.create_huffman_table(tree)
        encoded_data = self.huffman_encode_data(input_string, table)
        encoded_tree = self.encode_huffman_tree(tree)
        return (encoded_data, encoded_tree)

    def decode(self, encoded_data: str, encoded_tree: str) -> str:
        tree = self.decode_huffman_tree(encoded_tree)
        return self.huffman_decode_data(encoded_data, tree)

    def calculate_frequencies(self, input_string: str) -> dict:
        output = Counter(input_string)
        return output

    def create_huffman_tree(self, symbols_and_frequencies: dict[str, int]) -> HuffmanTreeNode:
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

    def huffman_encode_data(self, data: str, table: dict) -> str:
        encoded_data = ''
        for i in range(0, len(data)):
            encoded_data = encoded_data + table[data[i]]
        return encoded_data

    def encode_huffman_tree(self, root_node: HuffmanTreeNode) -> str:
        encoded_tree = self.add_node_to_encoded_tree(root_node)
        return encoded_tree

    def add_node_to_encoded_tree(self, node: HuffmanTreeNode, encoded_tree: str = '') -> str:
        if node is None:
            return
        if node.is_leaf():
            return encoded_tree + '1' + node.symbol
        encoded_tree = encoded_tree + '0'
        encoded_tree = self.add_node_to_encoded_tree(
            node.left_child, encoded_tree)
        encoded_tree = self.add_node_to_encoded_tree(
            node.right_child, encoded_tree)
        return encoded_tree

    def decode_huffman_tree(self, encoded_tree: str) -> HuffmanTreeNode:
        huffman_tree_root_and_remaining_code = self.add_node_to_decoded_tree(
            encoded_tree)
        return huffman_tree_root_and_remaining_code[0]

    def add_node_to_decoded_tree(self, code: str):
        char = code[0]
        code = code[1:]
        if char == '1':
            char = code[0]
            code = code[1:]
            return (HuffmanTreeNode(1, char), code)
        left_child, code = self.add_node_to_decoded_tree(code)
        right_child, code = self.add_node_to_decoded_tree(code)
        return (HuffmanTreeNode(0, '#', left_child, right_child), code)

    def huffman_decode_data(self, encoded_data: str, tree: HuffmanTreeNode) -> str:
        decoded_data = ''
        i = 0
        node = tree
        for i in range(0, len(encoded_data)):
            if encoded_data[i] == '0' and node.left_child:
                node = node.left_child
            elif node.right_child:
                node = node.right_child
            if node.is_leaf():
                decoded_data = decoded_data + node.symbol
                node = tree
        return decoded_data


if __name__ == "__main__":
    coder = HuffmanCoder()
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

    symbols_and_frequencies = {
        'H': 2,
        'o': 4,
        'w': 2,
        't': 4,
        'n': 3
    }
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

    tree_root = coder.create_huffman_tree(symbols_and_frequencies)
    print(tree_root)
    dictionary = coder.create_huffman_table(tree_root)
    print(dictionary)

    print()
    # TiRa-kurssimonisteen esimerkki
    # test_freqs = {
    #     '1': 1,
    #     '3': 3,
    #     '5_1': 5,
    #     '4': 4,
    #     '5_2': 5,
    #     '8_1': 8,
    #     '9': 9,
    #     '7': 7,
    #     '8_2': 8,
    #     '5_3': 5
    # }
    test_freqs = {
        'a': 1,
        'b': 3,
        'c': 5,
        'd': 4,
        'e': 5,
        'f': 8,
        'g': 9,
        'h': 7,
        'i': 8,
        'j': 5
    }
    tree_root = coder.create_huffman_tree(test_freqs)
    print(tree_root)
    dictionary = coder.create_huffman_table(tree_root)
    print(dictionary)

    print()
    test_freqs = {
        'A': 6,
        'B': 1,
        'C': 6,
        'D': 2,
        'E': 5
    }
    tree_root = coder.create_huffman_tree(test_freqs)
    print(tree_root)
    dictionary = coder.create_huffman_table(tree_root)
    print(dictionary)
