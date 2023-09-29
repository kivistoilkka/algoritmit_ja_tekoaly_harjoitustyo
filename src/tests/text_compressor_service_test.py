import unittest
from unittest.mock import Mock

from services.text_compressor_service import TextCompressorService
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder


class TestTextCompressorService(unittest.TestCase):
    def setUp(self):
        self.io_mock = Mock(wraps=FileIO)
        self.huffman_coder_mock = Mock(wraps=HuffmanCoder)
        self.service = TextCompressorService(
            self.io_mock, self.huffman_coder_mock)

    def test_encode_file_with_huffman_reads_file_and_encodes_data_and_saves_data_to_new_file(self):
        self.io_mock.read_file.return_value = '''aaaaabbbbbbbbbcccccccccccc\
dddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'''
        self.io_mock.write_file.return_value = True
        self.huffman_coder_mock.encode.return_value = (
            '11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000',
            '01f001c1d001a1b1e'
        )
        expected_written = '''01f001c1d001a1b1e
11001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000'''

        self.service.encode_file(
            './filename', './filename_encoded', 'huffman coding')

        self.io_mock.read_file.assert_called_with('./filename')
        self.huffman_coder_mock.encode.assert_called_with(
            'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        )
        self.io_mock.write_file.assert_called_with(
            expected_written, './filename_encoded')

    def test_encode_file_will_raise_error_if_called_with_non_available_encoding_method(self):
        self.io_mock.read_file.return_value = '''aaaaabbbbbbbbbcccccccccccc\
dddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'''

        with self.assertRaisesRegex(type(ValueError()), 'Encoding type "imaginary" not available'):
            self.service.encode_file(
                './filename', './filename_encoded', 'imaginary')
