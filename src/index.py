import argparse
from tkinter import Tk

from ui.cli import CLI
from ui.gui import GUI
from services.text_compressor_service import TextCompressorService
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder
from utils.lzw_coder import LZWCoder


def main(args):
    file_io = FileIO()
    huffman_coder = HuffmanCoder()
    lzw_coder = LZWCoder()
    service = TextCompressorService(file_io, huffman_coder, lzw_coder)

    if args.ui == 'gui':
        window = Tk()
        window.title('Text Compressor')
        window.resizable(False, False)
        window.geometry('420x240')

        gui = GUI(window, service)
        gui.start()
        window.mainloop()
    elif args.ui == 'cli':
        cli = CLI(service)
        cli.run()
    else:
        print('Unknown ui parameter')


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog='Text Compressor',
        description='Program for compressing text files with Huffman coding and LZW algorithms'
    )
    arg_parser.add_argument('-u', '--ui', default='gui',
                            help='User interface (gui/cli, defaults to gui)')

    args = arg_parser.parse_args()
    main(args)
