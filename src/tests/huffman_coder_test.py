import unittest

from bitstring import Bits, BitArray, ConstBitStream

from config import ENCODING
from utils.huffman_coder import HuffmanCoder
from entities.huffmantree_node import HuffmanTreeNode


class TestHuffmanCoder(unittest.TestCase):
    def setUp(self):
        self.coder = HuffmanCoder()
        self.maxDiff = None

    def test_encode_returns_bitarray(self):
        result = self.coder.encode('Hello world')
        self.assertTrue(isinstance(result, BitArray))

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
            'f': Bits(bin='0'),
            'c': Bits(bin='100'),
            'd': Bits(bin='101'),
            'a': Bits(bin='1100'),
            'b': Bits(bin='1101'),
            'e': Bits(bin='111')
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

    def test_huffman_encode_data_creates_correct_binary(self):
        data = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeee\
fffffffffffffffffffffffffffffffffffffffffffff'
        table = {
            'f': Bits(bin='0'),
            'c': Bits(bin='100'),
            'd': Bits(bin='101'),
            'a': Bits(bin='1100'),
            'b': Bits(bin='1101'),
            'e': Bits(bin='111')
        }
        expected = Bits(bin='\
11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101\
10110110110110110110110110110110111111111111111111111111111111111111111111111111100000000000000000\
0000000000000000000000000000'
                        )

        result = self.coder.huffman_encode_data(data, table)
        self.assertEqual(result, expected)

    def test_encode_huffman_tree_creates_correct_bitarray(self):
        symbols_and_frequencies = {
            97: 5,
            98: 9,
            99: 12,
            100: 13,
            101: 16,
            102: 45
        }
        expected = BitArray(
            bin='01011001100010110001110110010000101100001101100010101100101')

        tree = self.coder.create_huffman_tree(symbols_and_frequencies)
        result = self.coder.encode_huffman_tree(tree)
        self.assertEqual(result, expected)

    def test_decode_huffman_tree_creates_correct_tree_that_creates_correct_table(self):
        encoded_tree = ConstBitStream(
            bin='01011001100010110001110110010000101100001101100010101100101'
        )
        expected = {
            b'f': Bits(bin='0'),
            b'c': Bits(bin='100'),
            b'd': Bits(bin='101'),
            b'a': Bits(bin='1100'),
            b'b': Bits(bin='1101'),
            b'e': Bits(bin='111')
        }

        tree = self.coder.decode_huffman_tree(encoded_tree)
        result = self.coder.create_huffman_table(tree)
        self.assertDictEqual(result, expected)

    def test_huffman_decode_returns_correct_string(self):
        encoded_data = ConstBitStream(bin='\
11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101\
10110110110110110110110110110110111111111111111111111111111111111111111111111111100000000000000000\
0000000000000000000000000000'
                                      )
        encoded_tree = ConstBitStream(
            bin='01011001100010110001110110010000101100001101100010101100101'
        )
        expected = b'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeee\
fffffffffffffffffffffffffffffffffffffffffffff'

        tree = self.coder.decode_huffman_tree(encoded_tree)
        result = self.coder.huffman_decode_data(encoded_data, tree)
        self.assertEqual(result, expected)

    def test_decode_returns_correct_string(self):
        encoded_data = Bits(bin='\
01011001100010110001110110010000101100001101100010101100101110011001100110011001101110111011101110\
11101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111\
111111111111111111111111111111111111111111000000000000000000000000000000000000000000000'
                            )
        expected = b'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeee\
fffffffffffffffffffffffffffffffffffffffffffff'

        result = self.coder.decode(encoded_data)
        self.assertEqual(result, expected)

    def test_encode_returns_correct_bitarray(self):
        test_string = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeee\
fffffffffffffffffffffffffffffffffffffffffffff'
        expected_result = BitArray(bin='\
01011001100010110001110110010000101100001101100010101100101110011001100110011001101110111011101110\
11101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111\
111111111111111111111111111111111111111111000000000000000000000000000000000000000000000'
                                   )

        result = self.coder.encode(test_string)
        self.assertEqual(result, expected_result)

    def test_encode_can_encode_and_then_decode_string(self):
        test_string = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeee\
fffffffffffffffffffffffffffffffffffffffffffff'
        encoded = self.coder.encode(test_string)

        decoded_data = self.coder.decode(encoded)
        self.assertEqual(decoded_data, test_string.encode(encoding=ENCODING))

    def test_class_can_encode_and_then_decode_string2(self):
        test_string = 'How to code this string with Huffman coding?'
        encoded = self.coder.encode(test_string)

        decoded_data = self.coder.decode(encoded)
        self.assertEqual(decoded_data, test_string.encode(encoding=ENCODING))
