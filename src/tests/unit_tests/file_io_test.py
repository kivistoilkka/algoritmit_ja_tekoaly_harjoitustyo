import unittest
from pathlib import Path

from bitstring import Bits

from utils.file_io import FileIO


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.io = FileIO()

    def tearDown(self):
        test_text_files = [
            './src/tests/write_test1.txt', './src/tests/write_test2.txt', './src/tests/write_test3.txt', './src/tests/write_test4.txt', './src/tests/read_test1.txt'
        ]
        for file in test_text_files:
            if Path(file).exists():
                Path(file).unlink()

    def test_bytes_data_can_be_saved_to_binary_file(self):
        data = b'Lorem ipsum'
        expected = Bits('0x4C6F72656D20697073756D')

        result = self.io.write_binary_file(data, './src/tests/write_test3.txt')
        self.assertTrue(result)
        with open('./src/tests/write_test3.txt', mode='rb') as file:
            result_binary = file.read()
            self.assertEqual(result_binary, expected)

    def test_binary_file_is_read_to_bytes(self):
        data = Bits('0x4C6F72656D20697073756D')
        with open('./src/tests/read_test1.txt', mode='wb') as file:
            data.tofile(file)
        expected = b'Lorem ipsum'

        result = self.io.read_binary_file(
            './src/tests/read_test1.txt')
        self.assertEqual(result, expected)
