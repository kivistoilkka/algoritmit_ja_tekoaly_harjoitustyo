import unittest
from huffman_coder import HuffmanCoder

class TestHuffmanCoder(unittest.TestCase):
    def setUp(self):
        self.coder = HuffmanCoder()

    def test_encode_returns_string(self):
        result = self.coder.encode('Hello world')
        self.assertTrue(isinstance(result, str))

    def test_calculate_frequencies_returns_dictionary(self):
        result = self.coder.calculate_frequencies('How to code this string with Huffman coding?')
        self.assertTrue(isinstance(result, dict))

    def test_calculate_frequencies_returns_symbols_with_frequencies(self):
        result = self.coder.calculate_frequencies('How to code this string with Huffman coding?')
        expected = {
            'H': 2/44,
            'o': 4/44,
            'w': 2/44,
            ' ': 7/44,
            't': 4/44,
            'c': 2/44,
            'd': 2/44,
            'e': 1/44,
            'h': 2/44,
            'i': 4/44,
            's': 2/44,
            'r': 1/44,
            'n': 3/44,
            'g': 2/44,
            'u': 1/44,
            'f': 2/44,
            'm': 1/44,
            'a': 1/44,
            '?': 1/44
        }

        self.assertEqual(result, expected)
