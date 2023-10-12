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


if __name__ == "__main__":
    coder = LZWCoder()
    print()
    encoded = coder.encode('Testing this test thing here')
    print(encoded)
    print()
    decoded = coder.decode(encoded)
    print(decoded)

    print()
    encoded_long = coder.encode('''\
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''\
    )
    print(encoded_long)
    print()
    decoded_long = coder.decode(encoded_long)
    print(decoded_long)
