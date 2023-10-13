from io import BytesIO

from bitstring import Bits, BitArray


DICTIONARY_SIZE = 256
MAX_DICTIONARY_SIZE = 65535
RESET_DICTIONARY_CODE = 256
BITS_IN_WORD = 16


class LZWCoder:
    def __init__(self) -> None:
        pass

    def encode(self, data: bytes) -> bytes:
        dictionary = {i.to_bytes(1): i for i in range(DICTIONARY_SIZE)}
        output = BitArray()
        word = b''
        code = DICTIONARY_SIZE+1
        for character in data:
            char_byte = character.to_bytes(1)
            combined = word + char_byte
            if combined in dictionary:
                word = combined
            else:
                output.append(Bits(uint=dictionary[word], length=BITS_IN_WORD))
                dictionary[combined] = code
                code += 1
                word = char_byte
            if len(dictionary) == MAX_DICTIONARY_SIZE:
                output.append(Bits(uint=dictionary[word], length=BITS_IN_WORD))
                output.append(
                    Bits(uint=RESET_DICTIONARY_CODE, length=BITS_IN_WORD))
                dictionary = {i.to_bytes(1): i for i in range(DICTIONARY_SIZE)}
                word = b''
                code = DICTIONARY_SIZE+1
        if word:
            output.append(Bits(uint=dictionary[word], length=BITS_IN_WORD))
        return output.bytes

    def decode(self, encoded: bytes) -> bytes:
        dictionary = {i: i.to_bytes(1) for i in range(DICTIONARY_SIZE)}
        code = DICTIONARY_SIZE+1
        output = BytesIO()
        encoded_generator = Bits(encoded).cut(BITS_IN_WORD)
        key = next(encoded_generator).unpack(f'uint:{BITS_IN_WORD}')[0]
        word = dictionary[key]
        output.write(word)
        previous_reset = False
        reset_counter = 0
        for key_bits in encoded_generator:
            key = key_bits.unpack(f'uint:{BITS_IN_WORD}')[0]
            if reset_counter > 0:
                print(entry)
                reset_counter -= 1
            if key == RESET_DICTIONARY_CODE:
                previous_reset = True
                reset_counter = 50
                dictionary = {i: i.to_bytes(1) for i in range(DICTIONARY_SIZE)}
                code = DICTIONARY_SIZE+1
                continue
            if previous_reset:
                print(key, dictionary[key])
                previous_reset = False
                word = dictionary[key]
                output.write(word)
                continue
            if key in dictionary:
                entry = dictionary[key]
            elif key == code:
                entry = word + word[0].to_bytes(1)
            else:
                raise ValueError('Bad compressed key:', key)
            output.write(entry)
            dictionary[code] = word + entry[0].to_bytes(1)
            code += 1
            word = entry
        return output.getvalue()
