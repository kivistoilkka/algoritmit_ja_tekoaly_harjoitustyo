from collections import Counter
from heapq import heappush, heappop

from entities.huffmantree_node import HuffmanTreeNode


class HuffmanCoder:
    def __init__(self) -> None:
        pass

    def encode(self, input_string: str) -> str:
        return (input_string, input_string)

    def calculate_frequencies(self, input_string: str) -> dict:
        output = Counter(input_string)
        return output

    def create_huffman_tree(self, symbols_and_frequencies: dict[str, int]) -> HuffmanTreeNode:
        nodes = []
        for symbol, freq in symbols_and_frequencies.items():
            heappush(nodes, HuffmanTreeNode(freq, symbol))

        while len(nodes) > 1:
            left = heappop(nodes)
            right = heappop(nodes)
            left.huffman_code = 0
            right.huffman_code = 1

            new_node = HuffmanTreeNode(
                left.frequency+right.frequency,
                left.symbol+right.symbol,
                left,
                right
            )
            heappush(nodes, new_node)

        return nodes[0]

    def create_huffman_code_dictionary(self, root_node: HuffmanTreeNode):
        huffman_code_dictionary = {}
        self.add_node_to_dictionary(root_node, huffman_code_dictionary)
        return huffman_code_dictionary

    def add_node_to_dictionary(self, node: HuffmanTreeNode, dictionary: dict, val=''):
        new_val = val + str(node.huffman_code)
        if node.left_child:
            self.add_node_to_dictionary(node.left_child, dictionary, new_val)
        if node.right_child:
            self.add_node_to_dictionary(node.right_child, dictionary, new_val)
        if not node.left_child and not node.right_child:
            dictionary[node.symbol] = new_val


if __name__ == "__main__":
    # coder = HuffmanCoder()
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
    #     ' ': 7,
    #     't': 4
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

    # coder = HuffmanCoder()
    # tree_root = coder.create_huffman_tree(symbols_and_frequencies)
    # print(tree_root)
    # dictionary = coder.create_huffman_code_dictionary(tree_root)
    # print(dictionary)

    pass
