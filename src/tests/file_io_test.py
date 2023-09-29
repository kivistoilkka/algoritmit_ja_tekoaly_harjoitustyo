import unittest
from pathlib import Path

from utils.file_io import FileIO


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.io = FileIO()

    def tearDown(self):
        test_text_files = [
            './src/tests/write_test1.txt',
            './src/tests/write_test2.txt'
        ]
        for file in test_text_files:
            if Path(file).exists():
                Path(file).unlink()

    def test_ASCII_text_file_is_read(self):
        expected = '''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Ut enim \
ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat. Duis \
aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.'''

        text = self.io.read_file(
            './src/tests/text_files/loremipsum446_ISO8859-1.txt')
        self.assertEqual(text, expected)

    def test_string_data_can_be_saved_to_file(self):
        data = '''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Ut enim \
ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat. Duis \
aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.'''

        result = self.io.write_file(data, './src/tests/write_test1.txt')
        self.assertTrue(result)
        with open('./src/tests/write_test1.txt', encoding="ISO8859-1") as file:
            result_text = file.read()
            self.assertEqual(result_text, data)

    def test_ASCII_text_file_with_multiple_rows_is_read(self):
        expected = '''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.'''

        text = self.io.read_file(
            './src/tests/text_files/loremipsum446_3rows_ISO8859-1.txt'
        )
        self.assertEqual(text, expected)

    def test_string_data_with_two_line_breaks_can_be_saved_to_file(self):
        data = '''Lorem ipsum dolor sit amet, \
consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco \
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur \
sint occaecat cupidatat non proident, sunt in culpa \
qui officia deserunt mollit anim id est laborum.'''

        result = self.io.write_file(data, './src/tests/write_test2.txt')
        self.assertTrue(result)
        with open('./src/tests/write_test2.txt', encoding="ISO8859-1") as file:
            result_text = file.read()
            self.assertEqual(result_text, data)
