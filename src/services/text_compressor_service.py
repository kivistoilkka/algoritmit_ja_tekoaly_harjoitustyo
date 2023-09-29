from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder


class TextCompressorService:
    def __init__(self, file_io: FileIO, huffman_coder: HuffmanCoder) -> None:
        self.file_io = file_io
        self.huffman_coder = huffman_coder

    def encode_file(self, original_file_name: str, encoded_file_name: str, encoding_type: str):
        original_data = self.file_io.read_file(original_file_name)
        match encoding_type:
            case 'huffman coding':
                encoded_data, encoded_tree = self.huffman_coder.encode(
                    original_data)
                return self.file_io.write_file(encoded_tree+'\n'+encoded_data, encoded_file_name)
            case _default:
                raise ValueError('Encoding type "' +
                                 encoding_type + '" not available')

    def decode_file(self, encoded_file_name: str, decoded_file_name: str, encoding_type: str):
        data = self.file_io.read_file(encoded_file_name)
        match encoding_type:
            case 'huffman coding':
                split_data = data.split('\n')
                # TODO: Better way to handle line break characters, easier when working with bytes
                encoded_tree = '\n'.join(split_data[0:-1])
                encoded_data = split_data[-1]
                decoded_data = self.huffman_coder.decode(
                    encoded_data, encoded_tree)
                return self.file_io.write_file(decoded_data, decoded_file_name)
            case _default:
                raise ValueError('Encoding type "' +
                                 encoding_type + '" not available')
