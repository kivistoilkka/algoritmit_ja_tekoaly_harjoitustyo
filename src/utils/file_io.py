class FileIO:
    """Class handling file reading and writing
    """

    def __init__(self) -> None:
        pass

    def read_file(self, filename: str) -> str:
        """Method for reading text files, assumes that files are saved using ISO8859-1 encoding.

        Args:
            filename (str): Path and name of the file

        Returns:
            str: Text data read from the file
        """

        try:
            with open(filename, encoding="ISO8859-1") as file:
                data = file.read()
                return data
        except OSError:
            return None

    def write_file(self, data: str, filename: str) -> bool:
        """Method for writing data to text file using ISO8859-1 encoding.

        Args:
            data (str): Text data to be saved
            filename (str): Path and name of the file to be written

        Returns:
            bool: True if writing is successful
        """
        try:
            with open(filename, "w", encoding="ISO8859-1") as file:
                file.write(data)
            return True
        except OSError:
            return False
