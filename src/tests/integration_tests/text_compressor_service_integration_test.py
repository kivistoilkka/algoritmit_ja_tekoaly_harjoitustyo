import unittest
from pathlib import Path

import unittest
from unittest.mock import Mock

from services.text_compressor_service import TextCompressorService
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder


class TestTextCompressorService(unittest.TestCase):
    def setUp(self):
        self.io = FileIO()
        self.huffman_coder = HuffmanCoder()
        self.service = TextCompressorService(self.io, self.huffman_coder)

    def tearDown(self):
        test_text_files = [
            './src/tests/write_test_integration1.txt',
            './src/tests/write_test_integration2_encoded.txt',
            './src/tests/write_test_integration2_decoded.txt'
        ]
        for file in test_text_files:
            if Path(file).exists():
                Path(file).unlink()

    def test_encode_file_with_huffman_reads_file_encodes_data_and_saves_to_new_file(self):
        expected = '''01f001c1d001a1b1e
110011001100110011001101110111011101110111011101110111011001001001001001001001001001001001\
001011011011011011011011011011011011011011111111111111111111111111111111111111111111111110\
00000000000000000000000000000000000000000000'''

        result = self.service.encode_file(
            './src/tests/text_files/aabbccddeeff101_ISO8859-1.txt',
            './src/tests/write_test_integration1.txt',
            'huffman coding'
        )

        self.assertTrue(result)
        with open('./src/tests/write_test_integration1.txt', encoding="ISO8859-1") as written_file:
            written_data = written_file.read()
            self.assertEqual(written_data, expected)

        test_text_files = [
            './src/tests/write_test_integration1.txt',
            './src/tests/write_test_integration2.txt'
        ]
        for file in test_text_files:
            if Path(file).exists():
                Path(file).unlink()
