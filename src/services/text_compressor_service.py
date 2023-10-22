from bitstring import BitArray

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

    def _add_padding_to_huffman_coded_data(self, encoded_data: BitArray) -> bytes:
        needed_padding = 8-(len(encoded_data) % 8)
        padding_bits = BitArray(needed_padding)
        padded_data = (needed_padding.to_bytes() +
                        encoded_data+padding_bits).bytes
        return padded_data

    def _remove_padding_from_huffman_coded_data(self, data: bytes) -> BitArray:
        data_bitarray = BitArray(data)
        padding_bits_used = data_bitarray[0:8].int
        nonpadded_data = data_bitarray[8:-padding_bits_used]
        return nonpadded_data

    def encode_file(self, original_file_name: str, encoded_file_name: str, compression_method: str):
        """Encodes file with selected compression method to new file. LZW compressed
        data is written as is. When Huffman coding is used, needed amount of padding
        bits is calculated, then output data is written in the following format:
        [amount of padding bits (int), 1 byte][data, n-1 bytes][last byte of data + padding bits, 1 byte].
        Option 'both' first compresses data using LZW, then Huffman coding.

        Args:
            original_file_name (str): Absolute path to the file to be encoded
            encoded_file_name (str): Absolute path and file name for encoded file
            encoding_type (str): Encoding method (options: huffman coding, lzw, both)

        Raises:
            ValueError: If given encoding method is not available

        Returns:
            bool: True if encoding and file saving is successful
        """

        original_data = self.file_io.read_binary_file(original_file_name)
        match compression_method:
            case 'huffman coding':
                encoded_data = self.huffman_coder.encode(original_data)
                padded_data = self._add_padding_to_huffman_coded_data(encoded_data)
                return self.file_io.write_binary_file(padded_data, encoded_file_name)
            case 'lzw':
                encoded_data = self.lzw_coder.encode(original_data)
                return self.file_io.write_binary_file(encoded_data, encoded_file_name)
            case 'both':
                lzw_encoded_data = self.lzw_coder.encode(original_data)
                both_encoded_data = self.huffman_coder.encode(lzw_encoded_data)
                padded_data = self._add_padding_to_huffman_coded_data(both_encoded_data)
                return self.file_io.write_binary_file(padded_data, encoded_file_name)
            case _default:
                raise ValueError('Compression method "' +
                                 compression_method + '" not available')

    def decode_file(self, encoded_file_name: str, decoded_file_name: str, compression_method: str):
        """Decodes file with selected compression method to new file.

        Args:
            encoded_file_name (str): Absolute path to the encoded file
            decoded_file_name (str): Absolute path and file name for decoded file
            decoding_type (str): Decoding method (options: huffman coding, lzw, both)

        Raises:
            ValueError: If given decoding method is not available

        Returns:
            bool: True if decoding and file saving is successful
        """

        data = self.file_io.read_binary_file(encoded_file_name)
        match compression_method:
            case 'huffman coding':
                nonpadded_data = self._remove_padding_from_huffman_coded_data(data)
                decoded_data = self.huffman_coder.decode(nonpadded_data)
                return self.file_io.write_binary_file(decoded_data, decoded_file_name)
            case 'lzw':
                decoded_data = self.lzw_coder.decode(data)
                return self.file_io.write_binary_file(decoded_data, decoded_file_name)
            case 'both':
                nonpadded_data = self._remove_padding_from_huffman_coded_data(data)
                huffman_decoded_data = self.huffman_coder.decode(nonpadded_data)
                both_decoded_data = self.lzw_coder.decode(huffman_decoded_data)
                return self.file_io.write_binary_file(both_decoded_data, decoded_file_name)
            case _default:
                raise ValueError('Compression method "' +
                                 compression_method + '" not available')
