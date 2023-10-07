import unittest
from pathlib import Path

from bitstring import Bits, BitArray

from utils.file_io import FileIO


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.io = FileIO()

    def tearDown(self):
        test_text_files = [
            './src/tests/write_test1.txt'
            ,'./src/tests/write_test2.txt'
            ,'./src/tests/write_test3.txt'
            ,'./src/tests/write_test4.txt'
            ,'./src/tests/read_test1.txt'
        ]
        for file in test_text_files:
            if Path(file).exists():
                Path(file).unlink()

    def test_ASCII_text_file_is_read_to_bytes(self):
        expected = bytes('''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Ut enim \
ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat. Duis \
aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.''', encoding='ISO8859-1')

        text = self.io.read_text_file(
            './src/tests/text_files/loremipsum446_ISO8859-1.txt')
        self.assertEqual(text, expected)

    def test_bytes_data_can_be_saved_to_text_file(self):
        data = bytes('''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Ut enim \
ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat. Duis \
aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.''', encoding='ISO8859-1')
        expected = '''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Ut enim \
ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat. Duis \
aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.'''

        result = self.io.write_text_file(data, './src/tests/write_test1.txt')
        self.assertTrue(result)
        with open('./src/tests/write_test1.txt', encoding='ISO8859-1') as file:
            result_text = file.read()
            self.assertEqual(result_text, expected)

    def test_ASCII_text_file_with_multiple_rows_is_read_to_bytes(self):
        expected = bytes('''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.''', encoding='ISO8859-1')

        text = self.io.read_text_file(
            './src/tests/text_files/loremipsum446_3rows_ISO8859-1.txt'
        )
        self.assertEqual(text, expected)

    def test_bytes_data_with_two_line_breaks_can_be_saved_to_text_file(self):
        data = bytes('''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.''', encoding='ISO8859-1')
        expected = '''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.'''

        result = self.io.write_text_file(data, './src/tests/write_test2.txt')
        self.assertTrue(result)
        with open('./src/tests/write_test2.txt', encoding='ISO8859-1') as file:
            result_text = file.read()
            self.assertEqual(result_text, expected)

    def test_bitarray_data_can_be_saved_to_binary_file(self):
        data = BitArray(
            bytes('Lorem ipsum', encoding='ISO8859-1')
        )
        expected = Bits('0x4C6F72656D20697073756D')

        result = self.io.write_binary_file(data, './src/tests/write_test3.txt')
        self.assertTrue(result)
        with open('./src/tests/write_test3.txt', mode='rb') as file:
            result_binary = file.read()
            self.assertEqual(result_binary, expected)

    def test_bitarray_data_can_be_saved_to_binary_file_when_not_complete_bytes(self):
        data = BitArray(bin='0110 1010 111')
        expected = Bits('0x6AE0')

        result = self.io.write_binary_file(data, './src/tests/write_test4.txt')
        self.assertTrue(result)
        with open('./src/tests/write_test4.txt', mode='rb') as file:
            result_binary = file.read()
            self.assertEqual(result_binary, expected)

    def test_binary_file_is_read_to_bytes(self):
        data = Bits('0x4C6F72656D20697073756D')
        with open('./src/tests/read_test1.txt', mode='wb') as file:
            data.tofile(file)
        expected = bytes('Lorem ipsum', encoding='ISO8859-1')

        result = self.io.read_binary_file(
            './src/tests/read_test1.txt')
        self.assertEqual(result, expected)
