import time

from services.text_compressor_service import TextCompressorService


class CLI:
    def __init__(self, text_compressor_service: TextCompressorService):
        self.service = text_compressor_service

    def handle_compression(self):
        file_path = input('Enter path to the file: ')
        name_for_file = input('Enter path and name for the compressed file: ')
        encoding_option = input(
            'Select compression option (1 Huffman coding, 2 LZW, 3 both): ')
        match encoding_option:
            case '1':
                method = 'huffman coding'
            case '2':
                method = 'lzw'
            case '3':
                method = 'both'
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
                print('\n**********')
                if encoding_successful:
                    print(
                        f"FILE\n\n{file_path}\n\nDECOMPRESSED TO FILE\n\n{name_for_file}\n\nELAPSED TIME: {elapsed_time:.2f} seconds")
                else:
                    print(f"\nFILE\n\n{file_path}\n\nCOULDN'T BE DECOMPRESSED")
                print('\n**********')
            except (ValueError) as error:
                print('ERROR:', error)

    def handle_decompression(self):
        encoded_file = input('Enter path to compressed file: ')
        name_for_file = input(
            'Enter path and name for the decompressed file: ')
        decoding_option = input(
            'Select compression option (1 Huffman coding, 2 LZW, 3 both): ')
        match decoding_option:
            case '1':
                method = 'huffman coding'
            case '2':
                method = 'lzw'
            case '3':
                method = 'both'
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
                print('\n**********')
                if decoding_successful:
                    print(
                        f"FILE\n\n{encoded_file}\n\nDECOMPRESSED TO FILE\n\n{name_for_file}\n\nELAPSED TIME: {elapsed_time:.2f} seconds")
                else:
                    print(
                        f"\nFILE\n\n{encoded_file}\n\nCOULDN'T BE DECOMPRESSED")
                print('\n**********')
            except (ValueError) as error:
                print('ERROR:', error)

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
