from bitstring import BitArray

from config import ENCODING
from utils.file_io import FileIO
from utils.huffman_coder import HuffmanCoder
from utils.lzw_coder import LZWCoder


class TextCompressorService:
    """Service class for handling application logic
    """    

    def __init__(self, file_io: FileIO, huffman_coder: HuffmanCoder, lzw_coder: LZWCoder) -> None:
        self.file_io = file_io
        self.huffman_coder = huffman_coder
        self.lzw_coder = lzw_coder

    def encode_file(self, original_file_name: str, encoded_file_name: str, encoding_type: str):
        """Encodes file with selected encoding method to new file

        Args:
            original_file_name (str): Absolute path to the file to be encoded
            encoded_file_name (str): Absolute path and file name for encoded file
            encoding_type (str): Encoding method (options: huffman coding, lzw)

        Raises:
            ValueError: If given encoding method is not available

        Returns:
            bool: True if encoding and file saving is successful
        """

        match encoding_type:
            case 'huffman coding':
                original_data = self.file_io.read_text_file(original_file_name)
                encoded_data = self.huffman_coder.encode(original_data)
                needed_padding = 8-(len(encoded_data)%8)
                padding_bits = BitArray(needed_padding)
                padded_data = (needed_padding.to_bytes()+encoded_data+padding_bits).bytes
                return self.file_io.write_binary_file(padded_data, encoded_file_name)
            case 'lzw':
                original_data = self.file_io.read_binary_file(original_file_name)
                encoded_data = self.lzw_coder.encode(original_data)
                return self.file_io.write_binary_file(encoded_data, encoded_file_name)
            case _default:
                raise ValueError('Encoding type "' +
                                 encoding_type + '" not available')

    def decode_file(self, encoded_file_name: str, decoded_file_name: str, decoding_type: str):
        """Decodes file with selected decoding method to new file

        Args:
            encoded_file_name (str): Absolute path to the encoded file
            decoded_file_name (str): Absolute path and file name for decoded file
            decoding_type (str): Decoding method (options: huffman coding, lzw)

        Raises:
            ValueError: If given decoding method is not available

        Returns:
            bool: True if decoding and file saving is successful
        """

        match decoding_type:
            case 'huffman coding':
                data = self.file_io.read_binary_file(encoded_file_name)
                data_bitarray = BitArray(data)
                padding_bits_used = data_bitarray[0:8].int
                nonpadded_data = data_bitarray[8:-padding_bits_used]
                decoded_data = self.huffman_coder.decode(nonpadded_data)
                decoded_string = str(decoded_data, encoding=ENCODING)
                return self.file_io.write_text_file(decoded_string, decoded_file_name)
            case 'lzw':
                data = self.file_io.read_binary_file(encoded_file_name)
                decoded_data = self.lzw_coder.decode(data)
                return self.file_io.write_binary_file(decoded_data, decoded_file_name)
            case _default:
                raise ValueError('Encoding type "' +
                                 decoding_type + '" not available')
