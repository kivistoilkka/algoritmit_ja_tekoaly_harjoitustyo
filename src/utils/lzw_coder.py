from io import StringIO

from bitstring import Bits, BitArray

DICTIONARY_SIZE = 256
BITS_IN_WORD = 16

class LZWCoder:
    def __init__(self) -> None:
        pass

    def encode(self, data: str) -> list:
        dictionary = {chr(i): i for i in range(DICTIONARY_SIZE)}
        output = BitArray()
        word = ''
        code = DICTIONARY_SIZE
        for character in data:
            combined = word + character
            if combined in dictionary:
                word = combined
            else:
                output.append(Bits(int=dictionary[word], length=BITS_IN_WORD))
                dictionary[combined] = code
                code += 1
                word = character
        if word:
            output.append(Bits(int=dictionary[word], length=BITS_IN_WORD))
        return output.bytes

    def decode(self, encoded: bytes) -> str:
        dictionary = {i: chr(i) for i in range(DICTIONARY_SIZE)}
        code = DICTIONARY_SIZE
        output = StringIO()
        encoded_generator = Bits(encoded).cut(BITS_IN_WORD)
        word = next(encoded_generator).int
        word_chars = chr(word)
        output.write(word_chars)
        for key_bits in encoded_generator:
            key = key_bits.unpack(f'uint:{BITS_IN_WORD}')[0]
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
