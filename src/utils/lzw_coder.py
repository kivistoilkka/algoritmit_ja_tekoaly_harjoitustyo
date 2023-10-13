from io import StringIO

from bitstring import Bits, BitArray

from config import ENCODING


DICTIONARY_SIZE = 256
MAX_DICTIONARY_SIZE = 65536
RESET_DICTIONARY_CODE = 256
BITS_IN_WORD = 16

class LZWCoder:
    def __init__(self) -> None:
        pass

    def encode(self, data: str) -> list:
        dictionary = {chr(i): i for i in range(DICTIONARY_SIZE)}
        output = BitArray()
        word = ''
        code = DICTIONARY_SIZE+1
        for character in data:
            combined = word + character
            if combined in dictionary:
                word = combined
            else:
                output.append(Bits(uint=dictionary[word], length=BITS_IN_WORD))
                dictionary[combined] = code
                code += 1
                word = character
            if len(dictionary) == MAX_DICTIONARY_SIZE:
                output.append(Bits(uint=RESET_DICTIONARY_CODE), length=BITS_IN_WORD)
                dictionary = {chr(i): i for i in range(DICTIONARY_SIZE)}
        if word:
            output.append(Bits(uint=dictionary[word], length=BITS_IN_WORD))
        return output.bytes

    def decode(self, encoded: bytes) -> str:
        dictionary = {i: chr(i) for i in range(DICTIONARY_SIZE)}
        code = DICTIONARY_SIZE+1
        output = StringIO()
        encoded_generator = Bits(encoded).cut(BITS_IN_WORD)
        word = next(encoded_generator).uint
        word_chars = chr(word)
        output.write(word_chars)
        for key_bits in encoded_generator:
            key = key_bits.unpack(f'uint:{BITS_IN_WORD}')[0]
            if key == RESET_DICTIONARY_CODE:
                dictionary = {i: chr(i) for i in range(DICTIONARY_SIZE)}
                continue
            if key in dictionary:
                entry = dictionary[key]
            elif key == code:
                entry = word_chars + word_chars[0]
            else:
                raise ValueError('Bad compressed key:', key)
            output.write(entry)
            dictionary[code] = word_chars + entry[0]
            code += 1
            word_chars = entry
        return output.getvalue()
