from bitstring import BitArray

class FileIO:
    """Class handling file reading and writing
    """

    def __init__(self) -> None:
        pass

    def read_text_file(self, filename: str) -> str:
        """Method for reading text files, assumes that files are saved using ISO8859-1 encoding.

        Args:
            filename (str): Path and name of the file

        Returns:
            str: Text data read from the file
        """

        try:
            with open(filename, encoding='ISO8859-1') as file:
                data = file.read()
                return data
        except OSError:
            return None

    def write_text_file(self, data: str, filename: str) -> bool:
        """Method for writing data to text file using ISO8859-1 encoding.

        Args:
            data (str): Text data to be saved
            filename (str): Path and name of the file to be written

        Returns:
            bool: True if writing is successful
        """
        try:
            with open(filename, 'w', encoding='ISO8859-1') as file:
                file.write(data)
            return True
        except OSError:
            return False

    def read_binary_file(self, filename: str) -> bytes:
        """Method for reading binary files.

        Args:
            filename (str): Path and name of the file

        Returns:
            bytes: Binary data read from the file
        """

        try:
            with open(filename, 'rb') as file:
                data = file.read()
                return data
        except OSError:
            return None

    def write_binary_file(self, data: bytes, filename: str) -> bool:
        """Method for writing bytes data to binary file, filling with 0 bits at the end to complete bytes.

        Args:
            data (bytes): Binary data to be saved
            filename (str): Path and name of the file to be written

        Returns:
            bool: True if writing is successful
        """
        try:
            with open(filename, 'wb') as file:
                file.write(data)
            return True
        except OSError:
            return False
