class FileIO:
    def __init__(self) -> None:
        pass

    def read_file(self, filename: str):
        try:
            with open(filename, encoding="ISO8859-1") as file:
                data = file.read()
                return data
        except OSError:
            return None
