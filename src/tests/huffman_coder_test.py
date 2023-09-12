import unittest
from huffman_coder import HuffmanCoder


class TestHuffmanCoder(unittest.TestCase):
    def setUp(self):
        self.coder = HuffmanCoder()

    def test_encode_returns_tuple_of_string_and_string(self):
        result = self.coder.encode('Hello world')
        self.assertTrue(isinstance(result, tuple))
        self.assertTrue(len(result) == 2)
        self.assertTrue(isinstance(result[0], str))
        self.assertTrue(isinstance(result[1], str))

    def test_calculate_frequencies_returns_dictionary(self):
        result = self.coder.calculate_frequencies(
            'How to code this string with Huffman coding?')
        self.assertTrue(isinstance(result, dict))

    def test_calculate_frequencies_returns_symbols_with_frequencies(self):
        result = self.coder.calculate_frequencies(
            'How to code this string with Huffman coding?')
        expected = {
            'H': 2,
            'o': 4,
            'w': 2,
            ' ': 7,
            't': 4,
            'c': 2,
            'd': 2,
            'e': 1,
            'h': 2,
            'i': 4,
            's': 2,
            'r': 1,
            'n': 3,
            'g': 2,
            'u': 1,
            'f': 2,
            'm': 1,
            'a': 1,
            '?': 1
        }

        self.assertEqual(result, expected)

    def test_create_huffman_tree_returns_list(self):
        symbols_and_weights = {
            'H': 2,
            'o': 4,
            'w': 2,
            ' ': 7,
            't': 4
        }
        result = self.coder.create_huffman_tree(symbols_and_weights)
        self.assertTrue(isinstance(result, list))
