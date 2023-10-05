from services.text_compressor_service import TextCompressorService


class CLI:
    def __init__(self, text_compressor_service: TextCompressorService):
        self.service = text_compressor_service

    def handle_encoding(self):
        file_path = input('Enter path to the file: ')
        name_for_file = input('Enter path and name for the encoded file: ')
        encoding_option = input('Select encoding option (1 Huffman coding, 2 LZW): ')
        match encoding_option:
            case '1':
                encoding_successful = self.service.encode_file(
                    file_path, name_for_file, 'huffman coding'
                )
                if encoding_successful:
                    print(
                        f"\nFile {file_path} encoded to file {name_for_file}")
                else:
                    print(f"\nFile {file_path} couldn't be encoded")
            case '2':
                encoding_successful = self.service.encode_file(
                    file_path, name_for_file, 'lzw'
                )
                if encoding_successful:
                    print(
                        f"\nFile {file_path} encoded to file {name_for_file}")
                else:
                    print(f"\nFile {file_path} couldn't be encoded")
            case _default:
                print('Unknown selection')

    def handle_decoding(self):
        encoded_file = input('Enter path to encoded file: ')
        name_for_file = input('Enter path and name for the decoded file: ')
        decoding_option = input('Select decoding option (1 Huffman coding, 2 LZW): ')
        match decoding_option:
            case '1':
                decoding_successful = self.service.decode_file(
                    encoded_file, name_for_file, 'huffman coding'
                )
                if decoding_successful:
                    print(
                        f"\nFile {encoded_file} decoded to file {name_for_file}")
                else:
                    print(f"\nFile {encoded_file} couldn't be decoded")
            case '2':
                decoding_successful = self.service.decode_file(
                    encoded_file, name_for_file, 'lzw'
                )
                if decoding_successful:
                    print(
                        f"\nFile {encoded_file} decoded to file {name_for_file}")
                else:
                    print(f"\nFile {encoded_file} couldn't be decoded")
            case _default:
                print('Unknown selection')

    def run(self):
        print()
        print('### Text Compressor ###')

        while True:
            print('''
1. Encode text file
2. Decode encoded file
0. Exit
''')
            selection = input('Select option: ')
            match selection:
                case '0':
                    print('Thank you and good bye!')
                    break
                case '1':
                    self.handle_encoding()
                case '2':
                    self.handle_decoding()
                case _default:
                    print('Unknown selection')

            print('\n#######################')
