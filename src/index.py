from ui.cli import CLI
from services.text_compressor_service import TextCompressorService
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder
from utils.lzw_coder import LZWCoder


def main():
    file_io = FileIO()
    huffman_coder = HuffmanCoder()
    lzw_coder = LZWCoder()
    service = TextCompressorService(file_io, huffman_coder, lzw_coder)
    cli = CLI(service)
    cli.run()


if __name__ == "__main__":
    main()
