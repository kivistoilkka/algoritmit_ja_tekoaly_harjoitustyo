import unittest

from utils.lzw_coder import LZWCoder

class TestLZWCoder(unittest.TestCase):
    def setUp(self):
        self.coder = LZWCoder()
        self.maxDiff

    def test_encode_returns_list(self):
        result = self.coder.encode('Hello world!')
        self.assertTrue(isinstance(result, list))
