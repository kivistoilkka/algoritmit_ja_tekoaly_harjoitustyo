import time

from services.text_compressor_service import TextCompressorService


class CLI:
    def __init__(self, text_compressor_service: TextCompressorService):
        self.service = text_compressor_service

    def handle_compression(self):
        file_path = input('Enter path to the file: ')
        name_for_file = input('Enter path and name for the compressed file: ')
        encoding_option = input(
            'Select compression option (1 Huffman coding, 2 LZW): ')
        match encoding_option:
            case '1':
                method = 'huffman coding'
            case '2':
                method = 'lzw'
            case _default:
                method = 'unknown'

        if method == 'unknown':
            print('Unknown selection')
        else:
            try:
                start_time = time.time()
                encoding_successful = self.service.encode_file(
                    file_path, name_for_file, method
                )
                end_time = time.time()
                elapsed_time = end_time-start_time
                if encoding_successful:
                    print(
                        f"\nFile {file_path} compressed to file {name_for_file}, elapsed time: {elapsed_time}")
                else:
                    print(f"\nFile {file_path} couldn't be compressed")
            except (ValueError) as error:
                print('Error:', error)

    def handle_decompression(self):
        encoded_file = input('Enter path to compressed file: ')
        name_for_file = input(
            'Enter path and name for the decompressed file: ')
        decoding_option = input(
            'Select compression option (1 Huffman coding, 2 LZW): ')
        match decoding_option:
            case '1':
                method = 'huffman coding'
            case '2':
                method = 'lzw'
            case _default:
                method = 'unknown'

        if method == 'unknown':
            print('Unknown selection')
        else:
            try:
                start_time = time.time()
                decoding_successful = self.service.decode_file(
                    encoded_file, name_for_file, method
                )
                end_time = time.time()
                elapsed_time = end_time-start_time
                if decoding_successful:
                    print(
                        f"\nFile {encoded_file} decompressed to file {name_for_file}, elapsed time: {elapsed_time}")
                else:
                    print(f"\nFile {encoded_file} couldn't be decompressed")
            except (ValueError) as error:
                print('Error:', error)

    def run(self):
        print()
        print('### Text Compressor ###')

        while True:
            print('''
1. Compress text file
2. Decompress file
0. Exit
''')
            selection = input('Select option: ')
            match selection:
                case '0':
                    print('Thank you and good bye!')
                    break
                case '1':
                    self.handle_compression()
                case '2':
                    self.handle_decompression()
                case _default:
                    print('Unknown selection')

            print('\n#######################')
