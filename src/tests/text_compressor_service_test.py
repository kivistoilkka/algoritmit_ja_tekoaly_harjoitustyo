import unittest
from unittest.mock import Mock

from bitstring import Bits, BitArray, ConstBitStream

from services.text_compressor_service import TextCompressorService
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder
from utils.lzw_coder import LZWCoder


class TestTextCompressorService(unittest.TestCase):
    def setUp(self):
        self.io_mock = Mock(wraps=FileIO)
        self.huffman_coder_mock = Mock(wraps=HuffmanCoder)
        self.lzw_coder_mock = Mock(wraps=LZWCoder)
        self.service = TextCompressorService(
            self.io_mock, self.huffman_coder_mock, self.lzw_coder_mock)

    def test_encode_file_with_huffman_reads_file_and_encodes_data_and_saves_data_to_new_file(self):
        self.io_mock.read_text_file.return_value = 'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        self.io_mock.write_binary_file.return_value = True
        self.huffman_coder_mock.encode.return_value = (
            BitArray(bin='0101100110001011000111011001000010110000110110001010110010111001100110011001100110111011101110111011101110111011101100100100100100100100100100100100100101101101101101101101101101101101101101111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000')
        )
        expected_written = BitArray(bin='\
00000101\
01011001100010110001110110010000101100001101100010101100101\
11001100110011001100\
110111011101110111011101110111011101\
100100100100100100100100100100100100\
101101101101101101101101101101101101101\
111111111111111111111111111111111111111111111111\
000000000000000000000000000000000000000000000\
00000').bytes

        result = self.service.encode_file(
            './filename', './filename_encoded', 'huffman coding')

        self.assertTrue(result)
        self.io_mock.read_text_file.assert_called_with('./filename')
        self.huffman_coder_mock.encode.assert_called_with(
            'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        )
        self.io_mock.write_binary_file.assert_called_with(
            expected_written, './filename_encoded')

    def test_encode_file_will_raise_error_if_called_with_non_available_encoding_method(self):
        self.io_mock.read_text_file.return_value = '''aaaaabbbbbbbbbcccccccccccc\
dddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'''

        with self.assertRaisesRegex(type(ValueError()), 'Encoding type "imaginary" not available'):
            self.service.encode_file(
                './filename', './filename_encoded', 'imaginary')

    def test_decode_file_with_huffman_reads_file_and_decodes_data_and_saves_data_to_new_file(self):
        self.io_mock.read_binary_file.return_value = Bits(bin='\
00000101\
01011001100010110001110110010000101100001101100010101100101\
11001100110011001100\
110111011101110111011101110111011101\
100100100100100100100100100100100100\
101101101101101101101101101101101101101\
111111111111111111111111111111111111111111111111\
000000000000000000000000000000000000000000000\
00000').bytes
        self.io_mock.write_text_file.return_value = True
        self.huffman_coder_mock.decode.return_value = (
            'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        )
        expected_written = (
            'aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'
        )

        result = self.service.decode_file(
            './filename', './filename_decoded', 'huffman coding')

        self.assertTrue(result)
        self.io_mock.read_binary_file.assert_called_with('./filename')
        self.huffman_coder_mock.decode.assert_called_with(
            BitArray(bin='\
01011001100010110001110110010000101100001101100010101100101\
11001100110011001100\
110111011101110111011101110111011101\
100100100100100100100100100100100100\
101101101101101101101101101101101101101\
111111111111111111111111111111111111111111111111\
000000000000000000000000000000000000000000000\
')
        )
        self.io_mock.write_text_file.assert_called_with(
            expected_written, './filename_decoded')

    def test_decode_file_will_raise_error_if_called_with_non_available_encoding_method(self):
        with self.assertRaisesRegex(type(ValueError()), 'Encoding type "imaginary" not available'):
            self.service.decode_file(
                './filename', './filename_decoded', 'imaginary')
