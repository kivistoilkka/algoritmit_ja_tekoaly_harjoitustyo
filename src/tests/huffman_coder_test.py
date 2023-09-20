import unittest
from huffman_coder import HuffmanCoder
from entities.huffmantree_node import HuffmanTreeNode


class TestHuffmanCoder(unittest.TestCase):
    def setUp(self):
        self.coder = HuffmanCoder()
        self.maxDiff = None

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

    def test_create_huffman_tree_returns_HuffmanTreeNode(self):
        symbols_and_weights = {
            'H': 2,
            'o': 4,
            'w': 2,
            ' ': 7,
            't': 4
        }
        result = self.coder.create_huffman_tree(symbols_and_weights)
        self.assertTrue(isinstance(result, HuffmanTreeNode))

    def test_create_huffman_tree_returns_root_node(self):
        symbols_and_weights = {
            'H': 2,
            'o': 4,
            'w': 2,
            ' ': 7,
            't': 4
        }

        result = self.coder.create_huffman_tree(symbols_and_weights)
        self.assertEqual(len(result.symbol), 5)

    def test_create_huffman_table_returns_correct_dictionary(self):
        symbols_and_weights = {
            'a': 5,
            'b': 9,
            'c': 12,
            'd': 13,
            'e': 16,
            'f': 45
        }
        expected = {
            'f': '0',
            'c': '100',
            'd': '101',
            'a': '1100',
            'b': '1101',
            'e': '111'
        }

        tree = self.coder.create_huffman_tree(symbols_and_weights)
        result = self.coder.create_huffman_table(tree)
        self.assertDictEqual(result, expected)

    def test_create_huffman_table_returns_correct_dictionary_by_code_lengths(self):
        symbols_and_weights = {
            'H': 2,
            'o': 4,
            'w': 2,
            't': 4,
            'n': 3
        }
        tree = self.coder.create_huffman_tree(symbols_and_weights)
        result = self.coder.create_huffman_table(tree)
        self.assertEqual(len(result['o']), 2)
        self.assertEqual(len(result['t']), 2)
        self.assertEqual(len(result['n']), 2)
        self.assertEqual(len(result['H']), 3)
        self.assertEqual(len(result['w']), 3)

    # def test_create_huffman_table_returns_correct_dictionary_3(self):
    #     symbols_and_weights = {
    #         'H': 2,
    #         'o': 4,
    #         'w': 2,
    #         't': 4,
    #         'n': 3
    #     }
    #     expected = {
    #         'n': '01',
    #         'o': '10',
    #         't': '11',
    #         'H': '000',
    #         'w': '001',
    #     }

    #     tree = self.coder.create_huffman_tree(symbols_and_weights)
    #     result = self.coder.create_huffman_table(tree)
    #     self.assertDictEqual(result, expected)

    # def test_create_huffman_table_returns_correct_dictionary_4(self):
    #     symbols_and_weights = {
    #         'H': 2,
    #         'o': 4,
    #         'w': 2,
    #         ' ': 7,
    #         't': 4,
    #         'c': 2,
    #         'd': 2,
    #         'e': 1,
    #         'h': 2,
    #         'i': 4,
    #         's': 2,
    #         'r': 1,
    #         'n': 3,
    #         'g': 2,
    #         'u': 1,
    #         'f': 2,
    #         'm': 1,
    #         'a': 1,
    #         '?': 1
    #     }
    #     expected = {
    #         ' ': '101',
    #         'o': '011',
    #         'i': '001',
    #         't': '000',
    #         'n': '1001',
    #         'h': '11111',
    #         'd': '11110',
    #         'g': '11101',
    #         's': '11100',
    #         'H': '11011',
    #         'c': '11001',
    #         'w': '11000',
    #         'f': '1000',
    #         'r': '110101',
    #         'e': '110100',
    #         'm': '01011',
    #         'u': '01010',
    #         '?': '01001',
    #         'a': '01000',
    #     }

    #     tree = self.coder.create_huffman_tree(symbols_and_weights)
    #     result = self.coder.create_huffman_table(tree)
    #     self.assertDictEqual(result, expected)

    def test_huffman_encode_data_creates_correct_string(self):
        data = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        table = {
            'f': '0',
            'c': '100',
            'd': '101',
            'a': '1100',
            'b': '1101',
            'e': '111'
        }
        expected = '11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000'

        result = self.coder.huffman_encode_data(data, table)
        self.assertEqual(result, expected)

    def test_encode_huffman_tree_creates_correct_string(self):
        symbols_and_weights = {
            'a': 5,
            'b': 9,
            'c': 12,
            'd': 13,
            'e': 16,
            'f': 45
        }
        expected = '01f001c1d001a1b1e'

        tree = self.coder.create_huffman_tree(symbols_and_weights)
        result = self.coder.encode_huffman_tree(tree)
        self.assertEqual(result, expected)

    def test_decode_huffman_tree_creates_correct_tree_that_creates_correct_table(self):
        encoded_tree = '01f001c1d001a1b1e'
        expected = {
            'f': '0',
            'c': '100',
            'd': '101',
            'a': '1100',
            'b': '1101',
            'e': '111'
        }

        tree = self.coder.decode_huffman_tree(encoded_tree)
        result = self.coder.create_huffman_table(tree)
        self.assertDictEqual(result, expected)

    def test_huffman_decode_returns_correct_string(self):
        encoded_data = '11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000'
        encoded_tree = '01f001c1d001a1b1e'
        expected = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'

        tree = self.coder.decode_huffman_tree(encoded_tree)
        result = self.coder.huffman_decode_data(encoded_data, tree)
        self.assertEqual(result, expected)

    def test_decode_returns_correct_string(self):
        encoded_data = '11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000'
        encoded_tree = '01f001c1d001a1b1e'
        expected = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'

        result = self.coder.decode(encoded_data, encoded_tree)
        self.assertEqual(result, expected)

    def test_encode_returns_correct_tuple_of_two_strings(self):
        test_string = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        expected_encoded_data = '11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000'
        expected_encoded_tree = '01f001c1d001a1b1e'

        result_data, result_tree = self.coder.encode(test_string)
        self.assertEqual(result_data, expected_encoded_data)
        self.assertEqual(result_tree, expected_encoded_tree)

    def test_encode_can_encode_and_then_decode_string(self):
        test_string = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        encoded_data, encoded_tree = self.coder.encode(test_string)

        decoded_data = self.coder.decode(encoded_data, encoded_tree)
        self.assertEqual(decoded_data, test_string)

    def test_encode_can_encode_and_then_decode_string2(self):
        test_string = 'How to code this string with Huffman coding?'
        encoded_data, encoded_tree = self.coder.encode(test_string)

        decoded_data = self.coder.decode(encoded_data, encoded_tree)
        self.assertEqual(decoded_data, test_string)
