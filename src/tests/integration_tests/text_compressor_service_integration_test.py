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
            './src/tests/write_test_integration2_decoded.txt',
            # './src/tests/write_test_integration3_encoded.txt',
            # './src/tests/write_test_integration3_decoded.txt'
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

    def test_read_text_file_is_encoded_and_decoded_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/loremipsum446_ISO8859-1.txt',
            './src/tests/write_test_integration2_encoded.txt',
            'huffman coding'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration2_encoded.txt',
            './src/tests/write_test_integration2_decoded.txt',
            'huffman coding'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/loremipsum446_ISO8859-1.txt', encoding="ISO8859-1") as original_file:
            with open('./src/tests/write_test_integration2_decoded.txt', encoding="ISO8859-1") as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_read_multiple_row_text_file_is_encoded_and_decoded_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/loremipsum446_3rows_ISO8859-1.txt',
            './src/tests/write_test_integration3_encoded.txt',
            'huffman coding'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration3_encoded.txt',
            './src/tests/write_test_integration3_decoded.txt',
            'huffman coding'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/loremipsum446_3rows_ISO8859-1.txt', encoding="ISO8859-1") as original_file:
            with open('./src/tests/write_test_integration3_decoded.txt', encoding="ISO8859-1") as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)