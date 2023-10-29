import unittest
from pathlib import Path

from bitstring import Bits

from services.text_compressor_service import TextCompressorService
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder
from utils.lzw_coder import LZWCoder


class TestTextCompressorService(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.io = FileIO()
        self.huffman_coder = HuffmanCoder()
        self.lzw_coder = LZWCoder()
        self.service = TextCompressorService(
            self.io, self.huffman_coder, self.lzw_coder)

    def tearDown(self):
        test_text_files = [
            './src/tests/write_test_integration1.txt'
            , './src/tests/write_test_integration2_encoded.txt'
            , './src/tests/write_test_integration2_decoded.txt'
            , './src/tests/write_test_integration3_encoded.txt'
            , './src/tests/write_test_integration3_decoded.txt'
            , './src/tests/write_test_integration4.txt'
            , './src/tests/write_test_integration5_encoded.txt'
            , './src/tests/write_test_integration5_decoded.txt'
            , './src/tests/write_test_integration6_encoded.txt'
            , './src/tests/write_test_integration6_decoded.txt'
            , './src/tests/write_test_integration7_encoded.txt'
            , './src/tests/write_test_integration7_decoded.txt'
            , './src/tests/write_test_integration8_encoded.txt'
            , './src/tests/write_test_integration8_decoded.txt'
            , './src/tests/write_test_integration9_encoded.txt'
            , './src/tests/write_test_integration9_decoded.txt'
            , './src/tests/write_test_integration10_encoded.txt'
            , './src/tests/write_test_integration10_decoded.txt'
            , './src/tests/write_test_integration11_encoded.txt'
            , './src/tests/write_test_integration11_decoded.txt'
            , './src/tests/write_test_integration12_encoded.txt'
            , './src/tests/write_test_integration12_decoded.txt'
            , './src/tests/write_test_integration13_encoded.txt'
            , './src/tests/write_test_integration13_decoded.txt'
            , './src/tests/write_test_integration14_encoded.txt'
            , './src/tests/write_test_integration14_decoded.txt'
            , './src/tests/write_test_integration15_encoded.txt'
            , './src/tests/write_test_integration15_decoded.txt'
            , './src/tests/write_test_integration16_encoded.txt'
            , './src/tests/write_test_integration16_decoded.txt'
            , './src/tests/write_test_integration17_encoded.txt'
            , './src/tests/write_test_integration17_decoded.txt'
            , './src/tests/write_test_integration18_encoded.txt'
            , './src/tests/write_test_integration18_decoded.txt'
            , './src/tests/write_test_integration19_encoded.txt'
            , './src/tests/write_test_integration19_decoded.txt'
            , './src/tests/write_test_integration20_encoded.txt'
            , './src/tests/write_test_integration20_decoded.txt'
            , './src/tests/write_test_integration21_encoded.txt'
            , './src/tests/write_test_integration21_decoded.txt'
        ]
        for file in test_text_files:
            if Path(file).exists():
                Path(file).unlink()

    def test_encode_file_with_huffman_reads_file_encodes_data_and_saves_to_new_file(self):
        expected = Bits(bin='\
00000101\
01011001100010110001110110010000101100001101100010101100101\
11001100110011001100\
110111011101110111011101110111011101\
100100100100100100100100100100100100\
101101101101101101101101101101101101101\
111111111111111111111111111111111111111111111111\
000000000000000000000000000000000000000000000\
00000').bin

        result = self.service.encode_file(
            './src/tests/text_files/aabbccddeeff100_Windows-1252.txt',
            './src/tests/write_test_integration1.txt',
            'huffman coding'
        )

        self.assertTrue(result)
        with open('./src/tests/write_test_integration1.txt', mode='rb') as written_file:
            written_data = written_file.read()
            written_bits = Bits(written_data).bin
            self.assertEqual(written_bits, expected)

    def test_read_text_file_is_encoded_and_decoded_using_huffman_coding_and_then_saved_to_new_file_using_huffman_coding(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/loremipsum445_Windows-1252.txt',
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
        with open('./src/tests/text_files/loremipsum445_Windows-1252.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration2_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_read_multiple_row_text_file_is_encoded_and_decoded_using_huffman_coding_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/loremipsum445_3rows_Windows-1252.txt',
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
        with open('./src/tests/text_files/loremipsum445_3rows_Windows-1252.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration3_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_encode_file_with_lzw_reads_file_encodes_data_and_saves_to_new_file(self):
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
0000000100001000\
0000000100000010\
0000000001110100\
0000000100001000\
0000000100001010\
0000000100000110\
0000000000100000\
0000000001101000\
0000000001100101\
0000000001110010\
0000000001100101'
                        ).bin

        result = self.service.encode_file(
            './src/tests/text_files/testingthistest28_Windows-1252.txt',
            './src/tests/write_test_integration4.txt',
            'lzw'
        )

        self.assertTrue(result)
        with open('./src/tests/write_test_integration4.txt', mode='rb') as written_file:
            written_data = written_file.read()
            written_bits = Bits(written_data).bin
            self.assertEqual(written_bits, expected)

    def test_read_text_file_is_encoded_and_decoded_using_lzw_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/loremipsum445_Windows-1252.txt',
            './src/tests/write_test_integration5_encoded.txt',
            'lzw'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration5_encoded.txt',
            './src/tests/write_test_integration5_decoded.txt',
            'lzw'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/loremipsum445_Windows-1252.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration5_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_read_multiple_row_text_file_is_encoded_and_decoded_using_lzw_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/loremipsum445_3rows_Windows-1252.txt',
            './src/tests/write_test_integration6_encoded.txt',
            'lzw'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration6_encoded.txt',
            './src/tests/write_test_integration6_decoded.txt',
            'lzw'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/loremipsum445_3rows_Windows-1252.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration6_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_large_text_file_is_encoded_and_decoded_using_huffman_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/pg84_frankenstein_UTF8.txt',
            './src/tests/write_test_integration7_encoded.txt',
            'huffman coding'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration7_encoded.txt',
            './src/tests/write_test_integration7_decoded.txt',
            'huffman coding'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/pg84_frankenstein_UTF8.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration7_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_large_text_file_is_encoded_and_decoded_using_lzw_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/pg84_frankenstein_UTF8.txt',
            './src/tests/write_test_integration8_encoded.txt',
            'lzw'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration8_encoded.txt',
            './src/tests/write_test_integration8_decoded.txt',
            'lzw'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/pg84_frankenstein_UTF8.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration8_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_large_file_is_encoded_and_decoded_using_both_algorithms_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/pg84_frankenstein_UTF8.txt',
            './src/tests/write_test_integration9_encoded.txt',
            'both'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration9_encoded.txt',
            './src/tests/write_test_integration9_decoded.txt',
            'both'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/pg84_frankenstein_UTF8.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration9_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_two_same_letter_text_file_is_encoded_and_decoded_using_huffman_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/aa.txt',
            './src/tests/write_test_integration10_encoded.txt',
            'huffman coding'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration10_encoded.txt',
            './src/tests/write_test_integration10_decoded.txt',
            'huffman coding'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/aa.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration10_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_two_same_letter_text_file_is_encoded_and_decoded_using_lzw_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/aa.txt',
            './src/tests/write_test_integration11_encoded.txt',
            'lzw'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration11_encoded.txt',
            './src/tests/write_test_integration11_decoded.txt',
            'lzw'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/aa.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration11_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_two_same_letter_file_is_encoded_and_decoded_using_both_algorithms_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/aa.txt',
            './src/tests/write_test_integration12_encoded.txt',
            'both'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration12_encoded.txt',
            './src/tests/write_test_integration12_decoded.txt',
            'both'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/aa.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration12_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_two_different_letter_text_file_is_encoded_and_decoded_using_huffman_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/ab.txt',
            './src/tests/write_test_integration13_encoded.txt',
            'huffman coding'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration13_encoded.txt',
            './src/tests/write_test_integration13_decoded.txt',
            'huffman coding'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/ab.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration13_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_two_different_letter_text_file_is_encoded_and_decoded_using_lzw_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/ab.txt',
            './src/tests/write_test_integration14_encoded.txt',
            'lzw'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration14_encoded.txt',
            './src/tests/write_test_integration14_decoded.txt',
            'lzw'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/ab.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration14_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_two_different_letter_file_is_encoded_and_decoded_using_both_algorithms_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/ab.txt',
            './src/tests/write_test_integration15_encoded.txt',
            'both'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration15_encoded.txt',
            './src/tests/write_test_integration15_decoded.txt',
            'both'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/ab.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration15_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_one_letter_text_file_is_encoded_and_decoded_using_huffman_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/a.txt',
            './src/tests/write_test_integration16_encoded.txt',
            'huffman coding'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration16_encoded.txt',
            './src/tests/write_test_integration16_decoded.txt',
            'huffman coding'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/a.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration16_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_one_letter_text_file_is_encoded_and_decoded_using_lzw_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/a.txt',
            './src/tests/write_test_integration17_encoded.txt',
            'lzw'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration17_encoded.txt',
            './src/tests/write_test_integration17_decoded.txt',
            'lzw'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/a.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration17_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_one_letter_file_is_encoded_and_decoded_using_both_algorithms_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/a.txt',
            './src/tests/write_test_integration18_encoded.txt',
            'both'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration18_encoded.txt',
            './src/tests/write_test_integration18_decoded.txt',
            'both'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/a.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration18_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_empty_text_file_is_encoded_and_decoded_using_huffman_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/empty_file.txt',
            './src/tests/write_test_integration19_encoded.txt',
            'huffman coding'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration19_encoded.txt',
            './src/tests/write_test_integration19_decoded.txt',
            'huffman coding'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/empty_file.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration19_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_empty_text_file_is_encoded_and_decoded_using_lzw_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/empty_file.txt',
            './src/tests/write_test_integration20_encoded.txt',
            'lzw'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration20_encoded.txt',
            './src/tests/write_test_integration20_decoded.txt',
            'lzw'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/empty_file.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration20_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)

    def test_empty_file_is_encoded_and_decoded_using_both_algorithms_and_then_saved_to_new_file(self):
        result_encode = self.service.encode_file(
            './src/tests/text_files/empty_file.txt',
            './src/tests/write_test_integration21_encoded.txt',
            'both'
        )
        result_decode = self.service.decode_file(
            './src/tests/write_test_integration21_encoded.txt',
            './src/tests/write_test_integration21_decoded.txt',
            'both'
        )
        self.assertTrue(result_encode)
        self.assertTrue(result_decode)
        with open('./src/tests/text_files/empty_file.txt', mode='rb') as original_file:
            with open('./src/tests/write_test_integration21_decoded.txt', mode='rb') as written_file:
                original_text = original_file.read()
                decoded_text = written_file.read()
                self.assertEqual(decoded_text, original_text)
