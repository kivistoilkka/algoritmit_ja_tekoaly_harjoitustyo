import unittest

from bitstring import Bits

from utils.lzw_coder import LZWCoder

class TestLZWCoder(unittest.TestCase):
    def setUp(self):
        self.coder = LZWCoder()
        self.maxDiff

    def test_encode_returns_bytes(self):
        result = self.coder.encode('Hello world!')
        self.assertTrue(isinstance(result, bytes))

    def test_encode_returns_expected_bytes(self):
        test_string = 'Testing this test thing here'
        expected = Bits(bin='\
0000000001010100\
0000000001100101\
0000000001110011\
0000000001110100\
0000000001101001\
0000000001101110\
0000000001100111\
0000000000100000\
0000000001110100\
0000000001101000\
0000000001101001\
0000000001110011\
0000000100000111\
0000000100000001\
0000000001110100\
0000000100000111\
0000000100001001\
0000000100000101\
0000000000100000\
0000000001101000\
0000000001100101\
0000000001110010\
0000000001100101'
        ).bytes
        result = self.coder.encode(test_string)
        self.assertEqual(result, expected)

    def test_decode_returns_expected_string(self):
        test_bytes = Bits(bin='\
0000000001010100\
0000000001100101\
0000000001110011\
0000000001110100\
0000000001101001\
0000000001101110\
0000000001100111\
0000000000100000\
0000000001110100\
0000000001101000\
0000000001101001\
0000000001110011\
0000000100000111\
0000000100000001\
0000000001110100\
0000000100000111\
0000000100001001\
0000000100000101\
0000000000100000\
0000000001101000\
0000000001100101\
0000000001110010\
0000000001100101'
        ).bytes
        expected = 'Testing this test thing here'
        result = self.coder.decode(test_bytes)
        self.assertEqual(result, expected)

    def test_lzwcoder_can_encode_and_then_decode_longer_string(self):
        test_string = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\
'''
        encoded = self.coder.encode(test_string)
        decoded = self.coder.decode(encoded)
        self.assertEqual(decoded, test_string)
